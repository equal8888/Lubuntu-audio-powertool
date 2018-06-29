#!/usr/bin/python3
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

import sys
import csv # Read / Write csv
import io # For string file save for csv

import os
import subprocess
from subprocess import call


# Close Window
def close_window():
    top.destroy()

# for now
def EnterKey(event):
    print("You hit return.")
    writeToFile("Ubuntu-Audio-App.csv")

def Preferences01():
    nb.add(page999, text='Preferences')
    nb.select(page999)
    password_box.delete(0, END)

def writeToFile(filename):
    nb.hide(page999)
    inputValue=password_box.get()

    path = os.path.dirname("Ubuntu-Audio-App.csv")

    with open(os.path.join(path, filename), "w") as csv_file:
        writer = csv.writer(csv_file, lineterminator='\n')
        writer.writerow([inputValue])

# Memo: writerow(1)  CSV COMMANDS from https://docs.python.org/3.2/library/csv.html

# get passwd from CSV file
class Getpsswd():
    def __init__(self, filename):
        path = os.path.dirname("Ubuntu-Audio-App.csv")

        with open(os.path.join(path, filename)) as f_input:
            csv_input = csv.reader(f_input)
            self.details = list(csv_input)

    def get_col_row(self, col, row):
        return self.details[row-1][col-1]

# Getpsswd error handler
try:
    data = Getpsswd("Ubuntu-Audio-App.csv") # Get password from Ubuntu-Audio-App.csv
    pswd = data.get_col_row(0, 0)
    cmd='ls'
    call('echo {} | sudo -S {}'.format(pswd, cmd), shell=True)
except IndexError:
    pswd = 'null'

def login(*event):
    writeToFile("Ubuntu-Audio-App.csv")

