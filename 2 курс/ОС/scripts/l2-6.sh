#!/bin/bash

folder="fortests/"
> $folder/file-example
od -tc $folder/file-example
sentence="Accumsan malesuada eu a hymenaeos faucibus, bibendum convallis faucibus. Mi tempus fringilla quam sodales pellentesque"

echo "Some changes were made..."
echo $sentence >> $folder/file-example
od -tc $folder/file-example

sentence="Accumsan malesuada \0x0\neu a hymenaeos"
echo "Some changes were made..."
echo $sentence > $folder/file-example
od -tc $folder/file-example
