#!/usr/bin/python3
import tkinter                          # GUI toolkit
from tkinter import StringVar, Frame, Label, LabelFrame, Radiobutton, OptionMenu, Button, ttk, _setit # GUI toolkit
import subprocess                       # Pulseaudio/alsa config

top = tkinter.Tk()
def main():

# ---------- Define MainFrame ----------

    mainFrame=Frame(top,border=1)
    Description=Label(mainFrame,text="Audio Powertool:")

    mainFrame.master.title("Audio Powertool")
    mainFrame.master.resizable(False, False)

# End ----------

# ---------- Define Pages ----------

	# Menu for pages
    nb=ttk.Notebook(mainFrame.master)
    nb.grid(row=1,column=1,sticky='NESW')

	# Page 1 PulseAudio
    page1=ttk.Frame(nb)
    nb.add(page1,text='PulseAudio (Software Mixer)')

	# Page 2 ALSA
    page2=ttk.Frame(nb)
    nb.add(page2,text='ALSA (Hardware Mixer)')

# End ----------

# -------------------- Tab 1 (PulseAudio) --------------------
    # page1 main frame
    frame0=LabelFrame(page1,bd=5,bg="cyan")
    frame0.grid(row=0,column=0,sticky='NESW')

    # page1 frame
    frame1=LabelFrame(frame0,bd=5,bg="black")
    frame1.grid(row=0,column=1,rowspan=5,sticky='NESW')

	# PulseAudio Status and output info frame (white)
    frame2=Label(frame1)
    frame2.grid(row=2,column=3,columnspan=2,rowspan=2,sticky='es',padx=6)

# ---------- Show Info ----------

# show current PA status from button
    label=Label(frame2,textvariable=vPaRun,fg='white',bg='black',font=('Monospace Regular',11))
    label.grid(sticky='NESW')

# show current PA output from button
    label=Label(frame2,textvariable=ShvPaOut,fg='white',bg='black',font=('Monospace Regular',11))
    label.grid(sticky='NESW')

# Bitdepth Samplerate
    label=Label(frame1,textvariable=vConfPaBitdepth,fg='grey',bg='black',font=('Monospace Regular',11))
    label.grid(row=0,column=1,sticky='nsw')

# Primary Samplerate
    label=Label(frame1,textvariable=vConfPaPriRate,fg='grey',bg='black',font=('Monospace Regular',11))
    label.grid(row=1,column=1,columnspan=4,sticky='nsw')

# Alternative Samplerate
    label=Label(frame1,textvariable=vConfPaAltRate,fg='grey',bg='black',font=('Monospace Regular',11))
    label.grid(row=2,column=1,columnspan=4,sticky='nsw')

# Resampling
    resamplinglabel=Label(frame1,textvariable=vConfPaRe,fg='grey',bg='black',font=('Monospace Regular',11))
    resamplinglabel.grid(row=3,column=1,columnspan=4,sticky='nsw')

    label=Label(frame1,bg="black",text="----------------------------",font=('Monospace Regular',11))
    label.grid(row=0,column=2,sticky='nsw')

# End ----------

    label=Label(frame0,text=" 1) Bit Depth ",font=('Monospace Regular',11))
    label.grid(row=0,column=0,sticky='NESW')

# ---------- BithDepth Radio Buttons ----------

    RadBit16=Radiobutton(frame0,text='Default',font=('Monospace Regular',11),variable=vPaBitdepth,value='; default-sample-format = s16le',command=Pabitdepth,width=8)
    RadBit16.grid(row=1,column=0,sticky='nsw')

    RadBit16=Radiobutton(frame0,text='16 Bit',font=('Monospace Regular',11),variable=vPaBitdepth,value='default-sample-format = s16le',command=Pabitdepth,width=8)
    RadBit16.grid(row=2,column=0,sticky='nsw')

    RadBit24=Radiobutton(frame0,text='24 Bit',font=('Monospace Regular',11),variable=vPaBitdepth,value='default-sample-format = s24le',command=Pabitdepth,width=8)
    RadBit24.grid(row=3,column=0,sticky='nsw')

    RadBit32=Radiobutton(frame0,text='32 Bit',font=('Monospace Regular',11),variable=vPaBitdepth,value='default-sample-format = s32le',command=Pabitdepth,width=8)
    RadBit32.grid(row=4,column=0,sticky='nsw')

# End ----------

