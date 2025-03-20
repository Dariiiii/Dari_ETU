#!/bin/bash 

# перечислены все типы файлов
file_types="- b c d l p s"

# цикл по каждому типу
for file_type in $file_types 
do
	# выводится рассматриваемый тип
	echo "Current type: $file_type"
	#  рекурсивно рассматриваются все переданного каталога 
	# ищется совпадение с рассматриваевым типом файла
	file_example=`ls -l -R $1 | grep ^$file_type | head -1`
	# если не пустая строка
	if [[ -n $file_example ]]
	then 
		# вывод информации о файле
		echo $file_example
		# 	запуск написанной утилиты, которая разбивает
		# вывод команды ls -l на слова и достает оттуда
		# имя файла
		file_name=`echo $file_example | ./splitter`
		# если тип -- регулярный файл
		if [ $file_type = '-' ]
		then
			# рекурсивно ищет путь до файла 
			file_path=`find $1 -name $file_name -type f | head -1`
		else
			# рекурсивно ищет путь до файла 
			file_path=`find $1 -name $file_name -type $file_type | head -1`
		fi
		# вывод полного пути
		echo "$file_name located at $file_path"
	else
		# если не нашли файл такого типа
		echo "Not found"
	fi
	echo ""
	
done