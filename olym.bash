#!/bin/bash

echo ""
echo "Hi! Welcome to Indian Olympics Medal Tally Updater"
echo ""
echo "Enter the country name."
echo -n "=> "
read country
echo "Please be patient, this may take some moment"
echo ""

curl -s http://www.nbcolympics.com/medals > .temp
python olym.py $country

echo ""
echo "Hey! $USER, I'll remind you as soon as $country wins another medal!"
echo ""

while [ 1 ]
do
	curl -s http://www.nbcolympics.com/medals > .temp
	python update.py $country
done