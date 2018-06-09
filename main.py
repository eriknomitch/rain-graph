# import socket

# ------------------------------------------------
# ------------------------------------------------
# ------------------------------------------------
try:
    import usocket as _socket
except:
    import _socket
try:
    import ussl as ssl
except:
    import ssl

def https_get(domain, path, use_stream=True):
    s = _socket.socket()
    ai = _socket.getaddrinfo(domain, 443)

    print("Address infos:", ai)
    addr = ai[0][-1]

    print("Connect address:", addr)
    s.connect(addr)

    s = ssl.wrap_socket(s)

    if use_stream:
        # Both CPython and MicroPython SSLSocket objects support read() and
        # write() methods.
        s.write(b"GET {} HTTP/1.0\r\n\r\n".format(path))
        print(s.read(4096))
    else:
        # MicroPython SSLSocket objects implement only stream interface, not
        # socket interface
        s.send(b"GET %s HTTP/1.0\r\n\r\n", path)
        print(s.recv(4096))

    s.close()

# ------------------------------------------------
# NEOPIXEL ---------------------------------------
# ------------------------------------------------
import machine
import neopixel
import time

NUM_PIXELS = 16

np = neopixel.NeoPixel(machine.Pin(25), NUM_PIXELS)

def np_clear():
    for i in range(NUM_PIXELS):
        np[i] = (0, 0, 0)
    np.write()

def np_test():
    for times in range(3):
        for i in range(NUM_PIXELS):
            np[i] = (0, 255, 0)
            np.write()
            time.sleep_ms(20)
        np_clear()

def ds_test():
    https_get('api.darksky.net', '/forecast/99352fbb407a033341e9e421b84f7ff2/41.900303,-87.620142?exclude=hourly,minutely,daily,alerts,flags&units=si')

