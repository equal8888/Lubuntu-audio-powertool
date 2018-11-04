#!/usr/bin/python3

# ---------- Note to self ----------
# Double check imports 😘

from tkinter import *  					# the GUI toolkit.
from tkinter import ttk					# dd the tabs
import tkinter.messagebox   			# Self explanatory

import os
import os.path
from os import system as EmbedTerminal 	# renaming for EmbedTerminal

import time
import datetime     	   				# used to get the current time.
import readline

import csv 								# Read / Write csv
import io 								# For string file save for csv

import subprocess						# for pulseaudio config (for now)
from subprocess import call				# Might be useless

top = Tk()
def gui():
    mainFrame=Frame(top,relief="sunken",border=1)
    Description=Label(mainFrame,text="Audio Powertool:")

# ---------- Define MainFrame ----------
    mainFrame.master.title("Audio Powertool")
    mainFrame.master.minsize(width=731,height=293)
    mainFrame.master.maxsize(width=731,height=293)

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

    page3=ttk.Frame(nb)
    nb.add(page3,text='Terminal')

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

    vPaRespeexfloatN=Radiobutton(page1,indicatoron=0,text='speexfloat-N',variable=vPaRe,value='resample-method = speex-float-N',command=PaRe,width=12)
    vPaRespeexfloatN.grid(row=9,column=3)

    vPaRespeexfloat10=Radiobutton(page1,indicatoron=0,text='speexfloat-10',variable=vPaRe,value='resample-method = speex-float-10',command=PaRe,width=12)
    vPaRespeexfloat10.grid(row=9,column=4)

    vPaRemedium=Radiobutton(page1,indicatoron=0,text='medium',variable=vPaRe,value='resample-method = src-sinc-medium-quality',command=PaRe,width=12)
    vPaRemedium.grid(row=9,column=5)

    vPaRebest=Radiobutton(page1,indicatoron=0,text='best',variable=vPaRe,value='resample-method = src-sinc-best-quality',command=PaRe,width=12)
    vPaRebest.grid(row=9,column=6)

    vPaRezeroOrderhold=Radiobutton(page1,indicatoron=0,text='zero-orderhold',variable=vPaRe,value='resample-method = src-zero-order-hold',command=PaRe,width=12)
    vPaRezeroOrderhold.grid(row=9, column=7)

    vPaReStopResampling=Radiobutton(page1,indicatoron=0,text='Stop Resampling',variable=vPaRe,value='; resample-method = speex-float-1',command=PaRe,width=25)
    vPaReStopResampling.grid(row=10,column=1,columnspan=2)

    vPaReresamplemethod=Radiobutton(page1,indicatoron=0,text='resample-method',variable=vPaRe,value='resample-method = speex-fixed-N',command=PaRe,width=12)
    vPaReresamplemethod.grid(row=10,column=3)

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

    frame98=tkinter.LabelFrame(page1,borderwidth=3)
    frame98.grid(row=11,column=6,columnspan=2,sticky='NEW',padx=5, pady=5)

# ---------- Default & Apply PA Button ----------

    apply_btn1=Button(page1,text='Default Pulseaudio settings',command=defaultpulsebutton)
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

# PAGE3 Maincode

    # Define Frames
    frame301=tkinter.LabelFrame(page3)
    frame301.grid(row=1,column=2,sticky='NESW',padx=5,pady=5)

    Aroundterminalframe=tkinter.LabelFrame(frame301)
    Aroundterminalframe.grid(row=1,column=2,sticky='NESW')

    terminalframe=Label(Aroundterminalframe,fg='grey',bg='black',height=13,width=88)
    terminalframe.grid(row=1,column=1,sticky='sw')

# ----------------- xterm  -----------------
# ------------------------------------------


	# Terminal
    wid = terminalframe.winfo_id()
    os.system('sudo xterm -into %d -geometry 119x88 -sb &' % wid)

	# This can do untill I make something useful =/
    DirtyFixbtn=Button(frame301,text='Kill xterm',command=DirtyFix)
    DirtyFixbtn.grid(row=2,column=2,columnspan=2,padx=5,pady=5,sticky='es')


# ---------------------------

# Menubar
    menubar=Menu(mainFrame.master)
    filemenu=Menu(menubar,tearoff=0)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=mainFrame.master.quit)
    menubar.add_cascade(label="File",menu=filemenu)

    editmenu=Menu(menubar,tearoff=0)
    editmenu.add_command(label="preferences",command=Preferences01)
    menubar.add_cascade(label="Edit",menu=editmenu)

    helpmenu=Menu(menubar,tearoff=0)

