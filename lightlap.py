import socket #importing socket 
import wmi #importing windows management instrumentation wrapper. A module to communicate with WMI api of windows.
def autobright(value):

    if (value>=0 and value<=500):
        brightness = 40
    elif(value>500 and value<=1000):
        brightness = 60
    elif(value>1000 and value<=5000):
        brightness = 80 
    elif(value>5000):
        brightness = 100   
    wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(brightness, 0)#the screen brightness control code
    

host = ''#can use any address that is available
port = 50000 # give an unused port

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # creating the socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # setting the socket level options for reusing the ports
s.bind((host,port))#binding the socket

while 1:#giving a true condition to loop 
    message, address = s.recvfrom(4096)#UDP data recieve function. 4096 is the buffer size
    messageString = message.decode("utf-8")#converting binary string to normal string
    print(messageString) # view string for debugging purpose
    print(type(messageString))# gives str as output. Since there is no header we cannot parse via element tree parser
    start = messageString.find('<LightIntensity>')+16 #finding the Light intensity starting index
    end =messageString.find('</LightIntensity>',start)#finding the Light intensity closing tag index
    value = messageString[start:end]#extracting the vaule of light intensity
    print(value)#printing the value of light intensity
     
    autobright(float(value))#brightness adjust function
    