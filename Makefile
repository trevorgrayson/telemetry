LIBPATH=venv
PYTHON?=python3

export PYTHONPATH = $(LIBPATH)

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
MKDIR := $(dir $(mkfile_path))
VERSION_NEW := ${shell git tag -l v[0-9]* | sort -V -r | head -n1 |  awk '/v/{split($$NF,v,/[.]/); $$NF=v[1]"."v[2]"."++v[3]}1'}


compile: $(LIBPATH)
$(LIBPATH): requirements.txt requirements/*
	$(PYTHON) -m pip -V || wget -qO- https://bootstrap.pypa.io/get-pip.py | python
	$(PYTHON) -m pip install --target $(LIBPATH) -r requirements.txt 
	touch $(LIBPATH)

test: compile
	$(PYTHON) -m pytest

tox: compile
	tox

staging:
	# twine upload --repository-url https://test.pypi.org/legacy/ dist/*

package: compile
	rm -rf dist
	@echo "$(VERSION_NEW)" > VERSION
	git tag "$(VERSION_NEW)"
	$(PYTHON) setup.py sdist

publish: package
	$(PYTHON) -m twine upload dist/* || echo "ERROR: pushing to pypi. Already uploaded?"
	# git push --tags

clean:
	find . -name "*.pyc" -delete
	find . -name "*.sw*" -delete
	find . -name "__pycache__" -delete
	rm -rf $(LIBPATH)

version:
	@echo "$(VERSION)"

.PHONY: test clean
