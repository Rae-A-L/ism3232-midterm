# ISM3232 Midterm: Brightline Print Shop

- **Name:** Rae-Anthony Lewis
- **Version:** 1.0
- **Date:** 10/25/2026

## What This Program Does:
This projects helps the Brightline Print Shop price each print job and invoices the customer. It includes and applies discounts, setup fees, proofs, and overnight runs based on each order.

## Business Rules: 
* Print cost is found by multiplying price per copy and number of copies.

* Depending on the number of copies, the discounts reflect on it. Jobs with less than 200 copies get no discount, jobs with 200 to 999 get an 8% discount, and jobs with 1,000 or more get an 15% discount. 

* Registered student organizations with 200 copies or more get an extra 5% discount. 

* A job with $300 or more needs printed proof.

* A job with more than 500 copies or the job is over $400 needs an overnight press run.

## How to Run:

python3-m venv .venv 

source .venv/bin/activate

pip install -r requirements.txt

python3 main.py

## How to Test:

ruff format .
ruff check .
pytest -v

The test file has 20 tests, with both sides of the limit. 

## Files in This Repository
- business_rules.py: Has all business rules and functions 
- main.py: Runs the sample print jobs and displays the report 
- tests/test_business_rules.py: the pytest tests
- tests/__init__.py: allows the test files import the functions
- commands.md: terminal commands that builds the project
- README.md: this file
- requirements.txt: packages needed to install 
- .gitignore: keeps .venv and __pycache__ out of the repository

## AI Use Statement:
I did not use AI on this exam 


