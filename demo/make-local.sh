#!/bin/sh
# Wraps each published fragment into a standalone page that opens straight from disk.
# Edit the fragments only; rerun this after every change.
#   automaton-designer.html -> index.html
#   xylophone.html          -> xylophone-local.html
#   xylophone-player.html   -> xylophone-player-local.html
cd "$(dirname "$0")"
wrap() {
  {
    printf '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    printf '<style>body{margin:0}[hidden]{display:none!important}</style>\n</head>\n<body>\n'
    cat "$1"
    printf '\n</body>\n</html>\n'
  } > "$2"
  echo "wrote $(pwd)/$2"
}
wrap automaton-designer.html index.html
wrap xylophone.html xylophone-local.html
wrap xylophone-player.html xylophone-player-local.html
