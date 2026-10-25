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