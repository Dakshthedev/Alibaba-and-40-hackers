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


