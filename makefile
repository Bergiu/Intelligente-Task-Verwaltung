SHELL := /bin/sh
DIA_C = dia
DIA_SRCS=$(shell find -type f -iname "*.dia")
DIA_OBJS=$(DIA_SRCS:.dia=.png)
ODG_C = dia
ODG_SRCS=$(shell find -type f -iname "*.odg")
ODG_OBJS=$(ODG_SRCS:.odg=.pdf)

all: dia odg

# build them all
dia: $(DIA_OBJS)

%.png: %.dia
	$(DIA_C) $< -e $@

odg: $(ODG_OBJS)

%.pdf: %.odg
	libreoffice --convert-to pdf $@
