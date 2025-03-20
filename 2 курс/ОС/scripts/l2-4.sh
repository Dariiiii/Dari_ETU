#!/bin/bash
counter=0
# корневая директория
root='/home'
file=""

# если введен 1 аргумент
if [ $# -lt 1 ] 
then
	file=$1
# иначе используем файл по-умолчанию
else
	file="/home/vgnlkn/lb2/fortests/file.exe"
fi
# цикл по всем ссылкам внутри корневой директории
for f in `find -L $root -samefile $file`
do
	# если тип найденного файла -- сылка
	# вывод его на экран
	if [[ -n `ls -l $f | grep ^l` ]]
	then
		echo $f
	fi
done

