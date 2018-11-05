#!/usr/bin/python3

# ---------- Note to self ----------
# Double check imports 😘

from tkinter import *  					# the GUI toolkit.
from tkinter import ttk					# dd the tabs

import csv 								# Read / Write csv
import io 								# For string file save for csv

import subprocess						# for pulseaudio config (for now)
from subprocess import call				# Might be useless

# Render main  window
top = Tk()
def main():

    mainFrame=Frame(top,relief="sunken",border=1)
    Description=Label(mainFrame,text="Audio Powertool:")

# ---------- Define MainFrame ----------
    mainFrame.master.title("Audio Powertool")
    mainFrame.master.minsize(width=728,height=294)
    mainFrame.master.maxsize(width=728,height=294)

# End ----------

# ---------- Note to self ----------
# get rid of the globals 😘
    global nb
    global page99
# --------------------

    nb=ttk.Notebook(mainFrame.master)
    nb.grid(row=1,column=1,columnspan=50,rowspan=49,sticky='NESW')

    page1=ttk.Frame(nb)
    nb.add(page1,text='PulseAudio')

    frame1=tkinter.LabelFrame(page1)
    frame1.grid(row=1,column=2,sticky='NESW',padx=5,pady=5)

    page2=ttk.Frame(nb)
    nb.add(page2,text='ALSA')

    # Adds Settings tab of the notebook

    page99=ttk.Frame(nb)

# End ----------

# -------------------- Tab 1 (PulseAudio) --------------------

    # frame
    frame1=tkinter.LabelFrame(page1)
    frame1.grid(row=1,column=2,columnspan=7,rowspan=5,sticky='NESW')

    background_label=Label(frame1,bg="black")
    background_label.place(width=800,height=100)

    label=Label(page1,text=" Set bit depth ")
    label.grid(row=1,column=1,padx=1,pady=5)

# ---------- BithDepth Radio Buttons ----------

    RadBit16=Radiobutton(page1,text='16 Bit',variable=vPabitdepth,value='default-sample-format = s16le',command=Pabitdepth,width=9)
    RadBit16.grid(row=2,column=1,sticky='N')

    RadBit24=Radiobutton(page1,text='24 Bit',variable=vPabitdepth,value='default-sample-format = s24le',command=Pabitdepth,width=9)
    RadBit24.grid(row=3,column=1,sticky='N')

    RadBit32=Radiobutton(page1,text='32 Bit',variable=vPabitdepth,value='default-sample-format = s32le',command=Pabitdepth,width=9)
    RadBit32.grid(row=4,column=1,sticky='N')

# End ----------

    # Separator-1
    ttk.Separator(page1).grid(row=5,column=1,columnspan=11,sticky="ew")

# ---------- Primary Samplerate Radio Buttons ----------

    label=Label(page1,text="Primary Sample rate")
    label.grid(row=6,column=1,columnspan=2)

    RadPriRate44100=Radiobutton(page1,text='44,100 Hz',variable=vPaPriRate,value='default-sample-rate = 44100',command=PaPriRate,width=9)
    RadPriRate44100.grid(row=6,column=3)

    RadPriRate48000=Radiobutton(page1,text='48,000 Hz',variable=vPaPriRate,value='default-sample-rate = 48000',command=PaPriRate,width=9)
    RadPriRate48000.grid(row=6,column=4)

    RadPriRate88200=Radiobutton(page1,text='88,200 Hz',variable=vPaPriRate,value='default-sample-rate = 88200',command=PaPriRate,width=9)
    RadPriRate88200.grid(row=6,column=5)

    RadPriRate96000=Radiobutton(page1,text='96,000 Hz',variable=vPaPriRate,value='default-sample-rate = 96000',command=PaPriRate,width=9)
    RadPriRate96000.grid(row=6,column=6)

    RadPriRate192000=Radiobutton(page1,text='192,000 Hz',variable=vPaPriRate,value='default-sample-rate = 192000',command=PaPriRate,width=9)
    RadPriRate192000.grid(row=6,column=7)

# End ----------

