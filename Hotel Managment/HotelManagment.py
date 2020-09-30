import time

def menu():
    print("Main Menu - please select an option:")
    choice = input("""
                      1: Add Guest
                      2: Add room
                      3: Add booking
                      4: View bookings
                      5: Quit

                      Please enter your choice: """)
    if int(choice)==1:
        add_guest()
    elif int(choice)==2:
        add_room()
    elif int(choice)==3:
        add_booking()
    elif int(choice)==4:
        view_booking()
    elif (int(choice)==5):
        print ("Thanks for using FedUni Hotel Bookings!")
        time.sleep(2)
        exit()

def add_guest():
    reuse=True
    
    while reuse:
        name_=input("Please enter guest name:")
        print ("Guest "+ name_+"has been created with guest ID:")
        name.append(name_)
        print (len(name))
        id.append(len(name))
        #print(name)
        #print(id)
        print ("[A]dd a new guest")
        print("[R]eturn to the previous menu" )
        char=input("Would you like to?")
        if char=='A':
            reuse=True
        if char=='R':
            menu()
            break 
            

def add_room():
    reuse=True
    
    while reuse:
        room_number=int(input("Please enter room number:"))
        while True:
            
            if room_number in room:
                 room_number=int(input("Room already exists. Please enter room number"))
            if room_number not in room:
                break
        room_capa=int(input("Please enter room capacity:"))
       
        room.append(room_number)
        room_cap.append(room_capa)
        #print(name)
        #print(id)
        print ("[A]dd a new room?")
        print("[R]eturn to the previous menu?" )
        char=input("Would you like to?")
        if char=='A':
            reuse=True
        if char=='R':
            menu()
            break 

def add_booking():
    reuse=True
    
    while reuse:
        G_id=int(input("Please enter guest ID:"))
        while True:
            if G_id not in id:
                print("Guest does not exist." )
                G_id=int(input("Please enter guest ID:"))
            if G_id in id:
                 break
       
        while True:
            room_number=int(input("Please enter room number:"))
            while True:
                if room_number not in room:
                    print ("Room does not exist.")
                    room_number=int(input("Please enter room number:"))
                if room_number in room:
                     break
            guests=int(input("Please enter number of guests:"))
            if (guests>room_cap[room.index(room_number)]):
                print ("Guest count exceeds room capacity of:")
                print (room_cap[room.index(room_number)])
            if (guests<=room_cap[room.index(room_number)]):
                month_in=int(input("Please enter check-in month: "))
                while True:
                    if(month_in>12):
                        month_in=int(input("Invalid month. Please enter check-in month:"))
                    elif(month_in<=12):
                        m_in.append(month_in)
                        break 
                
                
                day_in=int(input("Please enter check-in day: "))
                while True:
                  
                    if(day_in>31):
                        day_in=int(input("Invalid month. Please enter check-in day:"))
                    elif(day_in<=31):
                        d_in.append(day_in)
                        break 
                
                
                month_out=int(input("Please enter check-out month: "))
                while True:
           
                    if(month_out>12):
                        month_out=int(input("Invalid month. Please enter check-out month:"))
                    elif(month_out<=12):
                        m_out.append(month_out)
                        break  
                   
              
                day_out=int(input("Please enter check-out day: "))
                while True:
                    
                    if(day_out>31):
                        day_out=int(input("Invalid month. Please enter check-out day:"))
                    elif(day_out<=31):
                        d_out.append(day_out)
                        break      
                print("*** Booking successful! *** ")
                break 
    
    
    
    
        print ("[A]dd a new booking?")
        print("[R]eturn to the previous menu?" )
        char=input("Would you like to?")
        if char=='A':
            reuse=True
        if char=='R':
            menu()
            break
   
  
     
def view_booking():
     while True:
        print ("[G]Guest Booking?")
        print("[R]Room Booking?" )
        print ("[X] Exit")
        char=input("Would you like to?")
        if char=='X':
            break
        elif char=='R':
             G_id=int(input("Please enter guest ID:"))
             while True:
                 if G_id not in id:
                     print("Guest does not exist." )
                     G_id=int(input("Please enter guest ID:"))
                 if G_id in id:
                     print("Guest :" + name[id.index(G_id)])
                     print("Booking :" +"Room " + str(room[id.index(G_id)])
                     +" , "+ str(room_cap[id.index(G_id)]) + " guests from "+ 
                     str(m_in[id.index(G_id)])+ "/" +str(d_in[id.index(G_id)]) +
                     " to "+ str(m_out[id.index(G_id)])+ "/"+ str(m_out[id.index(G_id)]))
                     break
        elif char=='G':
            room_number=int(input("Please enter room number:"))
            while True:
                if room_number not in room:
                    print ("Room does not exist.")
                    room_number=int(input("Please enter room number:"))
                if room_number in room:
                     print("Room :" + str(room[room.index(room_number)]))
                     print ("Booking : Guest "+ name[room.index(room_number)]+" , "+
                            str(room_cap[room.index(room_number)])+" guests from "+ 
                             str(m_in[room.index(room_number)])+ "/" +str(d_in[room.index(room_number)]) +
                     " to "+ str(m_out[room.index(room_number)])+ "/"+ str(m_out[room.index(room_number)]))
                     break
         
     


    
name=[]   
id=[]
room=[]
room_cap=[]
m_in=[]
d_in=[]
m_out=[]
d_out=[]
print ("-----------------------------------------------\n" 
       "------ Welcome to FedUni Hotel Bookings -------\n" 
       "-----------------------------------------------")



menu()





    
    