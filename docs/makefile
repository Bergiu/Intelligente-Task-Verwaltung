SHELL := /bin/sh
# config for dia
DIA_C = dia
DIA_SRCS=$(shell find -type f -iname "*.dia")
DIA_OBJS=$(DIA_SRCS:.dia=.png)
# config for libre office documents
ODG_C = libreoffice
ODG_SRCS=$(shell find -type f -iname "*.odg")
ODG_OBJS=$(ODG_SRCS:.odg=.pdf)

# build them all
all: dia odg

dia: $(DIA_OBJS)

%.png: %.dia
	$(DIA_C) $< -e $@

odg: $(ODG_OBJS)

%.pdf: %.odg
	$(ODG_C) --convert-to pdf $<

clean:
	rm $(ODG_OBJS) $(DIA_OBJS)
