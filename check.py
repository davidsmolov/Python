import Customers, Bookings, Rooms
import json, re


#Check Room input
##roomid, size, capacity, numberofbeds, type, price
def checkRoom(roomid, size, capacity, numberofbeds, type, price):
    if not re.match("^[1-9][0-9]{2}$", roomid):
        raise Exception("room id must be 3 digits long")
    if not re.match("^[1-9][0-9]*", size):
        raise Exception("insert a proper digit")
    if not re.match("^[1-9]{1}$", capacity):
        raise Exception("capacity can only be one digit")
    if not re.match("^[1-9]{1}$", numberofbeds):
        raise Exception("can only be one digit")
    with open ("Type.json",'r') as json_file:
        types = json.load(json_file)
        if type not in types["type"] :
             raise Exception("type can only be Basic, Deluxe, Suite")
    if not re.match("[0-9]+", price):
        raise Exception("only numbers allowed")

#Check Customer input
##id, name, address, city, email, age
def checkCustomer(id,name,address,city,email,age):
    if not re.match(re.compile(r'^[0-9]{9}$'), id):
        raise Exception("id has to be made out of 9 numbers")
    if not re.match(re.compile(r'^[a-zA-Z][a-zA-Z\'\- ]+[a-zA-Z]$'), name):
        raise Exception("no numbers and special characters in names")
    if not re.match(re.compile(r'^[0-9a-zA-Z\'\- ]+$'), address):
        raise Exception("no special characters allowed in address")
    if not re.match(re.compile(r'^[0-9a-zA-Z\'\- ]+$'), city):
        raise Exception("make sure to only use letters and not numbers and special character")
    if not re.match(re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'), email):
        raise Exception("You inserted an incorrect email")
    if not re.match("^[0-9]+$", age):
        raise Exception("Age inserted incorrectly, make sure you insert a number")

#Check Booking input
##arrivalDate, DepartureDate
def checkBooking(id,roomid,arrivaldate,departuredate):
    if not re.match("^[0-9]{9}$", id):
        raise Exception("id has to be made out of 9 numbers")
    if not re.match("^[1-9][0-9]{2}$", roomid):
        raise Exception("room id must be 3 digits long")
    if not re.match("^[0-3][0-9]/[0-1][0-9]/[0-9]{4}$", arrivaldate):
        raise Exception("Arrival date inserted badly")
    if not re.match("^[0-3][0-9]/[0-1][0-9]/[0-9]{4}$", departuredate):
        raise Exception("Departure date inserted badly")

#TESTING
