## Context

This tool is showcased in the project [IotaWorkshop](https://github.com/Tsangares/iotaworkshop)

# Summary

This is a high level e-paper libaray. It supports QR code displays and allows easy lines of text writing along with right text align. Ideally if used this libaray should be imported to use the helpful class `EPD`.

**Note** This works for all waveshare screens when you import it. Simply change the line from,

    from waveshare_epd import epd1in54_V2
	
To whatever screen you have. For instance the 5.83 inch BW screen

    from waveshare_epd import epd5in83
	
Or the color version (bc)

    from waveshare_epd import epd5in8bc
	
	
# Installation

This project depends on `Pillow` but there are a variety of ways of installing it so I did not mark it as a dependency in the pypi package, you can install it using,

    pip install pillow
   
Simply install this package from the pypi repo

    pip install piepd
	
# Command Line Interface

There are a few example displays that can be run through the cli,	

	epd occipied #Displays text saying the tools is occupied
	epd --help #To see altenative displays

# Implementation Example

	from epd import EPD
	epd = EPD()
	epd.setFontSize(21)
	epd.drawText("Hello world",draw=False) #Draws this text on the screen
	epd.drawText("Left",draw=False) #Does not display yet until draw=True
	
	#The following line will right align the text and put it on the previous line
	epd.drawText("Right",right=True,overlap=True,draw=True)
	
	#Once you are completly done using the dislplay run
	epd.close()
# Wiring

| Board pin name | Board pin | RPi pin name | 
|----------------|-----------|--------------|
| VCC            | 1         | 3v3          | 
| GND            | 6         | GND          | 
| DIN            | 19        | GPIO10, MOSI | 
| CLK            | 11        | GPIO11, SCKL | 
| CS             | 24        | GPIO8, CE0   | 
| DC             | 22        | GPIO25       | 
| RST            | 11        | GPIO17       | 
| BUSY           | 18        | GPIO24       | 
