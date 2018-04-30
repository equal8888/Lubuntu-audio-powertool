#!/bin/bash

# default alsa
dmixmax=$(grep "# defaults.pcm.dmix.max_periods 0" /usr/share/alsa/alsa.conf) && sudo sed -i "/${dmixmax}/ c defaults.pcm.dmix.max_periods 0" /usr/share/alsa/alsa.conf &&
dmixrate=$(grep "# defaults.pcm.dmix.rate 48000" /usr/share/alsa/alsa.conf) && sudo sed -i "/${dmixrate}/ c defaults.pcm.dmix.rate 48000" /usr/share/alsa/alsa.conf &&
currentaltsamplerate=$(grep "# defaults.pcm.dmix.format" /usr/share/alsa/alsa.conf) && sudo sed -i "/${currentaltsamplerate}/ c defaults.pcm.dmix.format" /usr/share/alsa/alsa.conf &&
dmixcard0=$(grep "# defaults.pcm.dmix.card defaults.pcm.card" /usr/share/alsa/alsa.conf) && sudo sed -i "/${dmixcard0}/ c defaults.pcm.dmix.card defaults.pcm.card" /usr/share/alsa/alsa.conf &&
dmixcard2=$(grep "# defaults.pcm.dmix.device defaults.pcm.device" /usr/share/alsa/alsa.conf) && sudo sed -i "/${dmixcard2}/ c defaults.pcm.dmix.device defaults.pcm.device" /usr/share/alsa/alsa.conf &&
dmixcard3=$(grep "# pcm.dmix cards.pcm.dmix" /usr/share/alsa/alsa.conf) && sudo sed -i "/${dmixcard3}/ c pcm.dmix cards.pcm.dmix" /usr/share/alsa/alsa.conf &&

# default asound.conf
sudo sed -i '/^/d' /etc/asound.conf &&

# default pulseaudio config

# default bitdepth
currentbitrate=$(grep "default-sample-format" /etc/pulse/daemon.conf) && sudo sed -i "/${currentbitrate}/ c ; default-sample-format = s16le" /etc/pulse/daemon.conf &&

# default sample rate's
currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c ; default-sample-rate = 44100" /etc/pulse/daemon.conf &&
currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c ; alternate-sample-rate = 44100" /etc/pulse/daemon.conf &&

# default resample
currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c ; resample-method = speex-float-1" /etc/pulse/daemon.conf &&

# start Everything
sudo alsa force-reload && pulseaudio -k &&

# Script finished
echo "Everything Default !"
