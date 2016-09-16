# Convenience makefile to set up the environment and build the documentation

python = python2.7

all: p-env/bin/pip docs

docs: docs/html/index.html

docs/html/index.html: README.rst docs/_static/css/* docs/_templates/* p-env/bin/sphinx-build docs_sources preprocess_sources
	@p-env/bin/sphinx-build -W docs docs/html
	@touch $@
	@echo "Documentation was generated at '$@'."

docs_sources: docs/*.rst docs/project_specific/*.rst

preprocess_sources: docs/project_specific/*.rst.jinja2
	p-env/bin/python code/bin/generate-docs

# NOTE: This requires you to have plantuml installed, so it's not hooked into
# any of the standard targets. Run it on demand.
plantuml: docs/diagrams/*.plantuml
	plantuml -tsvg $^


p-env/bin/sphinx-build: p-env/bin/pip
	@touch $@

p-env/bin/pip: p-env/bin/python
	p-env/bin/pip install -r requirements.txt

p-env/bin/python:
	virtualenv -p $(python) --no-site-packages p-env
	@touch $@


clean: clean_generated
	@rm -rf .Python p-env docs/html

clean_generated:
	@find -type f -iname '*_generated.rst' -delete

.PHONY: all docs clean preprocess_sources
