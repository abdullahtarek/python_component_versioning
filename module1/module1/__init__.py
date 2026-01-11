__version__ = "1.1.0"

def greet(name: str) -> str:
    """Return a greeting message including the module version."""
    return f"Hello {name}, from module1 v{__version__}"