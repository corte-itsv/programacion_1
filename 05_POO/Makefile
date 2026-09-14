NAME := 05_POO
SRC  := main.tex

all:
	latexmk -pdf -interaction=nonstopmode -jobname=$(NAME) $(SRC)

watch:
	latexmk -pvc -pdf -interaction=nonstopmode -jobname=$(NAME) $(SRC)

clean:
	latexmk -c -jobname=$(NAME)

distclean:
	latexmk -CA -jobname=$(NAME) && rm -f *.bbl *.blg *.run.xml *-blx.bib

.PHONY: all watch clean distclean
