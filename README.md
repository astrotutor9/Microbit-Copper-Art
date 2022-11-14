# Microbit-Copper-Art

The Microbit has a really great feature built in that makes it an excellent starting point for adding interactivity to a small piece of artwork. This exercise uses the Microbit Version 1.

A simple python command “is_touched” can be used to tell if one of the contacts on the base of the Microbit literally has been touched. If a wire is connected to the contacts then this sense can be taken away from the Microbit onto a canvas, painting or sculpture.

This exercise will use simple crocodile connectors, an LED and copper slug tape to make a simple drawing interactive.

## Design The Masterpiece

All good masterpieces start with a rough sketch. What will be the theme? A snowman and Christmas Tree or how about a sinking ship and a lighthouse?

![The bill of materials for the artwork](https://github.com/astrotutor9/Microbit-Copper-Art/blob/main/Art_and_copper_tape1.jpg)

The story behind the art is that a light can be switched on or off and also an element in the art can display a message to the viewer. What these are will be up to the artistic license of the artist. So get creative!

In the example shown here a lighthouse is on a rock. The rock itself will be copper tape. The light will be the LED. The pins of which are poked through the paper and stuck to copper tape on the back. And a ship in distress in the water has a hull of copper tape. Touching the hull will send a distress message, touching the rock will illuminate the lighthouse.

## Adding the Tape

Adding the tape could be seen as quite easy. It is self adhesive, so just stick it down. The trick, though, is to make it appear as part of the art work or even hidden.

![A rough outline sketch with ideas for where to place the copper tape](https://github.com/astrotutor9/Microbit-Copper-Art/blob/main/Art_and_copper_tape2.jpg)

The rock and ship’s hull have slits cut on two sides of the shape and the copper tape threaded through. The backing was glued to the rock and hull leaving the tape intact. The self adhesive backing was only used to attach the copper tape at the edge of the paper where the crocodile clips will clip to it.

Attach the lighthouse LED to two thinner strips of the tape stuck to the back of the paper with small pieces of more copper tape. The LED pins are pushed through holes in the paper and stuck really tightly onto the copper tape. See the LED Tips below.

A final piece of tape is needed on the art as a ground for the viewer to touch at the same time as the rock or hull.

![The final artwork with the led added and the copper tape stuck down.](https://github.com/astrotutor9/Microbit-Copper-Art/blob/main/Art_and_copper_tape3.jpg)

## LED Tips

The LED will only work if the electrical current flows in the correct direction. The short pin is attached to ground the long pin to the positive or 3v on the Microbit. With the pins bent over onto the tape you may lose sight of which is ground or positive.

To ensure the LED is firmly attached to the tape, connect the crocodile clips to each tape and the other ends to GND and 3v. Power up the Microbit with the battery pack or connect it to your computer. Press the pins onto the tape with your fingers. If the LED does not light up, switch the connections over and try again. If at any point the LED flashes on then the connections are the right way round. Just press the tape down more firmly to make the pin connection secure so that the LED stays on the whole time. Then disconnect the 3v crocodile clip.

## Wire Up and Start Coding

Connect each piece of copper tape to the Microbit. There is a ground for the LED pin and for the ground tape. Clip the two ground crocodile clips to each other. 

Then for the hull and rock connect to pin 0 and pin 1 of the Microbit. Connect the LED to pin 3. Which pin is actually connected to which tape is not important just as long as you know which is which for the coding. The code below maybe makes the connections clearer.

Using the Mu editor or the Microbit Python editor copy in the code below.

```
from microbit import *

hull = pin0
rock = pin1
lighthouse = pin2
lighthouse_light = False
```

These lines link the Microbit pin numbers to a named variable which makes the code easier to read. The final one is used in switching the LED from off to on or vice versa if it is in the opposite state.

These next lines be very careful when typing them in. Watch out for spelling, capital letters, punctuation and the indents from the side of the page. The indents are one Tab or four spaces but should happen automatically if the text is correctly typed in.

```
while True:

    # Check if ship hull is touched
    if ship_hull.is_touched():
        display.scroll("Call the RNLI")

    # Check if the rock was touched and light was off
    if rock.was_touched() and lighthouse_light == False:
            lighthouse.write_digital(1)
            lighthouse_light = True
            sleep(500)

    # Check if the rock was touched and light was already on
    elif rock.was_touched() and lighthouse_light == True:
            lighthouse_light = False
            lighthouse.write_digital(0)
            sleep(500)
```

This code is a forever loop. It constantly checks if anything happens. If a touch to the hull is sensed then the message displays on the Microbit. 
If the rock is touched and the value for lighthouse_light is False (which means off) then turn the light on and reassign lighthouse_light to True. The last part is the opposite of the above. If the light is on then reset to off.

With a special Microbit adapter to connect to all the possible pins, many touch sensitive areas on a piece of art could be used. And the Microbit could also play sounds or even have objects outside of the artwork operate. Imagine the lights in the room switching off when the lighthouse light switches on and the sounds of waves play over a speaker? The only real limitation is the artist’s imagination.
