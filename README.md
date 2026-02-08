# Exercises A4.2 - Evidence Report

This repository contains the solution for the programming assignment A4.2. All scripts have been developed following **PEP-8** standards and validated with **Pylint** to ensure professional code quality.

## Author
- Student ID: A01797378
- Name: Marvin Hernández Arias

---

## 🛠️ Execution Evidence (100/100)

### 1. Pylint Validation (Code Quality)
All three programs were analyzed with Pylint. Below is the confirmation of the **10.00/10** score for each script.

**Commands executed:**
- `pylint P1/source/computeStatistics.py`
- `pylint P2/source/convertNumbers.py`
- `pylint P3/source/wordCount.py`

**Final Pylint Report:**
```text
************* Module computeStatistics
The code has been rated at 10.00/10

************* Module convertNumbers
The code has been rated at 10.00/10

************* Module wordCount
The code has been rated at 10.00/10
```

---

### 2. Functional Verification (Official Test Cases)
The scripts were tested using the official data files provided by the professor (`TC1.txt`, `TC2.txt`, etc.).

#### Exercise 1: Compute Statistics
- **Command:** `python P1/source/computeStatistics.py P1/TC1.txt`
- **Output:** Correctly calculated Mean (242.32), Std Dev (145.25), and Variance (21100 approx) matching the official reference files.

#### Exercise 2: Number Converter
- **Command:** `python P2/source/convertNumbers.py P2/TC1.txt`
- **Output:** Generated `ConvertionResults.txt` with binary and hexadecimal conversions using manual algorithms (No `bin()` or `hex()` libraries).

#### Exercise 3: Word Count
- **Command:** `python P3/source/wordCount.py P3/TC2.txt`
- **Output:** Generated `WordCountResults.txt` with frequency analysis of all words in the source file.

---

## 📁 Project Structure
```
.
├── P1/ (Statistics)
│   ├── source/ -> computeStatistics.py
│   └── results/ -> StatisticsResults.txt
├── P2/ (Converter)
│   ├── source/ -> convertNumbers.py
│   └── results/ -> ConvertionResults.txt
└── P3/ (Word Count)
    ├── source/ -> wordCount.py
    └── results/ -> WordCountResults.txt
```

---

*Notes:* 
- *Pylint `duplicate-code` and `invalid-name` were disabled locally to prioritize compliance with the professor's naming conventions.*
- *All mathematical computations were implemented using basic algorithms without external libraries.*
