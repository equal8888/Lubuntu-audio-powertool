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

    mainFrame.master.title("Audio Powertool")
    mainFrame.master.minsize(width=717,height=258)
    mainFrame.master.resizable(False, False)

# End ----------

# ---------- Define Pages ----------

	# Menu for pages
    nb=ttk.Notebook(mainFrame.master)
    nb.grid(row=1,column=1,columnspan=50,rowspan=49,sticky='NESW')

	# Page 1 PulseAudio
    page1=ttk.Frame(nb)
    nb.add(page1,text='PulseAudio (Software Mixer)')

	# Page 2 ALSA
    page2=ttk.Frame(nb)
    nb.add(page2,text='ALSA (Hardware Mixer)')

# End ----------

# -------------------- Tab 1 (PulseAudio) --------------------


    frame0=tkinter.LabelFrame(page1,bd=1)
    frame0.grid(row=0,column=0,columnspan=9,rowspan=2,sticky='nesw')
    # frame
    frame1=tkinter.LabelFrame(frame0,bg="black")
    frame1.grid(row=0,rowspan=5,column=1)

	# Set the black background on app
    frame2=Label(frame1,bg="white")
    frame2.grid(row=3,column=3,sticky='nes')
#	(row=2,column=3,sticky='nes')
#    background_label.place(width=800,height=84)

# ---------- Show Info ----------

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
    label=Label(frame0,text="  Bit Depth  ")
    label.grid(row=0,column=0,sticky='nsw')

# ---------- BithDepth Radio Buttons ----------

	# Set the BithDepth value to Default for variable vPaBitdepth
    RadBit16=Radiobutton(frame0,text='Default',variable=vPaBitdepth,value='; default-sample-format = s16le',command=Pabitdepth,width=9)
    RadBit16.grid(row=1,column=0,sticky='nsw')

	# Set the BithDepth value to 16 Bit for variable vPaBitdepth
    RadBit16=Radiobutton(frame0,text='16 Bit',variable=vPaBitdepth,value='  default-sample-format = s16le',command=Pabitdepth,width=9)
    RadBit16.grid(row=2,column=0,sticky='nsw')

    # Set the BithDepth value to 24 Bit for variable vPaBitdepth
    RadBit24=Radiobutton(frame0,text='24 Bit',variable=vPaBitdepth,value='  default-sample-format = s24le',command=Pabitdepth,width=9)
    RadBit24.grid(row=3,column=0,sticky='nsw')

    # Set the BithDepth value to 32 Bit for variable vPaBitdepth
    RadBit32=Radiobutton(frame0,text='32 Bit',variable=vPaBitdepth,value='  default-sample-format = s32le',command=Pabitdepth,width=9)
    RadBit32.grid(row=4,column=0,sticky='nsw')

# End ----------

# ---------- Primary Samplerate Radio Buttons ----------

	# samplerate frame
    frame3=Label(page1)
    frame3.grid(row=5,column=0,columnspan=8,sticky='nesw')

	# "Sub frame" for samplerate frame
    frame4=Label(frame3)
    frame4.grid(row=5,column=0,columnspan=8,sticky='nesw')

	# Label
    label=Label(frame4,text="Primary Sample rate")
    label.grid(row=1,column=1)

	# Set the BithDepth value to default for variable vPaBitdepth
    RadPriRateDefault=Radiobutton(frame4,text='Default',variable=vPaPriRate,value='; default-sample-rate = 44100',command=PaPriRate,width=9)
    RadPriRateDefault.grid(row=1,column=2)

	# Set the BithDepth value to 44,100 Hz for variable vPaBitdepth
    RadPriRate44100=Radiobutton(frame4,text='44,100 Hz',variable=vPaPriRate,value='  default-sample-rate = 44100',command=PaPriRate,width=9)
    RadPriRate44100.grid(row=1,column=3)

	# Set the BithDepth value to 48,000 Hz for variable vPaBitdepth
    RadPriRate48000=Radiobutton(frame4,text='48,000 Hz',variable=vPaPriRate,value='  default-sample-rate = 48000',command=PaPriRate,width=9)
    RadPriRate48000.grid(row=1,column=4)

	# Set the BithDepth value to 88,200 Hz for variable vPaBitdepth
    RadPriRate88200=Radiobutton(frame4,text='88,200 Hz',variable=vPaPriRate,value='  default-sample-rate = 88200',command=PaPriRate,width=9)
    RadPriRate88200.grid(row=1,column=5)

	# Set the BithDepth value to 96,000 Hz for variable vPaBitdepth
    RadPriRate96000=Radiobutton(frame4,text='96,000 Hz',variable=vPaPriRate,value='  default-sample-rate = 96000',command=PaPriRate,width=9)
    RadPriRate96000.grid(row=1,column=6)

