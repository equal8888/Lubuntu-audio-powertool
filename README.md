## App for audio tweaks
<img src="https://drive.google.com/uc?id=1rc1VOeYE7tynZliLVu6sUqeqWavtIGvA" width="auto" height="200"/>
<br>
 <strong>Manual</strong>
<br>
<br>
First time: set sudo password from preferences menu and restart the application. From Pulseaudio samplerate: Safe option is 48,000 Hz. don't set sample rate to "maximum option available", that will do audio resampling and you don't want that! Bit depth instead should always be the highest available what your hardware can handle. App will reconfigure pulseaudio daemon.conf file.
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

Some buttons wont work ?

```
sudo apt-get install libnotify-bin

```

On app root directory


```
sudo chmod +x alsa-settings.sh

sudo chmod +x default-settings-pulseaudio.sh

```