# ---------- Note to self ----------
# move this 😘

    def helpmenu01():
        tkinter.messagebox.showinfo("FAQ","Bla Bla Bla\n")

    helpmenu.add_command(label="FAQ",command=helpmenu01)
    menubar.add_cascade(label="Help",menu=helpmenu)

    mainFrame.master.config(menu=menubar)

# ----------------- Preferences Page -----------------

# ---------- Note to self ----------
# fix this 😘

    frame300=tkinter.LabelFrame(page99)
    frame300.grid(row=1,column=2,columnspan=7,rowspan=5,sticky='NESW')

    Label(frame300,text='Sudo Password:\n( requires app restart )').grid(row=1,column=1,columnspan=2,padx=5,pady=5,sticky='NS')
    # adds password entry widget and defines its properties
    password_box=Entry(frame300) # Hiding password while typing is not user friendly feature, for that I have cut it from now --> show='*'
    password_box.insert(0,'')
    password_box.bind('<Return>',login)
    password_box.grid(row=2,column=1,sticky='NS')
    # adds login button and defines its properties
    login_btn=Button(frame300,text='authorize app',command=lambda:writeToFile("AppMemo.csv"))
    login_btn.bind('<Return>',login)
    login_btn.grid(row=3,column=1,sticky='NESW')

    top.mainloop()


# -----------------------------------------------------------
# -----------------------------------------------------------

# set home folder.
HOMEDIR=os.path.expanduser('~')
#binds the logfile and conf file to home foler path.audiopowertool:
logplace=HOMEDIR+'/.audiopowertoolmanager.log'
configfile=HOMEDIR+'/.audiopowertool.conf'
depfile=HOMEDIR+"/.depfile.dat"

# ---------- Variables ----------
vPabitdepth=StringVar() 	# PulseAudio BithDepth
vPaPriRate=StringVar() 		# PulseAudio Primary Samplerate
vPaAltRate=StringVar() 		# PulseAudio Alternative Samplerate
vPaRe=StringVar() 			# PulseAudio Resample method

bitdepthtextvariable=StringVar()
password_box=StringVar()

# ---------- Radiobutton Data ----------

def Pabitdepth():
    selection="You selected "+str(vPabitdepth.get())
    print(vPabitdepth.get())
#    label.config(text = selection)

def PaPriRate():
    selection="You selected "+str(vPaPriRate.get())
    print(vPaPriRate.get())
#    label.config(text = selection)

def PaAltRate():
    selection="You selected "+ str(vPaAltRate.get())
    print(vPaAltRate.get())
#    label.config(text = selection)

def PaRe():
    selection="You selected "+str(vPaRe.get())
    print(vPaRe.get())
#    label.config(text = selection)

# End ----------

# Kill xterm
def DirtyFix():
    subprocess.call('sudo killall xterm',shell=True)

# Default button
def defaultpulsebutton():
    subprocess.call('./default-settings-pulseaudio.sh',shell=True)

# ---------- Apply PA Button ----------

def applyPA():
    CvPabitdepth=(vPabitdepth.get())
    CvPaPriRate=(vPaPriRate.get())
    CvPaAltRate=(vPaAltRate.get())
    CvPaRe=(vPaRe.get())

    subprocess.call('sudo sed -i "/default-sample-format =/ c {}" /etc/pulse/daemon.conf && sudo sed -i "/default-sample-rate =/ c {}" /etc/pulse/daemon.conf && sudo sed -i "/alternate-sample-rate =/ c {}" /etc/pulse/daemon.conf && sudo sed -i "/resample-method =/ c {}" /etc/pulse/daemon.conf | pulseaudio --kill ; pulseaudio --start'.format(CvPabitdepth,CvPaPriRate,CvPaAltRate,CvPaRe),shell=True);

#   Show samlerate
def showsamplerate():
    showsamplerateoutput=subprocess.check_output(["(pacmd list-sinks | grep sample)"],shell=True)
    bitdepthtextvariable.set(showsamplerateoutput)

# preferences
# Close Window
def close_window():
    top.destroy()

# for now
def EnterKey(event):
    print("You hit return.")
    writeToFile("AppMemo.csv")

def Preferences01():
    nb.add(page99,text='Preferences')
    nb.select(page99)
#    password_box.delete(0, END)

def writeToFile(filename):
    nb.hide(page99)
    inputValue=password_box.get()

    path=os.path.dirname("AppMemo.csv")

    with open(os.path.join(path,filename),"w")as csv_file:
        writer=csv.writer(csv_file,lineterminator='\n')
        writer.writerow([inputValue])

