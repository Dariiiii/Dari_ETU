#!/bin/bash
# Скрипт демонстрирующий создание soft-ссылок
folder='/home/vgnlkn/lb2/fortests'
links_to_remove=`ls -l $folder | grep "^l" | cut -d ' ' -f 12`
for link in $links_to_remove
do
	rm $folder/$link
done

`ln -s $folder/file.exe $folder/symbolic-link-1`

