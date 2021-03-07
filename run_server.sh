#!/bin/bash

python manage.py runserver 0.0.0.0:5000 &
pr1=$!
npm start 0.0.0.0:8000 &
pr2=$!

echo $pr1 " , " $pr2 > process.txt

cndd
echo "do you want to kill the process (y/n)"
read cndd

if [ $cndd=="y" ]
then
	pkill node
	pkill npm
	pkill python
fi 
