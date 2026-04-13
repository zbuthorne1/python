import pytest
from television import *


def test_init():
    television = Television()
    assert str(television) == "Power = False, Channel = 0, Volume = 0"


def test_power():
    television = Television()
    television.power()
    assert str(television) == "Power = True, Channel = 0, Volume = 0"
    television.power()
    assert str(television) == "Power = False, Channel = 0, Volume = 0"


def test_mute():
    television = Television()
    television.muted()
    assert str(television) == "Power = False, Channel = 0, Volume = 0"
    television.power()
    television.volume_up()
    television.muted()
    assert str(television) == "Power = True, Channel = 0, Volume = 1"
    television.muted()
    assert str(television) == "Power = True, Channel = 0, Volume = 1"


def test_channel_up():
    television = Television()
    television.channel_up()
    assert str(television) == "Power = False, Channel = 0, Volume = 0"
    television.power()
    television.channel_up()
    assert str(television) == "Power = True, Channel = 1, Volume = 0"
    television.channel_up()
    television.channel_up()
    television.channel_up()
    assert str(television) == "Power = True, Channel = 0, Volume = 0"


def test_channel_down():
    television = Television()
    television.channel_down()
    assert str(television) == "Power = False, Channel = 0, Volume = 0"
    television.power()
    television.channel_down()
    assert str(television) == "Power = True, Channel = 3, Volume = 0"
    television.channel_down()
    television.channel_down()
    television.channel_down()
    assert str(television) == "Power = True, Channel = 0, Volume = 0"


def test_volume_up():
    television = Television()
    television.volume_up()
    assert str(television) == "Power = False, Channel = 0, Volume = 0"
    television.power()
    television.volume_up()
    assert str(television) == "Power = False, Channel = 0, Volume = 1"
    television.muted()
    television.volume_up()
    assert str(television) == "Power = True, Channel = 0, Volume = 2"


def test_volume_down():
    television = Television()
    television.volume_down()
    assert str(television) == "Power = False, Channel = 0, Volume = 0"
    television.power()
    television.volume_up()
    assert str(television) == "Power = True, Channel = 0, Volume = 0"
    television.volume_up()
    television.muted()
    television.volume_down()
    assert str(television) == "Power = True, Channel = 0, Volume = 0"
