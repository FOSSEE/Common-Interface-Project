SHELL := /bin/bash

BLOCKDIR := blocks/xcosblocks

COMMONSRCFILES := $(sort $(wildcard Xcos/common/*.py))
SRCFILES := $(COMMONSRCFILES)
BLOCKSRCFILES := $(sort $(wildcard Xcos/blocks/*.py))
SRCFILES += $(BLOCKSRCFILES)
PORTSRCFILES := $(sort $(wildcard Xcos/ports/*.py))
SRCFILES += $(PORTSRCFILES)
LINKSRCFILES := $(sort $(wildcard Xcos/links/*.py))
SRCFILES += $(LINKSRCFILES)

XCOS2XMLFILES := $(sort $(wildcard xcos2xml/head.xsl))
XCOS2XMLFILES += $(sort $(wildcard xcos2xml/blocks/*.xsl))
XCOS2XMLFILES += $(sort $(wildcard xcos2xml/ports/*.xsl))
XCOS2XMLFILES += $(sort $(wildcard xcos2xml/links/*.xsl))
XCOS2XMLFILES += $(sort $(wildcard xcos2xml/foot.xsl))

SEDFILE := xcosblocks.sed
TARGET := Xcos/xcosblocks.py
TARGET2 := $(BLOCKDIR)/xcosblocks.py
TARGET3 := eda-frontend/public/xcos2xml.xsl

all : $(SEDFILE) $(TARGET) $(TARGET2) $(TARGET3)

$(SEDFILE) : Makefile $(BLOCKSRCFILES) $(PORTSRCFILES) $(LINKSRCFILES)
	@echo Making $@ ...
	@( \
		sed -n 's/^def \([^(]*\).*/s,^\\( *\\(return\\)\\? \\)\\(\1(\\),\\1Blocks.\\3,/p' $(BLOCKSRCFILES); \
		sed -n 's/^def \([^(]*\).*/s,^\\( *\\(return\\)\\? \\)\\(\1(\\),\\1Ports.\\3,/p' $(PORTSRCFILES); \
		sed -n 's/^def \([^(]*\).*/s,^\\( *\\(return\\)\\? \\)\\(\1(\\),\\1Links.\\3,/p' $(LINKSRCFILES); \
	) > $@

$(TARGET) : xcosblocks.sed $(SRCFILES)
	@echo Making $@ ...
	@( \
		for f in $(COMMONSRCFILES); do \
	    echo "# BEGIN $$f"; \
	    sed -e '/^from \(blocks\|common\|links\|ports\)\..* import /d' "$$f"; \
	    echo; \
	    echo "# END $$f"; \
		done; \
		echo; \
		echo; \
	  echo 'class Blocks:'; \
		for f in $(BLOCKSRCFILES); do \
	    echo; \
	    echo "    # BEGIN $$f"; \
	    sed -e '/^from \(blocks\|common\|links\|ports\)\..* import /d' -e '/^$$/N;/^\n$$/D' "$$f" | sed 's/^\(.\)/    \1/'; \
	    echo "    # END $$f"; \
		done; \
		echo; \
		echo; \
	  echo 'class Ports:'; \
		for f in $(PORTSRCFILES); do \
	    echo; \
	    echo "    # BEGIN $$f"; \
	    sed -e '/^from \(blocks\|common\|links\|ports\)\..* import /d' -e '/^$$/N;/^\n$$/D' "$$f" | sed 's/^\(.\)/    \1/'; \
	    echo "    # END $$f"; \
		done; \
		echo; \
		echo; \
	  echo 'class Links:'; \
		for f in $(LINKSRCFILES); do \
	    echo; \
	    echo "    # BEGIN $$f"; \
	    sed -e '/^from \(blocks\|common\|links\|ports\)\..* import /d' -e '/^$$/N;/^\n$$/D' "$$f" | sed 's/^\(.\)/    \1/'; \
	    echo "    # END $$f"; \
		done; \
	) > $@
	@sed -i -f $< $@

flake8 : $(TARGET)
	flake8 --statistics

.srcflake8 : $(TARGET)
	@echo 'flake8 common/*.py blocks/*.py ports/*.py links/*.py'
	@flake8 $(TARGET)
	touch $@

$(TARGET2) : .srcflake8
	cp -f $(TARGET) $@

$(TARGET3) : $(XCOS2XMLFILES)
	@echo Making $@ ...
	@for f in $^; do \
	    cat "$$f"; \
	done > $@
