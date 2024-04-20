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
label11 = M5TextBox(138, 163, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label22 = M5TextBox(139, 186, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label33 = M5TextBox(140, 212, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
title0 = M5Title(title="User: Alibaba & 40 Hackers", x=3, fgcolor=0xFFFFFF, bgcolor=0x990303)
label5 = M5TextBox(20, 64, "Smart Plant Monitor", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label2211 = M5TextBox(5, 29, "Battery", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label1 = M5TextBox(20, 104, "label1", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=0)

def fun_core2_msg_(topic_data):
  # global params
  label1.setText(str(topic_data))
  pass

def buttonA_wasPressed():
  # global params
  Watering0.set_pump_status(0)
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  # global params
  while True:
    speaker.sing(448, 1)
    wait_ms(2)
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonA_wasPressed():
  # global params
  aws.start()
  pass
btnA.wasPressed(buttonA_wasPressed)


aws = AWS(things_name='ENV_TEST', host='a26covw2bu75im-ats.iot.eu-north-1.amazonaws.com', port=8883, keepalive=60, cert_file_path="/flash/res/9a0df6-certificate.pem.crt", private_key_path="/flash/res/9a0df6-public.pem.key")
aws.subscribe(str('core2/msg'), fun_core2_msg_)
aws.start()
Watering0.set_pump_status(0)
while True:
  aws.publish(str('core2/env'),str((json.dumps(({'tmp':(env3_1.temperature),'hum':(env3_1.humidity),'pressure':(env3_1.pressure)})))))
  wait(4)
  label1.setText(str(Watering0.get_adc_value()))
  label11.setText(str(env3_1.humidity))
  label22.setText(str(env3_1.temperature))
  label33.setText(str(env3_1.pressure))
  label1.setText(str(Watering0.get_adc_value()))
  label2211.setText(str(power.getBatteryLevel()))
  speaker.setVolume(1)
  if (Watering0.get_adc_value()) < 1000:
    Watering0.set_pump_status(1)
  else:
    Watering0.set_pump_status(0)
  wait(0.3)
  wait_ms(2)