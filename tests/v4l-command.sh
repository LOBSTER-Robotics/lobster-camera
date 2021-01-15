#!/bin/bash

function yes_or_no {
    while true; do
        read -p "$* [y/N]: " yn
        case $yn in
            [Yy]*) return 0  ;;  
            *) echo "Aborting" ; return  1 ;;
        esac
    done
}

CAMERA=0

while getopts 'hd:' c
do
	case $c in
		h) usage; exit ;;
		d) CAMERA="$OPTARG"; echo "Setting camera device to $CAMERA" ;;
	esac
done

v4l2-ctl -d"$CAMERA" -v width=1920,height=1080,pixelformat=MJPG

v4l2-ctl -d"$CAMERA" -V

echo "Is this good?"

yes_or_no || exit 1

v4l2-ctl -d"$CAMERA" --stream-user --stream-to file.mjpeg

echo "Convert with ffmpeg?"

yes_or_no || exit 1

ffmpeg -r 60 -f mjpeg -i file.mjpeg file.mp4
