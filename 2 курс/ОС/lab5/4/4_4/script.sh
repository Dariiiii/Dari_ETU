#!/bin/bash

for i in {1..100}
do
    ( echo -e "hi $i\n" ) | ( ./client & )
  
done
