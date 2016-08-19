#!/bin/bash

echo ""
echo "Hi! Welcome to Indian Olympics Medal Tally Updater"
echo ""
echo "Please be patient, this may take some moment"
echo ""

curl -s http://www.nbcolympics.com/medals > temp.html
python olym.py

echo ""
echo "Hey! $USER, I'll remind you as soon as India wins another medal!"
echo ""

while [ 1 ]
do
	curl -s http://www.nbcolympics.com/medals > temp.html
	python update.py
done