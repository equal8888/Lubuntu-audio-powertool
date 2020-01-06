## Audio Powertool
<img src="https://drive.google.com/uc?id=1BIkDhjF2F5TDhPeoBiACK9HKKYnJNBbE" width="auto" height="200"/>
<br>
 <strong>Current Development stage 0.7 </strong> 😔
<br>
Enables configuration of PulseAudio, ALSA & Operating System for Audio Playback devices.
<br>
<br>
Tested on 64-bit Lubuntu (16.04.3 LTS) Link -->
http://cdimage.ubuntu.com/lubuntu/releases/16.04/release/lubuntu-16.04.3-desktop-amd64.iso
<br>
In theory should work on other Debian/Lubuntu/Ubuntu versions but untested for now
## Usage

run command from terminal
```
./audiopowertool.py
```

## Prerequisites

this should cover everything
```
sudo apt-get install python3-tk
```

## Troubleshoot

1) Cannot run the app ? Make it executable with a command
```
chmod +x audiopowertool.py
```

2) The app will ask password from terminal.
Why ? Because of better combatibility

## Here is my settings
Just in case your interested 

1) From the tab 'System Config (OS)' <br>
Uninstall PulseAudio and let the OS reboot on its own

2) From the tab 'ALSA (Hardware Mixer)'
Select Scan Devices <br>
type the number of your sound device & press Enter from keyboard

