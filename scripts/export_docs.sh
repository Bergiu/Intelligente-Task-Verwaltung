#!/bin/sh


# goto project root
cd `dirname $0`/../
for file in $(find docs -type f -iname "*.dia")
do
	# entweder git diff
	diff="$(git diff HEAD^ --name-only --diff-filter=ACMR "$file")"
	dirname=$(dirname $file);
	base=$(basename $file);
	name=${base%.*};
	ext=${base##*.};
	if [ ! -z "$diff" ]
	then
		dia $dirname/$base -e $dirname/$name.png
	fi
done
