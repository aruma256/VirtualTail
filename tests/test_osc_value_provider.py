import time
from pythonosc.udp_client import SimpleUDPClient
from virtualtail.osc_value_provider import OSCValueProvider


PORT = 9889


def test_init():
    OSCValueProvider()


def test_get_latest_values():
    osc_value_provider = OSCValueProvider(port=PORT)
    osc_value_provider.start()
    client = SimpleUDPClient("127.0.0.1", PORT)
    # default value
    assert osc_value_provider.get_latest_values() == (None, None)
    # update L value
    client.send_message("/avatar/parameters/Contact/Tail/L", -1.0)
    time.sleep(0.1)
    assert osc_value_provider.get_latest_values() == (-1.0, None)
    # update R value
    client.send_message("/avatar/parameters/Contact/Tail/R", 1.5)
    time.sleep(0.1)
    assert osc_value_provider.get_latest_values() == (-1.0, 1.5)
    # ignore unsupported value
    client.send_message("/avatar/parameters/Contact/Tail/U", 0)
    time.sleep(0.1)
    assert osc_value_provider.get_latest_values() == (-1.0, 1.5)
