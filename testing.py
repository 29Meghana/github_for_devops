"""
Simple greeting module.

This module prints a greeting message to the user.
"""


def greet(name: str) -> None:
    """
    Print a greeting message.

    Args:
        name (str): Name of the person to greet.
    """
    print(f"Hello {name}")


def main() -> None:
    """Program entry point."""
    greet("Meghana")


if __name__ == "__main__":
    main()