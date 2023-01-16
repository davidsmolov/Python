import Customers, Bookings, Rooms, check
import json, re

def greeting():
    print("Welcome To Hotel Califoria.\nSuch a lovely Place such a lovely face\nCome on, you can checkout anytime you wantm but you can never leave\nMade By D. Smolovich\n\n")

def Command():
    print("Here are the Commands you can use, show, add, delete. follow it up with the datatype you wanna work with: booking, customer, room ")
    print("here is what you can go for: \nAdd Customer, Add Room, Add Booking\nDelete Room, Delete Customer, Delete Booking\nShow All Rooms, Show All Customers, Show All Bookings\nShow Room,Show Room By Type\nShow Customer By Id, Show Customer By Name\nShow Booking By Dates, Show Free Booking By Dates.\n Exit - To Exit\n\n")
    word = input()
    cases(word)


def cases(word):
    if word == "Add Room":
        print("Now please insert the room. with the following room parameters by order:\nroomid, size, capacity, numberofbeds, type, price ")
        print("make sure the roomid is a 3 num digit, and the type is one of the following: Basic, Deluxe, Suite.")
        roomid = input("Insert Room Number: ")
        size = input("Insert The Room's Size: ")
        capacity = input("Insert Capacity: ")
        numberofbeds = input("Insert The Number Of Beds: ")
        type = input("Insert Room Type: ")
        price = input("Insert The Room's Price Per Night: ")
        check.checkRoom(roomid,size,capacity,numberofbeds,type,price)
        room = Rooms.Room(roomid,size,capacity,numberofbeds,type,int(price))
        room.add_room()
        Command()

    elif word == "Add Customer":
        print("Now please insert a new customer. with the following parameters by order:\nid, name, address, city, email, age ")
        print("make sure the id is 0 numbered, and that the email is valid")
        id = input("Insert your ID: ")
        name = input("Whats your name: ")
        address = input("whats your address: ")
        city = input("which city are you from? ")
        email = input("What's your email? ")
        age = input("How old are you? ")
        check.checkCustomer(id,name,address,city,email,age)
        customer = Customers.Customers(id,name,address,city,email,age)
        customer.add_customer()
        Command()

    elif word == "Add Booking":
        print("Now please insert a new booking. with the following parameters by order:\nid, roomid, arrival date, departure date")
        print("make sure to insert your id correctly, and a room that exists. Also make sure you write the date in the following format: dd/mm/yyyy")
        id = input("Whats your id? ")
        roomid = input("Whats the room number you want to book? ")
        arrivaldate = input("When do you plan to arrive? ")
        departuredate = input("When do you plan on departing? ")
        check.checkBooking(id,roomid,arrivaldate,departuredate)
        booking = Bookings.Bookings(id,roomid,arrivaldate,departuredate)
        booking.add_booking()
        Command()

    elif word == "Delete Room":
        print("Now please insert the room's ID. Our Bulldozer is on standby to demolish it ")
        roomid = input()
        if not re.match("^[1-9][0-9]{2}$", roomid):
            raise Exception("room id must be 3 digits long")
        Rooms.delete_room(roomid)
        Command()

    elif word == "Delete Customer":
        print("Now please insert the Customer's ID. We have a shooting squad on standby ")
        id = input()
        if not re.match("^[0-9]{9}$", id):
            raise Exception("id has to be made out of 9 numbers")
        Customers.delete_Customer(id)
        Command()

    elif word == "Delete Booking":
        print("Now please insert the Vacation Parameters: Your id, The Room's Number and the arrival date")
        id = input("What is the ID Under the rservation: ")
        roomid = input("What room number did you order? ")
        arrivaldate = input("When were you supposed to get there")
        if not re.match("^[0-9]{9}$", id):
            raise Exception("id has to be made out of 9 numbers")
        if not re.match("^[1-9][0-9]{2}$", roomid):
            raise Exception("room id must be 3 digits long")
        if not re.match("^[0-3][0-9]/[0-1][0-9]/[0-9]{4}$", arrivaldate):
            raise Exception("Arrival date inserted badly")
        Bookings.delete_booking(id,roomid,arrivaldate)
        Command()

    elif word == "Show All Rooms":
        Rooms.print_rooms()
        Command()

    elif word == "Show Room":
        print("What the room's Number?")
        roomid = input()
        if not re.match("^[1-9][0-9]{2}$", roomid):
            raise Exception("room id must be 3 digits long")
        print(Rooms.get_room(roomid),"\n\n")
        Command()

    elif word == "Show Room By Type":
        print("Whats the room type you are interseted in?")
        type = input()
        with open ("Type.json",'r') as json_file:
            types = json.load(json_file)
            if type not in types["type"] :
                raise Exception("type can only be Basic, Deluxe, Suite")
        print(Rooms.get_RoomByType(type),"\n\n")
        Command()
    
    elif word == "Show All Customers":
        Customers.print_Customers()
        Command()
    
    elif word == "Show Customer By Id":
        print("Whats your ID?")
        id = input()
        if not re.match("^[0-9]{9}$", id):
            raise Exception("id has to be made out of 9 numbers")
        print(Customers.get_customer(id),"\n\n")
        Command()
    
    elif word == "Show Customer By Name":
        print("Whats Your Name?")
        name = input()
        if not re.match(re.compile(r'^[a-zA-Z][a-zA-Z\'\- ]+[a-zA-Z]$'), name):
            raise Exception("no numbers and special characters in names")
        print(Customers.get_customerByName(name))
        Command()

    elif word == "Show Booking By Dates":
        mindate = input("Insert Beginning Date")
        maxdate = input("Insert End Range Date")
        if not re.match("^[0-3][0-9]/[0-1][0-9]/[0-9]{4}$", mindate):
            raise Exception("min date inserted badly")
        if not re.match("^[0-3][0-9]/[0-1][0-9]/[0-9]{4}$", maxdate):
            raise Exception("max date inserted badly")
        Bookings.print_BookingByDates(mindate,maxdate)
        Command()
    
    elif word =="Show Free Booking By Dates":
        mindate = input("Insert Beginning Date")
        maxdate = input("Insert End Range Date")
        if not re.match("^[0-3][0-9]/[0-1][0-9]/[0-9]{4}$", mindate):
            raise Exception("min date inserted badly")
        if not re.match("^[0-3][0-9]/[0-1][0-9]/[0-9]{4}$", maxdate):
            raise Exception("max date inserted badly")
        Bookings.print_FreeBookingByDates(mindate,maxdate)
        Command()
    elif word== "Exit":
        print("This is hotel california, You Can Checkout Anytime you want. BUT YOU CAN NEVER LEAVE\n\n")
        Command()
    else:
        print("You Gave A Non Existing Command check again\n\n")
        Command()


greeting()
Command()
