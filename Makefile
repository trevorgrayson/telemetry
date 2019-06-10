PYTHONPATH := "venv"
VIRTDIR := ./venv
mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
MKDIR := $(dir $(mkfile_path))
VERSION_NEW := ${shell git tag -l v[0-9]* | sort -V -r | head -n1 |  awk '/v/{split($$NF,v,/[.]/); $$NF=v[1]"."v[2]"."++v[3]}1'}


virtualenv:
	@[ -d $(VIRTDIR) ] || virtualenv -q $(VIRTDIR)
	@. $(VIRTDIR)/bin/activate

compile: 
	@pip install -q -r requirements.txt

test: compile
	# maybe use env command?
	@PYTHONPATH=$(PYTHONPATH) python -m pytest

staging:
	# twine upload --repository-url https://test.pypi.org/legacy/ dist/*

publish:
	@echo $(VERSION_NEW)
	rm -rf dist
	# git tag "$(VERSION_NEW)"
	echo "$(VERSION_NEW)" > VERSION
	python setup.py sdist
	# twine upload dist/*
	# git push --tags

clean:
	find . -name "*.pyc" -delete
	find . -name "*.sw*" -delete
	find . -name "__pycache__" -delete
	rm -rf venv

version:
	@echo "$(VERSION)"

.EXPORT_ALL_VARIABLES:
.PHONY: test clean
