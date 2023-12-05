from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getweather():
    try:
        city=textfield.get()

        geolocator= Nominatim(user_agent="geoapiExercises")
        location= geolocator.geocode(city)
        obj= TimezoneFinder()
        result= obj.timezone_at(lng=location.longitude,lat=location.latitude)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text =current_time)
        name.config(text="CURRENT WEATHER") 


        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=646824f2b7b86caffec1d0b16ea77f79"

        json_data = requests.get(api).json()
        conditon = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        tem.config(text=(temp,"°"))
        con.config(text=(conditon,"|","FEELS","LIKE",temp,"°"))

        win.config(text=wind)
        humi.config(text=humidity)
        des.config(text=description)
        press.config(text=pressure)


    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!!")


search = PhotoImage(file="search.png")
simage = Label(image=search)
simage.place(x=20,y=20)

textfield = tk.Entry(root,justify="center", width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

search_icon = PhotoImage(file="search_icon.png")
siimage=Button(image=search_icon, borderwidth=0,cursor="hand2",bg="#404040",command=getweather)
siimage.place(x=400,y=34)

logo = PhotoImage(file="Weather.png")
logoimage=Label(image=logo, height=700, width=800)
logoimage.place(x=150,y=100)

frame=PhotoImage(file="box.png")
frameimage=Label(image=frame,fg="white")
frameimage.pack(padx=5,pady=5,side=BOTTOM)

name=Label(root,font=("arial",15,"bold"),fg="#ffa500")
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20),fg="#ffa500")
clock.place(x=30,y=130)

label1=Label(root,text="WIND",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMDITY",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

tem=Label(font=("arial",70,"bold"),fg="#ff0000")
tem.place(x=400,y=150)
con=Label(font=("arial",15,"bold"),fg="#ff0000")
con.place(x=400,y=250)



win=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef",fg="#800000")
win.place(x=120,y=430)

humi=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef",fg="#800000")
humi.place(x=250,y=430)

des=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef",fg="#800000")
des.place(x=430,y=430)

press=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef",fg="#800000")
press.place(x=650,y=430)


root.mainloop()






