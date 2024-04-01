#!/bin/bash

script_path=/opt/workspace/flask/ytdlpmod/BBdown
audio_path=/opt/data/media/Audio
#audio_path=/opt/data/sync/folders/Podcast

url=$1
folder=$2

cookie=`cat $script_path/BBDown.data` && echo $cookie

mkdir -p $audio_path/$folder \
&& cd $audio_path/$folder \
&& $script_path/BBDown $url --audio-only -c $cookie

#mv ./* $audio_path/

echo '下载完毕'
