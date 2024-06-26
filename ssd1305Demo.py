#hardware platform: FireBeetle-ESP32

from machine import Pin,I2C
import ssd1306
i2c = I2C(scl=Pin(12), sda=Pin(13), freq=100000)
lcd=ssd1306.SSD1306_I2C(128,64,i2c)

lcd.text("DFRobot",0,0)
# for i in range(0,28):
#   lcd.pixel(2*i,10,1)
list1 = [0x35,0x01,0x13,0x1D,0x03,0x19,0x7F,0xFF,
         0x8F,0xFF,0xF1,0xFF,0xFE,0x3C,0x00,0x07,
         0x80,0x00,0xF0,0x00,0x1E,0x00,0x03,0xC0,
         0x00,0x78,0x00,0x0F,0x00,0x01,0xFF,0xC0,
         0x3F,0xFF,0x07,0xFF,0xF0,0xC0,0x3F,0x00,
         0x01,0xF0,0x00,0x1E,0x00,0x03,0xE0,0x00,
         0x3C,0x00,0x07,0x80,0x00,0xF0,0x00,0x1E,
         0x00,0x03,0xC0,0x00,0xF8,0x00,0x1E,0x80,
         0x07,0xDE,0x03,0xF3,0xFF,0xFC,0x7F,0xFF,
         0x03,0xFF,0x00]
# lcd.line(0,12,54,12,1)              #draw a line from (0,12) to (54,12) color is blue
# lcd.hline(10,32,108,1)              #draw a horizontal line,from (10,32),length 108,color is blue
# lcd.vline(64,0,64,1)                #draw a vertical line,from (64,0),length 64,color is blue
# lcd.fill_rect(59,27,10,10,1)        #draw a rectangle,from (59,27) to (10,10) fill with blue
# lcd.rect(56,24,16,16,1)             #draw a rectangle frame,from (59,27) to (10,10) and color is blue
# lcd.fill_rect(59,27,10,10,1)
# lcd.fill_rect(88,0,40,20,1)
# lcd.line(88,0,128,20,0)             #draw a line from (88,0) to (128,20) color is black
# lcd.line(88,20,128,0,0)
lcd.blit(list1,0,0)
lcd.show()                          #display pix


