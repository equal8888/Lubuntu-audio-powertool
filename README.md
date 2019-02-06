## Now with ALSA 😉
<img src="https://drive.google.com/uc?id=1SUkGyXMAlLDD6wMpfgIOYbf75QFv_0mi" width="auto" height="200"/>
<br>
 <strong>Current Development stage 0.5 </strong> 😔
<br>
<br>
Tested on <strong>un-updated</strong> 64-bit Lubuntu (16.04.3 LTS) Link -->
<br>
http://cdimage.ubuntu.com/lubuntu/releases/16.04/release/lubuntu-16.04.3-desktop-amd64.iso
<br>

## Usage

run command from terminal
```
sudo ./Ubuntu-Audio-App.py
```

## Prerequisites

this should cover everything
```
sudo apt-get install python3-tk
```

## Troubleshoot

Cannot run the app
```
chmod +x  Ubuntu-Audio-App/*
```

ALSA page issues
<br>
ALSA might not work if the user allready has his own ALSA config. Create required /etc/asound.conf manually with following parameters *CASE SENSITIVE*:
```
defaults.pcm.card 1
defaults.ctl.card 1
```

## Known issues

if PulseAudio is removed --> During system reboot user MIGHT login to openbox desktop env.

workaround to lxde enviroment, has black color scheme and icons are not the same (With pure ALSA)
```
sudo apt-get install lxde -y && sudo apt install lxde-common
```

get back to Lubuntu enviroment (with PulseAudio)
```
sudo apt-get install alsa-base pulseaudio -y && sudo apt-get install lubuntu-desktop -y && sudo apt-get install lxde -y
```
