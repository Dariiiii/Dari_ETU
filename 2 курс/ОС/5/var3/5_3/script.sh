#!/bin/bash

for i in {1..3000000}
do
   echo -e "hi $i \n" | ./client &
  
done
