#!/bin/bash

# корневая директория
root='/home/vgnlkn'
# если введен 1 аргумент
if [ $# -lt 1 ] 
then
	file=$1
# иначе используем файл по-умолчанию
else
	file="/home/vgnlkn/lb2/fortests/file.exe"
fi
counter=0

# получаем список всех ссылок внутри директории root
links=`find $root -type l`
# рассматриваем каждую ссылку
for link in $links
do 
	# получаем информацию о ссылке
	link_description=`ls -l $link`
	# узнаем на какой файл указывает ссылка
	link_to=`echo $link_description | cut -d ' ' -f 11`
	# если указывает на заданный файл
	if [ "$link_to" = "$file" ]
	then
		# получаем путь к ссылке
		link_addr=`echo $link_description | cut -d ' ' -f 9`
		echo $link_addr
		counter=$((counter+1))
	fi
done

echo "There're $counter links on $file"





