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

1 Cannot run the app)
install " python3-tk " and chmod some files on app root directory
```
sudo apt-get install python3-tk
chmod +x  Ubuntu-Audio-App/*
```
2 ALSA page issues)
ALSA might not work if the user allready has his own ALSA config. Create required /etc/asound.conf manually with following parameters *CASE SENSITIVE*:
```
defaults.pcm.card 1
defaults.ctl.card 1
```

## Known issues

Alsa page might not work currently on systems with pulseaudio installed. (Update is coming for this)
