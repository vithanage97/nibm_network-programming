sum=0

def cal():
    if sum>=2000:
        discount = sum*10/100
        print("Discocunt : ",discount)
        print("Total Cost : ",sum-discount)
        
    elif sum>=1500:
        discount = sum*0.07
        print("Discocunt : ",discount)
        print("Total Cost : ",sum-discount)

    elif sum>=1000:
        discount = sum*0.05
        print("Discocunt : ",discount)
        print("Total Cost : ",sum-discount)

    elif sum<1000:
        print("No Discocunt")
        print("Total Cost : ",sum)

    else:
        print("not valid")
        exit()

def file():
    f=open("price.txt",'a+')
    print("\n")
    f.write(str(price))
    f.write("\n")
    f.close()

while True:
    try:
        price = int(input("enter price : "))
        sum=sum+price

    except:
        print("No Value Entered")
        break
    
    
cal()
file()
        




        




