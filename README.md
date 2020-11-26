# Summary

This is a high level e-paper libaray. It supports QR code displays and allows easy lines of text writing along with right text align. Ideally if used this libaray should be imported to use the helpful class `EPD`.

# Installation

Simply install this package from the pypi repo

    pip install piepd
	
# Command Line Interface

There are a few example displays that can be run through the cli,	

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

| Name | Pin | GRPIO  | Description                                                   |
|------|------------------------------------------------------------------------------|
| VCC  |  2  |   NA   | 3.3V                                                          |
| GND  |  6  |   NA   | GND                                                           |
| DIN  | 19  | GPIO10 | SPI MOSI                                                      |
| CLK  | 11  | GPIO11 | SPI SCK                                                       |
| CS   | 24  | GPIO9  | SPI chip select (Low active)                                  |
| DC   | 22  | GPIO25 | Data/Command control pin (High for data, and low for command) |
| RST  | 11  | GPIO17 | External reset pin (Low for reset)                            |
| BUSY | 18  | GPIO24 | Busy state output pin (Low for busy)                          |

