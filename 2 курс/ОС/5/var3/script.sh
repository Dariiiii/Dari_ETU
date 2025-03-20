#!/bin/bash

# loop through 10 times
for i in {1..300}
do
   echo -e "hi $i \n" | ./client &
  
done

