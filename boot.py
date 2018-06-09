import network

# ------------------------------------------------
# CONFIG -----------------------------------------
# ------------------------------------------------
WIFI_ESSID = 'Toad2G'
WIFI_PASSWORD = 'Madmen!!'

# ------------------------------------------------
# NETWORK ----------------------------------------
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

# ================================================
# MAIN ===========================================
# ================================================
connect_to_network()

