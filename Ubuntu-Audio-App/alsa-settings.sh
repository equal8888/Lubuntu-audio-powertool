#!/bin/bash

# Setup alsa

# defaults.pcm.dmix.max_periods 0
# defaults.pcm.dmix.rate 48000
# defaults.pcm.dmix.format
# defaults.pcm.dmix.card defaults.pcm.card
# defaults.pcm.dmix.device defaults.pcm.device
# pcm.dmix cards.pcm.dmix

dmixmax=$(grep "defaults.pcm.dmix.max_periods 0" /usr/share/alsa/alsa.conf) && sudo sed -i "/${dmixmax}/ c # defaults.pcm.dmix.max_periods 0" /usr/share/alsa/alsa.conf &&
dmixrate=$(grep "defaults.pcm.dmix.rate 48000" /usr/share/alsa/alsa.conf) && sudo sed -i "/${dmixrate}/ c # defaults.pcm.dmix.rate 48000" /usr/share/alsa/alsa.conf &&
currentaltsamplerate=$(grep "defaults.pcm.dmix.format 'unchanged'" /usr/share/alsa/alsa.conf) && sudo sed -i "/${currentaltsamplerate}/ c # defaults.pcm.dmix.format 'unchanged'" /usr/share/alsa/alsa.conf &&
dmixcard0=$(grep "defaults.pcm.dmix.card defaults.pcm.card" /usr/share/alsa/alsa.conf) && sudo sed -i "/${dmixcard0}/ c # defaults.pcm.dmix.card defaults.pcm.card" /usr/share/alsa/alsa.conf &&
dmixcard2=$(grep "defaults.pcm.dmix.device defaults.pcm.device" /usr/share/alsa/alsa.conf) && sudo sed -i "/${dmixcard2}/ c # defaults.pcm.dmix.device defaults.pcm.device" /usr/share/alsa/alsa.conf &&
dmixcard3=$(grep "pcm.dmix cards.pcm.dmix" /usr/share/alsa/alsa.conf) && sudo sed -i "/${dmixcard3}/ c # pcm.dmix cards.pcm.dmix" /usr/share/alsa/alsa.conf &&

# Create new asound.conf for hardware rendering
cd ~ &&
sudo cp Documents/gitfix/Ubuntu-Audio-App/asound.conf /etc/ &&

# Script finished
echo "ALSA: All Set !"
