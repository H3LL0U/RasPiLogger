This is a project that can help you create a simple keylogger with Raspberry pi pico and Raspberry pi zero 

Materials:
Raspberry pi pico
Raspberry pi zero (with GPIO pins and a mini SD card)
2 wires
Micro USB to female USB cable (in order to conect the keyboard to the RP zero)
An OTG cable and a Micro USB male to Micro USB adapter (alternativly you can use other cables but then it will take more usb slots from the computer)


Tutorial:
# Basic setup for Raspberry pi zero W
##First install the Raspberry pi OS image on your sd card: 
You can use tools like raspberry pi Imager. In my case i installed Rasperry pi OS (lite)

When you installed the OS put it into the raspberry pi and SSH into it (with tools like PUTTY)

After you are SSH'd into the keyboard you can create a disignated folder:
```
$ mkdir Scripts
```
After that we can work from there:
```
$ cd Scripts
```
We will also need to upgrade everything, install git and pip:
```
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install git
$ sudo apt install python3-pip
```
And we are also going to need a serial package after pip is installed:
```
$ sudo pip install pyserial
```
Also we need to enable a serial port on our Raspberry pi:
```
$ sudo raspi-config
```
Navigate to Interface options > Serial port > No > Yes

## files setup


After that you can install the fork of the package "keyboard" (you can also just install a normal package with pip install keyboard, but at the moment it contains a which doesn't allow for a keyboard to be disconected this fork contains a fix for it)
```
$ git clone https://github.com/H3LL0U/keyboard.git
```
And also this repo:
```
$ git clone https://github.com/H3LL0U/RasPiLogger.git
```
After that you can move all these files to a folder:
```
$ mkdir logger
$ mv ~/Scripts/RasPiLogger/'files for RP zero'/* ~/Scripts/logger
$ mv ~/Scripts/keyboard/keyboard ~/Scripts/logger
```
You can delete all the other files since they are not going to be needed anymore:
```
$ sudo rm -r ~/Scripts/keyboard
$ sudo rm -r ~/Scripts/RasPiLogger
```
And we are almost done with the setup for raspberry pi zero
The only thing that we need to do is make the script start automatically after each reboot
We can do this with:
$ sudo nano /etc/rc.local
You can add this line to one of the lines before exit 0
```
sudo python3 /home/turbo/Scripts/logger/Log.py &
```
At the end it's going to look something like this
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

sudo python3 /home/turbo/Scripts/logger/Log.py $

exit 0
```

Save and quit (ctrl+s and ctrl+x)

Congratulations! The setup for Raspberry pi zero is done!

#TODO: Finish full tutrial,
Reduce long boot time
