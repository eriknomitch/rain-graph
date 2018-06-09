# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import network
# import webrepl

# Config
# ------------------------------------------------
WIFI_ESSID = 'Toad2G'
WIFI_PASSWORD = 'Madmen!!'

# Network
# ------------------------------------------------
def connect_to_network():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(WIFI_ESSID, WIFI_PASSWORD)
        while not sta_if.isconnected():
            pass

    print('network config:', sta_if.ifconfig())

# Web REPL
# ------------------------------------------------
# webrepl.start()

