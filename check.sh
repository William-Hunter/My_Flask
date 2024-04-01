#!/bin/bash


resu=`lsof -i:5000`
#resu=`lsof -i:80`


if [ ! -n "$resu" ]; then
	echo "is null"
	cd /opt/workspace/flask && ./run.sh start
	echo "run flask"
else
	echo $resu
fi


