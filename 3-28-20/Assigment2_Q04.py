class Person:     
    def __init__(self, name, email):         
        self.name = name 
        self.email = email
class Address:     
    def __init__(self, street, city):         
        self.street = street         
        self.city = city
class Contact(Person, Address):    
    # constructor to initialize the person and Address class variables     
    def __init__(self, name, email, street, city):         
        Person.__init__(self, name, email)         
        Address.__init__(self, street, city) 
    def __str__(self):         
        return "Name: " + self.name + "\nEmail: " + self.email + "\nStreet: " + self.street + "\nCity: " + self.city + "\n" 
 
 
class Phonebook:     
    def __init__(self):        
        self.contactlist = [] 
    def add(self, contact: Contact):         
        # appending contact of type Contacts         
        self.contactlist.append(contact)
    # printing the whole contactlist     
    def show(self):         
        for i in self.contactlist:             
            print(i) 
 
    # sort by street name     
    def sortByStreet(self):         
        self.contactlist.sort(key=lambda x: x.street) 
 
    # sort by city name     
    def sortByCity(self):         
        self.contactlist.sort(key=lambda x: x.city)
    
     # search by street name     
    def searchByStreet(self, street):         
        for i in self.contactlist:             
            if i.street.lower() == street.lower():                 
                print(i) 
 
    # search by city name     
    def searchByCity(self, city):         
        for i in self.contactlist:             
            if i.city.lower() == city.lower():                 
                print(i)
                
if __name__ == "__main__":     
    phone = Phonebook()     
    # creating contact objects     
    c1 = Contact("Nilesh", "nileshkk9@example.com", "Baguihati", "Kolkata")     
    c2 = Contact("Raunak", "raunak9@example.com", "Manik", "Patna")     
    c3 = Contact("Nilesh", "dsjsd@example.com", "Baguihati", "Kolkata")
    c4 = Contact("Runi", "raunvsvsak9@example.com", "Kakurgachi", "Patna")     
    c5 = Contact("Bulla", "nilfvsveshkk9@example.com", "Hatiayara", "Kolkata")     
    c6 = Contact("John", "raunvsdvsak9@example.com", "Ultadanga", "Patna")     
    c7 = Contact("Varun", "nilevsdvsdshkk9@example.com", "Baharampur", "Kolkata")     
    c8 = Contact("Aman", "rauvdsvsdfnak9@example.com", "Manik", "Patna")     
    c9 = Contact("Rishab", "nisdslesdsvhkk9@example.com", "Baguihati", "Kolkata")     
    c10 = Contact("Hola", "sdvsfv@example.com", "Manik", "Patna") 
    
     # adding to list     
    phone.add(c1)     
    phone.add(c2)     
    phone.add(c3)     
    phone.add(c4)     
    phone.add(c5)     
    phone.add(c6)     
    phone.add(c7)     
    phone.add(c8)     
    phone.add(c9)     
    phone.add(c10)     
    # sorting by city name     
    phone.sortByCity()     
    # phone.searchByCity("patna")     
    # printing whole list     
    phone.show() 