﻿## App for audio tweaks
<img src="https://drive.google.com/uc?id=1UbZ4iKPcL0MTqFVs3c9A6ejGVs_8CzED" width="auto" height="200"/>
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

Some buttons wont work ?

```
sudo apt-get install libnotify-bin

```

On app root directory


```
sudo chmod +x alsa-settings.sh

sudo chmod +x default-settings.sh

```

