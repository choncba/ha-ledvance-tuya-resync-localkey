# Example Usage of TinyTuya
import tinytuya

DEVICE_ID = 'eb26742178deec2c576dmb'
IP_ADDRESS = '192.168.0.234'
LOCAL_KEY = 'eb7a2df4f1978444'

d = tinytuya.OutletDevice(DEVICE_ID, IP_ADDRESS, LOCAL_KEY)
d.set_version(3.3)
data = d.status() 
print('Device status: %r' % data)