from microbit import *

ship_hull = pin0
rock = pin1
lighthouse = pin2
lighthouse_light = False

while True:

    # Check if ship hull is touched
    if ship_hull.is_touched():
        display.scroll("Call the RNLI")

    # Check if the rock is touched and light is off
    if rock.is_touched() and lighthouse_light == False:
            lighthouse.write_digital(1)
            lighthouse_light = True
            sleep(500)

    # Check if the rock is touched and light is already on
    elif rock.is_touched() and lighthouse_light == True:
            lighthouse_light = False
            lighthouse.write_digital(0)
            sleep(500)
