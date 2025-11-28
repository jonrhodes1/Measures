# Measures

A small Python toolkit for computing basic statistical measures from numeric data.

## Features

- Mean, median, mode, variance, and standard deviation helpers
- Convenience `summary` function returning all statistics at once
- Command-line interface for quick calculations

## Installation

No external dependencies are required. You can run the package directly from the
repository:

```bash
python -m measures.cli 1 2 3 4
```

## Command-line usage

Provide numbers as positional arguments or via a file:

```bash
# Calculate a summary from inline numbers
python -m measures.cli 1 2 2 3

# Read values from a file
python -m measures.cli -f data.txt

# JSON output for scripting
python -m measures.cli 1 2 2 3 --json
```

Numbers can be separated by spaces or commas. When using a file, the content may
be any combination of whitespace or comma-delimited values.

## Python API

```python
from measures import mean, median, mode, variance, stdev, summary

values = [1, 2, 2, 3]
print(summary(values))
```
