import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
import tts
import random

def button_callback(channel):
    print("Button was pushed!")
    listLenght = len(myJokeList)
    print('The list has %s items' % listLenght)
      
    myRandomNumber = random.randint(0, (listLenght - 1))
    print('The randon number is %s' % myRandomNumber)

    print(myJokeList[myRandomNumber])

    tts.speak(myJokeList[myRandomNumber])
    time.sleep(1)
    
myJokeList = [
    'Why is Peter Pan always flying? He neverlands.', 
    'Why couldn\'t the bicycle stand up? Because it was two tired!',
    "I'm so good at sleeping. I can do it with my eyes closed.",
    'What did the traffic light say to the car? Don’t look! I’m about to change.',
    'Why wouldn’t the shrimp share his treasure? Because he was a little shellfish.',
    'What did one strand of DNA say to the other strand of DNA? Is it me or do these jeans make my butt look big.'
]


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback, bouncetime=3000) # Setup event on pin 10 rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter
