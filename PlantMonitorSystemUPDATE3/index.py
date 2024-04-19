from m5stack import *
from m5ui import *
from uiflow import *
from IoTcloud.AWS import AWS
import json

import time
import unit

setScreenColor(0x18135b)
Watering0 = unit.get(unit.WATERING, unit.PORTB)
env3_1 = unit.get(unit.ENV3, unit.PORTA)


label2 = M5TextBox(20, 163, "Humidity Level: ", lcd.FONT_Default, 0xd6ed23, rotate=0)
label3 = M5TextBox(20, 186, "Temperature:", lcd.FONT_Default, 0x19d8ff, rotate=0)
label4 = M5TextBox(20, 212, "Air Pressure:", lcd.FONT_Default, 0xfe02fa, rotate=0)
label11 = M5TextBox(138, 163, "", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label22 = M5TextBox(139, 186, "", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label33 = M5TextBox(140, 212, "", lcd.FONT_Default, 0xFFFFFF, roatet=0)
title0 = M5Title(title="User: daksh", x=3, fgcolor=0xFFFFFF, bgcolor=0x990303)
image0 = M5Img(208, 25, "res/default.jpg", True)
label5 = M5TextBox(20, 64, "Smart Plant Monitor", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
image1 = M5Img(208, 126, "res/default.jpg", True) 
label2211 = M5TextBox(5, 29, "Battery", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label1 = M5TextBox(20, 104, "label1", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=0)

def fun_core2_msg_(topic_data):
  # global params
  label1.setText(str(topic_data))
  pass   