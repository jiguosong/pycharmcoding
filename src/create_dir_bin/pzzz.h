#!/bin/sh

MYCM=$1
pwdname=${PWD##*/}

bpath='/home/songjiguo/PycharmProjects/interviewCode/src'
testpath='/home/songjiguo/PycharmProjects/interviewCode/test'

#mkdir $MYCM

sed -e s/XXX/$MYCM/g $bpath/python_template.txt > $bpath/$pwdname/$MYCM.py
sed -e s/XXX/$MYCM/g $bpath/pytest_template.txt > $testpath/$pwdname/$MYCM\_test.py

sed -i s/YYY/$pwdname/g $bpath/$pwdname/$MYCM.py
sed -i s/YYY/$pwdname/g $testpath/$pwdname/$MYCM\_test.py
