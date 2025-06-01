# 📊 Label Counter for YOLO Annotation Files

This Python script reads YOLO-style `.txt` annotation files in a specified directory and counts the frequency of class labels. It's useful for quickly inspecting dataset distribution in object detection projects.

## 🚀 Features

- Counts occurrences of class labels in annotation files
- Supports custom class labels (default: 0–9)
- Outputs results to console or optional output file
- Simple command-line interface using `argparse`

## 📁 Project Structure
```
txt_label_counting/
├── label_counter_v2.py # Current modular script
├── label_counter_v1.ipynb # Legacy version (notebook style)
├── README.md # Documentation
└── example_labels/ # Example label files 
├── sample1.txt
├── sample2.txt
└── sample3.txt
```

## 🧑‍💻 Usage

### ✅ Basic Usage

```bash
python label_counter.py path/to/label_files/
```

✅ With Custom Class Labels
```bash
python label_counter.py path/to/label_files/ --labels 0 1 4 7
```

✅ Save Results to File
```bash
python label_counter.py path/to/label_files/ --output result.txt
```

## 📌 Output Example
Class Frequency Count:
Class 0: 56
Class 1: 42
Class 2: 13

If --output result.txt is specified, the above will also be written to the file.

## 📝 Assumptions
Each line in a .txt file starts with a class label (e.g., 0 0.55 0.42 0.33 0.22).

Only .txt files in the specified directory are considered.

Non-numeric or unexpected labels are ignored unless explicitly listed using --labels.

## 🧪 Example Label File
Sample line inside sample1.txt:
```txt
0 0.1 0.11 0.22 0.355
2 0.11 0.55 0.668 0.333
4 0.25 0.877 0.3459 0.1
8 0.222 0.478 0.2 0.669
9 0.2225 0.478 0.366 0.325
```

## 📜 License
This project is licensed under the MIT License.

## 🤝 Contributions
Feel free to fork the repo, submit issues, or open pull requests. Improvements are always welcome!
