#!/bin/bash

function toMp3(){
	mp4=$1 
	mp3_name=$2
	/usr/bin/ffmpeg -i ./$mp4 -vn -c:a mp3 ./$mp3_name
}

function remove(){
	mp4=$1
	/usr/bin/mv ./$mp4 /root/Trash/
	echo 'removed'	
}

function processOne(){
	if [ "*.mp4" == "$1" ]; then
		return 0
	fi
	mp4=$1
	echo $mp4
	mp3_name=`echo $mp4 | sed -e "s/mp4/mp3/g" `
	echo $mp3_name
	toMp3 $mp4 $mp3_name && remove $mp4
}

function listAll(){
	IFS=`echo -e "\n"`
	for mp4 in *.mp4
	do
		echo "------"
		processOne $mp4
	done
}

if [ "" == "$kind" ]; then
	work_path=./
else
	work_path=$1
fi

cd $work_path

#cd /opt/data/media/Music/

/usr/bin/mv ./*.cmt.xml /root/Trash/

listAll

exit 0