# Mini Library Management System (Python)

## Contents
- `operations.py` : Core functions (add, search, update, delete, borrow, return)
- `demo.py` : Demonstration script showing system usage
- `tests.py` : Simple assert-based tests
- `UML.png` : UML diagram (hand-drawn layout rendered)
- `DesignRationale.pdf` : Design rationale document
- `README.md` : This file

## How to run
1. Make sure you have Python 3.7+ installed.
2. To run the demo:
```bash
python demo.py
```
3. To run tests:
```bash
python tests.py
```

## Notes
- The `operations.py` module raises Python exceptions (`ValueError`, `KeyError`) for invalid operations; you can wrap calls in try/except for graceful handling.
- Genres allowed: Fiction, Non-Fiction, Sci-Fi