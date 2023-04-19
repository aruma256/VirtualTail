import time
from pythonosc.udp_client import SimpleUDPClient
from virtualtail.osc_value_provider import OSCValueProvider


PORT = 9889


def test_init():
    OSCValueProvider()


def test_start():
    # default value
    osc_listener = OSCValueProvider(port=PORT)
    osc_listener.start()
    assert osc_listener.left is None
    assert osc_listener.right is None
    # update L value
    client = SimpleUDPClient("127.0.0.1", PORT)
    client.send_message("/avatar/parameters/Contact/Tail/L", 1)
    time.sleep(0.1)
    assert osc_listener.left == 1
    assert osc_listener.right is None
