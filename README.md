## App for audio tweaks
<img src="https://drive.google.com/uc?id=1uHj9NVVXV8XsdvtcsAnOdiv8MxiheALA" width="auto" height="200"/>
<br>
 <strong>Manual</strong>
<br>
<br>
This is a software mixer. don't set sample rate to "maximum option available", that will do audio resampling and you don't want that! Set sampling rate according to what you hear. Bit depth instead should always be the highest available what your hardware can handle. App will reconfigure pulseaudio daemon.conf file.
<br>
<br>
Tested on Lubuntu (16.04 LTS)
<br>

## Usage

from terminal
```
python3 Ubuntu-Audio-App.py
```

user will be prompted for his password

## Troubleshoot

button show samplerate wont work ?

```
sudo apt-get install libnotify-bin
```
