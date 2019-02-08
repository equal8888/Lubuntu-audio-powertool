#!/usr/bin/python3
from tkinter import *  					# the GUI toolkit.
from tkinter import ttk					# Define Pages and Separators
import tkinter.messagebox   			# Messagebox About page

import subprocess						# for pulseaudio config

top = Tk()
def main():

# ---------- Define MainFrame ----------

    mainFrame=Frame(top,relief="sunken",border=1)
    Description=Label(mainFrame,text="Audio Powertool:")

    mainFrame.master.title("Audio Powertool for Lubuntu 16.04.3 LTS")
    mainFrame.master.minsize(width=717,height=258)
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
    frame0=tkinter.LabelFrame(page1,bd=6,bg="blue3")
    frame0.grid(row=0,column=0,sticky='nesw')

    # page1 frame
    frame1=tkinter.LabelFrame(frame0,bd=5,bg="black")
    frame1.grid(row=0,rowspan=5,column=1)

	# White box around info txt
    frame2=Label(frame1,bg="white")
    frame2.grid(row=3,column=3,sticky='nes')

	# White box around info txt
    frame7=Label(frame1,bg="white")
    frame7.grid(row=2,column=3,sticky='nes')

# ---------- Show Info ----------

# show current PA status from button
    label=Label(frame7,textvariable=vPaRun,fg='white',bg='black',font=('Monospace Regular',11))
    label.grid(sticky='nes')

# show current PA output from button
    label=Label(frame2,textvariable=ShvPaOut,fg='white',bg='black',font=('Monospace Regular',11))
    label.grid(sticky='nes')

# Bitdepth Samplerate
    label=Label(frame1,textvariable=vPaBitdepth,fg='grey',bg='black',font=('Monospace Regular',11))
    label.grid(row=0,column=1,sticky='nsw')

# Primary Samplerate
    label=Label(frame1,textvariable=vPaPriRate,fg='grey',bg='black',font=('Monospace Regular',11))
    label.grid(row=1,column=1,columnspan=4,sticky='nsw')

# Alternative Samplerate
    label=Label(frame1,textvariable=vPaAltRate,fg='grey',bg='black',font=('Monospace Regular',11))
    label.grid(row=2,column=1,columnspan=4,sticky='nsw')

# Resampling
    label=Label(frame1,textvariable=vPaRe,fg='grey',bg='black',font=('Monospace Regular',11))
    label.grid(row=3,column=1,columnspan=4,sticky='nsw')

# Shortcut to get what I want atm....
    label=Label(frame1,bg="black",text="                     ")
    label.grid(row=0,column=2,sticky='nsw')

# End ----------

	# Label Resample method rowspan=4
    label=Label(frame0,text=" 1) Bit Depth ")
    label.grid(row=0,column=0,sticky='nesw')

# ---------- BithDepth Radio Buttons ----------

	# Set the BithDepth value to Default for variable vPaBitdepth
    RadBit16=Radiobutton(frame0,text='Default',variable=vPaBitdepth,value='; default-sample-format = s16le',command=Pabitdepth,width=8)
    RadBit16.grid(row=1,column=0,sticky='nsw')

	# Set the BithDepth value to 16 Bit for variable vPaBitdepth
    RadBit16=Radiobutton(frame0,text='16 Bit',variable=vPaBitdepth,value='  default-sample-format = s16le',command=Pabitdepth,width=8)
    RadBit16.grid(row=2,column=0,sticky='nsw')

    # Set the BithDepth value to 24 Bit for variable vPaBitdepth
    RadBit24=Radiobutton(frame0,text='24 Bit',variable=vPaBitdepth,value='  default-sample-format = s24le',command=Pabitdepth,width=8)
    RadBit24.grid(row=3,column=0,sticky='nsw')

    # Set the BithDepth value to 32 Bit for variable vPaBitdepth
    RadBit32=Radiobutton(frame0,text='32 Bit',variable=vPaBitdepth,value='  default-sample-format = s32le',command=Pabitdepth,width=8)
    RadBit32.grid(row=4,column=0,sticky='nsw')

# End ----------

    # Separator
    ttk.Separator(page1).grid(row=2,column=0,sticky="ew")

