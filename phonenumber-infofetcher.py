import phonenumbers   
from phonenumbers import geocoder as gc 
from phonenumbers import carrier as car
from phonenumbers import timezone as tz 

s=True
while(s):
    phno=input("Enter your phone number along with your country code\n")
    phone_number = phonenumbers.parse(phno)
    valid = phonenumbers.is_valid_number(phone_number)
    if(valid):
        print("The number is : "+phno)
        print("Operator : "+car.name_for_number(phone_number, 'en'))
        print("The Current Location: "+gc.description_for_number(phone_number,'en'))
        timezone=tz.time_zones_for_number(phone_number)
        for i in timezone:
            print("The current timezone : "+i,end=" ")
        print("\n")
        print("Do you search for another number--- Press 1 for yes otherwise press2")
        n=int(input())
        if(n==1):
            s=True
        else:
            s=False
        print("")
    else:
        print("please enter a valid phone number\n")
        s=True
