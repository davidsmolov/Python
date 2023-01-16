import json
import os
class Customers:
    def __init__(self, id, name, address, city, email, age):
        self.id = id
        self.name = name
        self.address = address
        self.city = city
        self.email = email
        self.age = age
    
    def add_customer(self):
        lst = [] #a list that will hold all the customers
        new_customer = {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "city": self.city,
            "email": self.email,
            "age": self.age
        }
        if os.path.getsize('Customers.json')>0:  #if the file is empty there is no need to read whats inside
            with open('Customers.json', 'r') as json_file:
                Customers = json.load(json_file)
                for num in range(0,len(Customers)):
                    if Customers[num]["id"]==self.id:
                        raise Exception("Error, Can not have 2 Customers with the same id")
                lst.append(Customers)
                

        # append the new Customer to the list of Customers
        lst.append(new_customer)
        # write the updated list of Customers to the JSON file
        with open('Customers.json', 'w') as json_file:
            json.dump(lst, json_file)
        with open('Customers.json','r') as json_file:
            data = json_file.read()
            print(data)
        #Remove all uncessary brackets to keep the json file format intact 
        data = data.replace("[","")
        data = data.replace("]","")
        with open("Customers.json",'w') as json_file: #write the entire json back to the file and add brackets at the beginning and end of it
            json_file.write("["+data+"]")

        print("Customer added successfully!")
    
def delete_Customer(id):
    worked = False
    with open('Customers.json') as json_file:
            Customers = json.load(json_file)
            for num in range(0,len(Customers)):
                if Customers[num]["id"]==id:
                    worked = True
                    del Customers[num]
                    break
            if not worked:
                raise Exception("The Customer You Requested To Remove Does Not Exist In Our Database")
                
    data = ''     
    with open("Customers.json",'w') as json_file:
        data = str(Customers)
        data = data.replace("'",'"')
        if data =="[]":
            json_file.write("")
        else:
            json_file.write(data)
        print("\nCustomer Was Successfully Executed\n")

#function to print out all the existing Customers
def print_Customers(): 
    with open('Customers.json') as json_file:
        Customers = json.load(json_file)
        print(f'Our Clients Are: {len(Customers)}\n')
        for Customer in Customers:
            print(f'The Customers id is: {Customer["id"]}. The Customer name Is: {Customer["name"]}. The Customer Home Address: {Customer["address"]}. The City the customer is from: {Customer["city"]}. The Customer email address is: {Customer["email"]}. And The Customer Is: {Customer["age"]} Years Old\n \n')

def get_customer(id):
    with open('Customers.json', 'r') as json_file:
        customers = json.load(json_file)
        for customer in customers:
            if customer["id"] == id:
                return {"name": customer["name"], "address": customer["address"], "city": customer["city"], "email": customer["email"], "age": customer["age"]}
        raise Exception("The ID You Requested Does Not Exist In Our Database")
def get_customerByName(name):
    with open('Customers.json', 'r') as json_file:
        customers = json.load(json_file)
        for customer in customers:
            if customer["name"] == name:
                return {"id": customer["id"], "address": customer["address"], "city": customer["city"], "email": customer["email"], "age": customer["age"]}
        raise Exception("The ID You Requested Does Not Exist In Our Database")

##TESTING