# ---------- Primary Samplerate Radio Buttons ----------

	# samplerate frame
    frame3=Label(page1)
    frame3.grid(row=5,column=0,sticky='nesw')

	# "Sub frame" for samplerate frame
    frame4=Label(frame3)
    frame4.grid(row=5,column=0,sticky='nesw')

	# Label
    label=Label(frame4,text="2) Primary Sample rate")
    label.grid(row=1,column=1)

	# Set the BithDepth value to default for variable vPaBitdepth
    RadPriRateDefault=Radiobutton(frame4,text='Default',variable=vPaPriRate,value='; default-sample-rate = 44100',command=PaPriRate,width=11)
    RadPriRateDefault.grid(row=1,column=2)

	# Set the BithDepth value to 44,100 Hz for variable vPaBitdepth
    RadPriRate44100=Radiobutton(frame4,text='44,100 Hz',variable=vPaPriRate,value='  default-sample-rate = 44100',command=PaPriRate,width=11)
    RadPriRate44100.grid(row=1,column=3)

	# Set the BithDepth value to 48,000 Hz for variable vPaBitdepth
    RadPriRate48000=Radiobutton(frame4,text='48,000 Hz',variable=vPaPriRate,value='  default-sample-rate = 48000',command=PaPriRate,width=11)
    RadPriRate48000.grid(row=1,column=4)

	# Set the BithDepth value to 88,200 Hz for variable vPaBitdepth
    RadPriRate88200=Radiobutton(frame4,text='88,200 Hz',variable=vPaPriRate,value='  default-sample-rate = 88200',command=PaPriRate,width=11)
    RadPriRate88200.grid(row=1,column=5)

	# Set the BithDepth value to 96,000 Hz for variable vPaBitdepth
    RadPriRate96000=Radiobutton(frame4,text='96,000 Hz',variable=vPaPriRate,value='  default-sample-rate = 96000',command=PaPriRate,width=11)
    RadPriRate96000.grid(row=1,column=6)

# End ----------

# ---------- Alternative Samplerate Radio Buttons ----------

	# Label
    label=Label(frame4,text="3) Alternative Sample rate")
    label.grid(row=2,column=1)

	# Set the BithDepth value to default for variable vPaAltRate
    RadAltRateDefault=Radiobutton(frame4,text='Default',variable=vPaAltRate,value='; alternate-sample-rate = 48000',command=PaAltRate,width=11)
    RadAltRateDefault.grid(row=2,column=2)

	# Set the BithDepth value to 48,000 Hz for variable vPaAltRate
    RadAltRate48000=Radiobutton(frame4,text='44,100 Hz',variable=vPaAltRate,value='  alternate-sample-rate = 44100',command=PaAltRate,width=11)
    RadAltRate48000.grid(row=2,column=3)

	# Set the BithDepth value to 88,200 Hz for variable vPaAltRate
    RadAltRate48000=Radiobutton(frame4,text='48,000 Hz',variable=vPaAltRate,value='  alternate-sample-rate = 48000',command=PaAltRate,width=11)
    RadAltRate48000.grid(row=2,column=4)

	# Set the BithDepth value to 96,000 Hz for variable vPaAltRate
    RadAltRate96000=Radiobutton(frame4,text='88,200 Hz',variable=vPaAltRate,value='  alternate-sample-rate = 88200',command=PaAltRate,width=11)
    RadAltRate96000.grid(row=2,column=5)

	# Set the BithDepth value to 192,000 Hz for variable vPaAltRate
    RadAltRate192000=Radiobutton(frame4,text='96,000 Hz',variable=vPaAltRate,value='  alternate-sample-rate = 96000',command=PaAltRate,width=11)
    RadAltRate192000.grid(row=2,column=6)

# End ----------

    # Separator-2
    ttk.Separator(page1).grid(row=8,column=0,sticky="ew")

