all : blocks/__init__.py

SRCFILES := $(sort $(filter-out blocks/__init__.py, $(wildcard blocks/*.py)))

blocks/__init__.py : $(SRCFILES)
	@echo Making $@ ...
	@for f in $^; do \
	    echo "### $$f"; \
	    cat "$$f"; \
	    echo; \
	done > $@
