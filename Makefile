export LIBPATH := ".venv"
mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
MKDIR := $(dir $(mkfile_path))
VERSION_NEW := ${shell git tag -l v[0-9]* | sort -V -r | head -n1 |  awk '/v/{split($$NF,v,/[.]/); $$NF=v[1]"."v[2]"."++v[3]}1'}


compile: 
	@pip install -q -r requirements.txt -t $(LIBPATH)

test: 
	@PYTHONPATH=$(LIBPATH) python -m pytest

staging:
	# twine upload --repository-url https://test.pypi.org/legacy/ dist/*

package:
	rm -rf dist
	@echo "$(VERSION_NEW)" > VERSION
	git tag "$(VERSION_NEW)"
	PYTHONPATH=$(LIBPATH) python setup.py sdist

publish: package
	twine upload dist/*
	# git push --tags

clean:
	find . -name "*.pyc" -delete
	find . -name "*.sw*" -delete
	find . -name "__pycache__" -delete
	rm -rf $(LIBPATH)

version:
	@echo "$(VERSION)"

.PHONY: test clean
