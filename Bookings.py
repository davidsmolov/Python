from datetime import datetime
from Customers import *
from Rooms import *
import os
class Bookings():
    def __init__(self, id, roomid, arrivaldate, departuredate):
        self.custid= id
        self.customer = get_customer(self.custid)
        self.roomid= roomid
        self.room = get_room(self.roomid)
        self.arrivaldate = arrivaldate
        self.departuredate = departuredate
        self.totalprice = None
    @property
    def number_of_days(self):
        arrival_date = datetime.strptime(self.arrivaldate, "%d/%m/%Y")
        departure_date = datetime.strptime(self.departuredate, "%d/%m/%Y")
        return (departure_date - arrival_date).days
    @property
    def totaldays(self):
        return self.number_of_days
    @property
    def totalprice(self):
        return self.totaldays*self.room["price"]
    @totalprice.setter
    def totalprice(self, value):
        self._totalprice = value


    def add_booking(self):
        lst = [] #a list that will hold all the customers
        new_booking = {
            "id": self.custid,
            "roomid": self.roomid,
            "arrivaldate": self.arrivaldate,
            "departuredate": self.departuredate,
            "totalPrice": self.totalprice
        }
        if self.totaldays<1:
            raise Exception("Cant reserve a room for less than a day")
        #check to see that the duration length is in sync with the room type
        roomType=get_room(self.roomid)
        if roomType["type"] == "Deluxe" and self.totaldays <2:
            raise Exception("Deluxe rooms cant be reserved for less than 2 days")
        elif roomType["type"] == "Suite" and self.totaldays < 3:
            raise Exception("Suite Can't Be Reserved for less than 3 days")
        if os.path.getsize('Bookings.json')>0:  #if the file is empty there is no need to read whats inside
            with open('Bookings.json', 'r') as json_file:
                Bookings = json.load(json_file)
                for booking in Bookings:
                    if booking["roomid"] == new_booking["roomid"]:
                        #datetime.strptime(self.arrivaldate, "%d/%m/%Y") converts the string into a date that can be compared to other dates
                        if datetime.strptime(booking["departuredate"],"%d/%m/%Y") >= datetime.strptime(self.arrivaldate,"%d/%m/%Y") or datetime.strptime(booking["arrivaldate"],"%d/%m/%Y") >= datetime.strptime(self.departuredate,"%d/%m/%Y"):
                            raise Exception("Sorry Room Is Already Reserved For These Days")
                lst.append(Bookings)
                

        # append the new Booking to the list of Bookings
        lst.append(new_booking)
        # write the updated list of Bookings to the JSON file
        with open('Bookings.json', 'w') as json_file:
            json.dump(lst, json_file)
        with open('Bookings.json','r') as json_file:
            data = json_file.read()
            print(data)
        #Remove all uncessary brackets to keep the json file format intact 
        data = data.replace("[","")
        data = data.replace("]","")
        with open("Bookings.json",'w') as json_file: #write the entire json back to the file and add brackets at the beginning and end of it
            json_file.write("["+data+"]")

        print("Booking added successfully!")

def get_bookById(id):
    with open('Bookings.json', 'r') as json_file:
        lst = []
        bookings = json.load(json_file)
        for booking in bookings:
            if booking["id"] == id:
                lst.append({"roomid": booking["roomid"], "arrivaldate": booking["arrivaldate"], "departuredate": booking["departuredate"], "totalPrice": booking["totalPrice"]})
        if len(lst) >0:
            return lst
        else:
            raise Exception("The id you requested has no booking")

def get_bookByRoomid(roomid):
    lst = []
    if os.path.getsize('Bookings.json')>0:  #if the file is empty there is no need to read whats inside
        with open('Bookings.json', 'r') as json_file:
            bookings = json.load(json_file)
            for booking in bookings:
                if booking["roomid"] == roomid:
                    lst.append({"id": booking["id"], "arrivaldate": booking["arrivaldate"], "departuredate": booking["departuredate"], "totalPrice": booking["totalPrice"]})
            if len(lst) >0:
                return lst
            else:
                raise Exception("No one has booked that room yet")
    else:
        return lst


def delete_booking(id,roomid, arrivaldate):
    worked = False
    with open('Bookings.json') as json_file:
            Bookings = json.load(json_file)
            for num in range(0,len(Bookings)):
                if Bookings[num]["id"]==id and Bookings[num]["roomid"]==roomid and Bookings[num]["arrivaldate"]==arrivaldate:
                    worked = True
                    del Bookings[num]
                    break
            if not worked:
                raise Exception("There Is No Such Reservation Stored in our")
                
    data = ''     
    with open("Bookings.json",'w') as json_file:
        data = str(Bookings)
        data = data.replace("'",'"')
        if data =="[]":
            json_file.write("")
        else:
            json_file.write(data)
        print("\Booking Was Successfully Canceled\n")

#function to print out all the existing Bookings
def print_Bookings(): 
    with open('Bookings.json') as json_file:
        Bookings = json.load(json_file)
        print(f'The Number of bookings we have is: {len(Bookings)}\n')
        for Booking in Bookings:
            print(f'The Customer\'s id that ordered the room is: {Booking["id"]}. The Room number Is: {Booking["roomid"]}. The Expected Arrival Date is: {Booking["arrivaldate"]}. The Expected Deparutre Date is: {Booking["departuredate"]}. The Overall Price Of Your Stay Is: {Booking["totalPrice"]}.\n \n')

lst = []
def print_BookingByDates(mindate,maxdate):
    mindate = datetime.strptime(mindate, "%d/%m/%Y")
    maxdate = datetime.strptime(maxdate, "%d/%m/%Y")
    if mindate > maxdate:
        raise Exception("min date cant be bigger than max date")
    with open('Bookings.json','r') as json_file:
        Bookings = json.load(json_file)
        for Booking in Bookings:
            arrivaeldate = datetime.strptime(Booking["arrivaldate"],"%d/%m/%Y")
            departuredate = datetime.strptime(Booking["departuredate"],"%d/%m/%Y")
            if (arrivaeldate >= mindate and maxdate >= arrivaeldate) or (departuredate <= maxdate and mindate <= departuredate):
                lst.append(Booking)
                print(f'Room {Booking["roomid"]} is booked for these days')

def print_FreeBookingByDates(mindate,maxdate):
    mindate = datetime.strptime(mindate, "%d/%m/%Y")
    maxdate = datetime.strptime(maxdate, "%d/%m/%Y")
    if mindate > maxdate:
        raise Exception("min date cant be bigger than max date")
    with open('Bookings.json','r') as json_file:
        Bookings = json.load(json_file)
        free_rooms = []
        for Booking in Bookings:
            arrivaeldate = datetime.strptime(Booking["arrivaldate"],"%d/%m/%Y")
            departuredate = datetime.strptime(Booking["departuredate"],"%d/%m/%Y")
            if (arrivaeldate < mindate or maxdate < arrivaeldate) and (departuredate > maxdate or mindate > departuredate):
                free_rooms.append(Booking["roomid"])
                print(f'Room {Booking["roomid"]} is free for these days\n\n')




        


####TESTING