# ---------- Resample method Radio Buttons ----------
    frame5=Label(page1)
    frame5.grid(row=9,column=0,sticky='nesw')


    # Label Resample method
    label=Label(frame5,text="4) Resample method")
    label.grid(row=1,column=1)

	# Set the Resample value to speexfloat-10 for variable vPaRe
    vPaRespeexfloat10=Radiobutton(frame5,indicatoron=0,text='speexfloat-10',variable=vPaRe,value='  resample-method = speex-float-10',command=PaRe,width=16)
    vPaRespeexfloat10.grid(row=1,column=4)

	# Set the Resample value to medium for variable vPaRe
    vPaRemedium=Radiobutton(frame5,indicatoron=0,text='medium',variable=vPaRe,value='  resample-method = src-sinc-medium-quality',command=PaRe,width=16)
    vPaRemedium.grid(row=1,column=5)

	# Set the Resample value to best for variable vPaRe
    vPaRebest=Radiobutton(frame5,indicatoron=0,text='best',variable=vPaRe,value='  resample-method = src-sinc-best-quality',command=PaRe,width=16)
    vPaRebest.grid(row=1,column=6)

	# Set the Resample value to zero-orderhold for variable vPaRe
    vPaRezeroOrderhold=Radiobutton(frame5,indicatoron=0,text='zero-orderhold',variable=vPaRe,value='  resample-method = src-zero-order-hold',command=PaRe,width=16)
    vPaRezeroOrderhold.grid(row=1, column=7)

	# Set the Resample value to Default Resampling for variable vPaRe
    vPaReStopResampling=Radiobutton(frame5,indicatoron=0,text='Default Resampling',variable=vPaRe,value='; resample-method = speex-float-1',command=PaRe,width=25)
    vPaReStopResampling.grid(row=2,column=1)

	# Set the Resample value to ffmpeg for variable vPaRe
    vPaReffmpeg=Radiobutton(frame5,indicatoron=0,text='ffmpeg',variable=vPaRe,value='  resample-method = ffmpeg',command=PaRe,width=16)
    vPaReffmpeg.grid(row=2,column=4)

	# Set the Resample value to src-linear for variable vPaRe
    vPaResrclinear=Radiobutton(frame5,indicatoron=0,text='src-linear',variable=vPaRe,value='  resample-method = src-linear',command=PaRe,width=16)
    vPaResrclinear.grid(row=2,column=5)

	# Set the Resample value to soxr-hq for variable vPaRe
    vPaResoxrhq=Radiobutton(frame5,indicatoron=0,text='soxr-hq',variable=vPaRe,value='  resample-method = soxr-hq',command=PaRe,width=16)
    vPaResoxrhq.grid(row=2,column=6)

	# Set the Resample value to soxr-vhq for variable vPaRe
    vPaResoxrvhq=Radiobutton(frame5,indicatoron=0,text='soxr-vhq',variable=vPaRe,value='  resample-method = soxr-vhq',command=PaRe,width=16)
    vPaResoxrvhq.grid(row=2,column=7)

# End ----------

    # Separator3
    ttk.Separator(page1).grid(row=11,column=0,sticky="ew")

	# Set the Buttons (Default Settings)
    frame5=Label(page1)
    frame5.grid(row=12,column=0,sticky='nesw')


	# Set the Apply Button
    frame6=Label(page1)
    frame6.grid(row=12,column=6,sticky='nesw')

# ---------- Default & Apply PA Button ----------

# ---------- Note to self ----------
# Make Default Button and
# Apply Button disable it self for few seconds after button press 😘

# Text below app
    label = Label(frame5, text="           Restarting services take few seconds           ")
    label.grid(row=1, column=3)

    RemPa12=tkinter.LabelFrame(frame5,text=" 5) Apply changes ")
    RemPa12.grid(row=1,column=4,sticky='NES',padx=5,pady=5)

    apply_btn2=Button(RemPa12,text='Apply & Restart PulseAudio',command=applyPA)
    apply_btn2.grid(row=1,column=1,padx=5,pady=5,sticky='e')

# End ----------
    RemPa14=tkinter.LabelFrame(frame5,text=" * Predefined PulseAudio Config ")
    RemPa14.grid(row=1,column=2,sticky='NESW',padx=5,pady=5)

    vPaConf01=Radiobutton(RemPa14,text='Default',variable=vPaPrefConf,value='Default',command=defpa)
    vPaConf01.grid(row=1,column=1,padx=5,sticky='NW')

    vPaConf02=Radiobutton(RemPa14,text='Recommended',variable=vPaPrefConf,value='Recommended',command=recpa)
    vPaConf02.grid(row=2,column=1,padx=5)

