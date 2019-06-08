export
TAGS := git pull --tags
PYTHONPATH := "venv"
VIRTDIR := ./venv
mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
MKDIR := $(dir $(mkfile_path))
VERSION_NEW := $(shell eval bin/version_new)


virtualenv:
	@[ -d $(VIRTDIR) ] || virtualenv -q $(VIRTDIR)
	@. $(VIRTDIR)/bin/activate

compile: virtualenv 
	@pip install -q -r requirements.txt

test: compile
	# maybe use env command?
	@PYTHONPATH=$(PYTHONPATH) python -m pytest

staging:
	# twine upload --repository-url https://test.pypi.org/legacy/ dist/*

publish:
	echo $(VERSION_NEW)
	# rm -rf dist
	# git tag "$(VERSION_NEW)"
	# python setup.py sdist
	# twine upload dist/*
	# git push --tags

clean:
	find . -name "*.pyc" -delete
	find . -name "*.sw*" -delete

version:
	@echo "$(VERSION)"

.EXPORT_ALL_VARIABLES:
.PHONY: test clean
