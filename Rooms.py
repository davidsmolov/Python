import json
import os

class Room:
    def __init__(self, roomid, size, capacity, numberofbeds, type, price):
        self.roomid = roomid
        self.size = size
        self.capacity = capacity
        self.numberofbeds = numberofbeds
        self.type = type
        self.price = price

    def add_room(self):
        lst= [] #a list that will hold all the rooms
        # create a new Room object
        new_room_dict = {"roomid": self.roomid, "size": self.size, "capacity": self.capacity, "numberofbeds": self.numberofbeds, "type": self.type, "price": self.price}

        # read the existing JSON file and then append it into a list
        if os.path.getsize('Rooms.json')>0:  #if the file is empty there is no need to read whats inside
            with open('Rooms.json', 'r') as json_file:
                rooms = json.load(json_file)
                for num in range(0,len(rooms)):
                    if rooms[num]["roomid"]==self.roomid:
                        raise Exception("Error, Can not have 2 rooms with the same numbers")
                lst.append(rooms)
                

        # append the new room to the list of rooms
        lst.append(new_room_dict)
        # write the updated list of rooms to the JSON file
        with open('Rooms.json', 'w') as json_file:
            json.dump(lst, json_file)
        with open('Rooms.json','r') as json_file:
            data = json_file.read()
            print(data)
        #Remove all uncessary brackets to keep the json file format intact 
        data = data.replace("[","")
        data = data.replace("]","")
        with open("Rooms.json",'w') as json_file: #write the entire json back to the file and add brackets at the beginning and end of it
            json_file.write("["+data+"]")

        print("Room added successfully!\n\n")
def delete_room(roomid):
    worked = False
    with open('Rooms.json') as json_file:
            rooms = json.load(json_file)
            for num in range(0,len(rooms)):
                if rooms[num]["roomid"]==roomid:
                    worked = True
                    del rooms[num]
                    break
            if not worked:
                raise Exception("The Room You Requested To Remove Does Not Exist In Our Database")
                
    data = ''     
    with open("Rooms.json",'w') as json_file:
        data = str(rooms)
        data = data.replace("'",'"')
        if data == "[]":
            json_file.write("")
        else:
            json_file.write(data)
        print("\nRoom Was Successfully Deleted\n")





#function to print out all the existing rooms
def print_rooms(): 
    with open('Rooms.json') as json_file:
        rooms = json.load(json_file)
        print(f'The Number Of Room We Have is: {len(rooms)}\n')
        for room in rooms:
            print(f'The Room id is: {room["roomid"]}. The Room Size Is: {room["size"]}. The Room Capacity Is: {room["capacity"]}. The Number Of Beds is: {room["numberofbeds"]}. The Room Type Is: {room["type"]}. And The Room Price Is: {room["price"]} \n \n')

#function to get a room's details
def get_room(roomid):
    with open('Rooms.json', 'r') as json_file:
        rooms = json.load(json_file)
        for room in rooms:
            if room["roomid"] == roomid:
                return {"size": room["size"], "capacity": room["capacity"], "numberofbeds": room["numberofbeds"], "type": room["type"], "price": room["price"]}
        raise Exception("The Room You Requested Does Not Exist In Our Database")

def get_RoomByType(type):
    with open('Rooms.json', 'r') as json_file:
        rooms = json.load(json_file)
        for room in rooms:
            if room["type"] == type:
                return {"roomid": room["roomid"],"size": room["size"], "capacity": room["capacity"], "numberofbeds": room["numberofbeds"], "price": room["price"]}
        raise Exception("The Room You Requested Does Not Exist In Our Database")
#####testing