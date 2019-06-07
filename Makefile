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

clean:
	find . -name "*.pyc" -delete
	find . -name "*.sw*" -delete

.EXPORT_ALL_VARIABLES:
.PHONY: test clean
