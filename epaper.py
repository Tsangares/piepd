#!/usr/bin/env
#Change this to your display
from waveshare_epd import epd1in54_V2
from PIL import Image,ImageDraw,ImageFont
import logging,time,qrcode
from fonts import nova
logging.basicConfig(level=logging.INFO)
class EPD:
    def __init__(self,clear=True):
        self.epd = epd1in54_V2.EPD()
        logging.info("init")
        self.epd.init()
        self.width = self.epd.width
        self.height = self.epd.height
        logging.info("clear")
        self.clear()
        time.sleep(1)
        self.fontsize = 24
        self.font = ImageFont.truetype(nova, self.fontsize)
        self.covered = 0

    def setFontSize(self,size):
        self.fontsize = size
        self.font = ImageFont.truetype(nova, self.fontsize)
        
    def clear(self):
        self.epd.Clear(0xFF)
        self.image = Image.new('1', (self.width, self.height), 255)
        
    def drawImg(self,img,angle=0,offset=[0,0],centerX=False,centerY=False,draw=True):
        image = Image.new('1', (self.width, self.height), 255)
        if centerX:
            offset[0] = int((self.width-img.size[0])/2)
        if centerY:
            offset[1] = int((self.height-img.size[1])/2)
        image.paste(img,offset)
        image.rotate(angle)
        self.image = image
        self.covered = offset[1]+img.height
        if draw: self.draw()

    def drawText(self,text,draw=True,overlap=False,right=False):
        img = ImageDraw.Draw(self.image)
        offset = [0,self.covered]
        if right:
            width = self.font.getsize(text)[0]
            offset[0] = self.width-width
        if overlap:
            offset[1] -= self.fontsize
        img.text(offset,text,font=self.font,fill=0)
        if not overlap: self.covered += self.fontsize
        if draw: self.draw()

    def draw(self):
        self.epd.display(self.epd.getbuffer(self.image))
        
    def drawQR(self,text,centerX=True,centerY=False,draw=True,right=False):
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=4,
            border=1,
        )
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        self.drawImg(img,centerX=centerX,centerY=centerY,draw=draw)
    def close(self):
        epd1in54_V2.epdconfig.module_exit()


def displayEscrow(args):
    address = args.address
    fee = args.fee
    epd = EPD()
    epd.setFontSize(24)
    epd.drawQR(address,draw=False)
    epd.drawText("Send me a",draw=False)
    epd.drawText(" refund address.",draw=False)
    epd.drawText("Fee: ",draw=False)
    epd.drawText(f"{fee} M\u03B9",right=True,overlap=True)
    epd.close()
        
def displayCost(agrs):
    address = args.address
    fee = args.fee
    deposit = args.collateral
    epd = EPD()
    epd.setFontSize(24)
    epd.drawQR(address,draw=False)
    epd.drawText("Deposit:",draw=False)
    epd.drawText(f"{deposit} M\u03B9",draw=False,overlap=True,right=True)
    epd.drawText("Fee: ",draw=False)
    epd.drawText(f"{fee} M\u03B9",right=True,overlap=True)
    epd.close()

def displayOccupied(args):
    epd = EPD()
    epd.setFontSize(21)
    epd.drawText("Tool is occupied",draw=False)
    epd.drawText("",draw=False)
    epd.drawText("Please return",draw=False)
    epd.drawText(" the tool to",draw=False)
    epd.drawText(" redeem your",draw=False)
    epd.drawText(" deposit.",draw=False)
    epd.drawText("",draw=False)
    epd.drawText("The RFID sensor",draw=False)
    epd.drawText(" must touch")
    epd.close()
    
if __name__=="__main__":
    #Cli support for the user display interface
    #Supports three modes
    # - Initalize escrow screen
    # - Deposit screen
    # - Tool occupied screen
    import argparse
    parser = argparse.ArgumentParser(description='Control display for escrow.')
    subparsers = parser.add_subparsers(help='Choose a prompt.')

    create = subparsers.add_parser('create', help='Prompts to start an escrow.')  
    create.add_argument('address',type=str, help='Escrow address')
    create.add_argument('fee',type=int, help='Non-refundable cost of use.')
    create.set_defaults(func=displayEscrow)

    deposit = subparsers.add_parser('deposit', help='Prompts to deposit collateral.')
    deposit.add_argument('address',type=str, help='Escrow address')
    deposit.add_argument('fee',type=int, help='Non-refundable cost of use.')
    deposit.add_argument('collateral',type=int, help='Refundable deposit for security.')
    deposit.set_defaults(func=displayCost)

    occupied = subparsers.add_parser('occupied', help='Prompts the occupied tool prompt')
    occupied.set_defaults(func=displayOccupied)

    args = parser.parse_args()
    args.func(args)