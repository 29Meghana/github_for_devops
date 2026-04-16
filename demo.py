"""
Demo module for simple math and loops.
"""


def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers and print the result.

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: Sum of the numbers
    """
    result = a + b
    print(f"Result is: {result}")
    return result


def print_numbers() -> None:
    """Print numbers from 0 to 4."""
    for i in range(5):
        print(i)


def main() -> None:
    """Program entry point."""
    add_numbers(10, 20)
    print_numbers()


if __name__ == "__main__":
    main()