# End ----------

# ---------- Alternative Samplerate Radio Buttons ----------

	# Label
    label=Label(frame4,text="Alternative Sample rate")
    label.grid(row=2,column=1)

	# Set the BithDepth value to default for variable vPaAltRate
    RadAltRateDefault=Radiobutton(frame4,text='Default',variable=vPaAltRate,value='; alternate-sample-rate = 48000',command=PaAltRate,width=9)
    RadAltRateDefault.grid(row=2,column=2)

	# Set the BithDepth value to 48,000 Hz for variable vPaAltRate
    RadAltRate48000=Radiobutton(frame4,text='48,000 Hz',variable=vPaAltRate,value='  alternate-sample-rate = 48000',command=PaAltRate,width=9)
    RadAltRate48000.grid(row=2,column=3)

	# Set the BithDepth value to 88,200 Hz for variable vPaAltRate
    RadAltRate48000=Radiobutton(frame4,text='88,200 Hz',variable=vPaAltRate,value='  alternate-sample-rate = 88200',command=PaAltRate,width=9)
    RadAltRate48000.grid(row=2,column=4)

	# Set the BithDepth value to 96,000 Hz for variable vPaAltRate
    RadAltRate96000=Radiobutton(frame4,text='96,000 Hz',variable=vPaAltRate,value='  alternate-sample-rate = 96000',command=PaAltRate,width=9)
    RadAltRate96000.grid(row=2,column=5)

	# Set the BithDepth value to 192,000 Hz for variable vPaAltRate
    RadAltRate192000=Radiobutton(frame4,text='192,000 Hz',variable=vPaAltRate,value='  alternate-sample-rate = 192000',command=PaAltRate,width=9)
    RadAltRate192000.grid(row=2,column=6)

# End ----------

    # Separator-2
    ttk.Separator(page1).grid(row=8,column=0,columnspan=11,sticky="ew")

# ---------- Resample method Radio Buttons ----------
    frame5=Label(page1)
    frame5.grid(row=9,column=0,columnspan=8,sticky='nesw')


    # Label Resample method
    label=Label(frame5,text="Resample method")
    label.grid(row=1,column=1,pady=4)

