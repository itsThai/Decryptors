import math
 
message = int(input("Enter the message to be encrypted: ")) 
 
p = int(input("Choose prime number p: "))
q = int(input("Choose prime number q: "))
n = p*q

def prime_check(a):
    if(a==2):
        return True
    elif((a<2) or ((a%2)==0)):
        return False
    elif(a>2):
        for i in range(2,a):
            if not(a%i):
                print("try again!")
    return True

def find_e(p, q):
    n = p*q
    phi_n = (q-1)*(p-1)
    print("key public can be")
    for i in range(2, phi_n):
        if math.gcd(i, phi_n) == 1:
            print(i)
            e = i
    return e

def encrypt(me):
    k_pub = int(input("Choose key public: "))
    en = math.pow(me,k_pub)
    c = en % n
    print("Encrypted Message is: ", c)
    return c

e = find_e(p, q)
c = encrypt(message)