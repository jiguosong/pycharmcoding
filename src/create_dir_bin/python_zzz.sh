#!/bin/sh

MYCM=$1
pwdname=${PWD##*/}

bpath='/home/songjiguo/PycharmProjects/interviewCode/src/'

mkdir $MYCM

sed -e s/XXX/$MYCM/g $bpath/python_template.txt > $MYCM/$MYCM.py
sed -e s/XXX/$MYCM/g $bpath/pytest_template.txt > $MYCM/$MYCM\_test.py

sed -i s/YYY/$pwdname/g $MYCM/$MYCM.py
sed -i s/YYY/$pwdname/g $MYCM/$MYCM\_test.py
