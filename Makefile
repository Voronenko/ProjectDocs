# Convenience makefile to set up the environment and build the documentation

python = python3.6

all: .v-env/bin/pip docs

docs: out/html/index.html

out/html/index.html: README.rst docs/_static/css/* docs/_templates/* .venv/bin/sphinx-build docs_sources preprocess_sources
	@.venv/bin/sphinx-build -W docs out/html
	@touch $@
	@echo "Documentation was generated at '$@'."

docs_sources: docs/*.rst docs/project_specific/*.rst

preprocess_sources: docs/project_specific/*.rst.jinja2
	.venv/bin/python code/bin/generate-docs

# NOTE: This requires you to have plantuml installed, so it's not hooked into
# any of the standard targets. Run it on demand.
plantuml: docs/diagrams/*.plantuml
	docker/plantuml -tsvg $^


.venv/bin/sphinx-build: .venv/bin/pip
	@touch $@

.venv/bin/pip: .venv/bin/python
	.venv/bin/pip install -r requirements.txt

.venv/bin/python:
# virtualenv eliminated
	@touch $@


clean: clean_generated
	@rm -rf .Python out

clean_generated:
	@find -type f -iname '*_generated.rst' -delete

.PHONY: all docs clean preprocess_sources

epub: README.rst docs/_static/css/* docs/_templates/* .venv/bin/sphinx-build docs_sources preprocess_sources
	@.venv/bin/sphinx-build -b epub -W docs -Q -D exclude_patterns=['**/*.doctrees*'] out/epub
	@echo "Build finished. The e-Pub pages are generated at 'out/epub'."

#mobi: README.rst docs/_static/css/* docs/_templates/* .venv/bin/sphinx-build docs_sources preprocess_sources
#	@.venv/bin/sphinx-build -b mobi -W docs -Q -D exclude_patterns=['**/*.doctrees*'] out/mobi
#	@echo "Build finished. The Mobi pages are generated at 'out/mobi'."

pdf: README.rst docs/_static/css/* docs/_templates/* .venv/bin/sphinx-build docs_sources preprocess_sources
	@.venv/bin/sphinx-build -b pdf -W docs -Q -D exclude_patterns=['**/*.doctrees*'] out/pdf
	@echo "Build finished. The Pdf pages are generated at 'out/pdf'."
