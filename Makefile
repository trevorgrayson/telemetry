export
PYTHONPATH := "venv"
VIRTDIR := ./venv
VERSION := ${shell git tag -l v[0-9]* | sort -r | head -n1}
VERSION_NEW := ${shell git tag -l v[0-9]* | sort -r | head -n1 |  awk '/v/{split($NF,v,/[.]/); $NF=v[1]"."v[2]"."++v[3]}1'}

virtualenv:
	@[ -d $(VIRTDIR) ] || virtualenv -q $(VIRTDIR)
	@. $(VIRTDIR)/bin/activate

compile: virtualenv 
	@pip install -q -r requirements.txt

test: compile
# maybe use env command?
	@PYTHONPATH=$(PYTHONPATH) python -m pytest

publish:
	git pull --tags
	python setup.py sdist upload
	git tag $(VERSION)
	git push --tags

clean:
	find . -name "*.pyc" -delete
	find . -name "*.sw*" -delete

version:
	@echo "$(VERSION)"

.EXPORT_ALL_VARIABLES:
.PHONY: test clean
