# pylint: disable=invalid-name, duplicate-code  # Disabled to comply with specific file naming and independent script requirements
"""
This script computes descriptive statistics (mean, median, mode,
standard deviation, and variance) from a file containing numbers.
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
                        numbers.append(float(item))
                    except ValueError:
                        print(f"Error: Invalid data skipped: {item}")
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return None
    return numbers


def calculate_mean(numbers):
    """Calculates the arithmetic mean."""
    if not numbers:
        return 0
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def calculate_median(numbers):
    """Calculates the median value."""
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]


def calculate_mode(numbers):
    """Calculates the mode(s)."""
    if not numbers:
        return None
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    max_count = 0
    for count in counts.values():
        max_count = max(max_count, count)

    modes = [val for val, count in counts.items() if count == max_count]

    if len(modes) == len(counts) and len(counts) > 1:
        return "N/A"
    return modes[0] if len(modes) == 1 else modes


def calculate_variance(numbers, mean):
    """Calculates the variance."""
    if len(numbers) < 2:
        return 0
    sum_sq_diff = 0
    for num in numbers:
        sum_sq_diff += (num - mean) ** 2
    return sum_sq_diff / len(numbers)


def main():
    """Main execution function."""
    if len(sys.argv) < 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        return

    start_time = time.time()
    file_path = sys.argv[1]

    numbers = get_numbers_from_file(file_path)
    if not numbers:
        print("No valid data to process.")
        return

    mean = calculate_mean(numbers)
    median = calculate_median(numbers)
    mode = calculate_mode(numbers)
    variance = calculate_variance(numbers, mean)
    std_dev = variance ** 0.5

    elapsed_time = time.time() - start_time

    results = [
        "--- Statistics Results ---",
        f"File: {file_path}",
        f"Count: {len(numbers)}",
        f"Mean: {mean}",
        f"Median: {median}",
        f"Mode: {mode}",
        f"Variance: {variance}",
        f"Std Deviation: {std_dev}",
        f"Execution Time: {elapsed_time:.4f} seconds"
    ]

    output_text = "\n".join(results)
    print(output_text)

    with open("StatisticsResults.txt", "w", encoding='utf-8') as results_file:
        results_file.write(output_text)


if __name__ == "__main__":
    main()
