#!/bin/bash
while true
do
   v=$(shuf -i 5-20 -n 1)
   curl -X POST http://localhost:3000/climate/temp/$v
   sleep 1
done
