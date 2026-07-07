import pickle
import os

FILE = "hotel.dat"

def load_data():
    if os.path.exists(FILE):
        f = open(FILE, "rb")
        data = pickle.load(f)
        f.close()
        return data
    return {}

def save_data(data):
    f = open(FILE, "wb")
    pickle.dump(data, f)
    f.close()

def add_customer(data):
    room = input("Enter Room Number: ")

    if room in data:
        print("Room already booked!")
        return

    name = input("Enter Customer Name: ")
    phone = input("Enter Phone Number: ")
    days = int(input("Enter Number of Days: "))

    record = {
        "Name": name,
        "Phone": phone,
        "Days": days
    }

    data[room] = record
    save_data(data)
    print("Room Booked Successfully")

def display_all(data):
    if len(data) == 0:
        print("No Records Found")
        return

    print("CUSTOMER DETAILS")
    for room in data:
        print("Room :", room)
        print("Name :", data[room]["Name"])
        print("Phone:", data[room]["Phone"])
        print("Days :", data[room]["Days"])
        print("---------------------------")

def search_customer(data):
    room = input("Enter Room Number: ")

    if room in data:
        print("Room :", room)
        print("Name :", data[room]["Name"])
        print("Phone:", data[room]["Phone"])
        print("Days :", data[room]["Days"])
    else:
        print("Record Not Found")

def check_rooms(data):
    print("\nAvailable Rooms")
    for i in range(101,111):
        if str(i) not in data:
            print(i,end=" ")
    print()

def bill(data):
    room=input("Enter Room Number: ")

    if room not in data:
        print("Room Not Found")
        return

    rent=1000
    days=data[room]["Days"]
    total=rent*days

    print("BILL")
    print("Customer :",data[room]["Name"])
    print("Room :",room)
    print("Days :",days)
    print("Rent Per Day :",rent)
    print("Total Bill :",total)

def checkout(data):
    room=input("Enter Room Number: ")

    if room in data:
        bill(data)
        del data[room]
        save_data(data)
        print("Checked Out Successfully")
    else:
        print("Room Not Found")

def update_days(data):
    room=input("Enter Room Number: ")

    if room in data:
        days=int(input("Enter New Number of Days: "))
        data[room]["Days"]=days
        save_data(data)
        print("Updated Successfully")
    else:
        print("Room Not Found")

def room_status(data):
    room=input("Enter Room Number: ")

    if room in data:
        print("Room Occupied")
    else:
        print("Room Available")

def delete_record(data):
    room=input("Enter Room Number: ")

    if room in data:
        del data[room]
        save_data(data)
        print("Record Deleted")
    else:
        print("Room Not Found")

def count_rooms(data):
    print("Booked Rooms :",len(data))
    print("Available Rooms :",10-len(data))

def menu():
    data=load_data()

    while True:
        print(" HOTEL MANAGEMENT SYSTEM ")
        print("1. Book Room")
        print("2. Display All Customers")
        print("3. Search Customer")
        print("4. Available Rooms")
        print("5. Generate Bill")
        print("6. Check Out")
        print("7. Update Stay")
        print("8. Room Status")
        print("9. Delete Record")
        print("10. Count Rooms")
        print("11. Exit")

        h=input("Enter Choice: ")

        if h=="1":
            add_customer(data)

        elif h=="2":
            display_all(data)

        elif h=="3":
            search_customer(data)

        elif h=="4":
            check_rooms(data)

        elif h=="5":
            bill(data)

        elif h=="6":
            checkout(data)

        elif h=="7":
            update_days(data)

        elif h=="8":
            room_status(data)

        elif h=="9":
            delete_record(data)

        elif h=="10":
            count_rooms(data)

        elif h=="11":
            print("Thank You")
            break

        else:
            print("Invalid Choice")

menu()