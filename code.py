from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)
BLACK = (0,0,0)

sense.clear()

def displaytemp(value):

	LEDvalue = ((value-(mintemp))/(maxtemp-(mintemp)))*8
	print("temp=",value)
	
	if( value > 21.5 and value < 22.5):
	  set_LED(LEDvalue,0,1,GREEN)
	elif(value < 22):
		set_LED(LEDvalue,0,1,BLUE)
	else:
		set_LED(LEDvalue,0,1,RED)
		

def displaypressure(value):
	
	LEDvalue = ((value-minpressure)/(maxpressure-minpressure))*8
	print("pressure=",value)
	
	if(value < 101.35 and value > 101.25):
	  set_LED(LEDvalue,3,4,GREEN)
	elif(value < 101.3):
		set_LED(LEDvalue,3,4,BLUE)
	else:
		set_LED(LEDvalue,3,4,RED)
		

def displayhumidity(value):

	LEDvalue = (value/maxhumidity)*8
	print("humidity=",value)
	
	if(value < 60.5 and value > 59.5):
		set_LED(LEDvalue,6,7,GREEN)
	elif(value < 60):
		set_LED(LEDvalue,6,7,BLUE)
	else:
		set_LED(LEDvalue,6,7,RED)
		

def set_LED(index,jmin,jmax,COLOR):

	for i in reversed(range(int(8-index),8)):
		for j in range(jmin,jmax+1):
			sense.set_pixel(j,i,COLOR)
	for k in reversed(range(0,int(8-index))):
		for l in range(jmin,jmax+1):
			sense.set_pixel(l,k,BLACK)


temp1=0
pressure1=0
humidity1=0
temp2=0
pressure2=0
humidity2=0

maxtemp = 120
mintemp = -40

maxpressure = 126
minpressure =26

maxhumidity = 100
minhumidity = 0

KEYSENSITIVITY = 0.5


while True:
	temp	 = sense.get_temperature()
	pressure = sense.get_pressure()/10
	humidity = sense.get_humidity()
	
	if(temp1 != temp):
		if(temp >= mintemp and temp <= maxtemp ):
			temp1	 =temp
			displaytemp(temp)
			temp2    =temp
		
	if(pressure1 != pressure):
		if(pressure >= minpressure and pressure <= maxpressure):
			pressure1=pressure
			displaypressure(pressure)
			pressure2=pressure
		
	if(humidity1 != humidity):
		if(humidity >= minhumidity and humidity <= maxhumidity):
			humidity1=humidity
			displayhumidity(humidity)
			humidity2=humidity
	
	for event in sense.stick.get_events():
		if(event.direction == "left" and event.action == "pressed" ):
			if(temp2 <= maxtemp - KEYSENSITIVITY):
				temp2 = temp2+KEYSENSITIVITY
				displaytemp(temp2)
		elif(event.direction == "left" and event.action == "held"):
			if(temp2 >= mintemp + KEYSENSITIVITY):
				temp2 = temp2-KEYSENSITIVITY
				displaytemp(temp2)
		elif(event.direction == "up" and event.action == "pressed" ):
			if(pressure2 <= maxpressure - KEYSENSITIVITY):
				pressure2 = pressure2+KEYSENSITIVITY
				displaypressure(pressure2)
		elif(event.direction == "up" and event.action == "held"):
			if(pressure2 >= minpressure + KEYSENSITIVITY):
				pressure2 = pressure2-KEYSENSITIVITY
				displaypressure(pressure2)
		elif(event.direction == "right" and event.action == "pressed" ):
			if(humidity2 <= maxhumidity - KEYSENSITIVITY):
				humidity2=humidity2+KEYSENSITIVITY
				displayhumidity(humidity2)
		elif(event.direction == "right" and event.action == "held" ):
			if(humidity2 >= minhumidity + KEYSENSITIVITY):
				humidity2=humidity2-KEYSENSITIVITY
				displayhumidity(humidity2)
		elif(event.direction == "down" and event.action == "pressed" ):
			KEYSENSITIVITY=KEYSENSITIVITY*0.1
		elif(event.direction == "down" and event.action == "held" ):
			KEYSENSITIVITY=1

