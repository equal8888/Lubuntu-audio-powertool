## ALSA repo 😉
<img src="https://drive.google.com/uc?id=1SUkGyXMAlLDD6wMpfgIOYbf75QFv_0mi" width="auto" height="200"/>
<br>
 <strong>Current Development stage 0.57 </strong> 😔
<br>
<br>
Tested on Lubuntu (16.04 LTS)
<br>

## Usage

first time run command from terminal
```
sudo ./Ubuntu-Audio-App.py
```

after first time run "sudo" is no longer needed
```
./Ubuntu-Audio-App.py
```

## Prerequisites

this should cover everything
```
sudo apt-get install python3-tk
```

## Troubleshoot

1) Cannot run the app
run the command "sudo apt-get install python3-tk" and
chmod some files on app root directory
```
chmod +x  Ubuntu-Audio-App/*
```
2) ALSA page issues
ALSA might not work if the user allready has his own ALSA config. Create required /etc/asound.conf manually with following parameters *CASE SENSITIVE*:
```
   defaults.pcm.card 1
   defaults.ctl.card 1
```

## Known issues

Alsa page might not work currently on systems with pulseaudio installed. (Update is coming for this)