# Render main  window
def main():
    root = tk.Tk()
    root.title("Audio Powertool")
    root.minsize(width=730, height=288)

    global password_box
    global pswd

    # define var's
    var = IntVar()
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()

    bitdepthtextvariable = StringVar()
    password_box = StringVar()

    # gives weight to the cells in the grid
    rows = 0
    while rows < 50:
        root.rowconfigure(rows, weight=1)
        root.columnconfigure(rows, weight=1)
        rows += 1

    # Defines and places the notebook widget
    global nb

    nb = ttk.Notebook(root)
    nb.grid(row=1, column=1, columnspan=50, rowspan=49, sticky='NESW')

    # Adds tab 1 of the notebook
    page1 = ttk.Frame(nb)
    nb.add(page1, text='PulseAudio')

    # page1 main frame
    frame99 = tkinter.LabelFrame(page1)
    frame99.grid(row=1, column=2, sticky='NESW', padx=5, pady=5)

    # Adds tab 2 of the notebook
    page2 = ttk.Frame(nb)
    nb.add(page2, text='ALSA')

    # Adds tab 3 of the notebook
    global page999
    page999 = ttk.Frame(nb)

    # Menubar
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="preferences", command=Preferences01)
    menubar.add_cascade(label="Edit", menu=editmenu)

    helpmenu = Menu(menubar, tearoff=0)
    def helpmenu01():
        tkinter.messagebox.showinfo("FAQ", "PulseAudio\n \nSet sample rate:\nFool proof option is 48,000 Hz \n")
    helpmenu.add_command(label="FAQ", command=helpmenu01)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)

    # PAGE1 Maincode

    # Blue frame
    frame97 = tkinter.LabelFrame(frame99)
    frame97.grid(row=1, column=2, columnspan=7, rowspan=5, sticky='NESW')

    background_label = Label(frame97, bg="blue")
    background_label.place(width=800, height=100)
    # bit depth text update
    label = Label(frame99, textvariable=bitdepthtextvariable, fg='yellow', bg='blue', font='bold')
    label.grid(row=1, column=1, sticky='E', rowspan=7, columnspan=7, padx=3, pady=2)

    label = Label(frame99, text=" Set bit depth ")
    label.grid(row=1, column=1, padx=1, pady=5)

    def select_bitdepth_16():
        subprocess.call('currentbitrate=$(grep "default-sample-format" /etc/pulse/daemon.conf) && sudo sed -i "/${currentbitrate}/ c default-sample-format = s16le" /etc/pulse/daemon.conf', shell=True)

    select_bitdepth_1=Radiobutton(frame99, command=select_bitdepth_16, text='16 Bit', variable=var, value=16, width=9)
    select_bitdepth_1.grid(row=2, column=1, sticky='N')

    def select_bitdepth_24():
        subprocess.call('currentbitrate=$(grep "default-sample-format" /etc/pulse/daemon.conf) && sudo sed -i "/${currentbitrate}/ c default-sample-format = s24le" /etc/pulse/daemon.conf', shell=True)

    select_bitdepth_1=Radiobutton(frame99, command=select_bitdepth_24, text='24 Bit', variable=var, value=24, width=9)
    select_bitdepth_1.grid(row=3, column=1, sticky='N')

    def select_bitdepth_32():
        subprocess.call('currentbitrate=$(grep "default-sample-format" /etc/pulse/daemon.conf) && sudo sed -i "/${currentbitrate}/ c default-sample-format = s32le" /etc/pulse/daemon.conf', shell=True)

    select_bitdepth_1=Radiobutton(frame99, command=select_bitdepth_32, text='32 Bit', variable=var, value=32, width=9)
    select_bitdepth_1.grid(row=4, column=1, sticky='N')

    # Separator1
    ttk.Separator(frame99).grid(row=5, column=1, columnspan=11, sticky="ew")

    # Set primary sample rate
    label = Label(frame99, text="Primary Sample rate")
    label.grid(row=6, column=1, columnspan = 2)

    def select_prisamplerate_44100():
        subprocess.call('currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c default-sample-rate = 44100" /etc/pulse/daemon.conf', shell=True)

    select_prisamplerate_1=Radiobutton(frame99, command=select_prisamplerate_44100, text='44,100 Hz', variable=var1, value=14100, width=9)
    select_prisamplerate_1.grid(row=6, column=3)

    def select_prisamplerate_48000():
        subprocess.call('currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c default-sample-rate = 48000" /etc/pulse/daemon.conf', shell=True)

    select_prisamplerate_1=Radiobutton(frame99, command=select_prisamplerate_48000, text='48,000 Hz', variable=var1, value=48000, width=9)
    select_prisamplerate_1.grid(row=6, column=4)

    def select_prisamplerate_88200():
        subprocess.call('currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c default-sample-rate = 88200" /etc/pulse/daemon.conf', shell=True)

    select_prisamplerate_1=Radiobutton(frame99, command=select_prisamplerate_88200, text='88,200 Hz', variable=var1, value=88200, width=9)
    select_prisamplerate_1.grid(row=6, column=5)

    def select_prisamplerate_96000():
        subprocess.call('currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c default-sample-rate = 96000" /etc/pulse/daemon.conf', shell=True)

    select_prisamplerate_1=Radiobutton(frame99, command=select_prisamplerate_96000, text='96,000 Hz', variable=var1, value=96000, width=9)
    select_prisamplerate_1.grid(row=6, column=6)

    def select_prisamplerate_192000():
        subprocess.call('currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c default-sample-rate = 192000" /etc/pulse/daemon.conf', shell=True)

    select_prisamplerate_1=Radiobutton(frame99, command=select_prisamplerate_192000, text='192,000 Hz', variable=var1, value=192000, width=9)
    select_prisamplerate_1.grid(row=6, column=7)

    # Set Secondary sample rate
    label = Label(frame99, text="Alternative Sample rate")
    label.grid(row=7, column=1, columnspan = 2)

    def select_altsamplerate_44100():
        subprocess.call('currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c alternate-sample-rate = 44100" /etc/pulse/daemon.conf', shell=True)

    select_altsamplerate_1=Radiobutton(frame99, text='44,100 Hz', variable=var2, command=select_altsamplerate_44100, value=14100, width=9)
    select_altsamplerate_1.grid(row=7, column=3)

    def select_altsamplerate_48000():
        subprocess.call('currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c alternate-sample-rate = 48000" /etc/pulse/daemon.conf', shell=True)

    select_altsamplerate_1=Radiobutton(frame99, text='48,000 Hz', variable=var2, command=select_altsamplerate_48000, value=48000, width=9)
    select_altsamplerate_1.grid(row=7, column=4)

    def select_altsamplerate_88200():
        subprocess.call('currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c alternate-sample-rate = 88200" /etc/pulse/daemon.conf', shell=True)

    select_altsamplerate_1=Radiobutton(frame99, text='88,200 Hz', variable=var2, command=select_altsamplerate_88200, value=88200, width=9)
    select_altsamplerate_1.grid(row=7, column=5)

    def select_altsamplerate_96000():
        subprocess.call('currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c alternate-sample-rate = 96000" /etc/pulse/daemon.conf', shell=True)

    select_altsamplerate_1=Radiobutton(frame99, text='96,000 Hz', variable=var2, command=select_altsamplerate_96000, value=96000, width=9)
    select_altsamplerate_1.grid(row=7, column=6)

    def select_altsamplerate_192000():
        subprocess.call('currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c alternate-sample-rate = 192000" /etc/pulse/daemon.conf', shell=True)

    select_altsamplerate_1=Radiobutton(frame99, text='192,000 Hz', variable=var2, command=select_altsamplerate_192000, value=192000, width=9)
    select_altsamplerate_1.grid(row=7, column=7)

    # Separator2
    ttk.Separator(frame99).grid(row=8, column=1, columnspan=11, sticky="ew")

    # Set Secondary sample rate
    label = Label(frame99, text="Resample method")
    label.grid(row=9, column=1, columnspan = 2)

    def select_prisamplerate_default():
        subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c ; resample-method = speex-float-1" /etc/pulse/daemon.conf', shell=True)

    select_resamplerate_1=Radiobutton(frame99, indicatoron=0, text='default', variable=var3, command=select_prisamplerate_default, value=1, width=12)
    select_resamplerate_1.grid(row=9, column=3)

    def select_prisamplerate_optimised():
        subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = speex-float-10" /etc/pulse/daemon.conf', shell=True)

    select_resamplerate_1=Radiobutton(frame99, indicatoron=0, text='fast', variable=var3, command=select_prisamplerate_optimised, value=2, width=12)
    select_resamplerate_1.grid(row=9, column=4)

    def select_prisamplerate_srcsincmediumquality():
        subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = src-sinc-medium-quality" /etc/pulse/daemon.conf', shell=True)

    select_resamplerate_1=Radiobutton(frame99, indicatoron=0, text='medium', variable=var3, command=select_prisamplerate_srcsincmediumquality, value=3, width=12)
    select_resamplerate_1.grid(row=9, column=5)

    def select_prisamplerate_srcsincbestquality():
        subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = src-sinc-best-quality" /etc/pulse/daemon.conf', shell=True)

    select_resamplerate_1=Radiobutton(frame99, indicatoron=0, text='best', variable=var3, command=select_prisamplerate_srcsincbestquality, value=4, width=12)
    select_resamplerate_1.grid(row=9, column=6)

    def select_prisamplerate_srczeroorderhold():
        subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = src-zero-order-hold" /etc/pulse/daemon.conf', shell=True)

    select_resamplerate_1=Radiobutton(frame99, indicatoron=0, text='zero-orderhold', variable=var3, command=select_prisamplerate_srczeroorderhold, value=5, width=12)
    select_resamplerate_1.grid(row=9, column=7)

    def select_prisamplerate_srclinear():
        subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = src-linear" /etc/pulse/daemon.conf', shell=True)

    select_resamplerate_1=Radiobutton(frame99, indicatoron=0, text='src-linear', variable=var3, command=select_prisamplerate_srclinear, value=6, width=12)
    select_resamplerate_1.grid(row=10, column=5)

    def select_prisamplerate_trivial():
        subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = trivial" /etc/pulse/daemon.conf', shell=True)

    select_resamplerate_1=Radiobutton(frame99, indicatoron=0, text='trivial', variable=var3, command=select_prisamplerate_trivial, value=7, width=12)
    select_resamplerate_1.grid(row=10, column=1)

    def select_prisamplerate_speexfloatN():
        subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = speex-float-N" /etc/pulse/daemon.conf', shell=True)

    select_resamplerate_1=Radiobutton(frame99, indicatoron=0, text='speex-float-N', variable=var3, command=select_prisamplerate_speexfloatN, value=8, width=12)
    select_resamplerate_1.grid(row=10, column=2)

    def select_prisamplerate_speexfixedN():
        subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = speex-fixed-N" /etc/pulse/daemon.conf', shell=True)

    select_resamplerate_1=Radiobutton(frame99, indicatoron=0, text='speex-fixed-N', variable=var3, command=select_prisamplerate_speexfixedN, value=9, width=12)
    select_resamplerate_1.grid(row=10, column=3)

    def select_prisamplerate_ffmpeg():
        subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = ffmpeg" /etc/pulse/daemon.conf', shell=True)

    select_resamplerate_1=Radiobutton(frame99, indicatoron=0, text='ffmpeg', variable=var3, command=select_prisamplerate_ffmpeg, value=10, width=12)
    select_resamplerate_1.grid(row=10, column=4)

    def select_prisamplerate_soxrhq():
        subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = soxr-hq" /etc/pulse/daemon.conf', shell=True)

    select_resamplerate_1=Radiobutton(frame99, indicatoron=0, text='soxr-hq', variable=var3, command=select_prisamplerate_soxrhq, value=12, width=12)
    select_resamplerate_1.grid(row=10, column=6)

    def select_prisamplerate_soxrvhq():
        subprocess.call('currentresamplerate=$(grep "resample-method" /etc/pulse/daemon.conf) && sudo sed -i "/${currentresamplerate}/ c resample-method = soxr-vhq" /etc/pulse/daemon.conf', shell=True)

    select_resamplerate_1=Radiobutton(frame99, indicatoron=0, text='soxr-vhq', variable=var3, command=select_prisamplerate_soxrvhq, value=13, width=12)
    select_resamplerate_1.grid(row=10, column=7)

    # Separator3 usb1button
    ttk.Separator(frame99).grid(row=11, column=1, columnspan=11, sticky="ew")

    frame98 = tkinter.LabelFrame(frame99, borderwidth=3)
    frame98.grid(row=11, column=6, columnspan=2, sticky='NEW', \
                      padx=5, pady=5)