# ---------- Primary Samplerate Radio Buttons ----------

	# samplerate frame
    frame4=LabelFrame(page1)
    frame4.grid(row=5,column=0,columnspan=2,sticky='NESW')

    label=Label(frame4,text=" 2) Primary Sample Rate         ",font=('Monospace Regular',11))
    label.grid(row=1,column=1,sticky='w')

    RadPriRateDefault=Radiobutton(frame4,text='Default',font=('Monospace Regular',11),variable=vPaPriRate,value='; default-sample-rate = 44100',command=PaPriRate,width=10)
    RadPriRateDefault.grid(row=1,column=2,sticky='NESW')

    RadPriRate44100=Radiobutton(frame4,text='44,100 Hz',font=('Monospace Regular',11),variable=vPaPriRate,value='default-sample-rate = 44100',command=PaPriRate,width=10)
    RadPriRate44100.grid(row=1,column=3,sticky='NESW')

    RadPriRate48000=Radiobutton(frame4,text='48,000 Hz',font=('Monospace Regular',11),variable=vPaPriRate,value='default-sample-rate = 48000',command=PaPriRate,width=10)
    RadPriRate48000.grid(row=1,column=4,sticky='NESW')

    RadPriRate88200=Radiobutton(frame4,text='88,200 Hz',font=('Monospace Regular',11),variable=vPaPriRate,value='default-sample-rate = 88200',command=PaPriRate,width=10)
    RadPriRate88200.grid(row=1,column=5,sticky='NESW')

    RadPriRate96000=Radiobutton(frame4,text='96,000 Hz',font=('Monospace Regular',11),variable=vPaPriRate,value='default-sample-rate = 96000',command=PaPriRate,width=10)
    RadPriRate96000.grid(row=1,column=6,sticky='NESW')

# End ----------

# ---------- Alternative Samplerate Radio Buttons ----------

    label=Label(frame4,text=" 3) Alternative Sample Rate ",font=('Monospace Regular',11))
    label.grid(row=2,column=1,sticky='w')

    RadAltRateDefault=Radiobutton(frame4,text='Default',font=('Monospace Regular',11),variable=vPaAltRate,value='; alternate-sample-rate = 48000',command=PaAltRate,width=10)
    RadAltRateDefault.grid(row=2,column=2)

    RadAltRate48000=Radiobutton(frame4,text='44,100 Hz',font=('Monospace Regular',11),variable=vPaAltRate,value='alternate-sample-rate = 44100',command=PaAltRate,width=10)
    RadAltRate48000.grid(row=2,column=3)

    RadAltRate48000=Radiobutton(frame4,text='48,000 Hz',font=('Monospace Regular',11),variable=vPaAltRate,value='alternate-sample-rate = 48000',command=PaAltRate,width=10)
    RadAltRate48000.grid(row=2,column=4)

    RadAltRate96000=Radiobutton(frame4,text='88,200 Hz',font=('Monospace Regular',11),variable=vPaAltRate,value='alternate-sample-rate = 88200',command=PaAltRate,width=10)
    RadAltRate96000.grid(row=2,column=5)

    RadAltRate192000=Radiobutton(frame4,text='96,000 Hz',font=('Monospace Regular',11),variable=vPaAltRate,value='alternate-sample-rate = 96000',command=PaAltRate,width=10)
    RadAltRate192000.grid(row=2,column=6)

# End ----------

    global PaAre

# Avoid resampling button
    def PaAre():
        global ToggleBtn
        if ToggleBtn == 'On':
            vPaAre.set('; avoid-resampling = false')
            print ("-----------------------------------------------------------")
            print ("\033[96m PulseAudio \033[00m")
            print ("-----------------------------------------------------------")
            print(vPaAre.get())
            vPaRestop.config(text='avoid resample', font=('Monospace Regular',11))

            vPaRedefault["state"] = "normal"
            vPaRemedium["state"] = "normal"
            vPaRebest["state"] = "normal"
            vPaRezeroOrderhold["state"] = "normal"
            vPaReffmpeg["state"] = "normal"
            vPaResrclinear["state"] = "normal"
            vPaResoxrhq["state"] = "normal"
            vPaResoxrvhq["state"] = "normal"

            ToggleBtn='Off'
        else:
            vPaAre.set('avoid-resampling = true')
            print ("-----------------------------------------------------------")
            print ("\033[96m PulseAudio \033[00m")
            print ("-----------------------------------------------------------")
            vPaRe.set('; resample-method = speex-float-1')
            vPaRestop.config(text='enable resample', font=('Monospace Regular',11))
            print(vPaAre.get())

            vPaRedefault["state"] = "disabled"
            vPaRemedium["state"] = "disabled"
            vPaRebest["state"] = "disabled"
            vPaRezeroOrderhold["state"] = "disabled"
            vPaReffmpeg["state"] = "disabled"
            vPaResrclinear["state"] = "disabled"
            vPaResoxrhq["state"] = "disabled"
            vPaResoxrvhq["state"] = "disabled"

            ToggleBtn='On'

