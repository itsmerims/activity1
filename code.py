dict = {"Cy":19, "Ken":25, "Ryan":14}

def dashboard():
    print("""
    SELECT ACTION
    [A] ADD User
    [B] SEARCH User
    [C] DELETE User
    [D] UPDATE User
    [X] VIEW ALL USERS
    """)
    x = input("Enter Action : ")
    if (x == 'b' or x == 'B'):
        view()
    elif (x == 'a' or x == 'A'):
        add()
    elif (x == 'c' or x == 'C'):
        delete()
    elif (x == 'd' or x == 'D'):
        update()
    elif (x == 'x' or x == 'X'):
        all()

def all():
    print(dict)
    dashboard()

def view():
    i = input("Enter Name to Search : ")
    if i in dict:
        j = dict[i]
        print("Search Successful Name : {} Age : {}".format (i,j))
    else:
        print("Name not registered!")
    dashboard()

def add():
    n = input("Enter Name: ")
    a = input("Enter Age: ")
    dict[n]=a
    print("User Successfully Added")
    dashboard()

def delete():
    d = input("Enter Name to delete: ")
    if d in dict:
        del dict[d]
        print("User Successfully Deleted")
    else:
        print("The name: {} is not registered!".format(d))
    dashboard()

def update():
    u = input("Enter Name to update : ")
    if u in dict:
        v = input("Enter New value for {}:".format(u))
        dict[u]=v
        print("The name: {} successfully updated!".format(u))
    else:
        print("The name: {} is not registered!".format(u))
    dashboard()

dashboard()
