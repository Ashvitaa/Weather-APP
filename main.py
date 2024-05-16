import requests
import tkinter
import ttkbootstrap
from tkinter import messagebox
from PIL import ImageTk,Image
def get_weather(city):
    api_key = '82fda0f60035d1b50f2dadd1a1885565'

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        #icon_id=data['weather'][0]['icon']
        temperature = data['main']['temp'] - 273.15
        description = data['weather'][0]['description']
        city = data['name']
        country = data['sys']['country']
        #icon_url=f"https://openweathermap.org/img/wn/{icon_id}10d@2x.png"
    else:
        print('Error fetching weather data')

    return (temperature,description,city,country)


def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    temperature, description, city, country = result
    location_lable.configure(text=f"{city} , {country}")

    '''icon =Image.open(requests.get(icon_url,stream=True).raw)
    ic = ImageTk.PhotoImage(icon)
    icon_lable.config(image=ic)
    icon_lable.icon = ic'''

    temperature_lable.configure(text=f"Temperature: {temperature} degree Celcius")
    description_lable.configure(text=f"Description: {description}")







#creating window, setting title and geometry
root=ttkbootstrap.Window(themename="cyborg")
root.title("WeatherInformation")
root.geometry("1000x700")

#mainimage
image=Image.open("imagesforproject/finalicon (1).png")
image1 = image.resize((150, 170))
img=ImageTk.PhotoImage(image1)
imglable=tkinter.Label(image=img)
imglable.place(x=120,y=7)

#Lables - for main title and subtitle
title_lable=ttkbootstrap.Label(text="WeatherApp", font=("Georgia","40","bold "))
title_lable.pack(pady=80,padx=140)
subtitle_lable=ttkbootstrap.Label(text="Get weather-information by just entering the city's name!",font=("Georgia","12","italic"))
subtitle_lable.pack(pady=5)

#frame1-for search bar
frame=ttkbootstrap.Frame(root,style="light")
frame.pack(pady=20)
search_title=ttkbootstrap.Label(frame,text="Enter the name of city below",font=("Georgia","12",),style="inverse-light")
search_title.pack(pady=15,padx=60)
city_entry=ttkbootstrap.Entry(frame,style="dark")
city_entry.pack(pady=7,padx=20)

#search button
search_button=ttkbootstrap.Button(text="SearchWeather",style="secondary-outline",command=search)
search_button.pack(pady=12)

#location-label- to show city/country name
location_lable=ttkbootstrap.Label(root,font=("Georgia",12))
location_lable.pack(pady=20)



temperature_lable=ttkbootstrap.Label(root,font=("Georgia",12,'bold'),style="light")
temperature_lable.pack(pady=20)
description_lable=ttkbootstrap.Label(root,font=("Georgia",12,'bold'),style="light")
description_lable.pack(pady=20)








root.mainloop()