#    vPaRespeexfloatN=Radiobutton(page1,indicatoron=0,text='???',variable=vPaRe,value='resample-method = speex-float-N',command=PaRe,width=12)
#    vPaRespeexfloatN.grid(row=9,column=3)

	# Set the Resample value to speexfloat-10 for variable vPaRe
    vPaRespeexfloat10=Radiobutton(frame5,indicatoron=0,text='speexfloat-10',variable=vPaRe,value='  resample-method = speex-float-10',command=PaRe,width=12)
    vPaRespeexfloat10.grid(row=1,column=4)

	# Set the Resample value to medium for variable vPaRe
    vPaRemedium=Radiobutton(frame5,indicatoron=0,text='medium',variable=vPaRe,value='  resample-method = src-sinc-medium-quality',command=PaRe,width=12)
    vPaRemedium.grid(row=1,column=5)

	# Set the Resample value to best for variable vPaRe
    vPaRebest=Radiobutton(frame5,indicatoron=0,text='best',variable=vPaRe,value='  resample-method = src-sinc-best-quality',command=PaRe,width=12)
    vPaRebest.grid(row=1,column=6)

	# Set the Resample value to zero-orderhold for variable vPaRe
    vPaRezeroOrderhold=Radiobutton(frame5,indicatoron=0,text='zero-orderhold',variable=vPaRe,value='  resample-method = src-zero-order-hold',command=PaRe,width=12)
    vPaRezeroOrderhold.grid(row=1, column=7)

	# Set the Resample value to Default Resampling for variable vPaRe
    vPaReStopResampling=Radiobutton(frame5,indicatoron=0,text='Default Resampling',variable=vPaRe,value='; resample-method = speex-float-1',command=PaRe,width=25)
    vPaReStopResampling.grid(row=2,column=1,columnspan=2)

#    vPaReresamplemethod=Radiobutton(page1,indicatoron=0,text='???',variable=vPaRe,value='resample-method = speex-fixed-N',command=PaRe,width=12)
#    vPaReresamplemethod.grid(row=10,column=3)

	# Set the Resample value to ffmpeg for variable vPaRe
    vPaReffmpeg=Radiobutton(frame5,indicatoron=0,text='ffmpeg',variable=vPaRe,value='  resample-method = ffmpeg',command=PaRe,width=12)
    vPaReffmpeg.grid(row=2,column=4)

	# Set the Resample value to src-linear for variable vPaRe
    vPaResrclinear=Radiobutton(frame5,indicatoron=0,text='src-linear',variable=vPaRe,value='  resample-method = src-linear',command=PaRe,width=12)
    vPaResrclinear.grid(row=2,column=5)

	# Set the Resample value to soxr-hq for variable vPaRe
    vPaResoxrhq=Radiobutton(frame5,indicatoron=0,text='soxr-hq',variable=vPaRe,value='  resample-method = soxr-hq',command=PaRe,width=12)
    vPaResoxrhq.grid(row=2,column=6)

	# Set the Resample value to soxr-vhq for variable vPaRe
    vPaResoxrvhq=Radiobutton(frame5,indicatoron=0,text='soxr-vhq',variable=vPaRe,value='  resample-method = soxr-vhq',command=PaRe,width=12)
    vPaResoxrvhq.grid(row=2,column=7)

# End ----------

    # Separator3
    ttk.Separator(page1).grid(row=11,column=0,columnspan=11,sticky="ew")

	# Set the Buttons (Default Settings, User Profile 01, Apply)
    frame5=Label(page1)
    frame5.grid(row=12,column=0,columnspan=11,sticky='nesw')


# ---------- Default & Apply PA Button ----------

# ---------- Note to self ----------
# Make Default Button and
# Apply Button disable it self for few seconds after button press 😘

    apply_btn1=Button(frame5,text='Default Settings',command=defaultpulsebutton)
    apply_btn1.grid(row=12,column=1,padx=5,pady=5)

    apply_btn1=Button(frame5,text='User Profile 01',command=userpulsebutton)
    apply_btn1.grid(row=12,column=3,padx=5,pady=5)

    apply_btn2=Button(frame5,text='Apply & Restart pulseaudio',command=applyPA)
    apply_btn2.grid(row=12,column=6,padx=15,pady=5,sticky='e')

# End ----------

# Text below app
    label=Label(frame5,text="Press apply for changes to take effect")
    label.grid(row=12,column=4,padx=5)


# Button Show Samplerate
    apply_btn3=Button(frame1,text='Show Current PA Output (Click to refresh)',command=showsamplerate)
    apply_btn3.grid(row=0,column=3)

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

    helpmenu.add_command(label="About",command=helpmenu01)
    menubar.add_cascade(label="Help",menu=helpmenu)

    mainFrame.master.config(menu=menubar)