#   default button for now
    def defaultpulsebutton():
        subprocess.call('defaultsettingspath=$(realpath --relative-base=$HOME default-settings-pulseaudio.sh) && realdefaultsettingspath="~/"$defaultsettingspath && eval $realdefaultsettingspath', shell=True)
    apply_btn1=Button(frame99, text='Default Pulseaudio settings', command=defaultpulsebutton )
    apply_btn1.grid(row=12, column=1, columnspan=2, padx=5, pady=5)

#   restart pulseaudio
    def restartpulse():
        subprocess.call('pulseaudio --kill ; pulseaudio --start', shell=True)
    apply_btn2=Button(frame99, text='Apply / Restart pulseaudio', command=restartpulse )
    apply_btn2.grid(row=12, column=6, columnspan=4, padx=5, pady=5)

#   samplerate button for now (row=1, column=1)
    def showsamplerate():
        showsamplerateoutput = subprocess.check_output(["(pacmd list-sinks | grep sample)"], shell=True)
        bitdepthtextvariable.set (showsamplerateoutput)

    apply_btn3=Button(frame99, text='Test for possiple resampling', command=showsamplerate )
    apply_btn3.grid(row=1, column=6, sticky='E', rowspan=2, columnspan=2, padx=3, pady=2)

# PAGE2 Maincode

    # page2 main frame
    frame101 = tkinter.LabelFrame(page2)
    frame101.grid(row=1, column=2, sticky='NESW', padx=5, pady=5)

    label = Label(frame101, text="ALSA Page is under development. Select PulseAudio from tab menu.")
    label.grid(row=1, column=1, rowspan = 3, padx=5, pady=5)

# Settings Maincode
    # green frame
    frame300 = tkinter.LabelFrame(page999)
    frame300.grid(row=1, column=2, columnspan=7, rowspan=5, sticky='NESW')

    background_label = Label(frame300, bg="Green")
    background_label.place(width=800, height=100)

# Password user input to csv file
    Label(frame300, text='Sudo Password:').grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky='NS')
    # adds password entry widget and defines its properties
    password_box = Entry(frame300, show='*')
    password_box.insert(0, '     ')
    password_box.bind('<Return>', login)
    password_box.grid(row=2, column=1, sticky='NS')
    # adds login button and defines its properties
    login_btn = Button(frame300, text='Grant Access', command=lambda: writeToFile("Ubuntu-Audio-App.csv"))
    login_btn.bind('<Return>', login)
    login_btn.grid(row=3, column=1, sticky='NESW')

    root.mainloop()

if __name__ == '__main__':
        main()
