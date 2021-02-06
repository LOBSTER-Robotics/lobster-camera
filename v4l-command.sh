#!/bin/bash

function usage {
	echo "Usage: $(basename $0) [-h] [-d CAMERA] [-l] [-r] [-c] [-i] [-f FILE] files"
        echo "  -h          print this help message"
        echo '  -d CAMERA   use /dev/video$(CAMERA) for recording.'
        echo "  -l          list recording properties"
        echo "  -r          record in raw. This will be in lower FPS"
        echo "  -f FILE     filename for converting or storing the recording."
        echo "  -c FILE     convert the file specified with -f and output it to \$FILE Use -r for converting raw footage."
        echo "  -i          use interactive mode"

}

FPS=60
USE_RAW=0
FILE_ARG=""
CONVERT_OUTPUT=""

function convert_and_quit {
        echo "converting with ffmpeg"
        if [ $USE_RAW == 1 ]
        then
                ffmpeg -r $FPS -pix_fmt uyvy422 -f rawvideo -s 1920x1080 -i "$FILE_ARG" "$CONVERT_OUTPUT"
        else
                ffmpeg -r $FPS -f mjpeg -i "$FILE_ARG" "$CONVERT_OUTPUT"
        fi
        exit 0
}

INTERACTIVE=0

function yes_or_no {
    if [ $INTERACTIVE == 0 ]
    then
            return 0
    fi
    while true; do
        read -p "$* [y/N]: " yn
        case $yn in
            [Yy]*) return 0  ;;  
            *) echo "Aborting" ; return  1 ;;
        esac
    done
}

CAMERA=0
LIST_AND_QUIT=0
PIXELFORMAT=MJPG
CONVERT=0

while getopts 'hd:lrc:f:i' c
do
	case $c in
		h) usage; exit ;;
		d) CAMERA="$OPTARG"; echo "Setting camera device to $CAMERA" ;;
		l) LIST_AND_QUIT=1 ;;
		r) USE_RAW=1; FPS=60; PIXELFORMAT=UYVY ;;
		f) FILE_ARG="$OPTARG" ;;
		c) CONVERT=1; CONVERT_OUTPUT="$OPTARG" ;;
                i) INTERACTIVE=1 ;;
	esac
done

# hoogste resolutie: 2304x1536 -- MJPG -- 48 fps
WIDTH_HEIGHT_PF="width=1920,height=1080,pixelformat=$PIXELFORMAT"

if [ $CONVERT == 1 ]
then
        convert_and_quit "$FILE_ARG"
fi

v4l2-ctl -d"$CAMERA" -v $WIDTH_HEIGHT_PF

v4l2-ctl -d"$CAMERA" -V

v4l2-ctl -d"$CAMERA" --list-frameintervals $WIDTH_HEIGHT_PF

if [ $LIST_AND_QUIT == 1 ]
then
        exit 0
fi


if [ $INTERACTIVE == 1 ]
then
        echo "Is this good?"
        yes_or_no || exit 1
fi


v4l2-ctl -d"$CAMERA" --stream-user --stream-to "$FILE_ARG"

if [ $INTERACTIVE == 1 ]
then
        echo "Convert with ffmpeg?"
        yes_or_no || exit 1
fi


