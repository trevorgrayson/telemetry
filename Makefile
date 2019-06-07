export
PYTHONPATH := "src:venv"
VIRTDIR := ./venv

virtualenv:
	@[ -d $(VIRTDIR) ] || virtualenv -q $(VIRTDIR)
	@. $(VIRTDIR)/bin/activate

compile: virtualenv 
	@pip install -q -r requirements.txt

test: compile
# maybe use env command?
	@PYTHONPATH=$(PYTHONPATH) python -m pytest

deploy:
	python setup.py sdist bdist_wheel upload --universal
	git tag 0.2.0
	git push --tags

clean:
	find . -name "*.pyc" -delete
	find . -name "*.sw*" -delete

.EXPORT_ALL_VARIABLES:
.PHONY: test clean