# ---------- Resample method Radio Buttons ----------

    frame5=Frame(page1)
    frame5.grid(row=9,column=0,sticky='NESW')

    frame4=Label(frame5)
    frame4.grid(row=1,column=1,sticky='NESW')

    # Label Resample method
    label=Label(frame4,text=" 4) Resample Method                  ",font=('Monospace Regular',11))
    label.grid(row=1,column=1,columnspan=2,sticky='NESW')

    vPaRedefault=Radiobutton(frame5,indicatoron=0,text='default',font=('Monospace Regular',11),variable=vPaRe,value='; resample-method = speex-float-1',command=PaRe,width=16)
    vPaRedefault.grid(row=1,column=4)

    vPaRemedium=Radiobutton(frame5,indicatoron=0,text='medium',font=('Monospace Regular',11),variable=vPaRe,value='resample-method = src-sinc-medium-quality',command=PaRe,width=16)
    vPaRemedium.grid(row=1,column=5)

    vPaRebest=Radiobutton(frame5,indicatoron=0,text='best',font=('Monospace Regular',11),variable=vPaRe,value='resample-method = src-sinc-best-quality',command=PaRe,width=16)
    vPaRebest.grid(row=1,column=6)

    vPaRezeroOrderhold=Radiobutton(frame5,indicatoron=0,text='zero-orderhold',font=('Monospace Regular',11),variable=vPaRe,value='resample-method = src-zero-order-hold',command=PaRe,width=16)
    vPaRezeroOrderhold.grid(row=1, column=7)

    vPaRestop=Button(frame5,text='avoid resampling',font=('Monospace Regular',11),command=PaAre)
    vPaRestop.grid(row=2,column=1,sticky='ew')

    vPaReffmpeg=Radiobutton(frame5,indicatoron=0,text='ffmpeg',font=('Monospace Regular',11),variable=vPaRe,value='resample-method = ffmpeg',command=PaRe,width=16)
    vPaReffmpeg.grid(row=2,column=4)

    vPaResrclinear=Radiobutton(frame5,indicatoron=0,text='src-linear',font=('Monospace Regular',11),variable=vPaRe,value='resample-method = src-linear',command=PaRe,width=16)
    vPaResrclinear.grid(row=2,column=5)

    vPaResoxrhq=Radiobutton(frame5,indicatoron=0,text='soxr-hq',font=('Monospace Regular',11),variable=vPaRe,value='resample-method = soxr-hq',command=PaRe,width=16)
    vPaResoxrhq.grid(row=2,column=6)

    vPaResoxrvhq=Radiobutton(frame5,indicatoron=0,text='soxr-vhq',font=('Monospace Regular',11),variable=vPaRe,value='resample-method = soxr-vhq',command=PaRe,width=16)
    vPaResoxrvhq.grid(row=2,column=7)

# End ----------

    frame6=LabelFrame(page1)
    frame6.grid(row=12,column=0,sticky='NESW')

# ---------- Default & Apply PA Button ----------

# Text below app
    label = Label(frame6, text="     Restarting services take few seconds     ",font=('Monospace Regular',11))
    label.grid(row=1, column=3)

    RemPa12=LabelFrame(frame6,text=" 5) Apply changes ",font=('Monospace Regular',11))
    RemPa12.grid(row=1,column=4,sticky='NES',padx=5,pady=5)

    apply_btn2=Button(RemPa12,text='Apply & Restart PulseAudio',font=('Monospace Regular',11),command=applyPA)
    apply_btn2.grid(row=1,column=1,padx=5,pady=5,sticky='NESW')

# End ----------

    RemPa14=LabelFrame(frame6,text=" * Predefined PulseAudio Config ",font=('Monospace Regular',11))
    RemPa14.grid(row=1,column=2,sticky='NESW',padx=5,pady=5)

    vPaConf01=Radiobutton(RemPa14,text='Default',font=('Monospace Regular',11),variable=vPaPrefConf,value='Default',command=defpa)
    vPaConf01.grid(row=1,column=1,padx=5,sticky='NW')

    vPaConf02=Radiobutton(RemPa14,text='Recommended',font=('Monospace Regular',11),variable=vPaPrefConf,value='Recommended',command=recpa)
    vPaConf02.grid(row=2,column=1,padx=5)

