import os
import argparse
from collections import defaultdict


def count_classes_in_txt(directory, labels=None):
    """
    Count the frequency of label classes in .txt files inside the specified directory.

    Parameters:
    - directory (str): Path to the directory containing annotation .txt files.
    - labels (list of str): List of valid class labels to count. Defaults to '0'–'9'.

    Returns:
    - dict: Dictionary mapping class label to frequency count.
    """
    if labels is None:
        labels = [str(i) for i in range(10)]  # Default: 0–9

    class_counts = defaultdict(int)

    txt_files = [os.path.join(directory, file)
                 for file in os.listdir(directory)
                 if file.endswith('.txt')]

    for txt_file in txt_files:
        with open(txt_file, 'r') as f:
            for line in f:
                label = line.strip()[0]
                if label in labels:
                    class_counts[label] += 1

    return dict(sorted(class_counts.items(), key=lambda x: x[0]))


def main():
    parser = argparse.ArgumentParser(description="Count class occurrences from annotation label .txt files.")
    parser.add_argument(
        "directory", type=str, help="Directory containing .txt label files (e.g., YOLO annotations)")
    parser.add_argument(
        "--labels", type=str, nargs="*", help="List of class labels to consider (default: 0–9)")
    parser.add_argument(
        "--output", type=str, help="Optional path to save results (as .txt)")
    args = parser.parse_args()

    result = count_classes_in_txt(args.directory, args.labels)

    print("\nClass Frequency Count:")
    for label, count in result.items():
        print(f"Class {label}: {count}")

    if args.output:
        with open(args.output, "w") as out_file:
            for label, count in result.items():
                out_file.write(f"{label}: {count}\n")
        print(f"\nSaved output to {args.output}")


if __name__ == "__main__":
    main()
