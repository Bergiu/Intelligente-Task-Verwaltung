#!/bin/sh


# goto project root
cd `dirname $0`/../docs

for file in $(find -type f -iname "*.dia")
do
	diff="$(git diff HEAD^ --name-only --diff-filter=ACMR "$file")"
	if [ ! -z "$diff" ]
	then
		dirname=$(dirname $file);
		base=$(basename $file);
		name=${base%.*};
		ext=${base##*.};
		dia $dirname/$base -e $dirname/$name.png
	fi
done
