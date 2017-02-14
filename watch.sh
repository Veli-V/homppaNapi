# !/bin/bash
dir="/home/veli-v/Downloads"
echo $dir
arr=$("$dir"/*)
echo " mitä vittua??? : ${#arr[@]}"

for file in $arr
do
	echo "$file"
done

