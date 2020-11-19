# result.json should be a telegram export file
cat result.json | jq '.messages[] | select(.from == "$1") | .text' | sed 's/^./\u/g' | sed 's/\"$/./g' | sed 's/\"//g' | tr "\n" " " > $2.txt


