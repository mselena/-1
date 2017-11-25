import ephem
import datetime
date = str(datetime.datetime.now().date()).replace("-","/")

planet = input('Введите планету ')
if planet == 'Mars':
    planet_place = ephem.Mars(date)
elif planet == 'Saturn':
    planet_place = ephem.Saturn(date)
elif planet == 'Mercury':
    planet_place = ephem.Mercury(date)
elif planet == 'Venus':
    planet_place = ephem.Venus(date)
elif planet == 'Earth':
    planet_place = ephem.Earth(date)
elif planet == 'Jupiter':
    planet_place = ephem.Jupiter(date)
elif planet == 'Uranus':
    planet_place = ephem.Uranus(date)
elif planet == 'Neptune':
    planet_place = ephem.Neptune(date)
elif planet == 'Pluto':
    planet_place = ephem.Pluto(date)
else:
    print('Нет такой планеты в солнечной системе')

print(ephem.constellation(planet_place))