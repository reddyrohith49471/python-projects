#install (pip install pywhatkit) in terminal or cmd
import pywhatkit
from datetime import datetime

now = datetime.now()

chour = now.strftime("%H")
mobile = input('Enter Mobile No of Receiver(Including country code) : ')
message = input('Enter Message you wanna send : ')
hour = int(input('Enter hour(In 24hr mode) : '))
minute = int(input('Enter minute : '))

pywhatkit.sendwhatmsg(mobile,message,hour,minute)
