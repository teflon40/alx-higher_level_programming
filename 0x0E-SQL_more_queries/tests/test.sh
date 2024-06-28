#!/usr/bin/bash

DIRPATH="/root/alx-higher_level_programming/0x0E-SQL_more_queries/tests/"

if [ $# -eq 1 ]
then
	TEST=$DIRPATH$1
	cat $TEST | mysql -hlocalhost -uroot -p hbtn_0d_usa
else
	echo "Usage: test.sh <sql file>"
fi
