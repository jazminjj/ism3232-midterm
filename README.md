# ISM3232 Midterm: Harvest Table Catering

- **Name:** jazmin joseph
- **Version:** beta
- **Date:** 10/25/26

## What This Program Does
This program calculates the price of each catering event from the price per guest and the number of guests. It applies a discount and service fee rules, then flags events that need a sign off from the manager or a second chef. It then prints a report the owner can read, with a one line summary and totals.
## Business Rules
1. The food cost is the price per guest * number og guests
2. Events with < 25 guests get no discount, events with 25-99 guests get 5%, 100+ guests get 12%
3. The 12% discount is only for nonprofits, any other event with 100+ gets 5%
4.A $75 service fee is added when the discounted cost is $500 or less
5. An event total of more than $2500 needs a manager signoff
6.Second chef is needed when event has more than 80 guests or total is >$3000

## How to Run
'''bash
git clone  https://github.com/jazminjj/ism3232-midterm.git
cd ism3232-midterm
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py

## How to Test
'''bash
ruff check .
pytest -v
''''

## Files in This Repository
business_rules.py:8 functions to apply the business rules
main.py: list of events, then prints the report and summary
commands.md: record of commands that I ran
READ.ME: describes the entire project
requirements.txt: packages needed to run and test the project, from pip freeze
.gitignore: keeps `.venv/` and `__pycache__/` out of the repository
tests/__init__.py: empty file that makes tests a package
tests/test_business_rules.py: 20 pytest for business rules

## AI Use Statement
I, Jazmin Joseph, did not use AI on this midterm project or exam.
