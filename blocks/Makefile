SHELL := /bin/bash

BLOCKDIR := blocks/xcosblocks

SRCFILES := $(sort $(wildcard Xcos/common/*.py))
SRCFILES += $(sort $(wildcard Xcos/blocks/*.py))
SRCFILES += $(sort $(wildcard Xcos/ports/*.py))
SRCFILES += $(sort $(wildcard Xcos/links/*.py))

XCOS2XMLFILES := $(sort $(wildcard xcos2xml/head.xsl))
XCOS2XMLFILES += $(sort $(wildcard xcos2xml/blocks/*.xsl))
XCOS2XMLFILES += $(sort $(wildcard xcos2xml/ports/*.xsl))
XCOS2XMLFILES += $(sort $(wildcard xcos2xml/links/*.xsl))
XCOS2XMLFILES += $(sort $(wildcard xcos2xml/foot.xsl))

IMPORT := Xcos/xcosblocks.py
TARGET := xcosblocks.py
TARGET2 := $(BLOCKDIR)/$(TARGET)
TARGET3 := eda-frontend/public/xcos2xml.xsl

all : $(IMPORT) $(TARGET) $(TARGET2) $(TARGET3)

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
	    grep -v "from .* import" "$$f"; \
	    echo; \
	    echo "# END $$f"; \
	done > $@

flake8 : $(TARGET)
	flake8 --statistics

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

$(TARGET3) : $(XCOS2XMLFILES)
	@echo Making $@ ...
	@for f in $^; do \
	    cat "$$f"; \
	done > $@
