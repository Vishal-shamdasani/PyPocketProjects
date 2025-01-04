a=input('''if you want to code a message type C\nelse if you want to decode type D ''')
try:
    if a=="C":
        b=input("enter your message it should be more than 3 letters long ")
        if len(b)<3:
            raise ValueError("the message should be atleast 3 letters long")
        else:
            c=b[0]
            d=b[1:]+c
            print(d[::-1])
    elif a=="D":
        b=input("enter the message you want to decode ")
# vinasadmahs lahsi
        if len(b)<3:
            raise ValueError("the message should be atleast 3 letters long")
        else:
            c=b[::-1]
            # print(c)
            d=b[0]+c[:-1]
            print(d)
            #vlahsi
    else:
        raise TypeError("given argument is not a option")
except ValueError:
    print("the message should be atleast 3 letters long")

