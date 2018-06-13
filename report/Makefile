SRC="./src"
OUT="./out"
FILE="25965158-Kelvin-report"

pdf:
	pandoc $(SRC)/* \
		-o $(OUT)/$(FILE).pdf \
		--tab-stop 2 \
		--bibliography=references.bib \
		--template=./templates/template.tex

tex:
	pandoc $(SRC)/* \
		-o $(OUT)/$(FILE).tex \
		--tab-stop 2 \
		--bibliography=references.bib \
		--template=./templates/template.tex
