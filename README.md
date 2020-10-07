## Audio Powertool
[![Header](https://github.com/equal8888/Lubuntu-audio-powertool/blob/master/audiopowertool.png "Header")]()
<br>
 <strong>Current Development stage 0.7 </strong> 😔
<br>
Enables configuration of PulseAudio & ALSA.
<br>
<br>
Tested on 64-bit Lubuntu (16.04.3 LTS) Link -->
http://cdimage.ubuntu.com/lubuntu/releases/16.04/release/lubuntu-16.04.3-desktop-amd64.iso
<br>
<br>
In theory should work on other Debian/Lubuntu/Ubuntu versions but untested for now
<br>

## Usage

run command from terminal
```
sudo ./audiopowertool.py
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

1) If system is updated -> select tab 'System Config (OS)' else skip to step 2 <br>
Uninstall PulseAudio and let the OS reboot on its own.

2) From the tab 'ALSA (Hardware Mixer)'
Select Scan Devices <br>
type the corresponding name of your sound device & press Enter from keyboard

3) From the tab 'System Config (OS)'
Select Alsa compatible Browser <br>
Install Chromium to get audio from www-browser

4) Type in the terminal (replace "X" with the soundcard name)

```
amixer -c X cset name='IEC958 Playback Switch' on
```

5) Reboot
