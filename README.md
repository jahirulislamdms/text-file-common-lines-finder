# 📄 Text File Common Lines Finder

A Python script that compares two text files and extracts the common lines into a new output file.

The script automatically tries multiple encodings to safely read different types of text files.

---

## 🚀 Features

- Compares two text files
- Finds exact matching lines
- Removes duplicates automatically
- Supports multiple encodings:
  - utf-8
  - latin-1
  - ascii
  - utf-16
- Outputs results in UTF-8 format
- Returns total count of common lines

---

## 🛠 Requirements

- Python 3.x
- No external libraries required

---

## ▶️ Usage

Edit the file paths inside the script:

```python
file1_path = r"C:\path\to\file1.txt"
file2_path = r"C:\path\to\file2.txt"
output_path = r"C:\path\to\common_lines.txt"
```

Then run:

```bash
python compare_text_files_common_lines.py
```

---

## 📂 Output

- Creates a new file containing only the common lines.
- Lines are sorted alphabetically.
- Output file is saved using UTF-8 encoding.

---

## 📌 How It Works

1. Tries multiple encodings to read both files.
2. Converts file lines into sets (removes duplicates).
3. Finds intersection between both sets.
4. Writes sorted common lines into output file.

---

## 📊 Example

If:

**file1.txt**
```
apple
banana
orange
```

**file2.txt**
```
banana
grape
orange
```

**Output (common_lines.txt)**
```
banana
orange
```

---

## 📄 License

Free to use and modify.
