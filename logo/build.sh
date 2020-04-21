#!/bin/bash -ex

inkscape clangd.svg --export-png=card.png -h=640
SMALLER="-strip -define png:compression-filter=3"
PAD_TO="-background none -gravity center -extent"
LOGO_ONLY="--export-id=CD --export-background-opacity=0"
CONTRAST="-level 20%,100%,1.4"
mogrify $SMALLER card.png
inkscape clangd.svg --export-png=logo.png -h=1024 $LOGO_ONLY
mogrify $SMALLER $PAD_TO 1024x1024 logo.png
inkscape clangd.svg --export-png=favicon.png -h=16 $LOGO_ONLY --export-area-snap
mogrify -define png:exclude-chunk=all $CONTRAST $PAD_TO 16x16 favicon.png
