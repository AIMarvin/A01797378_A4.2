# pylint: disable=invalid-name, duplicate-code  # Disabled to comply with specific file naming and independent script requirements
"""
This script converts numbers from a file into binary and hexadecimal.
"""

import sys
import time


def get_numbers_from_file(file_path):
    """Reads numbers from a file, handling invalid data."""
    numbers = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                items = line.split()
                for item in items:
                    try:
                        numbers.append(int(float(item)))
                    except ValueError:
                        print(f"Error: Invalid data skipped: {item}")
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return None
    return numbers


def to_binary(n):
    """Converts a number to binary using a basic algorithm."""
    if n == 0:
        return "0"

    is_negative = n < 0
    num = abs(n)
    binary = ""

    while num > 0:
        binary = str(num % 2) + binary
        num //= 2

    return "-" + binary if is_negative else binary


def to_hexadecimal(n):
    """Converts a number to hexadecimal using a basic algorithm."""
    if n == 0:
        return "0"

    is_negative = n < 0
    num = abs(n)
    hex_chars = "0123456789ABCDEF"
    hex_str = ""

    while num > 0:
        remainder = num % 16
        hex_str = hex_chars[remainder] + hex_str
        num //= 16

    return "-" + hex_str if is_negative else hex_str


def main():
    """Main execution function."""
    if len(sys.argv) < 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        return

    start_time = time.time()
    file_path = sys.argv[1]

    numbers = get_numbers_from_file(file_path)
    if not numbers:
        return

    results = [
        "Index\tNumber\tBinary\tHexadecimal",
        "--------------------------------------"
    ]

    for i, num in enumerate(numbers, 1):
        bin_val = to_binary(num)
        hex_val = to_hexadecimal(num)
        results.append(f"{i}\t{num}\t{bin_val}\t{hex_val}")

    elapsed_time = time.time() - start_time
    results.append(f"\nExecution Time: {elapsed_time:.4f} seconds")

    output_text = "\n".join(results)
    print(output_text)

    with open("ConvertionResults.txt", "w", encoding='utf-8') as results_file:
        results_file.write(output_text)


if __name__ == "__main__":
    main()
