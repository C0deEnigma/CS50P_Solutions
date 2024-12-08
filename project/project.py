import pyttsx3
import requests
from datetime import datetime
from num2words import num2words
now=datetime.now()
engine=pyttsx3.init()


def main():
    print(date())
    print(time())
    print(weather())
    engine.say(date())
    engine.runAndWait()
    engine.say(time())
    engine.runAndWait()
    engine.say(weather())
    engine.runAndWait()



def date():
    day_in_words = num2words(now.day, to='ordinal').title()
    year_in_words = num2words(now.year, to='ordinal').title()
    month_name = now.strftime('%B')
    weekday=now.strftime('%A').capitalize()
    return f'Today is {weekday}, {day_in_words} of {month_name}, {year_in_words}'



def time():
    hour=now.hour
    minute=now.minute
    if hour>=12:
        hour-=12
        period='PM'
    else:
        period='AM'
    return f'Time is {hour:02}:{minute:02} {period}'


def get_city():
    url = 'http://ipinfo.io/json'
    data=requests.get(url).json()
    return data['city']



def weather():
    city=get_city()
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d13e913a090e16475014943e3147e564&units=metric'
    weather_data=requests.get(url).json()
    description=weather_data['weather'][0]['description']
    temp=weather_data['main']['temp']
    humidity=weather_data['main']['humidity']
    wind_speed=weather_data['wind']['speed']
    return f'Temperature - {temp}°Celsius,\n Humidity - {humidity},\n Wind Speed - {wind_speed} meter per second,\n Description - {description}'




if __name__=='__main__':
    main()