# ---------- Alternative Samplerate Radio Buttons ----------

    label=Label(page1,text="Alternative Sample rate")
    label.grid(row=7,column=1,columnspan = 2)

    RadAltRate44100=Radiobutton(page1,text='44,100 Hz',variable=vPaAltRate,value='alternate-sample-rate = 44100',command=PaAltRate,width=9)
    RadAltRate44100.grid(row=7,column=3)

    RadAltRate48000=Radiobutton(page1,text='48,000 Hz',variable=vPaAltRate,value='alternate-sample-rate = 48000',command=PaAltRate,width=9)
    RadAltRate48000.grid(row=7,column=4)

    RadAltRate48000=Radiobutton(page1,text='88,200 Hz',variable=vPaAltRate,value='alternate-sample-rate = 88200',command=PaAltRate,width=9)
    RadAltRate48000.grid(row=7,column=5)

    RadAltRate96000=Radiobutton(page1,text='96,000 Hz',variable=vPaAltRate,value='alternate-sample-rate = 96000',command=PaAltRate,width=9)
    RadAltRate96000.grid(row=7,column=6)

    RadAltRate192000=Radiobutton(page1,text='192,000 Hz',variable=vPaAltRate,value='alternate-sample-rate = 192000',command=PaAltRate,width=9)
    RadAltRate192000.grid(row=7,column=7)

# End ----------

    # Separator-2
    ttk.Separator(page1).grid(row=8,column=1,columnspan=11,sticky="ew")

# ---------- Resample method Radio Buttons ----------

    label=Label(page1,text="Resample method")
    label.grid(row=9,column=1,columnspan = 2,pady=4)

#    vPaRespeexfloatN=Radiobutton(page1,indicatoron=0,text='???',variable=vPaRe,value='resample-method = speex-float-N',command=PaRe,width=12)
#    vPaRespeexfloatN.grid(row=9,column=3)

    vPaRespeexfloat10=Radiobutton(page1,indicatoron=0,text='speexfloat-10',variable=vPaRe,value='resample-method = speex-float-10',command=PaRe,width=12)
    vPaRespeexfloat10.grid(row=9,column=4)

    vPaRemedium=Radiobutton(page1,indicatoron=0,text='medium',variable=vPaRe,value='resample-method = src-sinc-medium-quality',command=PaRe,width=12)
    vPaRemedium.grid(row=9,column=5)

    vPaRebest=Radiobutton(page1,indicatoron=0,text='best',variable=vPaRe,value='resample-method = src-sinc-best-quality',command=PaRe,width=12)
    vPaRebest.grid(row=9,column=6)

    vPaRezeroOrderhold=Radiobutton(page1,indicatoron=0,text='zero-orderhold',variable=vPaRe,value='resample-method = src-zero-order-hold',command=PaRe,width=12)
    vPaRezeroOrderhold.grid(row=9, column=7)

    vPaReStopResampling=Radiobutton(page1,indicatoron=0,text='Default Resampling',variable=vPaRe,value='; resample-method = speex-float-1',command=PaRe,width=25)
    vPaReStopResampling.grid(row=10,column=1,columnspan=2)

#    vPaReresamplemethod=Radiobutton(page1,indicatoron=0,text='???',variable=vPaRe,value='resample-method = speex-fixed-N',command=PaRe,width=12)
#    vPaReresamplemethod.grid(row=10,column=3)

    vPaReffmpeg=Radiobutton(page1,indicatoron=0,text='ffmpeg',variable=vPaRe,value='resample-method = ffmpeg',command=PaRe,width=12)
    vPaReffmpeg.grid(row=10,column=4)

    vPaResrclinear=Radiobutton(page1,indicatoron=0,text='src-linear',variable=vPaRe,value='resample-method = src-linear',command=PaRe,width=12)
    vPaResrclinear.grid(row=10,column=5)

    vPaResoxrhq=Radiobutton(page1,indicatoron=0,text='soxr-hq',variable=vPaRe,value='resample-method = soxr-hq',command=PaRe,width=12)
    vPaResoxrhq.grid(row=10,column=6)

    vPaResoxrvhq=Radiobutton(page1,indicatoron=0,text='soxr-vhq',variable=vPaRe,value='resample-method = soxr-vhq',command=PaRe,width=12)
    vPaResoxrvhq.grid(row=10,column=7)

# End ----------

    # Separator3
    ttk.Separator(page1).grid(row=11,column=1,columnspan=11,sticky="ew")

# ---------- Default & Apply PA Button ----------

# ---------- Note to self ----------
# Rewrite Default Button 😘

    apply_btn1=Button(page1,text='Default Values',command=defaultpulsebutton)
    apply_btn1.grid(row=12,column=1,columnspan=2,padx=5,pady=5)

    apply_btn2=Button(page1,text='Apply & Restart pulseaudio',command=applyPA)
    apply_btn2.grid(row=12,column=6,columnspan=5,padx=5,pady=5)

