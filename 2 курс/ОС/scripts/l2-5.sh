#!/bin/bash

root="/"
types='f c d l s b p'

# цикл по всем типам файлов
for type in $types
do
	echo $type
	# получение расширенной инф-ии о типе заданного файла
	extended_info=`find $root -type $type -ls | head -1`
	if [[ -n $extended_info ]]
	then
		echo $extended_info
	else
		echo "Not found"
	fi
done





