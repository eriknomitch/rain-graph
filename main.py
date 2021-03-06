from umqtt import MQTTClient
from machine import Pin
import ubinascii
import machine
import micropython
import neopixel
import ujson
import utime as time

SERVER = "192.168.1.10"
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
TOPIC = b"rain-graph"
NUM_PIXELS = 16

np = neopixel.NeoPixel(machine.Pin(25), NUM_PIXELS)

def np_clear():
    global np

    for i in range(np.n):
        np[i] = (0, 0, 0)

    np.write()

def np_status_blink():
    global np

    np_clear()

    np[0] = (0, 255, 0)

    time.sleep_ms(1000)

    np_clear()


def sub_cb(topic, msg):
    global np

    print((topic, msg))
    print(ujson.loads(msg))

    np_clear()

    np[0] = (50, 50, 50)

    i = 1;

    try:
        for precipitation in ujson.loads(msg)['rain']:
            np[i] = (0, 0, precipitation)
            i = i+1
        np.write()
    except:
        np_clear()
        np[2] = (1, 0, 0)
        np.write()


def main(server=SERVER):

    c = MQTTClient(CLIENT_ID, server)
    # Subscribed messages will be delivered to this callback
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(TOPIC)
    print("Connected to %s, subscribed to %s topic" % (server, TOPIC))

    np_clear()

    #np_status_blink()

    try:
        while 1:
            #micropython.mem_info()
            c.wait_msg()
    finally:
        c.disconnect()

main()
