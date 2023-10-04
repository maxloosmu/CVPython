### Before running any commands, do this:
Install and configure Xming:
- Open the Xming Configuration (XLaunch) application.
- In the "XLaunch Wizard," make sure you select "Multiple windows" as the window mode.
- On the "Specify parameter settings" screen, check the box for "No Access Control" if it's not already checked. This will allow incoming X connections.
- Complete the wizard and save your configuration as a config.xlaunch file if prompted.
- Start Xming with the configured settings.

Run this command after checking the WSL IPv4 IP address of the machine:
- export DISPLAY=<Windows_IP>:0.0

So, on my Lenovo machine, I run:
- export DISPLAY=172.18.144.1:0.0

This is based on running `config /all` in my command prompt, where part of the output is this:
- Ethernet adapter vEthernet (WSL):

    - Connection-specific DNS Suffix  . :
    - Description . . . . . . . . . . . : Hyper-V Virtual Ethernet Adapter
    - Physical Address. . . . . . . . . : 00-15-5D-E1-CD-54
    - DHCP Enabled. . . . . . . . . . . : No
    - Autoconfiguration Enabled . . . . : Yes
    - Link-local IPv6 Address . . . . . : fe80::c873:ab57:2bd4:4e17%37(Preferred)
    - IPv4 Address. . . . . . . . . . . : 172.18.144.1(Preferred)


### List of commands to run before running Python scripts here:
- python3 -m venv myenv
- source myenv/bin/activate
- pip install -r requirements.txt
- python3 drawshapes.py

On Windows 10, I have to turn off the Windows Defender public network firewall to get `python3 drawshapes.py` to show the image output in a separate window.  
