#!/bin/bash

#root="/usr/lib"
root="/home/vgnlkn/lb2"
#root="/"

# если введен 1 аргумент
if [ $# -lt 1 ] 
then
	file=$1
# иначе используем файл по-умолчанию
else
	file="fortests/file.exe"
fi

# inode входного файла
file_inode=`ls -li $file | cut -d ' ' -f 1 | tr -d " "`

# проходимся по каждой директории
for dir in `du $root | cut -f 2`
do
	# достаем все файлы с нужным inode
	files=`ls -li $dir | grep $file_inode`
	if [[ -n $files ]]
	then	
		# вывод результата
		echo "$dir :"
		echo "$files"
	fi
done
