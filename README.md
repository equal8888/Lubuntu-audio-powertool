## App for audio tweaks (This isnt a real app !!! doesnt work on other peoples OS !!!)
<img src="https://drive.google.com/uc?id=1dZ4ZPrwCtNvj5mPGV1OACUt4DAI4EVBK" width="auto" height="200"/>
<br>
 <strong>Current Development stage 0.4 - 0.5 </strong>
<br>
<br>
 <strong>Manual</strong>
<br>
First time: set sudo password from preferences menu and restart the application. From Pulseaudio samplerate: Safe option is 48,000 Hz. don't set sample rate to "maximum option available", that will do audio resampling and you don't want that! Bit depth instead should always be the highest available what your hardware can handle. App will reconfigure pulseaudio daemon.conf file.
<br>
<br>
Tested on Lubuntu (16.04 LTS)
<br>

## Usage

cd to app root directory and run
```
python3 Ubuntu-Audio-App.py
```

## Troubleshoot

chmod some file on app root directory
```
sudo chmod +x default-settings-pulseaudio.sh
```

