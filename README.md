# Pre-Change-Capture
I created this script for Implementation and Deployment Engineers to capture essential information before executing network changes
Often times i've seen inexperienced Engineers perform network changes and not capture essential "before" change information

To execute this script, edit the "devices.txt" file and list the Ip's or Hostnames of the devices you wish to capture
(note: You can list 1 devices or multiple)


The Script runs the following Commands on the devices lists in the "devices.txt " file
sh run | i hostname
sh run
sh int status
sh ip int bri
sh vlan
sh ver
sh inventory
sh mod
sh mac address-table
sh arp
sh cdp neighbors
sh ip protocols
sh ip route
sh vpc
