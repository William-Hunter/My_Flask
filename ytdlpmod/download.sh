#!/bin/bash

### you-get下载油管资源

echo $1
echo $2
url=$1
_type=$2
folder=$3

#/opt/setproxy.sh

export http_proxy=http://127.0.0.1:7890 && export https_proxy=http://127.0.0.1:7890

#downloader=yt-dlp
downloader=/opt/workspace/flask/ytdlpmod/yt-dlp_linux


#video_root=/opt/data/sync/folders/outsider
video_root=/opt/data/media/Video
audio_root=/opt/data/media/Audio
#audio_root=/opt/data/sync/folders/Podcast

if [ "mp3" == "$_type" ]; then
	echo 'mp3'
	mkdir -p $audio_root/$folder && cd $audio_root/$folder \
	&& $downloader --extract-audio --format 'bestaudio' --audio-format 'mp3'  $url
else
	mkdir -p $video_root/$folder && cd $video_root/$folder
	if [ "mp4" == "$_type" ]; then
		echo 'mp4'
		$downloader -f 'bv[ext=mp4]+ba[ext=m4a]' $url
	elif [ "normal" == "$_type" ]; then
		echo 'normal'
		$downloader -f 'bv[ext=mp4]+ba[ext=m4a]' $url
	elif [ "HD" == "$_type" ]; then
		echo 'HD'
		$downloader -f 'bv[height=1080][ext=mp4]+ba[ext=m4a]' $url
	fi
fi

echo '下载完毕'

