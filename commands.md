# Terminal Record: [Brightline Print Shop]
# Author: Rae Anthony Lewis 

## 1. Building the project
DESKTOP-FJGPNR6% cd ~/ism3232/ism3232-midterm
DESKTOP-FJGPNR6% ll
total 8
drwxr-xr-x  2 raeanthonylew raeanthonylew 4096 Oct 19 14:10 .
drwxr-xr-x 16 raeanthonylew raeanthonylew 4096 Oct 19 14:10 ..
DESKTOP-FJGPNR6% touch README.md
DESKTOP-FJGPNR6% python3 -m venv .venv
DESKTOP-FJGPNR6% source .venv/bin/activate
(.venv) DESKTOP-FJGPNR6% pip install pytest ruff
Collecting pytest
  Using cached pytest-9.1.1-py3-none-any.whl.metadata (7.6 kB)
Collecting ruff
  Downloading ruff-0.17.1-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (20 kB)
Collecting iniconfig>=1.0.1 (from pytest)
  Using cached iniconfig-2.3.1-py3-none-any.whl.metadata (2.8 kB)
Collecting packaging>=22 (from pytest)
  Using cached packaging-26.3-py3-none-any.whl.metadata (3.5 kB)
Collecting pluggy<2,>=1.5 (from pytest)
  Downloading pluggy-1.7.0-py3-none-any.whl.metadata (5.0 kB)
Collecting pygments>=2.7.2 (from pytest)
  Using cached pygments-2.21.0-py3-none-any.whl.metadata (2.5 kB)
