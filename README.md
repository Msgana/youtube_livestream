Youtube_LiveStream

This Youtube_LiveStream repository is developed and used by the Phoenix College NASA Ascend Team.

Description and Background
This program is developed to stream a live video feed to the Phoenix College NASA Ascend youtube channel. 

Hardware
Below is a list of the hardware used to for the system.

RaspberryPi 3B
Raspberrpi mini Camera module 10MP

Platform to run python script

Python Libraries
Below is a list of python dependencies.
import subprocess
Create Youtube Beta account and get stream url and key

How it works
stream.py is apython code that runs a subprocess of bash script that will tell the raspi-cam to start taking a video stream using the raspivid command tool to stream it to Phoenix College NASA ASCEND youtube channel. 

APRS packet received through SDR (Primary Callsign)
APRS packet received from APRS-IS (Primary Callsign)
It then determines the azimuth and elevation angles to send back to the Arduino Mega. Finally, the Arduino Mega sends instructions to turn the rotors to the calculated position.

Troubleshooting
The rasperrypi cameras tend to break quickly make sure there is a back up camera in case there is an issue.

Notes
The program runs as long as there is a connection between the payload and the ground station. There might be a short delay untill all the packets arrive to be streamed to youtube.

If there is a internet outage or disconnection the program will remain running and continues once there is internet available.

Wiring
Attach the camera to the correct place on the raspberrypi

License
Add License info here. Include link to license file

About
Phoenix College NASA Ascend place logo here

Contact
misganayohannes@gmail.com    sam@gmail.com

