#!/bin/bash

# default pulseaudio config

# default autospawn
sudo sed -i "/autospawn =/ c ; autospawn = yes" /etc/pulse/client.conf &&

# default bitdepth
sudo sed -i "/default-sample-format =/ c ; default-sample-format = s16le" /etc/pulse/daemon.conf &&

# default sample rate's
sudo sed -i "/default-sample-rate =/ c ; default-sample-rate = 44100" /etc/pulse/daemon.conf &&

sudo sed -i "/alternate-sample-rate =/ c ; alternate-sample-rate = 44100" /etc/pulse/daemon.conf &&

# default resample
sudo sed -i "/resample-method =/ c ; resample-method = speex-float-1" /etc/pulse/daemon.conf &&

# restart pulseaudio
pulseaudio --kill ; pulseaudio --start &&

# Script finished
echo "--------------------- Audio Powertool -----------------------" &&
GREEN='\033[0;32m'
NC='\033[0m' # No Color
printf "${GREEN} Pulseaudio${NC} Set to default !\n" &&

RED='\033[0;31m'
NC='\033[0m' # No Color
printf "${RED} Services${NC} Restarting (wait 3 seconds)\n" &&
echo "-------------------------------------------------------------"
