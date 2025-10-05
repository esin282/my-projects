def toplama(x,y):
    return x+y
def çıkarma(x,y):
    return x-y
def çarpma (x,y):
    return x*y
def bölme(x,y):
    return x/y

try:
   first = float(input("1. sayı:"))
   sign = input("işlem (+, -, *, /):")
   second = float(input("2. sayı:"))

   if sign == "+":
    print("sonuç: " + str(toplama(first,second)))
   elif sign == "-":
    print("sonuç: " + str(çıkarma(first,second)))
   elif sign == "*":
    print("sonuç: " + str(çarpma(first,second)))
   elif sign == "/":
       if second == 0:
        print("bir sayıyı 0'a bölemezsiniz.")
       else:
            print("sonuç: " + str(bölme(first,second)))
   else:
    print("işlem yapılamadı.")
    
except ValueError:
    print("lütfen sadece sayı girin.")
