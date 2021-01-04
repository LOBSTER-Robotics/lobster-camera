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

v4l2-ctl -d0 -v width=1920,height=1080,pixelformat=MJPG

v4l2-ctl -d0 -V

echo "Is this good?"

yes_or_no || exit 1

v4l2-ctl -d0 --stream-count 1000 --stream-mmap --stream-to file.mjpeg

echo "Convert with ffmpeg?"

yes_or_no || exit 1

ffmpeg -i file.mjpeg file.mp4
