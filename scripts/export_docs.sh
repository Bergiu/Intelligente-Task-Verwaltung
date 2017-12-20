#!/bin/sh


# goto project root
echo dirname: `dirname $0`
echo `pwd`
cd `dirname $0`/../docs
echo `pwd`

for file in $(find -type f -iname "*.dia")
do
	echo file: $file;
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
