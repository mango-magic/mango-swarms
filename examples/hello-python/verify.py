from greeting import greet

assert greet("Ada") == "Hello, Ada!"
assert greet("  Ada  ") == "Hello, Ada!"
assert greet("") == "Hello, world!"
assert greet("   ") == "Hello, world!"
print("PASS: all four greeting cases")
