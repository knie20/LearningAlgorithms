set PYTHONPATH=.

REM   Update, as needed, to point to your own Python installation or
REM   just eliminate if you already have Python executables in your path
REM   ------------------------------------------------------------------
set PYTHON3=python

echo "Running test cases -- should take about 15 minutes."
%PYTHON3% -m unittest discover > tests.txt

echo "Generating figures and tables for the book. This will take about six hours."
%PYTHON3% book.py > book.txt

echo "Generating Timing results for each chapter. Should take about one hour."
%PYTHON3% algs\timing.py > algs.txt
%PYTHON3% ch02\timing.py > ch02.txt
%PYTHON3% ch03\timing.py > ch03.txt
%PYTHON3% ch04\timing.py > ch04.txt
%PYTHON3% ch05\timing.py > ch05.txt
%PYTHON3% ch07\timing.py > ch07.txt

echo "Generating challenge exercises for each chapter. Should take about two hours."
%PYTHON3% ch01\challenge.py > ch01.txt
%PYTHON3% ch02\challenge.py > ch02.txt
%PYTHON3% ch03\challenge.py > ch03.txt
%PYTHON3% ch04\challenge.py > ch04.txt
%PYTHON3% ch05\challenge.py > ch05.txt
%PYTHON3% ch06\challenge.py > ch06.txt
%PYTHON3% ch07\challenge.py > ch07.txt
