SHELL := /bin/bash

BLOCKDIR := ../blocks/blocks/xcosblocks

SRCFILES := $(sort $(wildcard Xcos/common/*.py))
SRCFILES += $(sort $(wildcard Xcos/blocks/*.py))
SRCFILES += $(sort $(wildcard Xcos/ports/*.py))
SRCFILES += $(sort $(wildcard Xcos/links/*.py))

IMPORT := Xcos/xcosblocks.py
TARGET := xcosblocks.py
TARGET2 := $(BLOCKDIR)/$(TARGET)

all : $(IMPORT) $(TARGET) $(TARGET2)

$(IMPORT) : $(SRCFILES)
	@echo Making $@ ...
	@for f in $^; do \
	    g=$${f%.py}; \
	    g=$${g#Xcos/}; \
	    g=$${g//\//.}; \
	    echo "from $$g import *"; \
	done > $@

$(TARGET) : $(SRCFILES)
	@echo Making $@ ...
	@for f in $^; do \
	    echo "# BEGIN $$f"; \
	    echo; \
	    echo; \
	    cat "$$f"; \
	    echo; \
	    echo "# END $$f"; \
	done > $@

flake8 : $(TARGET)
	flake8 --statistics $(TARGET)

.xcosblocks.txt : $(TARGET) Xcos/parsexcosblocks.awk
	@echo Making $@ ...
	@Xcos/parsexcosblocks.awk $(TARGET) > $@

.srcflake8 : $(TARGET) .xcosblocks.txt Xcos/usexcosblocks.awk
	@echo 'flake8 common/*.py blocks/*.py ports/*.py links/*.py'
	@flake8 $(TARGET) | Xcos/usexcosblocks.awk .xcosblocks.txt -; \
	    exit $${PIPESTATUS[0]}
	touch $@

$(TARGET2) : .srcflake8
	cp -f $(TARGET) $@
