# 1- Import related librairs to LED project

import gpiod 								                  # Is used to controll and read GPIO.
import time 								                  # Is used to add pause.

# 2- Define variables

LED_PIN = 17								                  # This variable contains the Broadcom pin reference for a GPIO pin.
chip = gpiod.Chip("gpiochip4") 			    	    # This variable contains the GPIO location.
led_line = chip.get_line(LED_PIN) 			      # This variable store a reference to the LED GPIO pin.  
led_line.request(consumer="LED",
                 type=gpiod.LINE_REQ_DIR_OUT) # This variable set the LED as an output.

# 3 - Main Body of project to run and control LED!
try:
   while True:
       led_line.set_value(1)
       time.sleep(1)
       led_line.set_value(0)
       time.sleep(1)
finally:
   led_line.release()
