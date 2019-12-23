# Youtube_LiveStream

This Youtube_LiveStream repository is developed and used by the Phoenix College NASA Ascend Team.

## Description and Background
This program is developed to stream a live video feed to the Phoenix College NASA Ascend youtube channel. 

## Hardware
Below is a list of the hardware used to for the system.
  * RaspberryPi 3B
  * Raspberrpi mini Camera module 10MP
  * Platform to run python script
  
## Python Libraries
Below is a list of python dependencies.
 * import subprocess
 * Create Youtube Beta account and get stream url and key

## How it works
stream.py is apython code that runs a subprocess of bash script that will tell the raspi-cam to start taking a video stream using the raspivid command tool to stream it to Phoenix College NASA ASCEND youtube channel. 

## Troubleshooting
The rasperrypi cameras tend to break quickly make sure there is a back up camera in case there is an issue.

## Notes
The program runs as long as there is a connection between the payload and the ground station. There might be a short delay untill all the packets arrive to be streamed to youtube.

If there is a internet outage or disconnection the program will remain running and continues once there is internet available.

## Wiring
Attach the camera to the correct place on the raspberrypi

## License
Add License info here. Include link to license file

## About
Phoenix College NASA Ascend place logo here