# Memo: writerow(1)  CSV COMMANDS from https://docs.python.org/3.2/library/csv.html

# Get password
class Getpsswd():
    def __init__(self,filename):
        path=os.path.dirname("AppMemo.csv") # os path

        with open(os.path.join(path,filename))as f_input:
            csv_input=csv.reader(f_input)
            self.details=list(csv_input)

    def get_col_row(self,col,row):
        return self.details[row-0][col-0]
try:
    data=Getpsswd("AppMemo.csv") # Get password from csv
    pswd=data.get_col_row(0, 0)
    command='clear && echo "--------------------- Audio Powertool -----------------------"'
    subprocess.call('echo {} | sudo -S {}'.format(pswd,command),shell=True);
except IndexError:                          # if password not found
    pswd="null"
    subprocess.call('clear && echo "--------------------- Audio Powertool -----------------------" && echo " Warning: Password not set !" && echo " Set sudo password from the Preferences menu and restart !"'.format(),shell=True);

# def login event
def login(*event):
    writeToFile("AppMemo.csv")

#checks the current time and prints it on the screen.
def print_time():
     now=datetime.datetime.now()
     chour=str(now.hour)+ ":"
     cmin=str(now.minute)
     print("\nFinished at: " +chour+cmin)


#installs the required dependencyes when called.
def installdep():
    os.system("clear")
    os.system("sudo apt-get install xterm | sudo apt install libnotify-bin")
    sevFrame.destroy()

#called if log must be enabled.
def logsetyes():
    logcmd="| tee -a ~/.aptmanager.log"
    conf=open(configfile,"w")
    conf.write("")
    conf.close()

    conf=open(configfile,"a")
    conf.write("log=enabled\n")
    conf.close()
    fifthFrame.destroy()
    notifysetyesButton.pack(pady = 10)
    notifysetnoButton.pack(pady = 10)


#called if log must be disabled.
def logsetno():
    global notifysetyesButton
    global notifysetnoButton
    logcmd=""
    conf=open(configfile,"w")
    conf.write("")
    conf.close()

    conf=open(configfile,"a")
    conf.write("log=disabled\n")
    conf.close()
    fifthFrame.destroy()
    notifysetyesButton.pack(pady=10)
    notifysetnoButton.pack(pady=10)

#asks the user for dependency installation.
def depntfound():
   print("A required dependency is not installed.")
   ask_user=raw_input("1 to Install It.\n2 to Continue Without It\n3 Don'nt bother Me Again.\n?1/2/3: ")

   if ask_user=="1":
       os.system("sudo apt-get install xterm | sudo apt install libnotify-bin | tee -a ~/.aptmanager.log")
       print("Done.")
       raw_input("Press <enter> to continue.")
       os.system("clear")


# sets the string that is passed to bash to "" to avoid command not found errors.
   if ask_user=="2":
       notifycmd=""
       print("Audio Powertool will continue, but with out the embedded Terminal")
       raw_input("Press <enter> to continue.")
       os.system("clear")

   if ask_user=="3":
       dep_pref=open(depfile,"w")
       dep_pref.close()
       os.system("clear")

   else:
       os.system("clear")
       depntfound()

#reads conf file and sets the respective variables.
if os.path.exists(configfile):

    conf=open(configfile,"r")
    while True:
        line=conf.readline()

        if"log=disabled"in line:
            logcmd=""

        elif"log=enabled"in line:
            logcmd="| tee -a ~/.aptmanager.log"

        if"EOF"in line:
            conf.close()
            break

#creates a default conf file if it does not exists.
else :
    print("No conf file found!\nTaking Default...")
    time.sleep(1)
    notifycmd ="notify-send 'Audio Powertool:' 'Commands Finished'"
    logcmd="| tee -a ~/.aptmanager.log"
    conf=open(configfile,"w")
    conf.write("")
    conf.close()

    conf=open(configfile,"a")
    conf.write("log=enabled\n")

    conf.write("notification=enabled\n")
    conf.write("EOF")
    conf.close()


#checks if something exists in path (aka installed), if not, depntfound is executed.
for dir in os.environ['PATH'].split(':'):
        prog=os.path.join(dir,"notify-send")

        #checks if depfile.dat exists in home folder.
        if os.path.exists(depfile):
            notifycmd=""
            os.system("clear")
            gui()

        #checks if file exist (this determines if depntfound() is called.)
        if os.path.exists(prog):
            gui()

depntfound()
