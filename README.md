## App for any usb dac
<img src="https://drive.google.com/uc?id=19Ji3oPgKkJSHb8GmZWtcm0Q3Zm6JTawI" width="auto" height="200"/>
<br>
 <strong>Manual</strong>
<br>
don't set sample rate to "maximum option available", that will do audio resampling and you don't want that! (you can if you want) Set sampling rate according to what you hear. Bit depth instead should always be the highest available, whereas 32bit seems to be the highest the best usb dacs can handle. App will reconfigure pulseaudio daemon.conf file.
<br>

## Usage
from terminal
```
python3 Ubuntu-Audio-App.py
```
user will be prompted for his password
