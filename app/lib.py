import math


def wallpaper(room_width, room_length, room_height, wallpaper_width, wallpaper_length, wallpaper_repeat):
    room_perimeter = 2 * (room_width + room_length)

    panel_number_all = room_perimeter / wallpaper_width
    panel_number_all = math.ceil(panel_number_all)

    panel_number_wallpaper = wallpaper_length // (room_height + wallpaper_repeat)

    wallpaper_number = panel_number_all / panel_number_wallpaper
    wallpaper_number = math.ceil(wallpaper_number)
    return wallpaper_number
