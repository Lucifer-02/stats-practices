render:
	xfce4-terminal --tab --title render --command="mdbook serve --open ./Stat/translate"

watch:
	xfce4-terminal --tab --title render --command="mdbook watch ./Stat/translate/"

edit:
	cd 
	# ./Stat/translate/src/

run: render watch edit
