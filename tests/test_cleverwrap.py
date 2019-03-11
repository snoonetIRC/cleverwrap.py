from cleverwrap import CleverWrap


def test_init():
    cw = CleverWrap("API_KEY")

    assert cw.key == "API_KEY"
