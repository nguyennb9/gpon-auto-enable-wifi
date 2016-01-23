import requests
import sys

#Enter you password to access point
login = requests.post("http://192.168.1.1/GponForm/LoginForm", data={'username': 'admin', 'password': '*****'})

found = login.text.find("devinfo")
if found > -1:
	print ("Login to wifi router success!")

	#your command only is 'on' or 'off'
	arg = str(sys.argv)
	print ("Your option: %s" % str(sys.argv[1]))

	if sys.argv[1] and sys.argv[1] == "off" :
		wifi_enable = 0
		print ("Wifi is turned off")
	elif sys.argv[1] == "on" :
		wifi_enable = 1
		print ("Wifi is turned on")
	else:
		wifi_enable = 1
		print ("Please enter 'on' or 'off'. You are not enter command exactly, default to turn on wifi...")

	set = requests.get("http://192.168.1.1/GponForm/wifi_XForm?XWebPageName=wifi&wifi_en=" + str(wifi_enable))
else :
	print ("Login fail, Please check the username, password!")