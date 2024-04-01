#!/bin/bash

### 使用you-get下载西瓜影视的资源


url=$1
kind=$2

echo "url=$1"
echo "kind=$2"

if [ "mp3" == "$kind" ]; then
    echo ' mp3'
    cd /opt/data/sync/folders/Music/
    /usr/local/bin/you-get $url && /opt/data/sync/folders/Music/convert2mp3.sh 
else 
    echo ' mp4'
#    cd /opt/data/sync/folders/Video/
    cd /opt/data/media/Video/
    /usr/local/bin/you-get $url 
fi

/usr/bin/mv ./*.cmt.xml /root/Trash/

echo 'END'