# End ----------

    top.mainloop()

# ---------- Variable Config ----------

vPaBitdepth=StringVar() 			# PulseAudio BithDepth
vPaPriRate=StringVar() 				# PulseAudio Primary Samplerate
vPaAltRate=StringVar() 				# PulseAudio Alternative Samplerate
vPaRe=StringVar() 					# PulseAudio Resample method

ShvPaOut=StringVar() 				# Show Current PA output

# End ----------

# ---------- Set some Values for Variable on app startup ----------

vPaBitdepth.set('  default-sample-format = s24le') 		# PulseAudio BithDepth
vPaPriRate.set('  default-sample-rate = 44100') 		# PulseAudio Primary Samplerate
vPaAltRate.set('  alternate-sample-rate = 48000') 		# PulseAudio Alternative Samplerate
vPaRe.set('; resample-method = speex-float-1') 			# PulseAudio Resample method
ShvPaOut.set('')										# Show Current PA output

# ---------- Print Variable Data ----------

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

# End ----------

# ---------- Button Commands ----------

def helpmenu01():
    tkinter.messagebox.showinfo("About Audio Powertool: ","PulseAudio is only a SOFTWARE MIXER' \n \nDont set the Samplerate to Maximum option available\n \nthat will do audio resampling and you dont want that!")

# Default button
def defaultpulsebutton():
# Set new values for variables
    vPaBitdepth.set('; default-sample-format = s16le')
    vPaPriRate.set('; default-sample-rate = 44100')
    vPaAltRate.set('; alternate-sample-rate = 48000')
    vPaRe.set('; resample-method = speex-float-1')
# Show variables
    print ("-----------------------------")
    print(vPaBitdepth.get())
    print(vPaPriRate.get())
    print(vPaAltRate.get())
    print(vPaRe.get())
    print ("-----------------------------")

# End ----------

# Recommended values button
def userpulsebutton():
# Set new values for variables
    vPaBitdepth.set('  default-sample-format = s24le')
    vPaPriRate.set('  default-sample-rate = 48000')
    vPaAltRate.set('  alternate-sample-rate = 96000')
    vPaRe.set('; resample-method = speex-float-1')
# Show variables
    print ("-----------------------------")
    print(vPaBitdepth.get())
    print(vPaPriRate.get())
    print(vPaAltRate.get())
    print(vPaRe.get())
    print ("-----------------------------")
# End ----------


# Apply PA Button
def applyPA():
    CvPaBitdepth=(vPaBitdepth.get())
    CvPaPriRate=(vPaPriRate.get())
    CvPaAltRate=(vPaAltRate.get())
    CvPaRe=(vPaRe.get())

    subprocess.call('sudo sed -i "/default-sample-format =/ c {}" /etc/pulse/daemon.conf && sudo sed -i "/default-sample-rate =/ c {}" /etc/pulse/daemon.conf && sudo sed -i "/alternate-sample-rate =/ c {}" /etc/pulse/daemon.conf && sudo sed -i "/resample-method =/ c {}" /etc/pulse/daemon.conf | pulseaudio --kill ; pulseaudio --start'.format(CvPaBitdepth,CvPaPriRate,CvPaAltRate,CvPaRe),shell=True);

# The current PulseAudio output setting is passed to variable

# ---------- Note ----------
# the output string has a "/n" in the end
# that's why here is this workaround. 😘
def showsamplerate():
    showsamplerateoutput=subprocess.check_output(["pacmd list-sinks | grep sample"],shell=True);
    ShvPaOut.set(showsamplerateoutput[1:31])
# Show the command also on terminal -->
    subprocess.call('pacmd list-sinks | grep sample', shell=True)

# End ----------

# Close Window
def close_window():
    root.destroy()

# End ----------

    root.mainloop()

if __name__ == '__main__':
    main()
