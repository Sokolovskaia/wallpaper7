from app.lib import wallpaper


def test_wallpaper():
    assert 11 == wallpaper(5, 6, 2.75, 1.06, 10, 0.65)
