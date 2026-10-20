#!/usr/bin/env python3
"""Check repository links and the file-based use-case catalogue without model calls."""

import collections
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "toolkit"))
from mango_swarms.cli import parser  # noqa: E402
from mango_swarms.workflow import MODES  # noqa: E402


def outside_fences(text):
    return re.sub(r"^```[^\n]*\n.*?^```\s*$", "", text,
                  flags=re.MULTILINE | re.DOTALL)


def heading_ids(text):
    counts = collections.Counter()
    result = set(re.findall(r'<a\s+id="([^"]+)"', text))
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*$", outside_fences(text), re.MULTILINE):
        slug = re.sub(r"[^\w -]", "", heading.lower()).replace(" ", "-")
        result.add(slug + ("-" + str(counts[slug]) if counts[slug] else ""))
        counts[slug] += 1
    return result


class AssetLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
        for key in ("src", "href"):
            if attributes.get(key):
                self.links.append(attributes[key])
        if attributes.get("srcset"):
            self.links.extend(item.strip().split()[0]
                              for item in attributes["srcset"].split(","))


def check():
    problems = []
    documents = sorted(p for p in ROOT.rglob("*.md")
                       if not any(part in {".git", ".venv", "bin", "__pycache__"}
                                  for part in p.relative_to(ROOT).parts))
    texts = {p.resolve(): p.read_text(encoding="utf-8") for p in documents}
    link_count = 0
    for path, text in texts.items():
        plain = outside_fences(text)
        html = AssetLinks()
        html.feed(plain)
        links = re.findall(r"\[[^\]\n]*\]\(([^)\s]+)\)", plain) + html.links
        for link in links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            link_count += 1
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                problems.append(str(path.relative_to(ROOT)) + ": link leaves repository: " + link)
                continue
            if not target.exists():
                problems.append(str(path.relative_to(ROOT)) + ": missing link: " + link)
            elif parsed.fragment and target.suffix == ".md":
                if unquote(parsed.fragment) not in heading_ids(texts[target]):
                    problems.append(str(path.relative_to(ROOT)) + ": missing anchor: " + link)

    catalogue = sorted((ROOT / "use-cases").glob("*.md"))
    categories = [p for p in catalogue if p.name != "README.md"]
    if len(categories) != 20:
        problems.append("Expected 20 use-case categories.")
    identifiers, titles, prompts = [], [], []
    mode_counts = collections.Counter()
    cli = parser()
    for path in categories:
        text = texts[path.resolve()]
        entries = list(re.finditer(r'^<a id="uc-(\d{3})"></a>\n## (\d{3})\. ([^\n]+)\n(.*?)(?=^<a id=|\Z)',
                                  text, re.MULTILINE | re.DOTALL))
        if len(entries) != 10:
            problems.append(path.name + ": expected ten entries.")
        for entry in entries:
            anchor, number, title, body = entry.groups()
            label = path.name + " #" + number
            identifiers.append(number)
            titles.append(title.casefold().rstrip("."))
            if anchor != number:
                problems.append(label + ": anchor does not match entry number.")
            fields = {}
            for field in ("Mode", "Inputs", "Outputs", "Validation / approval"):
                matches = re.findall(r"^\*\*" + re.escape(field) + r":\*\* (.+)$", body, re.MULTILINE)
                if len(matches) != 1:
                    problems.append(label + ": expected exactly one " + field + " field.")
                fields[field] = matches[0] if matches else ""
            mode = fields["Mode"].strip("`")
            if mode not in MODES:
                problems.append(label + ": unsupported mode.")
                continue
            mode_counts[mode] += 1
            files = {field: re.findall(r"`([^`]+)`", fields[field])
                     for field in ("Inputs", "Outputs")}
            starter = re.search(r"\*\*Starter prompt:\*\*\n\n((?:> [^\n]+\n?)+)", body)
            if not starter:
                problems.append(label + ": missing starter prompt.")
                continue
            prompt = "\n".join(line[2:] for line in starter.group(1).splitlines())
            prompts.append(" ".join(prompt.lower().split()))
            for field, filenames in files.items():
                if not filenames:
                    problems.append(label + ": missing named " + field.lower() + ".")
                for filename in filenames:
                    if filename not in prompt:
                        problems.append(label + ": prompt does not mention " + filename)
                    if Path(filename).is_absolute() or ".." in Path(filename).parts:
                        problems.append(label + ": unsafe example filename.")
            args = [mode, "example-workspace", "--max-tasks", "1", "-g", prompt, "--dry-run"]
            for filename in files["Inputs"]:
                args.extend(["--context", filename])
            parsed = cli.parse_args(args)
            if parsed.context != files["Inputs"] or parsed.apply:
                problems.append(label + ": starter command does not preserve staged-file semantics.")

    if sorted(identifiers) != [str(i).zfill(3) for i in range(1, 201)]:
        problems.append("Catalogue must contain each ID from 001 to 200 exactly once.")
    for name, values in (("titles", titles), ("starter prompts", prompts)):
        if len(values) != len(set(values)):
            problems.append("Duplicate use-case " + name + ".")
    if set(mode_counts) != set(MODES):
        problems.append("Catalogue must cover all five supported modes.")
    if problems:
        raise SystemExit("Documentation checks failed:\n" + "\n".join(problems))
    print("PASS: %d Markdown documents, %d local links, 20 categories, 200 unique titles/prompts, "
          "and 200 CLI argument checks; no model requests." % (len(documents), link_count))
    print("Mode coverage: " + ", ".join("%s=%d" % item for item in sorted(mode_counts.items())))


if __name__ == "__main__":
    check()
