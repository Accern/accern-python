help:
	@echo "The following make targets are available:"
	@echo "dev	install all deps for dev env"
	@echo "docs	create pydocs for all relveant modules"
	@echo "test	run all tests with coverage"

clean:
	rm -rf dist/*

dev:
	pip install coverage
	pip install codecov
	pip install pylint
	pip install twine
	pip install -e .

docs:
	$(MAKE) -C docs html

lint-comment:
	! find . -name '*.py' -and -not -path './venv/*' | xargs grep -nE '#.*(todo|xxx|fixme|n[oO][tT][eE]:|Note:|nopep8\s*$)'

lint-pycodestyle:
	pycodestyle --exclude=venv --ignore=E266,E501,W503 .

lint-pylint:
	find . -name '*.py' -and -not -path './venv/*' | sort | tee /dev/tty | xargs pylint -j 6 -d E0602,W0511,R0205,C0111,C0103,C0301,R0913,R0902,R0903

package:
	python setup.py sdist
	python setup.py bdist_wheel

test:
	coverage run -m unittest discover
	coverage html
