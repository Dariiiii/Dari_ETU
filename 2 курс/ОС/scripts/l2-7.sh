#!/bin/bash

directory='fortests/'
echo `du $directory -hs`
mkdir $directory/1
mkdir $directory/2
mkdir $directory/3
mkdir $directory/4
> $directory/1.txt
> $directory/2.txt
> $directory/3.txt
> $directory/4.txt
echo Created 4 directories and 4 files
echo `du $directory -hs`
rm $directory/1 -r
rm $directory/2 -r
rm $directory/3 -r
rm $directory/4 -r
rm $directory/*.txt
echo Removed early created files
echo `du $directory -hs`
