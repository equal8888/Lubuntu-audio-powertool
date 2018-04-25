#!/usr/bin/env python3
import tkinter
from tkinter import *
from tkinter import ttk, Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, E, W
import subprocess
import os

class AppGUI1:
    def __init__(self, master):
        window = master
        master.minsize(width=775, height=225)
        master.maxsize(width=775, height=225)
        master.title("Ubuntu Audio App")
        master.geometry("100x500")

        fm = Frame(master) # bg="blue"

        filename = PhotoImage(file = "desk03.gif")
        background_label = Label(fm, image=filename)
        background_label.image = filename # anchor
        background_label.place(x=50, y=0, relwidth=1, relheight=1)
        background_label.place()


        label = Label(fm, text=" Set bit depth")
        label.pack(side=TOP, anchor=NW)

        Setbit1_button = Button(fm, text="   16bit   ", command=self.Setbit1)
        Setbit1_button.pack(side=TOP, anchor=NW)

        Setbit2_button = Button(fm, text="   24bit   ", command=self.Setbit2)
        Setbit2_button.pack(side=TOP, anchor=NW)
        fm.pack(fill=BOTH)

        fm2 = Frame(master)
        label = Label(fm2, text="Set primary sample rate ->    ")
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
        label = Label(master, text="Set alternative sample rate ->")
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
        fm3.pack(fill=BOTH)

        ttk.Separator(root).place(x=0, y=131, relwidth=10)

        fm4 = Frame(master)
        label = Label(text="Resample method")
        label.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        label.place(relx=1, x=-770, y=135)

        SetRe1_button = Button(text="Default Settings", command=self.SetRe1)
        SetRe1_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        SetRe1_button.place(relx=1, x=-774, y=195)

        SetRe3_button = Button(master, text="medium quality", command=self.SetRe3)
        SetRe3_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        SetRe3_button.place(relx=1, x=-495, y=134)

        SetRe4_button = Button(master, text="best quality", command=self.SetRe4)
        SetRe4_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        SetRe4_button.place(relx=1, x=-372, y=134)

        SetRe5_button = Button(master, text="zero order hold", command=self.SetRe5)
        SetRe5_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        SetRe5_button.place(relx=1, x=-273, y=134)

        SetRe10_button = Button(master, text="ffmpeg", command=self.SetRe10)
        SetRe10_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        SetRe10_button.place(relx=1, x=-566, y=134)

        SetRe12_button = Button(master, text="soxr-hq", command=self.SetRe12)
        SetRe12_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        SetRe12_button.place(relx=1, x=-154, y=134)

        SetRe13_button = Button(master, text="soxr-vhq", command=self.SetRe13)
        SetRe13_button.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        SetRe13_button.place(relx=1, x=-81, y=134)
        fm4.pack(fill=BOTH)

        ttk.Separator(root).place(x=0, y=163, relwidth=10)

        fm5 = Frame(master)
        label = Label(master, text="Predefined settings")
        label.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
        label.place(relx=1, x=-770, y=171)

        Class1_button = Button(master, text="USB Audio: Class 1", command=self.Class1)
        Class1_button.pack()
        Class1_button.place(relx=1, x=-649, y=195)

        Class2_button = Button(master, text="USB Audio: Class 2", command=self.Class2)
        Class2_button.pack()
        Class2_button.place(relx=1, x=-508, y=195)

#        Test_button = Button(master, text="Show current sample rate", command=self.Test)
#        Test_button.pack()
#        Test_button.place(relx=1, x=-2, y=2, anchor=NE)

        Confirm_button = Button(master, text="   Apply !   ", command=self.Confirm)
        Confirm_button.pack()
        Confirm_button.place(relx=1, x=-160, y=195)

        close_button = Button(master, text="Close ", command=master.quit)
        close_button.pack()
        close_button.place(relx=1, x=-65, y=195)
        fm5.pack(fill=BOTH)

    def Class1(self):
           subprocess.call('currentbitrate=$(grep "default-sample-format" /etc/pulse/daemon.conf) && sudo sed -i "/${currentbitrate}/ c default-sample-format = s24le" /etc/pulse/daemon.conf && currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c default-sample-rate = 96000" /etc/pulse/daemon.conf && currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c alternate-sample-rate = 96000" /etc/pulse/daemon.conf', shell=True)

    def Class2(self):
           subprocess.call('currentbitrate=$(grep "default-sample-format" /etc/pulse/daemon.conf) && sudo sed -i "/${currentbitrate}/ c default-sample-format = s24le" /etc/pulse/daemon.conf && currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c default-sample-rate = 192000" /etc/pulse/daemon.conf && currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c alternate-sample-rate = 192000" /etc/pulse/daemon.conf && currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf)', shell=True)

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
           subprocess.call('currentbitrate=$(grep "default-sample-format" /etc/pulse/daemon.conf) && sudo sed -i "/${currentbitrate}/ c default-sample-format = s16le" /etc/pulse/daemon.conf && currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c ; resample-method = speex-float-1" /etc/pulse/daemon.conf && currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c ; default-sample-rate = 44000" /etc/pulse/daemon.conf && currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c alternate-sample-rate = 44000" /etc/pulse/daemon.conf', shell=True)

    def SetRe3(self):
           subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = src-sinc-medium-quality" /etc/pulse/daemon.conf', shell=True)

    def SetRe4(self):
           subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = src-sinc-best-quality" /etc/pulse/daemon.conf', shell=True)

    def SetRe5(self):
           subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = src-zero-order-hold" /etc/pulse/daemon.conf', shell=True)

    def SetRe10(self):
           subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = ffmpeg" /etc/pulse/daemon.conf', shell=True)

    def SetRe12(self):
           subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = soxr-hq" /etc/pulse/daemon.conf', shell=True)

    def SetRe13(self):
           subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = soxr-vhq" /etc/pulse/daemon.conf', shell=True)


    def Test(self):
           subprocess.call('pacmd list-sinks | grep sample', shell=True)

    def Confirm(self):
           subprocess.call('pulseaudio --kill && pulseaudio --start', shell=True)


root = Tk()
my_gui = AppGUI1(root)
root.mainloop()
