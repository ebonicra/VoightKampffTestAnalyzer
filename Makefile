all: run

run:
	python3 main.py

test:
	cd tests && coverage run -m pytest && coverage report

lint:
	python3 -m autopep8 --in-place *.py
	cd tests && python3 -m autopep8 --in-place *.py

doc:
	cd docs && make html

clean:
	rm -rf docs/build
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf user_responses.json
	rm -rf .coverage
	rm -rf tests/user_responses.json
	rm -rf tests/__pycache__
	rm -rf tests/.pytest_cache
	rm -rf tests/.coverage

install:
	python3 -m pip install -r ../requirements.txt