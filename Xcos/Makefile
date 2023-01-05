SRCFILES := $(sort $(wildcard common/*.py))
SRCFILES += $(sort $(wildcard blocks/*.py))
SRCFILES += $(sort $(wildcard ports/*.py))
SRCFILES += $(sort $(wildcard links/*.py))

TARGET := xcosblocks.py

all : $(TARGET)

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

srcflake8 : $(SRCFILES)
	flake8 $(SRCFILES)
