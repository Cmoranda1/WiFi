from wireless import Wireless

wireless = Wireless()

#name of network to connect to
ssid_name = str(raw_input("Enter wifi name: "))

#password for respective network
password_name = str(raw_input("Enter Password: "))

#connect to network (might want to put in a sleep for
#a few seconds afte this to ensure connection before
#running any commands
wireless.connect(ssid = ssid_name, password = password_name)
