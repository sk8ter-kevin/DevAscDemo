"""A small reusable feature for building friendly greetings."""


def greet(name: str = "world") -> str:
	"""Return a greeting for the supplied name."""
	clean_name = name.strip()
	if not clean_name:
		clean_name = "world"
	return f"Hello, {clean_name}!"
print(greet("Alice"))  # Output: Hello, Alice!