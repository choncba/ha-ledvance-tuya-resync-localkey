import tinytuya

DEVICE_ID = 'eb26742178deec2c576dmb'
IP_ADDRESS = '192.168.0.234'
LOCAL_KEY = 'eb7a2df4f1978444'

import time

"""
OUTLET Device
"""
d = tinytuya.BulbDevice(DEVICE_ID, IP_ADDRESS, LOCAL_KEY)
d.set_version(3.3)  # IMPORTANT to set this regardless of version
d.set_socketPersistent(True)  # Optional: Keep socket open for multiple commands
data = d.status()

# Show status of first controlled switch on device
print('Dictionary %r' % data)

# Set to RED Color - set_colour(r, g, b):
#  d.turn_on()
# data = d.set_colour(255,0,0)  
d.turn_off()
# print(data)

# Cycle through the Rainbow
# rainbow = {"red": [255, 0, 0], "orange": [255, 127, 0], "yellow": [255, 200, 0],
#           "green": [0, 255, 0], "blue": [0, 0, 255], "indigo": [46, 43, 95],
#           "violet": [139, 0, 255]}


# while True:

#     for color in rainbow:
#         [r, g, b] = rainbow[color]
#         d.set_colour(r, g, b, nowait=True)  # nowait = Go fast don't wait for response
#         time.sleep(0.25)

# # Brightness: Type A devices range = 25-255 and Type B = 10-1000
# d.set_brightness(1000)

# # Set to White - set_white(brightness, colourtemp):
# #    colourtemp: Type A devices range = 0-255 and Type B = 0-1000
# d.set_white(1000,10)

# # Set Bulb to Scene Mode
# d.set_mode('scene')

# # Scene Example: Set Color Rotation Scene
# d.set_value(25, '07464602000003e803e800000000464602007803e803e80000000046460200f003e803e800000000464602003d03e803e80000000046460200ae03e803e800000000464602011303e803e800000000')