# Button Show Samplerate
    apply_btn3=Button(frame1,text='PulseAudio Status & Output (Click to refresh)',command=showsamplerate)
    apply_btn3.grid(row=0,column=3)

# -------------------- Tab 2 (ALSA) --------------------


# End ----------


# ----------------- Menubar  -----------------

    menubar=Menu(mainFrame.master)
    filemenu=Menu(menubar,tearoff=0)
#    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=mainFrame.master.quit)
    menubar.add_cascade(label="File",menu=filemenu)

    editmenu=Menu(menubar,tearoff=0)
    editmenu.add_command(label="Config",state=DISABLED) # No config menu
    menubar.add_cascade(label="Edit",menu=editmenu)

    helpmenu=Menu(menubar,tearoff=0)

    helpmenu.add_command(label="About",command=helpmenu01)
    menubar.add_cascade(label="Help",menu=helpmenu)

    mainFrame.master.config(menu=menubar)

# End ----------

    top.mainloop()

# ---------- Variable Config ----------

# PulseAudio
vPaBitdepth=StringVar() 			# BithDepth
vPaPriRate=StringVar() 				# Primary Samplerate
vPaAltRate=StringVar() 				# Alternative Samplerate
vPaRe=StringVar() 					# Resample method
vPaRun=StringVar()                  # Check Running PulseAudio instances
vPaPrefConf=StringVar()             # Predefined Conf


ShvPaOut=StringVar() 				# Show Current PA output

# End ----------

# ---------- Set some Values for Variable on app startup ----------

# PulseAudio
vPaBitdepth.set('; default-sample-format = s16le')      # PulseAudio BithDepth
vPaPriRate.set('; default-sample-rate = 44100')         # PulseAudio Primary Samplerate
vPaAltRate.set('; alternate-sample-rate = 48000')       # PulseAudio Alternative Samplerate
vPaRe.set('; resample-method = speex-float-1')          # PulseAudio Resample method
vPaRun.set('')                                          # Check Running PulseAudio instances
vPaPrefConf.set('')                                     # Predefined Conf initial value
ShvPaOut.set('')                                        # Show Current PA output

# ---------- Print Variable Data ----------

# PulseAudio
def Pabitdepth():
    print(vPaBitdepth.get())

def PaPriRate():
    print(vPaPriRate.get())

def PaAltRate():
    print(vPaAltRate.get())

def PaRe():
    print(vPaRe.get())

def PaOut():
    print(ShvPaOut.get())

def PaRun():
    print(vPaRun.get())

def PaUninst():
    print(vPaUninst.get())

def PaPrefConf():
    print(vPaPrefConf.get())

# ALSA
def ADefDev():
    print(vADefDev.get())

# End ----------

# ---------- Button Commands ----------

def helpmenu01():
    tkinter.messagebox.showinfo("About Audio Powertool: ","PulseAudio is only a SOFTWARE MIXER' \n \nDont set the Samplerate to Maximum option available\n \nthat will do audio resampling and you dont want that!")

# Default button
def defpa():
# Set new values for variables
    vPaBitdepth.set('; default-sample-format = s16le')
    vPaPriRate.set('; default-sample-rate = 44100')
    vPaAltRate.set('; alternate-sample-rate = 48000')
    vPaRe.set('; resample-method = speex-float-1')
# Show variables
    print ("-------------- Default Values ---------------")
    print(vPaBitdepth.get())
    print(vPaPriRate.get())
    print(vPaAltRate.get())
    print(vPaRe.get())
    print ("---------------------------------------------")

# End ----------

def recpa():
# Set new values for variables
    vPaBitdepth.set('  default-sample-format = s24le')
    vPaPriRate.set('  default-sample-rate = 44100')
    vPaAltRate.set('  alternate-sample-rate = 48000')
    vPaRe.set('  resample-method = speex-float-10')
