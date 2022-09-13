SRCFILES := $(sort $(wildcard common/*.py))
SRCFILES += $(sort $(wildcard blocks/*.py))
SRCFILES += $(sort $(wildcard ports/*.py))
SRCFILES += $(sort $(wildcard links/*.py))

TARGET := xcosblocks.py

all : $(TARGET)

$(TARGET) : $(SRCFILES)
	@echo Making $@ ...
	@for f in $^; do \
	    echo "### $$f"; \
	    echo; \
	    cat "$$f"; \
	    echo; \
	done > $@
