## App for audio tweaks
<img src="https://drive.google.com/uc?id=1snjZFm5inBeYqGPHspc6e3qs-XYH-3UL" width="auto" height="200"/>
<br>
 <strong>Manual</strong>
<br>
don't set sample rate to "maximum option available", that will do audio resampling and you don't want that! Set sampling rate according to what you hear. Bit depth instead should always be the highest available what your hardware can handle. App will reconfigure pulseaudio daemon.conf file.
<br>
<br>
Tested on Lubuntu (15.04 & 16.04)
<br>

## Usage

from terminal
```
python3 Ubuntu-Audio-App.py
```

user will be prompted for his password
