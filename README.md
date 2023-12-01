# Pre-Change-Capture
I created this script for Implementation and Deployment Engineers to capture essential information before executing network changes
Often times i've seen inexperienced Engineers perform network changes and not capture essential "before" change information



To execute this script, edit the "devices.txt" file and list the Ip's or Hostnames of the devices you wish to capture
(note: You can list 1 devices or multiple)

The Script runs the following Commands on the devices lists in the "devices.txt " file

sh run | i hostname<br /> 
sh run<br /> 
sh int status<br /> 
sh ip int bri<br /> 
sh vlan<br /> 
sh ver<br /> 
sh inventory<br /> 
sh mod<br /> 
sh mac address-table<br /> 
sh arp<br /> 
sh cdp neighbors<br /> 
sh ip protocols<br /> 
sh ip route<br /> 
sh vpc<br /> 

(This Script uses Python,Netmiko and Getpass)