# Button Show Samplerate

    apply_btn3=Button(frame1,text='PulseAudio Status & Output (Click to refresh)',font=('Monospace Regular',11),command=showsamplerate)
    apply_btn3.grid(row=0,column=3)

# -------------------- Tab 2 (ALSA) --------------------

    # page2 main frame
    frame222=LabelFrame(page2,bd=6,bg="green3")
    frame222.grid(row=0,column=1,columnspan=10,sticky='NESW')

    # page frame
    frame33=LabelFrame(frame222,bd=5,bg="black")
    frame33.grid(row=0,column=1,rowspan=10,sticky='NESW')

	# ALSA conf info frame (white)
    frame122=Label(frame222)
    frame122.grid(row=1,column=1,columnspan=2,sticky='nes',padx=5,pady=5)


    frame101=LabelFrame(page2,text='2) Apply changes')
    frame101.grid(row=1,column=10,sticky='NES',padx=5,pady=5)

    frame102=LabelFrame(page2,text='1) Select Card')
    frame102.grid(row=1,column=1,sticky='NSW',padx=5,pady=5)

# End ----------

    label=Label(frame33,bg="black",text="------------------------------------------------------------------",font=('Monospace Regular',11))
    label.grid(row=0,column=1,columnspan=10,sticky='nsw')

    # ---------- Show Device Info ----------

    # Show Devices number
    label=Label(frame33,textvariable=vADefDevId,fg='grey',bg='black',font=('Monospace Regular',11))
    label.grid(row=1,column=0,columnspan=2,sticky='esw')

    # Show Devices name
    label=Label(frame33,textvariable=vADefDevName,fg='grey',bg='black',font=('Monospace Regular',11))
    label.grid(row=1,column=2,columnspan=2,sticky='esw')

    # Show ALSA Config
    label=Label(frame122,textvariable=ShvALConf,fg='white',bg='black',font=('Monospace Regular',11))
    label.grid(row=1,column=5,rowspan=8,columnspan=8,sticky='nes')


    # End ----------

