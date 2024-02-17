from tkinter import *
from tkinter import ttk 
import requests 
from PIL import Image, ImageTk
def data():

  city = com.get() 
  api_key = "e6cd96994edc36ad836c5895f221ad54"  
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

  response = requests.get(url)
  data = response.json()
 
  label20.config(text=data['weather'][0]['main'])
  label30.config(text=data['weather'][0]['description'])
  label40.config(text=str(int(data['main']['temp']-273.15)))
  label5.config(text=data["main"]['pressure'])
  label60.config(text=data['wind']['speed'])
  label70.config(text=data['main']['humidity'])
  

root=Tk()
root.title('Weather forecasting')
root.config(bg='sky blue')
root.geometry('500x600')
root.iconbitmap("C:\\Users\\bansa\\Downloads\\weather_43796.ico")

image=Image.open("C:\\Users\\bansa\\Downloads\\5667.jpg")

tk_image=ImageTk.PhotoImage(image)

label1=Label(root, image=tk_image)
label1.place(x=0, y=0)


label1= Label(root, text="Welcome to weather forecasting!!",fg='black',bg='#c0bfdd', font=("Times new roman",16,"bold"))
label1.pack(pady=60)
city_name=StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com=ttk.Combobox(root, text="hello", values=list_name,font=('times new roman',16))

com.pack(pady=20)

done_button=Button(root, text='Check',font=('Times new roman',14,'bold'),width=5, height=1, command=data)
done_button.pack(pady=15)

label2=Label(root, text="Weather Climate", font=("times new roman",14))
label2.place(x=20,y=300)
label20=Label(root, text="", font=("times new roman",14))
label20.place(x=250,y=300)

label3=Label(root, text="Weather description", font=("times new roman",14))
label3.place(x=20, y=340)
label30=Label(root, text="", font=("times new roman",14))
label30.place(x=250, y=340)

label4=Label(root, text="Temperature", font=("times new roman",14))
label4.place(x=20, y=380)
label40=Label(root, text="", font=("times new roman",14))
label40.place(x=250, y=380)

label5=Label(root, text="", font=("times new roman",14))
label5.place(x=250,y=420)
label50=Label(root, text="Pressure", font=("times new roman",14))
label50.place(x=20,y=420)

label6=Label(root,text="Wind speed", font=("times new roman",14))
label6.place(x=20,y=460)
label60=Label(root, text="", font=("times new roman",14))
label60.place(x=250,y=460)

label7=Label(root,text="Humidity", font=("times new roman",14))
label7.place(x=20,y=500)
label70=Label(root,text="",font=("times new roman",14))
label70.place(x=250,y=500)

root.mainloop()