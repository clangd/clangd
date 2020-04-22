#!/bin/bash -ex

SMALLER="-strip -define png:compression-filter=3"
PAD_TO="-background none -gravity center -extent"
LOGO_ONLY="--export-id=CD --export-background-opacity=0"
CONTRAST="-level 20%,100%,1.4"
inkscape clangd.svg $LOGO_ONLY --export-plain-svg=logo.svg
inkscape clangd.svg --export-png=card.png -h=640
mogrify $SMALLER card.png
inkscape clangd.svg --export-png=logo.png -h=1024 $LOGO_ONLY
mogrify $SMALLER $PAD_TO 1024x1024 logo.png
inkscape clangd.svg --export-png=favicon.png -h=16 $LOGO_ONLY --export-area-snap
mogrify -define png:exclude-chunk=all $CONTRAST $PAD_TO 16x16 favicon.png

# Set CARD="vscode coc www" to generate cards with subtitles.
for CARD in $CARDS; do
  xmlstarlet < clangd.svg edit -P \
    --update "//*[@id='subtitle']/*[local-name()='tspan']" --value "$CARD" \
    | inkscape - --export-png=card-$CARD.png -h=640
  mogrify $SMALLER card-$CARD.png
done
