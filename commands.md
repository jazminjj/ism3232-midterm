# Terminal Record: Harvest Table Catering

## 1. Building the project
cd ~
mkdir ism3232-midterm && cd ism3232-midterm
git init -b main
python3 -m venv .venv
source .venv/bin/activate
pip install pytest ruff
touch business_rules.py main.py commands.md README.md .gitignore tests/__init__.py tests/test_business_rules.py
pip freeze > requirements.txt
git add .
git commit -m "Start ISM3232 midterm project"
git remote add origin https://github.com/jazminjj/ism3232-midterm.git
git branch -M main
git push -u origin main

## 2. The virtual environment
"which python3"
/home/jazminj/ism3232-midterm/.venv/bin/python3

"tree -L 2"
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

## 3. The project structure
## 4. Every function and test

## 5. Which files print
main.py
## 6. The commit history