email = input("Enter your email : ")
# MInimum no of characters in the email   a@b.com = 7
k,j,d = 0,0,0
if len(email)>=7:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():
                            j =1
                    elif i.isdigit():
                        continue
                    elif i == " " or i=="." or i == "@":
                        continue
                    else:
                        d = 1
                        
                if k == 1 or j==1 or d==1:
                    print("Wrong email 5: space in email")
            else: 
                print(" Invalid email 4: POsition of dot and number of dot")
        else: 
            print("Wrong email 3: @ in email and @ count")
    else:
        print("Invalid email 2: First character should be  a alphabet")
else:
    print("Wrong email : no of characters less than 7")

