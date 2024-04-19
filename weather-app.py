from tkinter import *
from tkinter import ttk
import requests 
def data_get():
    try:
        city = city_name.get()
        data = requests.get("url" + city + "& appid=api key").json()
        w_label1.config(text=data["weather"][0]["main"])
        wd_label1.config(text=data["weather"][0]["description"])
        temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
        p_label1.config(text=data["main"]["pressure"])
    except Exception as e:
        print("Error:",e)  
     


win = Tk()
win.title("My Weather Station")
win.config(bg = "Light blue")
win.geometry("1000x1000")
name_label = Label(win,text="My Weather Station",
                   font=("Times New Roman",40,"bold"))
name_label.place(x=250,y=50,height=100,width=500)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="My Weather Station",values=list_name,
                   font=("Times New Roman",20,"bold"),textvariable=city_name)
com.place(x=250,y=180,height=50,width=500)
#climate
w_label = Label(win,text="Weather Climate",
                   font=("Times New Roman",20,"bold"))
w_label.place(x=300,y=370,height=50,width=400)
#climate label
w_label1 = Label(win,text=" ",
                   font=("Times New Roman",20,"bold"))
w_label1.place(x=750,y=370,height=50,width=200)

#description
wd_label = Label(win,text="Weather Description",
                   font=("Times New Roman",20,"bold"))
wd_label.place(x=300,y=430,height=50,width=400)

# description label
wd_label1 = Label(win,text=" ",
                   font=("Times New Roman",20,"bold"))
wd_label1.place(x=750,y=430,height=50,width=200)
#temprature
temp_label = Label(win,text="Temperature",
                   font=("Times New Roman",20,"bold"))
temp_label.place(x=300,y=490,height=50,width=400)

#temprature label
temp_label1 = Label(win,text=" ",
                   font=("Times New Roman",20,"bold"))
temp_label1.place(x=750,y=490,height=50,width=200)

#pressure
p_label = Label(win,text="Pressure",
                   font=("Times New Roman",20,"bold"))
p_label.place(x=300,y=550,height=50,width=400)
#presuree label
p_label1 = Label(win,text=" ",
                   font=("Times New Roman",20,"bold"))
p_label1.place(x=750,y=550,height=50,width=200)

done_button = Button(win,text="Done",font=("Times New Roman",20,"bold"),command=data_get)
done_button.place(y=250,height=100,width=150,x=400)

win.mainloop()