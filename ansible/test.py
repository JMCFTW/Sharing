def fail():
    tracking_device = "在有跟沒有之間。"
    assert isinstance(tracking_device, bool), "市長在有，跟沒有之間。"

def success():
    iron_fans = "他做得這麼辛苦, 為何你們要抹黑他??? 哇凍未條拉, 喔氣氣氣氣氣氣氣"
    fake_fans = "為什麼大家都要黑他? 他明明什麼事都沒做???????"
    assert iron_fans != fake_fans


if __name__ == '__main__':
    success()
    fail()