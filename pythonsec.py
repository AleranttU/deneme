import colorama
from colorama import Fore, Back, Style
colorama.init()

# Yazı Rengi

print(Fore.RED)
	
print("### PythonSec ###")
print("Sürüm: 1.0.0")
print(Style.RESET_ALL)
while True:
	password = input("Şifre Giriniz: ")
	rpassword = "anan"
	if password==rpassword:
	    print("\n\n")
	    print("Dosya eklemek için",Fore.YELLOW,"[1]",Style.RESET_ALL)
	    print("Dosya açmak için",Fore.YELLOW,"  [2]",Style.RESET_ALL)
	        
	    cop = int(input("Seçtiğiniz Değeri Giriniz: "))
	    if cop == 1:
	        print(Fore.CYAN + "Dosya Ekleme\n" + Style.RESET_ALL)
	        createtext = input(" - Dosya İçeriğini Giriniz: ")
	        ths = open("//storage//emulated//0//pythonsec//pass", "w")
	        ths.write(createtext)
	        print(Fore.GREEN,"Değişiklikleriniz kaydedildi.",Style.RESET_ALL)
	    elif cop == 2:
	        f = open("//storage//emulated//0//pythonsec//pass", "r")
	        print("-------------- ",Back.RED,Fore.WHITE," DOSYA ",Style.RESET_ALL," --------------\n")
	        print("   ",f.read())
	        print("\n-----------------------------------")
	else:
	    print("Yanlış Şifre Giridiniz. Tekrar deneyiniz")
	
	
	