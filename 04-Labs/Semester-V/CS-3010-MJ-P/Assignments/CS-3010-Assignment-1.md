# Assignment 1: Data Representation & Database Setup

## Problem Statement / Aim
To understand the concepts of data representation formats (JSON, XML, CSV) and setup a suitable database environment to store such data.

## Theory & Concept
Data representation is the method of presenting data in a structured format so that systems can easily process, store, and transport it. Common formats include:
- **JSON (JavaScript Object Notation):** Lightweight data-interchange format, easy for humans to read and write and for machines to parse and generate. Used extensively in NoSQL databases like MongoDB.
- **XML (eXtensible Markup Language):** Defines a set of rules for encoding documents in a format that is both human-readable and machine-readable.
- **CSV (Comma-Separated Values):** Simple file format used to store tabular data.

Setting up a database involves selecting the appropriate type (SQL vs NoSQL) based on the data representation format and application requirements. Document databases naturally handle JSON-like data.

## Fully Solved Code / Implementation
*Setting up a basic JSON representation to be used in subsequent labs:*

```json
{
  "student_id": "S1001",
  "name": "John Doe",
  "department": "Computer Science",
  "courses": ["CS-3010", "CS-3020"],
  "cgpa": 8.5
}
```

*Basic script to convert CSV to JSON (Python):*

```python
import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    data = []
    with open(csv_file_path, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            data.append(rows)

    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

# Example usage:
# csv_to_json('students.csv', 'students.json')
```

## Expected Output
A well-formed JSON object representing the data correctly, validating its syntax, and understanding the transformation from structured (CSV) to semi-structured (JSON) data formats.

[[CS-3010-Viva-1|View Viva Questions]]