Using cached pytest-9.1.1-py3-none-any.whl (386 kB)
Downloading pluggy-1.7.0-py3-none-any.whl (27 kB)
Downloading ruff-0.17.1-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (10.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.4/10.4 MB 45.5 MB/s eta 0:00:00
Using cached iniconfig-2.3.1-py3-none-any.whl (7.6 kB)
Using cached packaging-26.3-py3-none-any.whl (129 kB)
Using cached pygments-2.21.0-py3-none-any.whl (1.3 MB)
Installing collected packages: ruff, pygments, pluggy, packaging, iniconfig, pytest
Successfully installed iniconfig-2.3.1 packaging-26.3 pluggy-1.7.0 pygments-2.21.0 pytest-9.1.1 ruff-0.17.1
(.venv) DESKTOP-FJGPNR6% pip list
Package   Version
--------- -------
iniconfig 2.3.1
packaging 26.3
pip       25.1.1
pluggy    1.7.0
Pygments  2.21.0
pytest    9.1.1
ruff      0.17.1
(.venv) DESKTOP-FJGPNR6% pip freeze > requirements.txt
(.venv) DESKTOP-FJGPNR6% cat requirements.txt
iniconfig==2.3.1
packaging==26.3
pluggy==1.7.0
Pygments==2.21.0
pytest==9.1.1
ruff==0.17.1
(.venv) DESKTOP-FJGPNR6% echo '.venv/' > .gitignore
(.venv) DESKTOP-FJGPNR6% echo '__pycache__/' >> .gitignore
(.venv) DESKTOP-FJGPNR6% echo '*.pyc' >> .gitignore
(.venv) DESKTOP-FJGPNR6% cat .gitignore
.venv/
__pycache__/
*.pyc
(.venv) DESKTOP-FJGPNR6% ls - la
ls: cannot access '-': No such file or directory
ls: cannot access 'la': No such file or directory
(.venv) DESKTOP-FJGPNR6% ls -la
total 20
drwxr-xr-x  3 raeanthonylew raeanthonylew 4096 Oct 19 14:21 .
drwxr-xr-x 16 raeanthonylew raeanthonylew 4096 Oct 19 14:10 ..
-rw-r--r--  1 raeanthonylew raeanthonylew   26 Oct 19 14:24 .gitignore
drwxr-xr-x  5 raeanthonylew raeanthonylew 4096 Oct 19 14:18 .venv
-rw-r--r--  1 raeanthonylew raeanthonylew    0 Oct 19 14:18 README.md
-rw-r--r--  1 raeanthonylew raeanthonylew   91 Oct 19 14:20 requirements.txt
(.venv) DESKTOP-FJGPNR6% touch business_rules.py main.py
(.venv) DESKTOP-FJGPNR6% ll
total 20
drwxr-xr-x  3 raeanthonylew raeanthonylew 4096 Oct 19 14:35 .
drwxr-xr-x 16 raeanthonylew raeanthonylew 4096 Oct 19 14:10 ..
-rw-r--r--  1 raeanthonylew raeanthonylew   26 Oct 19 14:24 .gitignore
drwxr-xr-x  5 raeanthonylew raeanthonylew 4096 Oct 19 14:18 .venv
-rw-r--r--  1 raeanthonylew raeanthonylew    0 Oct 19 14:18 README.md
-rw-r--r--  1 raeanthonylew raeanthonylew    0 Oct 19 14:35 business_rules.py
-rw-r--r--  1 raeanthonylew raeanthonylew    0 Oct 19 14:35 main.py
-rw-r--r--  1 raeanthonylew raeanthonylew   91 Oct 19 14:20 requirements.txt
(.venv) DESKTOP-FJGPNR6% touch commands.md
(.venv) DESKTOP-FJGPNR6% ll
total 20
drwxr-xr-x  3 raeanthonylew raeanthonylew 4096 Oct 19 14:35 .
drwxr-xr-x 16 raeanthonylew raeanthonylew 4096 Oct 19 14:10 ..
-rw-r--r--  1 raeanthonylew raeanthonylew   26 Oct 19 14:24 .gitignore
drwxr-xr-x  5 raeanthonylew raeanthonylew 4096 Oct 19 14:18 .venv
-rw-r--r--  1 raeanthonylew raeanthonylew    0 Oct 19 14:18 README.md
-rw-r--r--  1 raeanthonylew raeanthonylew    0 Oct 19 14:35 business_rules.py
-rw-r--r--  1 raeanthonylew raeanthonylew    0 Oct 19 14:35 commands.md
-rw-r--r--  1 raeanthonylew raeanthonylew    0 Oct 19 14:35 main.py
-rw-r--r--  1 raeanthonylew raeanthonylew   91 Oct 19 14:20 requirements.txt
(.venv) DESKTOP-FJGPNR6% mkdir -p tests && touch tests/__init__.py tests/test_business_rules.py
(.venv) DESKTOP-FJGPNR6% ll
total 24
drwxr-xr-x  4 raeanthonylew raeanthonylew 4096 Oct 19 14:36 .
drwxr-xr-x 16 raeanthonylew raeanthonylew 4096 Oct 19 14:10 ..
-rw-r--r--  1 raeanthonylew raeanthonylew   26 Oct 19 14:24 .gitignore
drwxr-xr-x  5 raeanthonylew raeanthonylew 4096 Oct 19 14:18 .venv
-rw-r--r--  1 raeanthonylew raeanthonylew    0 Oct 19 14:18 README.md
-rw-r--r--  1 raeanthonylew raeanthonylew    0 Oct 19 14:35 business_rules.py
-rw-r--r--  1 raeanthonylew raeanthonylew    0 Oct 19 14:35 commands.md
-rw-r--r--  1 raeanthonylew raeanthonylew    0 Oct 19 14:35 main.py
-rw-r--r--  1 raeanthonylew raeanthonylew   91 Oct 19 14:20 requirements.txt
drwxr-xr-x  2 raeanthonylew raeanthonylew 4096 Oct 19 14:36 tests
(.venv) DESKTOP-FJGPNR6% cd /tests
cd: no such file or directory: /tests
(.venv) DESKTOP-FJGPNR6% cd ~/tests
cd: no such file or directory: /home/raeanthonylew/tests
(.venv) DESKTOP-FJGPNR6% pwd
/home/raeanthonylew/ism3232/ism3232-midterm
(.venv) DESKTOP-FJGPNR6% cd tests
(.venv) DESKTOP-FJGPNR6% ll
total 8
drwxr-xr-x 2 raeanthonylew raeanthonylew 4096 Oct 19 14:36 .
drwxr-xr-x 4 raeanthonylew raeanthonylew 4096 Oct 19 14:36 ..
-rw-r--r-- 1 raeanthonylew raeanthonylew    0 Oct 19 14:36 __init__.py
-rw-r--r-- 1 raeanthonylew raeanthonylew    0 Oct 19 14:36 test_business_rules.py
(.venv) DESKTOP-FJGPNR6% git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: will change to "main" in Git 3.0. To configure the initial branch name
hint: to use in all of your new repositories, which will suppress this warning,
hint: call:
hint:
hint:   git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint:   git branch -m <name>
hint:
hint: Disable this message with "git config set advice.defaultBranchName false"
Initialized empty Git repository in /home/raeanthonylew/ism3232/ism3232-midterm/tests/.git/
(.venv) DESKTOP-FJGPNR6% git add .
(.venv) DESKTOP-FJGPNR6% git commit -m "Pre-setup for Brightline Print Shop"
[master (root-commit) e9824c5] Pre-setup for Brightline Print Shop
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 __init__.py
 create mode 100644 test_business_rules.py
(.venv) DESKTOP-FJGPNR6% git remote add origin https://github.com/Rae-A-L/ism3232-midterm.git
git branch -M main
git push -u origin main
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 14 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 266 bytes | 266.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/Rae-A-L/ism3232-midterm.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
(.venv) DESKTOP-FJGPNR6% cd ..
(.venv) DESKTOP-FJGPNR6% pwd
/home/raeanthonylew/ism3232/ism3232-midterm
(.venv) DESKTOP-FJGPNR6% git remote add origin https://github.com/Rae-A-L/ism3232-midterm.git
git branch -M main
git push -u origin main
error: remote origin already exists.
branch 'main' set up to track 'origin/main'.
Everything up-to-date
(.venv) DESKTOP-FJGPNR6% ll
total 24
drwxr-xr-x  4 raeanthonylew raeanthonylew 4096 Oct 19 14:36 .
drwxr-xr-x 16 raeanthonylew raeanthonylew 4096 Oct 19 14:10 ..
-rw-r--r--  1 raeanthonylew raeanthonylew   26 Oct 19 14:24 .gitignore
drwxr-xr-x  5 raeanthonylew raeanthonylew 4096 Oct 19 14:18 .venv
-rw-r--r--  1 raeanthonylew raeanthonylew    0 Oct 19 14:18 README.md
-rw-r--r--  1 raeanthonylew raeanthonylew    0 Oct 19 14:35 business_rules.py
-rw-r--r--  1 raeanthonylew raeanthonylew    0 Oct 19 14:35 commands.md
-rw-r--r--  1 raeanthonylew raeanthonylew    0 Oct 19 14:35 main.py
-rw-r--r--  1 raeanthonylew raeanthonylew   91 Oct 19 14:20 requirements.txt
drwxr-xr-x  3 raeanthonylew raeanthonylew 4096 Oct 19 14:43 tests
(.venv) DESKTOP-FJGPNR6% ls -la
total 24
drwxr-xr-x  4 raeanthonylew raeanthonylew 4096 Oct 19 14:36 .
drwxr-xr-x 16 raeanthonylew raeanthonylew 4096 Oct 19 14:10 ..
-rw-r--r--  1 raeanthonylew raeanthonylew   26 Oct 19 14:24 .gitignore
drwxr-xr-x  5 raeanthonylew raeanthonylew 4096 Oct 19 14:18 .venv
-rw-r--r--  1 raeanthonylew raeanthonylew    0 Oct 19 14:18 README.md
-rw-r--r--  1 raeanthonylew raeanthonylew    0 Oct 19 14:35 business_rules.py
-rw-r--r--  1 raeanthonylew raeanthonylew    0 Oct 19 14:35 commands.md
-rw-r--r--  1 raeanthonylew raeanthonylew    0 Oct 19 14:35 main.py
-rw-r--r--  1 raeanthonylew raeanthonylew   91 Oct 19 14:20 requirements.txt
drwxr-xr-x  3 raeanthonylew raeanthonylew 4096 Oct 19 14:43 tests
(.venv) DESKTOP-FJGPNR6% rm -r .git
rm: cannot remove '.git': No such file or directory
(.venv) DESKTOP-FJGPNR6% git push
Everything up-to-date
(.venv) DESKTOP-FJGPNR6% ls -la
total 24
drwxr-xr-x  4 raeanthonylew raeanthonylew 4096 Oct 19 14:36 .
drwxr-xr-x 16 raeanthonylew raeanthonylew 4096 Oct 19 14:10 ..
-rw-r--r--  1 raeanthonylew raeanthonylew   26 Oct 19 14:24 .gitignore
drwxr-xr-x  5 raeanthonylew raeanthonylew 4096 Oct 19 14:18 .venv
-rw-r--r--  1 raeanthonylew raeanthonylew    0 Oct 19 14:18 README.md
-rw-r--r--  1 raeanthonylew raeanthonylew    0 Oct 19 14:35 business_rules.py
-rw-r--r--  1 raeanthonylew raeanthonylew    0 Oct 19 14:35 commands.md
-rw-r--r--  1 raeanthonylew raeanthonylew    0 Oct 19 14:35 main.py
-rw-r--r--  1 raeanthonylew raeanthonylew   91 Oct 19 14:20 requirements.txt
drwxr-xr-x  3 raeanthonylew raeanthonylew 4096 Oct 19 14:43 tests
(.venv) DESKTOP-FJGPNR6% rm -r .git
rm: cannot remove '.git': No such file or directory
(.venv) DESKTOP-FJGPNR6% git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: will change to "main" in Git 3.0. To configure the initial branch name
hint: to use in all of your new repositories, which will suppress this warning,
hint: call:
hint:
hint:   git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint:   git branch -m <name>
hint:
hint: Disable this message with "git config set advice.defaultBranchName false"
Initialized empty Git repository in /home/raeanthonylew/ism3232/ism3232-midterm/.git/
(.venv) DESKTOP-FJGPNR6% cd tests
(.venv) DESKTOP-FJGPNR6% ll
total 12
drwxr-xr-x 3 raeanthonylew raeanthonylew 4096 Oct 19 14:43 .
drwxr-xr-x 5 raeanthonylew raeanthonylew 4096 Oct 19 14:48 ..
drwxr-xr-x 7 raeanthonylew raeanthonylew 4096 Oct 19 14:45 .git
-rw-r--r-- 1 raeanthonylew raeanthonylew    0 Oct 19 14:36 __init__.py
-rw-r--r-- 1 raeanthonylew raeanthonylew    0 Oct 19 14:36 test_business_rules.py
(.venv) DESKTOP-FJGPNR6% rm -r .git
rm: remove write-protected regular file '.git/objects/da/bf1b07543787505fc9d797d7ca18496b0e4cc6'? y
rm: remove write-protected regular file '.git/objects/e6/9de29bb2d1d6434b8b29ae775ad8c2e48c5391'? y
rm: remove write-protected regular file '.git/objects/e9/824c5846a1627f6904cf67c342af29fc24e7bc'?
rm: cannot remove '.git/objects/e9': Directory not empty
(.venv) DESKTOP-FJGPNR6% ll
total 12
drwxr-xr-x 3 raeanthonylew raeanthonylew 4096 Oct 19 14:43 .
drwxr-xr-x 5 raeanthonylew raeanthonylew 4096 Oct 19 14:48 ..
drwxr-xr-x 3 raeanthonylew raeanthonylew 4096 Oct 19 14:52 .git
-rw-r--r-- 1 raeanthonylew raeanthonylew    0 Oct 19 14:36 __init__.py
-rw-r--r-- 1 raeanthonylew raeanthonylew    0 Oct 19 14:36 test_business_rules.py
(.venv) DESKTOP-FJGPNR6% rm -r .git
rm: remove write-protected regular file '.git/objects/e9/824c5846a1627f6904cf67c342af29fc24e7bc'? y
(.venv) DESKTOP-FJGPNR6% ll
total 8
drwxr-xr-x 2 raeanthonylew raeanthonylew 4096 Oct 19 14:52 .
drwxr-xr-x 5 raeanthonylew raeanthonylew 4096 Oct 19 14:48 ..
-rw-r--r-- 1 raeanthonylew raeanthonylew    0 Oct 19 14:36 __init__.py
-rw-r--r-- 1 raeanthonylew raeanthonylew    0 Oct 19 14:36 test_business_rules.py
(.venv) DESKTOP-FJGPNR6% cd ..
(.venv) DESKTOP-FJGPNR6% pwd
/home/raeanthonylew/ism3232/ism3232-midterm
(.venv) DESKTOP-FJGPNR6% git init
Reinitialized existing Git repository in /home/raeanthonylew/ism3232/ism3232-midterm/.git/
(.venv) DESKTOP-FJGPNR6% git add .
(.venv) DESKTOP-FJGPNR6% git commit -m "Pre-setup for Brightline Print Shop"
[master (root-commit) 5f12481] Pre-setup for Brightline Print Shop
 8 files changed, 9 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
 create mode 100644 business_rules.py
 create mode 100644 commands.md
 create mode 100644 main.py
 create mode 100644 requirements.txt
 create mode 100644 tests/__init__.py
 create mode 100644 tests/test_business_rules.py
(.venv) DESKTOP-FJGPNR6% git remote add origin https://github.com/Rae-A-L/ism3232-midterm.git
git branch -M main
git push -u origin main
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 14 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 581 bytes | 290.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/Rae-A-L/ism3232-midterm.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
(.venv) DESKTOP-FJGPNR6% code .

## 2. The Virtual Enviroment
Output: /home/raeanthonylew/ism3232/ism3232-midterm/.venv/bin/python3

It shows that it is running from the .venv instead of the systems Python. 

## 3. The project structure 
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

__pycahce__ doesn't show on my GitHub because it has files that Git does not track.

## 4. Every functions and test 

business_rules.py
1:def calculate_print_cost(copy_price: float, copies: int) -> float:
6:def get_volume_discount(copies: int, student_org: bool = False) -> float:
19:def calculate_job_total(
34:def requires_proof(total: float) -> bool:
42:def needs_overnight_run(copies: int, total: float) -> bool:
50:def total_invoiced(jobs: list) -> float:
60:def largest_job(jobs: list) -> str:
74:def format_job_line(title: str, total: float, proof: bool, overnight_run: bool) -> str:

commands.md
121:hint: Using 'master' as the name for the initial branch. This default branch name
126:hint:   git config --global init.defaultBranch <name>
133:hint: Disable this message with "git config set advice.defaultBranchName false"
205:hint: Using 'master' as the name for the initial branch. This default branch name
210:hint:   git config --global init.defaultBranch <name>
217:hint: Disable this message with "git config set advice.defaultBranchName false"

tests/test_business_rules.py
13:def test_calculate_print_cost():
17:def test_discount_below_200():
21:def test_discount_200():
25:def test_discount_999():
29:def test_discount_1000():
33:def test_student_org_discount():
37:def test_student_org_1000():
41:def test_setup_fee_add():
45:def test_setup_fee_exact():
49:def test_proof_above():
53:def test_proof_above_limit():
57:def test_overnight_500_copies():
61:def test_overnight_copies_over():
65:def test_overnight_400():
69:def test_overnight_over():
73:def test_total_invoice_adds_every_job():
81:def test_total_invoice_empty_list():
85:def test_largest_job_goes_first():
93:def test_largest_job_empty_list_is_empty_string():
97:def test_job_line_yes_no():

Business_rules.py defines 8 functions, and tests/test_business_rules.py defines 20 tests.

## 5. Which files print

business_rules.py
tests/test_business_rules.py
main.py

All of the python files contain print, and business_rules.py is on the list because it is in the functions and definitions. 

## 6. The commit history

git log --oneline
c493bb6 (HEAD -> main, origin/main) Part 5: Listing the evidence and proof that I built the project (Step 1)
1c3f485 Part 4: Test functions and limits at least 20 (complete)
61fecb1 Part 4: Test functions and limits (3/4 check)
d4ced98 Part 3: Put the functions in main.py to generate the job report
bb1dc29 Part 2: Added functions for discounts, totals, proof checks, and overnight runs
5f12481 Pre-setup for Brightline Print Shop

There were 6 commits at that point. 