import tkinter as tk
from tkinter import *
from tkinter import ttk
import subprocess


# Bit depth Button functions
def select_bitdepth_(var):
    selection = var.get()
    print('Bit depth', selection)

    text_dict = {
        0: 'Nothing selected!',
        16: subprocess.call('currentbitrate=$(grep "default-sample-format" /etc/pulse/daemon.conf) && sudo sed -i "/${currentbitrate}/ c default-sample-format = s16le" /etc/pulse/daemon.conf', shell=True),
        24: subprocess.call('currentbitrate=$(grep "default-sample-format" /etc/pulse/daemon.conf) && sudo sed -i "/${currentbitrate}/ c default-sample-format = s24le" /etc/pulse/daemon.conf', shell=True),
        32: subprocess.call('currentbitrate=$(grep "default-sample-format" /etc/pulse/daemon.conf) && sudo sed -i "/${currentbitrate}/ c default-sample-format = s32le" /etc/pulse/daemon.conf', shell=True)
        }

    text_to_print = text_dict[selection]
    print(text_to_print)

# primary sample rate button functions
def select_prisamplerate1_(var1):
    selection = var1.get()
    print('Primary Sample Rate', selection)

    text_dict = {
        0: 'Nothing selected!',
        14100: subprocess.call('currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c default-sample-rate = 44100" /etc/pulse/daemon.conf', shell=True),
        48000: subprocess.call('currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c default-sample-rate = 48000" /etc/pulse/daemon.conf', shell=True),
        88200: subprocess.call('currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c default-sample-rate = 88200" /etc/pulse/daemon.conf', shell=True),
        96000: subprocess.call('currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c default-sample-rate = 96000" /etc/pulse/daemon.conf', shell=True),
        192000: subprocess.call('currentsamplerate=$(grep "default-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentsamplerate}/ c default-sample-rate = 192000" /etc/pulse/daemon.conf', shell=True)
        }

    text_to_print = text_dict[selection]
    print(text_to_print)

# secondary sample rate button functions
def select_prisamplerate2_(var2):
    selection = var2.get()
    print('Secondary Sample Rate', selection)

    text_dict = {
        0: 'Nothing selected!',
        14100: subprocess.call('currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c alternate-sample-rate = 44100" /etc/pulse/daemon.conf', shell=True),
        48000: subprocess.call('currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c alternate-sample-rate = 48000" /etc/pulse/daemon.conf', shell=True),
        88200: subprocess.call('currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c alternate-sample-rate = 88200" /etc/pulse/daemon.conf', shell=True),
        96000: subprocess.call('currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c alternate-sample-rate = 96000" /etc/pulse/daemon.conf', shell=True),
        192000: subprocess.call('currentaltsamplerate=$(grep "alternate-sample-rate" /etc/pulse/daemon.conf) && sudo sed -i "/${currentaltsamplerate}/ c alternate-sample-rate = 192000" /etc/pulse/daemon.conf', shell=True)
        }

    text_to_print = text_dict[selection]
    print(text_to_print)


# Render main  window
def main():
    root = tk.Tk()
    root.title("GUI")
    root.geometry("775x225")

    # define var's
    var = IntVar()
    var1 = IntVar()
    var2 = IntVar()


    # background image
    filename = PhotoImage(file = "desk03.gif")
    background_label = Label( image=filename)
    background_label.image = filename # anchor
    background_label.place(x=70, y=-75, relwidth=1, relheight=1)

    # Set bit depth

    label = Label(text="Set bit depth")
    label.grid(row=1, column=1)

    select_bitdepth_1=Radiobutton(root, text='16 Bit', variable=var, command=lambda: select_bitdepth_(var), value=16, width=8)
    select_bitdepth_1.grid(row=2, column=1)

    select_bitdepth_2=Radiobutton(root, text='24 Bit', variable=var, command=lambda: select_bitdepth_(var), value=24, width=8)
    select_bitdepth_2.grid(row=3, column=1)

    select_bitdepth_3=Radiobutton(root, text='32 Bit', variable=var, command=lambda: select_bitdepth_(var), value=32, width=8)
    select_bitdepth_3.grid(row=4, column=1)

    # Separator1
    ttk.Separator(root).place(x=0, y=77, relwidth=10)

    # Set primary sample rate

    label = Label(text="Primary Sample rate")
    label.grid(row=5, column=1, columnspan = 2,)

    select_prisamplerate_1=Radiobutton(root, text='44,100 Hz', variable=var1, command=lambda: select_prisamplerate1_(var1), value=14100, width=8)
    select_prisamplerate_1.grid(row=5, column=3)

    select_prisamplerate_1=Radiobutton(root, text='48,000 Hz', variable=var1, command=lambda: select_prisamplerate1_(var1), value=48000, width=8)
    select_prisamplerate_1.grid(row=5, column=4)

    select_prisamplerate_1=Radiobutton(root, text='88,200 Hz', variable=var1, command=lambda: select_prisamplerate1_(var1), value=88200, width=8)
    select_prisamplerate_1.grid(row=5, column=5)

    select_prisamplerate_1=Radiobutton(root, text='96,000 Hz', variable=var1, command=lambda: select_prisamplerate1_(var1), value=96000, width=8)
    select_prisamplerate_1.grid(row=5, column=6)

    select_prisamplerate_1=Radiobutton(root, text='192,000 Hz', variable=var1, command=lambda: select_prisamplerate1_(var1), value=192000, width=8)
    select_prisamplerate_1.grid(row=5, column=7)

    # Set Secondary sample rate

    label = Label(text="Secondary Sample rate")
    label.grid(row=6, column=1, columnspan = 2,)

    select_secsamplerate_1=Radiobutton(root, text='44,100 Hz', variable=var2, command=lambda: select_prisamplerate2_(var2), value=14100, width=8)
    select_secsamplerate_1.grid(row=6, column=3)

    select_secsamplerate_1=Radiobutton(root, text='48,000 Hz', variable=var2, command=lambda: select_prisamplerate2_(var2), value=48000, width=8)
    select_secsamplerate_1.grid(row=6, column=4)

    select_secsamplerate_1=Radiobutton(root, text='88,200 Hz', variable=var2, command=lambda: select_prisamplerate2_(var2), value=88200, width=8)
    select_secsamplerate_1.grid(row=6, column=5)

    select_secsamplerate_1=Radiobutton(root, text='96,000 Hz', variable=var2, command=lambda: select_prisamplerate2_(var2), value=96000, width=8)
    select_secsamplerate_1.grid(row=6, column=6)

    select_secsamplerate_1=Radiobutton(root, text='192,000 Hz', variable=var2, command=lambda: select_prisamplerate2_(var2), value=192000, width=8)
    select_secsamplerate_1.grid(row=6, column=7)

    # Separator2
    ttk.Separator(root).place(x=0, y=117, relwidth=10)

    # Set Secondary sample rate

    label = Label(text="Resample method")
    label.grid(row=7, column=1, columnspan = 2,)

#   Premade ENTER button with no actual function at now
#    ser_port_btn=Button(root, text='ENTER', command=lambda: select_bitdepth_(var))
#    ser_port_btn.grid(row=5, column=1)

    root.mainloop()

if __name__ == '__main__':
    main()
