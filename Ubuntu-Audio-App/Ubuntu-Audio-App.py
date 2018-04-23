#!/usr/bin/env python3
import tkinter
from tkinter import *
import tkinter.messagebox    #coming soon.
from tkinter import ttk, Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, E, W
import subprocess
import os
import os.path         #used to check the system path.
import time            #used to put the program to sleep.
import datetime        #used to get the current time.
import readline        #enables user to have inline editing and history.

class MyFirstGUI1:
    def __init__(self, master):
        window = master
        master.minsize(width=790, height=225)
        master.maxsize(width=790, height=225)
        master.title("Ubuntu Audio Settings")
        master.geometry("100x500")

        fm = Frame(master, bg="blue")
        label = Label(fm, text=" Set bitdepth")
        label.pack(side=TOP, anchor=NW)

        # Terminal

#        termf = Frame(master)
#        termf.pack(fill=BOTH, expand=YES)
#        wid = termf.winfo_id()
#        os.system('lxterminal -into[ expr [winfo id .f ]] -e $env(EDITOR) &')


        # Notify

        #

        Setbit1_button = Button(fm, text="   16bit   ", command=self.Setbit1)
        Setbit1_button.pack(side=TOP, anchor=NW)

        Setbit2_button = Button(fm, text="   24bit   ", command=self.Setbit2)
        Setbit2_button.pack(side=TOP, anchor=NW)
        fm.pack(fill=BOTH)

        fm2 = Frame(master)
        label = Label(fm2, text="Set primary quality ->")
        label.pack(side=LEFT, anchor=NW, fill=X, expand=YES)

        Set1_button = Button(fm2, text="44,100 Hz", command=self.Set1)
        Set1_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)

        Set2_button = Button(fm2, text="48,000 Hz", command=self.Set2)
        Set2_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)

        Set3_button = Button(fm2, text="88,200 Hz", command=self.Set3)
        Set3_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)

        Set4_button = Button(fm2, text="96,000 Hz", command=self.Set4)
        Set4_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)

        Set5_button = Button(fm2, text="192,000 Hz", command=self.Set5)
        Set5_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        fm2.pack(fill=BOTH)

        fm3 = Frame(master)
        label = Label(master, text="Set alternative quality ->")
        label.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        Setalt1_button = Button(master, text="44,100 Hz", command=self.Setalt1)
        Setalt1_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)

        Setalt2_button = Button(master, text="48,000 Hz", command=self.Setalt2)
        Setalt2_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)

        Setalt3_button = Button(master, text="88,200 Hz", command=self.Setalt3)
        Setalt3_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)

        Setalt4_button = Button(master, text="96,000 Hz", command=self.Setalt4)
        Setalt4_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)

        Setalt5_button = Button(master, text="192,000 Hz", command=self.Setalt5)
        Setalt5_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        fm3.pack(fill=BOTH, padx=10)

        ttk.Separator(root).place(x=0, y=131, relwidth=10)

        fm4 = Frame(master)
        label = Label(text="Resample method")
        label.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        label.place(relx=1, x=-782, y=135)

        SetRe1_button = Button(text="Default", command=self.SetRe1)
        SetRe1_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        SetRe1_button.place(relx=1, x=-663, y=134)

        SetRe2_button = Button(master, text="Fastest", command=self.SetRe2)
        SetRe2_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        SetRe2_button.place(relx=1, x=-592, y=134)

        SetRe3_button = Button(master, text="Medium quality", command=self.SetRe3)
        SetRe3_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        SetRe3_button.place(relx=1, x=-521, y=134)

        SetRe4_button = Button(master, text="Best quality", command=self.SetRe4)
        SetRe4_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        SetRe4_button.place(relx=1, x=-400, y=134)

        SetRe5_button = Button(master, text="Zero order hold", command=self.SetRe5)
        SetRe5_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        SetRe5_button.place(relx=1, x=-301, y=134)

        SetRe6_button = Button(master, text="SRC Linear", command=self.SetRe6)
        SetRe6_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        SetRe6_button.place(relx=1, x=-663, y=163)

        SetRe7_button = Button(master, text="Trivial", command=self.SetRe7)
        SetRe7_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        SetRe7_button.place(relx=1, x=-570, y=163)

        SetRe8_button = Button(master, text="Speed float N", command=self.SetRe8)
        SetRe8_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        SetRe8_button.place(relx=1, x=-507, y=163)

        SetRe9_button = Button(master, text="Speed fixed N", command=self.SetRe9)
        SetRe9_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        SetRe9_button.place(relx=1, x=-398, y=163)

        SetRe10_button = Button(master, text="ffmpeg", command=self.SetRe10)
        SetRe10_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        SetRe10_button.place(relx=1, x=-286, y=163)

        SetRe11_button = Button(master, text="soxr-mq", command=self.SetRe11)
        SetRe11_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        SetRe11_button.place(relx=1, x=-663, y=191)

        SetRe12_button = Button(master, text="soxr-hq", command=self.SetRe12)
        SetRe12_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        SetRe12_button.place(relx=1, x=-586, y=191)

        SetRe13_button = Button(master, text="soxr-vhq", command=self.SetRe13)
        SetRe13_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        SetRe13_button.place(relx=1, x=-513, y=191)
        fm4.pack(fill=BOTH)

        fm5 = Frame(master)
        Test_button = Button(master, text="Show current sample rate", command=self.Test)
        Test_button.pack()
        Test_button.place(relx=1, x=-2, y=2, anchor=NE)

        Confirm_button = Button(master, text="Apply !", command=self.Confirm)
        Confirm_button.pack()
        Confirm_button.place(relx=1, x=-140, y=191)

        close_button = Button(master, text="Close", command=master.quit)
        close_button.pack()
        close_button.place(relx=1, x=-65, y=191)
        fm5.pack(fill=BOTH)

    def Setbit1(self):
           subprocess.call('currentbitrate=$(grep "default-sample-format" /etc/pulse/daemon.conf) && sudo sed -i "/${currentbitrate}/ c default-sample-format = s16le" /etc/pulse/daemon.conf', shell=True)

    def Setbit2(self):
           subprocess.call('currentbitrate=$(grep "default-sample-format" /etc/pulse/daemon.conf) && sudo sed -i "/${currentbitrate}/ c default-sample-format = s24le" /etc/pulse/daemon.conf', shell=True)


    def Set1(self):
           subprocess.call('currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c default-sample-rate = 44000" /etc/pulse/daemon.conf', shell=True)

    def Set2(self):
           subprocess.call('currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c default-sample-rate = 48000" /etc/pulse/daemon.conf', shell=True)

    def Set3(self):
           subprocess.call('currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c default-sample-rate = 88000" /etc/pulse/daemon.conf', shell=True)

    def Set4(self):
           subprocess.call('currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c default-sample-rate = 96000" /etc/pulse/daemon.conf', shell=True)

    def Set5(self):
           subprocess.call('currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c default-sample-rate = 192000" /etc/pulse/daemon.conf', shell=True)


    def Setalt1(self):
           subprocess.call('currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c alternate-sample-rate = 44000" /etc/pulse/daemon.conf', shell=True)

    def Setalt2(self):
           subprocess.call('currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c alternate-sample-rate = 48000" /etc/pulse/daemon.conf', shell=True)

    def Setalt3(self):
           subprocess.call('currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c alternate-sample-rate = 88000" /etc/pulse/daemon.conf', shell=True)

    def Setalt4(self):
           subprocess.call('currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c alternate-sample-rate = 96000" /etc/pulse/daemon.conf', shell=True)

    def Setalt5(self):
           subprocess.call('currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c alternate-sample-rate = 192000" /etc/pulse/daemon.conf', shell=True)


    def SetRe1(self):
           subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = speex-float-1" /etc/pulse/daemon.conf', shell=True)

    def SetRe2(self):
           subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = src-sinc-fastest" /etc/pulse/daemon.conf', shell=True)

    def SetRe3(self):
           subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = src-sinc-medium-quality" /etc/pulse/daemon.conf', shell=True)

    def SetRe4(self):
           subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = src-sinc-best-quality" /etc/pulse/daemon.conf', shell=True)

    def SetRe5(self):
           subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = src-zero-order-hold" /etc/pulse/daemon.conf', shell=True)

    def SetRe6(self):
           subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = src-linear" /etc/pulse/daemon.conf', shell=True)

    def SetRe7(self):
           subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = trivial" /etc/pulse/daemon.conf', shell=True)

    def SetRe8(self):
           subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = speex-float-N" /etc/pulse/daemon.conf', shell=True)

    def SetRe9(self):
           subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = speex-fixed-N" /etc/pulse/daemon.conf', shell=True)

    def SetRe10(self):
           subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = ffmpeg" /etc/pulse/daemon.conf', shell=True)

    def SetRe11(self):
           subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = soxr-mq" /etc/pulse/daemon.conf', shell=True)

    def SetRe12(self):
           subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = soxr-hq" /etc/pulse/daemon.conf', shell=True)

    def SetRe13(self):
           subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = soxr-vhq" /etc/pulse/daemon.conf', shell=True)

    def Test(self):
           #subprocess.call('pacmd list-sinks | grep sample', shell=True)
           os.system('clear')
           cmd14="pacmd list-sinks | grep sample"
           os.system(cmd14)

    def Confirm(self):
           subprocess.call('pulseaudio --kill && pulseaudio --start', shell=True)

    # notification

    def notify():
        global sixthFrame
        global notify

        notifycmd ="notify-send APT-Mananger 'Operation Finished'"
        conf.write("notification=enabled\n")
        conf.write("EOF")
        conf.close()
        sixthFrame.destroy()


root = Tk()
my_gui = MyFirstGUI1(root)
root.mainloop()
