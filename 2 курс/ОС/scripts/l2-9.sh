#!/bin/bash

echo chmod [-Rv] mode file
echo Опция –R используется для изменения прав доступа ко всем файлам в указанном каталоге и в подкаталогах. Права доступа, mode, записываются в следующем виде:
echo [who]operator[permissions][,symbolic_mode]
echo "Здесь who указывает для кого необходимо изменить права доступа, и может принимать одно из следующих значений: u (для владельца файла), g (для группы-владельца), o (для всех остальных) или a (для всех). Operator указывает действие: + (добавить право), - (удалить право) или = (задать права на чтение, запись и выполнение). Permissions указывает собственно права, которые должны быть изменены: r (чтение), w (запись), x (выполнение), s (право на выполнение файла от имени его владельца, то есть SUID (если в поле who содержится или подразумевается u), или от имени группы-владельца, то есть SGID (если в поле who содержится или подразумевается g)) и другие."

sudo ls -l fortests-chmod
echo "Разрешить все для всех"
sudo chmod ugo+rwx -R fortests-chmod
ls -l fortests-chmod
echo "Отобрать право на исполнение для владельца:"
sudo chmod u-x -R fortests-chmod 
sudo ls -l fortests-chmod
echo "Отобрать право на запись для остальных пользователей:"
sudo chmod o-w -R fortests-chmod 
sudo ls -l fortests-chmod
echo "Отобрать право на чтение для группы файлов:"
sudo chmod g-r -R fortests-chmod 
sudo ls -l fortests-chmod

echo "chown -- change owner -- сменить владельца"
echo "chgrp -- change group -- сменить группу"
echo "Поменяем владельца файлу fortests-chmod/1 на root"
sudo ls -l fortests-chmod/1
sudo chown root fortests-chmod/1
echo "После изменения"
sudo ls -l fortests-chmod/1
echo "set group ID upon execution — «установка ID группы во время выполнения») являются флагами прав доступа в Unix, которые разрешают пользователям запускать исполняемые файлы с правами владельца или группы исполняемого файла."
echo "установим файлу fortests-chmod/2 SUID флаг"
sudo ls -l fortests-chmod/2
chmod +s fortests-chmod/2
sudo ls -l fortests-chmod/2
