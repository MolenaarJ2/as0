import numpy as np


def main() -> None:
    """Main"""
    print("Hello from oop-assignment-0-jj!")


def add_two_integer_lists(a: list[int], b: list[str]) -> int:
    """Adding 2 integer lists"""
    arr = np.array(a) + np.array(b)
    print(f"My added array: {arr}")
    return arr


if __name__ == "__main__":
    arr = add_two_integer_lists([1, 2, 3], [4, 5, 6])
