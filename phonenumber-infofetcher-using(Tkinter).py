import phonenumbers   
from phonenumbers import geocoder as gc 
from phonenumbers import carrier as car
from phonenumbers import timezone as tz
from tkinter import * 
  
         
root = Tk()
root.title("PHONENUMBER INFORMATION SYSTEM")
root.geometry("800x600")

def phonefetch():
    pt=e1.get()
    phone_number = phonenumbers.parse(pt)
    e2.insert(0, pt)
    op=car.name_for_number(phone_number, 'en')
    e3.insert(0, op)
    gl=gc.description_for_number(phone_number,'en')
    e4.insert(0, gl)
    timezone=tz.time_zones_for_number(phone_number)
    t=""
    for i in timezone:
            t=t+i+" "
    e5.insert(0, t)

    
label = Label(root, text ='Enter your phone number along with your country code')               
label.grid(row = 10, column = 1)

label1 = Label(root, text ='Phone Number')               
label1.grid(row = 15, column = 1)
label2 = Label(root, text ='Operator')
label2.grid(row = 16, column = 1)
l3 = Label(root, text ="Current Location")
l3.grid(row = 17, column = 1)
l4 = Label(root, text ="Current Timezone")
l4.grid(row = 18, column = 1)



e1 = Entry(root)
e1.grid(row = 11, column = 1)
e2 = Entry(root)
e2.grid(row = 15, column = 2)
e3 = Entry(root)
e3.grid(row = 16, column = 2)
e4 = Entry(root)
e4.grid(row = 17, column = 2)
e5 = Entry(root)
e5.grid(row = 18, column = 2)

ent = Button(root, text = "Fetch Details", bg ="red", fg ="white", command = phonefetch)
ent.grid(row = 11, column = 2)

root.mainloop()