# Show variables
    print ("-------------- Default Values ---------------")
    print(vPaBitdepth.get())
    print(vPaPriRate.get())
    print(vPaAltRate.get())
    print(vPaRe.get())
    print ("---------------------------------------------")

# Apply PA Button
def applyPA():
    CvPaBitdepth=(vPaBitdepth.get())
    CvPaPriRate=(vPaPriRate.get())
    CvPaAltRate=(vPaAltRate.get())
    CvPaRe=(vPaRe.get())

    subprocess.call('sudo sed -i "/default-sample-format =/ c {}" /etc/pulse/daemon.conf && sudo sed -i "/default-sample-rate =/ c {}" /etc/pulse/daemon.conf && sudo sed -i "/alternate-sample-rate =/ c {}" /etc/pulse/daemon.conf && sudo sed -i "/resample-method =/ c {}" /etc/pulse/daemon.conf | pulseaudio --kill ; pulseaudio --start'.format(CvPaBitdepth,CvPaPriRate,CvPaAltRate,CvPaRe),shell=True);

# The current PulseAudio output setting is passed to variable and printed to terminal
def showsamplerate():
    try:
        showsamplerateoutput=subprocess.check_output(["pacmd list-sinks | grep sample"],universal_newlines=True,shell=True,stderr=subprocess.STDOUT).strip()
        ShvPaOut.set(showsamplerateoutput)
        PaStatus=subprocess.check_output(["pulseaudio --check"],universal_newlines=True,shell=True,stderr=subprocess.STDOUT).strip()
        vPaRun.set("Status: On")
        print ("---------------- PulseAudio ----------------")
        print (vPaRun.get())
        print (ShvPaOut.get())
        print ("--------------------------------------------")
    except subprocess.CalledProcessError as e:
        ShvPaOut.set("Output: N/A")
        vPaRun.set("Status: Off")
        print ("---------------- PulseAudio ----------------")
        print (vPaRun.get())
        print (ShvPaOut.get())
        print ("--------------------------------------------")
        sys.stderr.write(
        "return code: %s\n"
        % (e.returncode))


# End ----------

# Apply Alsa
def applyAL():
    cADefDev=(vADefDev.get())
    cADefDev=(vADefDev.get())
    subprocess.call('sudo sed -i "/defaults.pcm.card / c defaults.pcm.card {}" /etc/asound.conf && sudo sed -i "/defaults.ctl.card / c defaults.ctl.card {}" /etc/asound.conf | sudo alsa force-reload'.format(cADefDev,cADefDev),shell=True);

# Uninstall/install PulseAudio
def installerPA():
    try:
        PaUninst=(vPaUninst.get())
        subprocess.call('{}'.format(PaUninst),shell=True);
        vPaRun.set("Status: Off")
        ShvPaOut.set("Output: N/A")
        print ("---------------- PulseAudio ----------------")
        print (vPaRun.get())
        print (ShvPaOut.get())
        print ("--------------------------------------------")
    except subprocess.CalledProcessError as response:
        print ("---------------- PulseAudio ----------------")
        print ("Installer: Error")
        print ("--------------------------------------------")
        response = err.returncode
# End ----------


# The current ALSA device list is passed to variable and printed to terminal
def showalsadevices():
    showalsadeviceslist=subprocess.check_output(["aplay -l | awk -F \: '/,/{print $2}' | awk '{print $1}' | uniq"],universal_newlines=True,shell=True).strip();
    vADefDevList.set(showalsadeviceslist)
    print (vADefDevList.get())
# End ----------

# Run at start for now to be 100% that --> asound.conf exist and if not it will be created (config file creation will fail if app is not run with sudo. Alternatively config can be created manually by following this tutorial --> https://www.alsa-project.org/main/index.php/Setting_the_default_device)
# subprocess.call('[ -f /etc/asound.conf ] && echo "----------------------------- Audio Powertool -----------------------------" || echo "defaults.pcm.card 1\ndefaults.ctl.card 1" > /etc/asound.conf', shell=True)

# Close Window
def close_window():
    root.destroy()
# End ----------

    root.mainloop()

if __name__ == '__main__':
    main()
