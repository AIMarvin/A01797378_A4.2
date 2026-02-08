# pylint: disable=invalid-name, duplicate-code  # Disabled to comply with specific file naming and independent script requirements
"""
This script counts the frequency of each distinct word in a file.
"""

import sys
import time


def get_words_from_file(file_path):
    """Reads words from a file, handling errors."""
    words = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line_words = line.split()
                for word in line_words:
                    words.append(word.strip().lower())
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return None
    except OSError as error:
        print(f"Error: OS level error while reading file: {error}")
        return None
    return words


def count_word_frequencies(words):
    """Counts frequencies using a basic dictionary algorithm."""
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies


def main():
    """Main execution function."""
    if len(sys.argv) < 2:
        print("Usage: python wordCount.py fileWithData.txt")
        return

    start_time = time.time()
    file_path = sys.argv[1]

    words = get_words_from_file(file_path)
    if not words:
        return

    frequencies = count_word_frequencies(words)

    sorted_freq = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

    results = [
        "Word\t\tFrequency",
        "--------------------------"
    ]

    for word, count in sorted_freq:
        results.append(f"{word}\t\t{count}")

    elapsed_time = time.time() - start_time
    results.append(f"\nExecution Time: {elapsed_time:.4f} seconds")

    output_text = "\n".join(results)
    print(output_text)

    with open("WordCountResults.txt", "w", encoding='utf-8') as results_file:
        results_file.write(output_text)


if __name__ == "__main__":
    main()
