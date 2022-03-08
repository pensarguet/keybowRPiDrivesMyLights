# keybow RPi Drives My Lights
Keybow RPi drives Shelly plugs / bulbs

## Description
With the covid, and by force of circumstance, I started to work at home by obligation then by pleasure until I dedicated a room at home with my own setup. 
With a house on 2 floors, and moments when I am in a meeting, recording videos or simply available, I wanted to manage the availability of access to the room ... in short a kind of "On Air" to indicate my status. Ok, I can hear you from where you are... why didn't I just buy one? Well, it was too simple, and I like to make things!  

## Setup
So, it is quite naturally that I turned to [Raspberry](https://www.raspberrypi.com/) with its smaller form factor, [Raspberry Pi Zero W](https://www.raspberrypi.com/products/raspberry-pi-zero-w/) on which I could adapt a mini keyboard. To manage the lights, after some chat with friends on Twitter, it appears that [Shelly](https://shelly.cloud/) solutions seamed to be the most appropriate for want I wanted to do, switching on and off thanks to HTTP requests

Here are the component I used:
- [Raspberry Pi Zero W](https://www.raspberrypi.com/products/raspberry-pi-zero-w/) by [Raspberry](https://www.raspberrypi.com/)
- [GPIO Hammer Header (Solderless)](https://shop.pimoroni.com/products/gpio-hammer-header?variant=35643241098) by [Pimoroni](https://shop.pimoroni.com/)
- [Keybow Kit (3-key)](https://shop.pimoroni.com/products/keybow-mini-3-key-macro-pad-kit?variant=27890390696019) by [Pimoroni](https://shop.pimoroni.com/)
- 16+Gb micro SD Memory card
- [Shelly Plug S](https://shop.shelly.cloud/shelly-plug-s-wifi-smart-home-automation#62) by [Shelly](https://shelly.cloud/)
- [Shelly Duo - RGBW](https://shop.shelly.cloud/shelly-bulb-rgbw-e27-wifi-smart-home-automation#436) by [Shelly](https://shelly.cloud/)
    
## How to use it
### Step 0 - Hardware setup
For this project, I reused a spare [Raspberry Pi Zero W](https://www.raspberrypi.com/products/raspberry-pi-zero-w/) I already had. As I'm not mastering soldering, I used a solderless GPIO header thanks to [GPIO Hammer Header (Solderless)](https://shop.pimoroni.com/products/gpio-hammer-header?variant=35643241098) to give GPIO connectivity for the keyboard. Honestly if you can buy one natively soldered, I recommend to do so, here is the reference: [Raspberry Pi Zero WH](https://shop.pimoroni.com/products/raspberry-pi-zero-w?variant=39458414297171). 

I used the [Keybow Kit (3-key)](https://shop.pimoroni.com/products/keybow-mini-3-key-macro-pad-kit?variant=27890390696019) that brings 3 RGB mechanical keys to trigger actions. Pimoroni team released some interesting material to [assemble the keybow mini](https://learn.pimoroni.com/article/assembling-keybow-mini).

To manage the lights, I bough [Shelly Plug S](https://shop.shelly.cloud/shelly-plug-s-wifi-smart-home-automation#62) by [Shelly](https://shelly.cloud/), and I pre-ordered [Shelly Duo - RGBW](https://shop.shelly.cloud/shelly-bulb-rgbw-e27-wifi-smart-home-automation#436) in order to manage two lamps and a bulb.

### Step 1 - Micro SD Card Setup
So first step is to download the OS image, I used to download [Raspberry Pi OS Lite](https://www.raspberrypi.com/software/operating-systems/) from the official [Raspberry](https://www.raspberrypi.com/) web site.

Then you have to flash the OS to the micro SD card. Even if there are several option, I mainly used [Etcher](https://www.balena.io/etcher/) created by [Balena](https://www.balena.io/), that makes things very simple: You just have to select the image, select your MicroSD card, and flash!

Because Etcher unmount the micro SD card after end of flashing process, you have to reinsert it, because there are 2 files to trick! You will observe that all the OS has been st into the `/boot` folder. Fist, in `/boot`, create a file called `ssh` without extension to enable SSH on the Raspberry Pi. Because you are moving forward screenless, you have to activate Wifi on the Raspberr Pi. To do so, you have to create on `/boot` a configuration file called `wpa_supplicant.conf` that will allow you to pre-configure the WiFi credentials. At first boot time, the Raspberry Pi will copy and use this as the default configuration file.

In this file, place the following content and adapt it to your own Wifi configuration:
```
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
ssid="WIFI_SSID"
scan_ssid=1
psk="WIFI_PASSWORD"
key_mgmt=WPA-PSK
}
```
> Note: More information can be found in the official [Raspberry Pi documentation](https://www.raspberrypi.com/documentation/computers/configuration.html#configuring-networking-2) on the section "Configuring Networking" of "Setting up a Headless Raspberry Pi"!

Now, you just have to save the updated content of `wpa_supplicant.conf`, then unmount you micro SD card.

First step is done!

### Step 2 - SSH to the Pi Zero W
Now that's the **tada** moment, just insert the micro SD Card in the slot, and power up thanks to USB cable! Wait 2 to 5 minutes for the first boot.

Use your prefered IP scanner tool, or just connect to your box router to find the IP address of the Rapsberry Pi, then ```ssh pi@IP_ADDRESS```, the default password is ```raspberry```, and you will have the prompt waiting for you!

Of course, I have to recommende to update your device's OS and change the default password.

It's quite simple, you just have to type those two commands at the prompt:

```sudo apt-get update && sudo apt-get upgrade -y```
and
```passwd```

### Step 3 - Install the lib for the mini

### Step 4 - Install the Python app as systemctl service

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
