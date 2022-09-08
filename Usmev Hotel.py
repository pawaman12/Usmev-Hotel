print("*****")
print(" Welcome To The úsměv Hotel =) ") #the word translates to smile :)
print("*****")
print("What would you like to do today? =)")
print("Enter the digits to state your reason for visit =)")
print("1.Check In" "\n" "2.Exit The Hotel" "\n" "3.Leave A Review" "\n" "4.Display Data (Requires Passcode ;) )" "\n" "5.Save Database" "\n" "6.Total Bill" "\n" "7.Press any other key to exit the application.")
info=[] #initialized an empty list
def check_in(): #this function takes in the details of the person checking in
    print("\n")
    print("Thankyou for choosing our hotel =) ")
    while True: #created a while loop to make the input user dependent
        name=input(str("Please Enter Your Full Name:"))
        identity=input(str("Please Enter Your CNIC Number:"))
        room=input(str("Please Enter How Many Rooms You Require:"))
        days=input(str("Please Enter The Number Of Days You'll Stay:"))
        age=input(str("Please Enter Your Age:"))
        print()
        list_of_rec=[name,identity,room,days,age]
        info.append(list_of_rec) #appended the data to a empty list to be later used
        choice=input("Would you like to continue? Enter y if you do:")
        if choice!="y":
            break
def display_data():
    print("Only A Manager Can See Our Database =)")
    pwd=input("Please Enter The Password:") #a security measure to ensure the data is safe
    if pwd=="smile":
        print("Hello Sir =)")
        count=0 #a counter to keep in count the number of records being displayed
        for i in range(len(info)):
            print("Person's Name:",info[count][0]) #used slicing of the list to get to the specific fields
            print("CNIC Number:",info[count][1])
            print("Total Rooms Required:",info[count][2])
            print("Days:",info[count][3])
            print("Age:",info[count][4])
            print() #printed an empty space for records to be seperated 
            count+=1          
    else:
        print("You are not allowed to view this data =(")
def save_file():
    f=open("HOTEL.txt","w") #creates a new file everytime the function is called thus creating a new file daily
    count=0
    for element in info:
        f.write(info[count][0]+",")
        f.write(info[count][1]+",")
        f.write(str(info[count][2])+",")
        f.write(str(info[count][3])+",")
        f.write(str(info[count][4])+"\n")
        count+=1
    f.close()

def load_file(): #displays the records 
    f=open("HOTEL.txt")
    for element in f:
        r=element.split(",")
        print(r)
    f.close()

def leave(): #asks the user to enter a review
    print("We hope you enjoyed your stay!")
    print("Thankyou for choosing úsměv Hotel =)")
    print("Please leave a small review on our hotel and service if you can and remember to keep smiling =)")
    print("Please Enter Anything To Exit")

def review(): #enters a review to be saved and used for later
    v=open("reviews.txt","w") 
    review=input("Enter Your Review Here =):")
    v.write(review)
    v.close()

def total_bill(): #uses a custom formula for a user to estimate or pay his bill
    m1=int(input("Enter The Number Of Rooms You Used:"))
    m2=int(input("Enter The Number Of Days You Stayed:"))
    print("Your total bill is:",(m2*10*m1),'$')

info=[] 
while True: #this is the driver code which calls all the functions one by one
    print("Hello =)")
    ch=int(input("Enter The Option You'd Like To Choose =) :"))
    if ch==1:
        check_in()
    elif ch==2:
        leave()
    elif ch==3:
        review()
    elif ch==4:
        display_data()
    elif ch==5:
        save_file()
    elif ch==6:
        total_bill()
    else: #breaks if the user enters anything else
        print("Have a good day! =)")
        break