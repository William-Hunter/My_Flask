#!/bin/bash

script_path=/opt/workspace/flask/ytdlpmod/BBdown
video_path=/opt/data/sync/folders/outsider

url=$1
folder=$2

cookie=`cat $script_path/BBDown.data` && echo $cookie

mkdir -p $video_path/$folder \
&& cd $video_path/$folder \
&& $script_path/BBDown $url --skip-subtitle -c $cookie

echo '下载完毕'
