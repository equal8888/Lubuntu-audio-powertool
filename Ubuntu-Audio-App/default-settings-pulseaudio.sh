#!/bin/bash

# default pulseaudio config

# default autospawn
pulsespawn=$(grep "autospawn" /etc/pulse/client.conf) && sudo sed -i "/${pulsespawn}/ c ; autospawn = yes" /etc/pulse/client.conf &&

# default bitdepth
currentbitrate=$(grep "default-sample-format" /etc/pulse/daemon.conf) && sudo sed -i "/${currentbitrate}/ c ; default-sample-format = s16le" /etc/pulse/daemon.conf &&

# default sample rate's
currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c ; default-sample-rate = 44100" /etc/pulse/daemon.conf &&
currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c ; alternate-sample-rate = 44100" /etc/pulse/daemon.conf &&

# default resample
currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c ; resample-method = speex-float-1" /etc/pulse/daemon.conf &&

# Script finished
echo "Pulseaudio Default"