# ---------- ALSA Apply ----------

    try:
        ALSAdevName0=subprocess.check_output(["cat /proc/asound/card0/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
        vADefDevName0.set(ALSAdevName0)
    except subprocess.CalledProcessError as e:
        vADefDevName0.set("---")

    try:
        ALSAdevName1=subprocess.check_output(["cat /proc/asound/card1/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
        vADefDevName1.set(ALSAdevName1)
    except subprocess.CalledProcessError as e:
        vADefDevName1.set("---")

    try:
        ALSAdevName2=subprocess.check_output(["cat /proc/asound/card2/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
        vADefDevName2.set(ALSAdevName2)
    except subprocess.CalledProcessError as e:
        vADefDevName2.set("---")

    try:
        ALSAdevName3=subprocess.check_output(["cat /proc/asound/card3/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
        vADefDevName3.set(ALSAdevName3)
    except subprocess.CalledProcessError as e:
        vADefDevName3.set("---")

    try:
        ALSAdevName4=subprocess.check_output(["cat /proc/asound/card4/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
        vADefDevName4.set(ALSAdevName4)
    except subprocess.CalledProcessError as e:
        vADefDevName4.set("---")

    try:
        ALSAdevName5=subprocess.check_output(["cat /proc/asound/card5/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
        vADefDevName5.set(ALSAdevName5)
    except subprocess.CalledProcessError as e:
        vADefDevName5.set("---")

    try:
        ALSAdevName6=subprocess.check_output(["cat /proc/asound/card6/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
        vADefDevName6.set(ALSAdevName6)
    except subprocess.CalledProcessError as e:
        vADefDevName6.set("---")

    try:
        ALSAdevName7=subprocess.check_output(["cat /proc/asound/card7/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
        vADefDevName7.set(ALSAdevName7)
    except subprocess.CalledProcessError as e:
        vADefDevName7.set("---")

    try:
        ALSAdevName8=subprocess.check_output(["cat /proc/asound/card8/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
        vADefDevName8.set(ALSAdevName8)
    except subprocess.CalledProcessError as e:
        vADefDevName8.set("---")


    OPTIONS = [
    vADefDevName0.get(),
    vADefDevName1.get(),
    vADefDevName2.get(),
    vADefDevName3.get(),
    vADefDevName4.get(),
    vADefDevName5.get(),
    vADefDevName6.get(),
    vADefDevName7.get(),
    vADefDevName8.get()
    ]

    variable01 = StringVar(frame101)
    variable01.set(OPTIONS[0]) # default value

    FindAL01=OptionMenu(frame102, variable01, *OPTIONS )
    FindAL01.grid(row=1,column=0,sticky='nsw')

    def optionsupdate():

        # clear optionmenu
        FindAL01['menu'].delete(0, 'end')

        try:
            ALSAdevName0=subprocess.check_output(["cat /proc/asound/card0/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
            vADefDevName0.set(ALSAdevName0)
        except subprocess.CalledProcessError as e:
            vADefDevName0.set("---")

        try:
            ALSAdevName1=subprocess.check_output(["cat /proc/asound/card1/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
            vADefDevName1.set(ALSAdevName1)
        except subprocess.CalledProcessError as e:
            vADefDevName1.set("---")

        try:
            ALSAdevName2=subprocess.check_output(["cat /proc/asound/card2/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
            vADefDevName2.set(ALSAdevName2)
        except subprocess.CalledProcessError as e:
            vADefDevName2.set("---")

        try:
            ALSAdevName3=subprocess.check_output(["cat /proc/asound/card3/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
            vADefDevName3.set(ALSAdevName3)
        except subprocess.CalledProcessError as e:
            vADefDevName3.set("---")

        try:
            ALSAdevName4=subprocess.check_output(["cat /proc/asound/card4/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
            vADefDevName4.set(ALSAdevName4)
        except subprocess.CalledProcessError as e:
            vADefDevName4.set("---")

        try:
            ALSAdevName5=subprocess.check_output(["cat /proc/asound/card5/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
            vADefDevName5.set(ALSAdevName5)
        except subprocess.CalledProcessError as e:
            vADefDevName5.set("---")

        try:
            ALSAdevName6=subprocess.check_output(["cat /proc/asound/card6/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
            vADefDevName6.set(ALSAdevName6)
        except subprocess.CalledProcessError as e:
            vADefDevName6.set("---")

        try:
            ALSAdevName7=subprocess.check_output(["cat /proc/asound/card7/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
            vADefDevName7.set(ALSAdevName7)
        except subprocess.CalledProcessError as e:
            vADefDevName7.set("---")

        try:
            ALSAdevName8=subprocess.check_output(["cat /proc/asound/card8/id"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
            vADefDevName8.set(ALSAdevName8)
        except subprocess.CalledProcessError as e:
            vADefDevName8.set("---")

        OPTIONS = [
        vADefDevName0.get(),
        vADefDevName1.get(),
        vADefDevName2.get(),
        vADefDevName3.get(),
        vADefDevName4.get(),
        vADefDevName5.get(),
        vADefDevName6.get(),
        vADefDevName7.get(),
        vADefDevName8.get()
        ]

        variable01.set(OPTIONS[0]) # default value

        #new optionmenu

        for choice in OPTIONS:
           FindAL01['menu'].add_command(label=choice, command=_setit(variable01, choice))


        ALSAdevId=subprocess.check_output([" aplay -l | awk -F \: '/,/{print $1}' | uniq "],universal_newlines=True,shell=True).strip();
        vADefDevId.set(ALSAdevId)

        ALSAdevName=subprocess.check_output(["aplay -l | awk -F \: '/,/{print $2}' | awk '{print $1}' | uniq"],universal_newlines=True,shell=True).strip();
        vADefDevName.set(ALSAdevName)
        subprocess.call('echo "-----------------------------------------------------------" && echo "\e[32m ALSA \e[0m \n"-----------------------------------------------------------""', shell=True)
        subprocess.call('echo "Detected ALSA Soundcards \n"', shell=True)
        print (vADefDevName.get())


    # Button Show Devices
    FindAL=Button(frame33,text='Detect Soundcards',command=optionsupdate)
    FindAL.grid(row=0,column=0,columnspan=9,rowspan=1,padx=5,pady=5,sticky='nsw')

    def applyalsa():
        print(variable01.get())
        Cappterminal=(variable01.get())
        subprocess.call('sudo sed -i "/card / c card {}" /etc/asound.conf'.format(Cappterminal),shell=True);

        ALSAConf=subprocess.check_output(["cat /etc/asound.conf"],universal_newlines=True,shell=True,stderr=subprocess.STDOUT).strip()
        ShvALConf.set(ALSAConf)

        subprocess.call('alsactl kill rescan && alsactl nrestore ',stderr=subprocess.DEVNULL, shell=True)
        subprocess.call('echo "-----------------------------------------------------------" && echo "\e[32m ALSA \e[0m \n"-----------------------------------------------------------""', shell=True)
        subprocess.call('echo "Current /etc/asound.conf file \n"', shell=True)
        subprocess.call('cat /etc/asound.conf', shell=True)
#        subprocess.call('echo "-----------------------------------------------------------"', shell=True)


    apply_btn3=Button(frame101,text='Apply & Restart Alsa',font=('Monospace Regular',11),command=applyalsa)
    apply_btn3.grid(row=1,column=1,sticky='nesw')

# End ----------
    top.mainloop()

# ---------- Variable Config ----------

# PulseAudio
vConfPaBitdepth=StringVar()                 # Current BithDepth
vConfPaPriRate=StringVar()                  # Current Primary Samplerate
vConfPaAltRate=StringVar()                  # Current Alternative Samplerate
vConfPaRe=StringVar()                       # Current Resample method

vPaBitdepth=StringVar()                 # BithDepth
vPaPriRate=StringVar()                  # Primary Samplerate
vPaAltRate=StringVar()                  # Alternative Samplerate
vPaRe=StringVar()                       # Resample method
vPaAre=StringVar()                      # avoid-resampling
vPaRun=StringVar()                      # Check Running PulseAudio instances
vPaPrefConf=StringVar()                 # Predefined Conf

ShvPaOut=StringVar()                    # Show Current PA output
ToggleBtn=StringVar()                   # Toggle Button

# ALSA
ShvALConf=StringVar()                   # Alsa asound.conf file data
vADefDev=StringVar()                    # Default Device
vADefDevId=StringVar()                  # Device id
vADefDevName=StringVar()                # Device name list

vADefDevName0=StringVar()               # Device name list
vADefDevName1=StringVar()               # Device name list
vADefDevName2=StringVar()               # Device name list
vADefDevName3=StringVar()               # Device name list
vADefDevName4=StringVar()               # Device name list
vADefDevName5=StringVar()               # Device name list
vADefDevName6=StringVar()               # Device name list
vADefDevName7=StringVar()               # Device name list
vADefDevName8=StringVar()               # Device name list

# End ----------

# ---------- Set some Values for Variable on app startup ----------

# PulseAudio
vPaBitdepth.set('; default-sample-format = s16le')      # PulseAudio BithDepth
vPaPriRate.set('; default-sample-rate = 44100')         # PulseAudio Primary Samplerate
vPaAltRate.set('; alternate-sample-rate = 48000')       # PulseAudio Alternative Samplerate
vPaRe.set('; resample-method = speex-float-1')          # PulseAudio Resample method
vPaAre.set('; avoid-resampling = false')                # PulseAudio Avoid Resample

ToggleBtn='Off'                                         # PulseAudio resample button variable

vPaRun.set('')                                          # Check Running PulseAudio instances
vPaPrefConf.set('')                                     # Predefined Conf initial value
ShvPaOut.set('')                                        # Show Current PA output


# ALSA
vADefDev.set('')                                        # ALSA Default Device
vADefDevName.set('')                                    # ALSA Default name list

# ---------- Print Variable Data ----------

# PulseAudio
def Pabitdepth():
    print ("-----------------------------------------------------------")
    print ("\033[96m PulseAudio \033[00m")
    print ("-----------------------------------------------------------")
    print(vPaBitdepth.get())

def PaPriRate():
    print ("-----------------------------------------------------------")
    print ("\033[96m PulseAudio \033[00m")
    print ("-----------------------------------------------------------")
    print(vPaPriRate.get())

def PaAltRate():
    print ("-----------------------------------------------------------")
    print ("\033[96m PulseAudio \033[00m")
    print ("-----------------------------------------------------------")
    print(vPaAltRate.get())

def PaRe():
    print ("-----------------------------------------------------------")
    print ("\033[96m PulseAudio \033[00m")
    print ("-----------------------------------------------------------")
    print(vPaRe.get())

def PaOut():
    print ("-----------------------------------------------------------")
    print ("\033[96m PulseAudio \033[00m")
    print ("-----------------------------------------------------------")
    print(ShvPaOut.get())

def PaRun():
    print(vPaRun.get())

def PaPrefConf():
    print(vPaPrefConf.get())

# ALSA
def ADefDev():
    print(vADefDev.get())

# End ----------

# ---------- Predefined Commands ----------

# Default button
def defpa():
    vPaBitdepth.set('; default-sample-format = s16le')
    vPaPriRate.set('; default-sample-rate = 44100')
    vPaAltRate.set('; alternate-sample-rate = 48000')
    vPaRe.set('; resample-method = speex-float-1')

    if ToggleBtn == 'On':
        PaAre()

    print ("-----------------------------------------------------------")
    print ("\033[96m PulseAudio \033[00m")
    print ("-----------------------------------------------------------")
    print ("Default Values ")

# Recommended button
def recpa():
    vPaBitdepth.set('default-sample-format = s24le')
    vPaPriRate.set('default-sample-rate = 44100')
    vPaAltRate.set('alternate-sample-rate = 48000')
    vPaRe.set('resample-method = src-sinc-best-quality')

    if ToggleBtn == 'On':
        PaAre()

    print ("-----------------------------------------------------------")
    print ("\033[96m PulseAudio \033[00m")
    print ("-----------------------------------------------------------")
    print ("Recommended Values ")
# End ----------


# Apply PA Button
def applyPA():

    try:
        CvPaBitdepth=(vPaBitdepth.get())
        CvPaPriRate=(vPaPriRate.get())
        CvPaAltRate=(vPaAltRate.get())
        CvPaRe=(vPaRe.get())
        CvPaAre=(vPaAre.get())

        print ("-----------------------------------------------------------")
        print ("\033[96m PulseAudio \033[00m")
        print ("-----------------------------------------------------------")
        print ("Applying Settings ")
        subprocess.call('sudo sed -i "/default-sample-format =/ c {}" /etc/pulse/daemon.conf && sudo sed -i "/default-sample-rate =/ c {}" /etc/pulse/daemon.conf && sudo sed -i "/alternate-sample-rate =/ c {}" /etc/pulse/daemon.conf && sudo sed -i "/resample-method =/ c {}" /etc/pulse/daemon.conf && sudo sed -i "/avoid-resampling =/ c {}" /etc/pulse/daemon.conf'.format(CvPaBitdepth,CvPaPriRate,CvPaAltRate,CvPaRe,CvPaAre),shell=True);

        print ("Restarting PulseAudio ")
        PaStatus01=subprocess.check_output(["pulseaudio --kill"],universal_newlines=True,shell=True,stderr=subprocess.STDOUT).strip()

    except subprocess.CalledProcessError as e:

        print ("Handling PulseAudio Error ")
        subprocess.call('pulseaudio --start', shell=True);
        print ("Done ")
        print ("-----------------------------------------------------------")

# The current PulseAudio output setting is passed to variable and printed to terminal
def showsamplerate():
    try:
        showsamplerateoutput=subprocess.check_output(["pacmd list-sinks | grep sample"],universal_newlines=True,shell=True,stderr=subprocess.STDOUT).strip()
        ShvPaOut.set(showsamplerateoutput)
        PaStatus=subprocess.check_output(["pulseaudio --check"],universal_newlines=True,shell=True,stderr=subprocess.STDOUT).strip()
        vPaRun.set("Status: On")

        print ("-----------------------------------------------------------")
        print ("\033[96m PulseAudio \033[00m")
        print ("-----------------------------------------------------------")
        print ("Status: \033[92m On \033[00m")
        print (ShvPaOut.get())

        # Check current pulseaudio config and show it to user at startup

        showdefbitdepth=subprocess.check_output(["cat '/etc/pulse/daemon.conf' | sed -n 's/\(default-sample-format\)/\1/p'"],universal_newlines=True,shell=True,stderr=subprocess.STDOUT).strip()
        vConfPaBitdepth.set("default-sample-format"+showdefbitdepth)

        showdefsamplerate=subprocess.check_output(["cat '/etc/pulse/daemon.conf' | sed -n 's/\(default-sample-rate\)/\1/p'"],universal_newlines=True,shell=True,stderr=subprocess.STDOUT).strip()
        vConfPaPriRate.set("default-sample-rate"+showdefsamplerate)

        showaltsamplerate=subprocess.check_output(["cat '/etc/pulse/daemon.conf' | sed -n 's/\(alternate-sample-rate\)/\1/p'"],universal_newlines=True,shell=True,stderr=subprocess.STDOUT).strip()
        vConfPaAltRate.set("alternate-sample-rate"+showaltsamplerate)

        showresamplemethod=subprocess.check_output(["cat '/etc/pulse/daemon.conf' | sed -n 's/\(resample-method\)/\1/p'"],universal_newlines=True,shell=True,stderr=subprocess.STDOUT).strip()

        vConfPaRe.set("resample-method"+showresamplemethod)

        print()
        print(vConfPaBitdepth.get())
        print(vConfPaPriRate.get())
        print(vConfPaAltRate.get())
        print(vConfPaRe.get())

    except subprocess.CalledProcessError as e:
        ShvPaOut.set("Output: N/A")
        vPaRun.set("Status: Off")
        print ("-----------------------------------------------------------")
        print ("\033[96m PulseAudio \033[00m")
        print ("-----------------------------------------------------------")
        print ("Status:\033[91m Off \033[00m")
        print (ShvPaOut.get())
        print ("No Running PulseAudio Detected (Run Apply & Restart PulseAudio)")

#        e.stderr.write(
#        "No PulseAudio playback detected: %s\n"
#        % (e.returncode))
# End ----------

# Apply Alsa
def applyAL():
    cADefDev=(vADefDev.get())
    cADefDev=(vADefDev.get())

    subprocess.call('sudo sed -i "/card / c card {}" /etc/asound.conf && sudo sed -i "/card / c card {}" /etc/asound.conf | alsactl kill rescan && alsactl nrestore'.format(cADefDev,cADefDev),shell=True);

# End ----------


# The current ALSA device list is passed to variable and printed to terminal
def showalsadevices():

    ALSAdevId=subprocess.check_output([" aplay -l | awk -F \: '/,/{print $1}' | uniq "],universal_newlines=True,shell=True).strip();
    vADefDevId.set(ALSAdevId)

    ALSAdevName=subprocess.check_output(["aplay -l | awk -F \: '/,/{print $2}' | awk '{print $1}' | uniq"],universal_newlines=True,shell=True).strip();
    vADefDevName.set(ALSAdevName)
    subprocess.call('echo "-----------------------------------------------------------" && echo "\e[32m ALSA \e[0m  \n"-----------------------------------------------------------""', shell=True)
    subprocess.call('echo "Detected ALSA Soundcards"', shell=True)
    print (vADefDevName.get())

# End ----------

# Run at start to check --> asound.conf exist and if not it will be created. Alternatively config can be created manually by following this tutorial --> https://www.alsa-project.org/main/index.php/Setting_the_default_device)
try:
    subprocess.check_output(["cat /etc/asound.conf"],stderr=subprocess.DEVNULL,universal_newlines=True,shell=True).strip();
except subprocess.CalledProcessError as e:
    subprocess.call('echo "-----------------------------------------------------------" && echo "\e[33m Creating SystemWide file \e[0m  \n"-----------------------------------------------------------""', shell=True)
    subprocess.call('echo "--------------------- /etc/asound.conf --------------------" && sudo touch /etc/asound.conf && echo "-----------------------------------------------------------" && echo "pcm.!default {\ntype hw\ncard 1\n} \nctl.!default {\ntype hw\ncard 1\n}" | sudo tee /etc/asound.conf', shell=True)
    subprocess.call('alsactl kill rescan && alsactl nrestore ', stderr=subprocess.DEVNULL,shell=True)
    subprocess.call('echo "-----------------------------------------------------------"', shell=True)
    subprocess.call('echo "\e[31m Please Setup Soundcard from ALSA Tab \e[0m"', shell=True)
    subprocess.call('echo "-----------------------------------------------------------"', shell=True)

ALSAConf=subprocess.check_output(["sudo cat /etc/asound.conf"],universal_newlines=True,shell=True,stderr=subprocess.STDOUT).strip()
ShvALConf.set(ALSAConf)

# Check current pulseaudio config and show it to user at startup
try:
    showdefbitdepth=subprocess.check_output(["cat '/etc/pulse/daemon.conf' | sed -n 's/\(default-sample-format\)/\1/p'"],universal_newlines=True,shell=True,stderr=subprocess.STDOUT).strip()
    vConfPaBitdepth.set("default-sample-format"+showdefbitdepth)

    showdefsamplerate=subprocess.check_output(["cat '/etc/pulse/daemon.conf' | sed -n 's/\(default-sample-rate\)/\1/p'"],universal_newlines=True,shell=True,stderr=subprocess.STDOUT).strip()
    vConfPaPriRate.set("default-sample-rate"+showdefsamplerate)

    showaltsamplerate=subprocess.check_output(["cat '/etc/pulse/daemon.conf' | sed -n 's/\(alternate-sample-rate\)/\1/p'"],universal_newlines=True,shell=True,stderr=subprocess.STDOUT).strip()
    vConfPaAltRate.set("alternate-sample-rate"+showaltsamplerate)

    showresamplemethod=subprocess.check_output(["cat '/etc/pulse/daemon.conf' | sed -n 's/\(resample-method\)/\1/p'"],universal_newlines=True,shell=True,stderr=subprocess.STDOUT).strip()

    vConfPaRe.set("resample-method"+showresamplemethod)

except subprocess.CalledProcessError as e:
    print ("Cannot show current pulseaudio config")
# End ----------

if __name__ == '__main__':
    main()