# Text below app
    label=Label(page1,text="Restarting services take few seconds")
    label.grid(row=12,column=3,columnspan=3)

# showsamplerate text update
    label=Label(frame1,textvariable=bitdepthtextvariable,fg='grey',bg='black',font=('Monospace Regular',11))
    label.grid(row=1,column=1,sticky='W',pady=3)

# Button Show Samplerate
    apply_btn3=Button(page1,text='Show Current PA Output',command=showsamplerate)
    apply_btn3.grid(row=1,column=6,sticky='N, E',rowspan=2,columnspan=2,padx=4,pady=7)

 # PAGE2 Maincode

    # page2 main frame
    frame101=tkinter.LabelFrame(page2)
    frame101.grid(row=1,column=2,sticky='NESW',padx=5,pady=5)

    label=Label(frame101,text="Nothing here, yet")
    label.grid(row=1,column=1,rowspan=3,padx=5,pady=5)

# End ----------

# ----------------- Menubar  -----------------

    menubar=Menu(mainFrame.master)
    filemenu=Menu(menubar,tearoff=0)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=mainFrame.master.quit)
    menubar.add_cascade(label="File",menu=filemenu)

    editmenu=Menu(menubar,tearoff=0)
    editmenu.add_command(label="Config",) # No config menu
    menubar.add_cascade(label="Edit",menu=editmenu)

    helpmenu=Menu(menubar,tearoff=0)

# ---------- Note to self ----------
# move this 😘

    def helpmenu01():
        tkinter.messagebox.showinfo("About Audio Powertool: ","Dont set sample rate to 'maximum option available' \n \nthat will do audio resampling and you dont want that!\n \n App will reconfigure pulseaudio daemon.conf file")

    helpmenu.add_command(label="About",command=helpmenu01)
    menubar.add_cascade(label="Help",menu=helpmenu)

    mainFrame.master.config(menu=menubar)

# End ----------
    top.mainloop()

# End ----------
# End -----

# ---------- Variables ----------

vPabitdepth=StringVar() 			# PulseAudio BithDepth
vPaPriRate=StringVar() 				# PulseAudio Primary Samplerate
vPaAltRate=StringVar() 				# PulseAudio Alternative Samplerate
vPaRe=StringVar() 					# PulseAudio Resample method

bitdepthtextvariable=StringVar() 	# Show Samplerate

# End ----------

# ---------- Set Default Values for Variable ----------

vPabitdepth.set('; default-sample-format = s16le')
vPaPriRate.set('; default-sample-rate = 44100')
vPaAltRate.set('; alternate-sample-rate = 48000')
vPaRe.set('; resample-method = speex-float-1')

# ---------- Print Radiobutton Data ----------

def Pabitdepth():
    print(vPabitdepth.get())

def PaPriRate():
    print(vPaPriRate.get())

def PaAltRate():
    print(vPaAltRate.get())

def PaRe():
    print(vPaRe.get())

# End ----------

# ---------- Button Commands ----------

# Default button.
def defaultpulsebutton():
    vPabitdepth.set('; default-sample-format = s16le')
    vPaPriRate.set('; default-sample-rate = 44100')
    vPaAltRate.set('; alternate-sample-rate = 48000')
    vPaRe.set('; resample-method = speex-float-1')
    print(vPabitdepth.get())
    print(vPaPriRate.get())
    print(vPaAltRate.get())
    print(vPaRe.get())

# Apply PA Button
def applyPA():
    CvPabitdepth=(vPabitdepth.get())
    CvPaPriRate=(vPaPriRate.get())
    CvPaAltRate=(vPaAltRate.get())
    CvPaRe=(vPaRe.get())

    subprocess.call('sudo sed -i "/default-sample-format =/ c {}" /etc/pulse/daemon.conf && sudo sed -i "/default-sample-rate =/ c {}" /etc/pulse/daemon.conf && sudo sed -i "/alternate-sample-rate =/ c {}" /etc/pulse/daemon.conf && sudo sed -i "/resample-method =/ c {}" /etc/pulse/daemon.conf | pulseaudio --kill ; pulseaudio --start'.format(CvPabitdepth,CvPaPriRate,CvPaAltRate,CvPaRe),shell=True);

# Show samlerate
def showsamplerate():
    showsamplerateoutput=subprocess.check_output('pacmd list-sinks | grep sample',shell=True)
    bitdepthtextvariable.set(showsamplerateoutput)

# Close Window
def close_window():
    root.destroy()

# End ----------

    root.mainloop()

if __name__ == '__main__':
    main()
