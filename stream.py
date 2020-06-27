import picamera
from subprocess import call
from datetime import datetime
from time import sleep


#Streamkey from the youtube channel (key changes sometimes!)

print "starting youtube livestream ....."

print("Live streaming started!")

# Video streaming to youtube 
liveStreamCommand = 'raspivid -o - -t 0 -vf -hf -fps 20 -b 4500000 | ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv youTubeUrl/youTubeStreamKey'

#excute the live streaming command
call([liveStreamCommand], shell=True)
