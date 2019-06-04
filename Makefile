export PYTHONPATH = "src:venv"
VIRTDIR=./venv

virtualenv:
	@[ -d $(VIRTDIR) ] || virtualenv -q $(VIRTDIR)
	@. $(VIRTDIR)/bin/activate

compile: virtualenv 
	@pip install -q -r requirements.txt

test: compile
	@PYTHONPATH=src python -m pytest


.EXPORT_ALL_VARIABLES:
.PHONY: test
