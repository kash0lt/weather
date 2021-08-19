import tkinter as tk
import requests
from apiid import myapiid
# myapiid inits a keyvalue that comes from THIS users openweathermap.org account
# class myapiid():
#    def __init__(self):
#       self.keyvalue = '<your-key-goes-here>'

HEIGHT = 500
WIDTH = 600
CANVAS = '#80c1ff'


def getWeather(cityToSearch):
    apikey = myapiid()
    weatherURL = 'https://api.openweathermap.org/data/2.5/weather'   # this is a openweathermap API call string
    params = {'appid': apikey.keyvalue, 'q': cityToSearch, 'units': 'imperial'}
    response = requests.get(weatherURL, params=params)
    label['text'] = format_weather(response.json())


def format_weather(weatherjsonstring):
    # print(weatherjsonstring)
    try:
        w_name = weatherjsonstring['name']
        w_weather = weatherjsonstring['weather'][0]['description']
        w_icon = weatherjsonstring['weather'][0]['icon']
        w_temp = weatherjsonstring['main']['temp']
        w_feels = weatherjsonstring['main']['feels_like']
        w_humidity = weatherjsonstring['main']['humidity']
        # print(w_name, w_weather, w_temp, w_feels, w_humidity)
        finalStr = 'City: %s \nConditions: %s \nTemp: %s (°F) \nFeels Like: %s (°F) \nHumidity: %s %%' \
            % (w_name, w_weather, w_temp, w_feels, w_humidity)
    except:
        finalStr = "Invalid response from web"
    return finalStr


if __name__ == '__main__':
    root = tk.Tk()
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()
    backgroundImage = tk.PhotoImage(file='rainier1.png')
    backgroundLabel = tk.Label(root, image=backgroundImage)
    backgroundLabel.place(relwidth=1, relheight=1)
    frameTop = tk.Frame(root, bg=CANVAS, bd=2)
    frameTop.place(anchor='n', relx=0.5, rely=0.1, relwidth=0.85, relheight=0.1)
    entry = tk.Entry(frameTop, bg='white', font=40)
    entry.place(relwidth=0.65, relheight=1)
    button = tk.Button(frameTop, text="Get Weather", font=40, command=lambda: getWeather(entry.get()))
    button.place(relx=0.66, relwidth=0.33, relheight=1)
    frameLower = tk.Frame(root, bg=CANVAS, bd=5)
    frameLower.place(anchor='n', relx=0.5, rely=0.25, relwidth=0.85, relheight=0.6)
    label = tk.Label(frameLower, text='', bg='white', font=40, anchor='w', justify='left', bd=4)
    label.place(relwidth=1, relheight=1)
    label['text'] = 'Enter either you city above\nor you may use a zip code\nor you may use a city, xx\nwhere xx is a country code'

    root.mainloop()
