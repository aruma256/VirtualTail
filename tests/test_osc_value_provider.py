import time
from pythonosc.udp_client import SimpleUDPClient
from virtualtail.osc_value_provider import OSCValueProvider


PORT = 9889


def test_init():
    OSCValueProvider()


def test_start():
    osc_listener = OSCValueProvider(port=PORT)
    osc_listener.start()
    client = SimpleUDPClient("127.0.0.1", PORT)
    # default value
    assert osc_listener.left is None
    assert osc_listener.right is None
    # update L value
    client.send_message("/avatar/parameters/Contact/Tail/L", 0.25)
    time.sleep(0.1)
    assert osc_listener.left == 0.25
    assert osc_listener.right is None
    # update R value
    client.send_message("/avatar/parameters/Contact/Tail/R", 0.5)
    time.sleep(0.1)
    assert osc_listener.left == 0.25
    assert osc_listener.right == 0.5
    # ignore unsupported value
    client.send_message("/avatar/parameters/Contact/Tail/U", 0.75)
    time.sleep(0.1)
    assert osc_listener.left == 0.25
    assert osc_listener.right == 0.5
