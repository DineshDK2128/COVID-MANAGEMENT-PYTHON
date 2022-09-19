import mysql.connector,datetime
user_acc =mysql.connector.connect(
            host="localhost",
            user="root",
            password="6383007540",
            database="Report"
           
           )
def data_insert(state,distic,village,positive,death,recovery):
           
            mycursor=user_acc.cursor()
            current_time = datetime.datetime.now()
            print (current_time)
            data_insert="insert into data(state,district,village,positive_case,death_case,recovered_case) value(%s,%s,%s,%s,%s,%s)"
            data=(state,district,village,positive,death,recovery)
            mycursor.execute(data_insert,data)
            user_acc.commit()
            print("data added Successful!")
def village(v):
    mycursor=user_acc.cursor()
    mycursor.execute(f"select positive_case,death_case,recovered_case from data where village='{v}'")
    result=mycursor.fetchall()
    if result!=[]:
        virus=result[0]
        print(f"{v} positive cases='{virus[0]}'")
        print(f"{v} death_cases='{virus[1]}'")
        print(f"{v} recovered_cases='{virus[2]}'")
    else:
        print("Enter valdi village name")
def district(district):
    
    mycursor=user_acc.cursor()
    mycursor.execute(f"select village from data where distic='{district}' ")
    result=mycursor.fetchall()
    if result!=[]:
        for i in range(len(result)):
          virus=result[i]
          print(f"'{i}'",virus[0])
        v=input("Enter your village Name: ")
        village(v)
    else:
        print("Please enter valid district")

def search(state):
    
            mycursor=user_acc.cursor()
            mycursor.execute(f"select distic from data where state='{state}' ")
            result=mycursor.fetchall()
            if result!=[]:
              for i in range(len(result)):
                 virus=result[i]
                 print(f"'{i}'",virus[0])
              distic=input("Enter your district: ")
              district(distic)
            else:
               print("Please enter valid state")

user=int(input("\n Enter 1 to Add Data\n Enter 2 to search your data\n"))
if user==1:
    state=input("Enter Your State: ")
    district=input("Enter Your district: ")
    village=input("Enter Your village: ")
    positive=input("Enter Your positive: ")
    death=input("Enter Your death: ")
    recovery=input("Enter Your recovery: ")
    data_insert(state,district,village,positive,death,recovery)
elif user==2:
    state=input("Enter your state: ")
    search(state)
else:
    print("Thanks for visit")

