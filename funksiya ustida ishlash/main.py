def info():
     a = int(input("birinchi son :"))
     b = int(input("ikkinchi son :"))
     if a > b :
         print(a)
     else:
         print(b)

# info()
def info():
    kocha = "oybek"
    mahalla = "navruz"
    tuman = "angor"
    viloyat = "surxondaryo"
    print (f"{kocha} kochasi,  \n{mahalla} mahallasi,  \n{tuman} tumani, \n{viloyat} viloyati," )
    manzil = [kocha, mahalla, tuman, viloyat]
    for i in manzil:
        print(i)
# info()