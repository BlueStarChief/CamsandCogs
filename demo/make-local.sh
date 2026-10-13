#!/bin/sh
# Wraps the published fragment (automaton-designer.html) into a standalone page (index.html)
# that opens straight from disk. Edit the fragment only; rerun this after every change.
cd "$(dirname "$0")"
{
  printf '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
  printf '<style>body{margin:0}[hidden]{display:none!important}</style>\n</head>\n<body>\n'
  cat automaton-designer.html
  printf '\n</body>\n</html>\n'
} > index.html
echo "wrote $(pwd)/index.html"
