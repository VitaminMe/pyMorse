init:
	py -m pip install -r requirements.txt
test:
	py -m unittest discover tests
run:
	py main.py
