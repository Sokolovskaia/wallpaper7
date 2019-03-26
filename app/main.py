import os

import waitress
from flask import Flask, render_template, request

from app.lib import wallpaper


def start():
    app = Flask(__name__)

    @app.route('/')  # правило сопоставления запроса (урла) функции-обработчику
    def frontpage():
        print(request.args)
        room_width = request.args.get('room_width')
        room_length = request.args.get('room_length')
        room_height = request.args.get('room_height')
        wallpaper_width = request.args.get('wallpaper_width')
        wallpaper_length = request.args.get('wallpaper_length')
        wallpaper_repeat = request.args.get('wallpaper_repeat')
        # print(type(weight))
        if room_width and room_length and room_height and wallpaper_width and wallpaper_length and wallpaper_repeat:
            calculate_wallpaper = wallpaper(float(room_width), float(room_length), float(room_height),
                                            float(wallpaper_width),
                                            float(wallpaper_length), float(wallpaper_repeat))
            return render_template('index.html', title='Количество обоев на стену',
                                   calculate_wallpaper=calculate_wallpaper, room_width=room_width,
                                   room_length=room_length, room_height=room_height, wallpaper_width=wallpaper_width,
                                   wallpaper_length=wallpaper_length, wallpaper_repeat=wallpaper_repeat)

        return render_template('index.html', title='Расчет рулонов')

    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(port=9878, debug=True)


if __name__ == '__main__':
    start()
