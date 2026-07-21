def toplama(x,y):
    return x+y
def çıkarma(x,y):
    return x-y
def çarpma (x,y):
    return x*y
def bölme(x,y):
    return x/y

while True:
    try:
        first = float(input("1. sayı:"))
        sign = input("işlem (+, -, *, /):")
        second = float(input("2. sayı:"))

        if sign == "+":
            print("sonuç: ", toplama(first,second))
        elif sign == "-":
            print("sonuç: ", çıkarma(first,second))
        elif sign == "*":
            print("sonuç: ", çarpma(first,second))
        elif sign == "/" and second == 0:
            print("bir sayıyı 0'a bölemezsiniz.")
        elif sign == "/":
            print("sonuç: ", bölme(first,second))
        else:
            print("lütfen geçerli bir karakter girin.")
        

    except ValueError:
        print("lütfen geçerli bir karakter girin.")
