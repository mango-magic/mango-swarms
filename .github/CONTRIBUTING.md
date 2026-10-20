# Contributing.

Use Python 3.9+ and the standard library. Keep provider integrations explicit,
preserve existing files, and avoid automatic paid fallbacks or permission
bypasses.

Run from the repository root:

```sh
cd toolkit
python3 -m unittest discover -s tests -v
python3 -m compileall -q mango_swarms scripts launch.py
python3 scripts/check_docs.py
python3 scripts/audit_public.py
```

Tests use offline subprocess and loopback HTTP fixtures. Live model tests are
optional and consume local resources or existing provider allowance. Do not add
credentials to CI. Record which platform/model was actually tested.

Submit changes through a pull request with the problem, resulting behaviour and
verification evidence. Include regression coverage for path safety, concurrency,
provider contracts and platform-specific launcher changes.

For performance reports, publish only sanitised metrics. Separate measured
correctness/latency from estimated capacity. Include failed attempts and model
settings. Do not equate agent counts with employees.

By contributing, you agree to license your original contribution under this
repository's MIT licence. Keep third-party code attribution and licence
requirements explicit.
