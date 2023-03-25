import math
import lists
from lists import *
import time
import random
import os
from list import *
import sys
import banner
from banner import *
from password import *

                # الالة الحاسبة الفيزيائية
                                     # physical calculator
                                                          # by ramses

class colors:
    BLUE        = '\033[94m'
    GREEN       = '\033[32m'
    RED         = '\033[0;31m'
    DEFAULT     = '\033[0m'
    ORANGE      = '\033[33m'
    WHITE       = '\033[97m'
    BOLD        = '\033[1m'
    BR_COLOUR   = '\033[1;37;40m'
    BLACK       = '\033[30m'
    YELLOW      = '\003[33m'
    CYAN        = '\003[36m'

os.system('clear')
time.sleep(.2)

                           # here the script will strat 
 # slow print code

def slprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(.005)

                  # password

count = int(4)
def password() :
    inp = (input(" enter password  :  "))
    if inp in pwd :
     os.system("clear")
     print(colors.GREEN+"""

success login ...

""")
     start()
    else :
     print(colors.RED+"""

failed login

"""+colors.WHITE)
     password()
 # start

def start():
    ban = random.randint(1,2)
    if ban == 1:
     slprint(colors.WHITE+banner1w1)
     slprint(colors.WHITE+banner1r)
     slprint(colors.WHITE+banner1w2)
    elif ban == 2:
     slprint(colors.GREEN+banner2)
    print(" ")
    slprint(colors.BLUE+list_all)
    print(" ")
    allc = input(colors.DEFAULT+" اختر نوع الالة : ")
    print(" ")
    if allc == "1":
     os.system("clear")
     slprint(colors.ORANGE+list_eq)
     slprint(colors.RED+list_er)
     slprint(colors.ORANGE+list_eb)
     time.sleep(0)
     chois = input(colors.DEFAULT+"   اختر المطلوب : ")
     print(" ")
     time.sleep(.2)

                           # the chois 1 ---> 1

     if chois == "1":
         os.system("clear")
         slprint(colors.ORANGE+list1)
         list1c = input(colors.DEFAULT+"   اختر المعطيات : ")
         slprint(" ")
         time.sleep(.2)
         if list1c == "1":
          os.system('clear')
          print(" ")
          a1 = int(input(colors.ORANGE+"   اكتب الحجم :  "))
          print(" ")
          b1 = int(input("   اكتب الكثافة :  "))
          print(" ")
          time.sleep(.2)
          print(" ")
          print(colors.DEFAULT," الكتلة "," = "," الكثافة "," × "," الحجم "," = ",a1 * b1)
          time.sleep(3)
          print(" ")
          start()
                           # the chois 1 ---> 2
         elif list1c == "2":
            os.system('clear')
            print(" ")
            c1 = int(input(colors.DEFAULT+"  اكتب الوزن : "))
            print(" ")
            time.sleep(.2)
            print(colors.DEFAULT," الكتلة "," = "," الوزن "," ÷ "," عجلة الجاذبية ( 10 ) "," = ",c1 / 10)
            print(" ")
            time.sleep(3)
            print(" ")
            start()

                           #  the chois 1 ---> 3

         elif list1c == "3":
            os.system('clear')
            print(" ")
            e1 = int(input(colors.ORANGE+" : اكتب السرعة  "))
            print(" ")
            f1 = int(input(" : اكتب طاقة الحركة  "))
            print(" ")
            time.sleep(.2)
            print(colors.DEFAULT," الكتلة "," = "," ( السرعة × 2  ) "," ÷ "," ( طاقة الحركة تربيع ) "," = ",(2*e1) / (f1*f1))
            time.sleep(3)
            print(" ")
            start()

                           # the chois 1 ---> back

         elif list1c == "0":
            print(" ")
            slprint(colors.GREEN+" [+]   ...جار التراجع ")
            time.sleep(2)
            os.system('clear')
            start()


         elif list1c == "x":
            print(" ")
            slprint("-------------------------")
            print(" ")
            slprint(colors.GREEN+" شكرا على الاستخدام [+] ")
            print(" ")
            sys.exit(0)


         elif list1c == "X":
            print(" ")
            slprint("-------------------------")
            print(" ")
            slprint(colors.GREEN+" شكرا على الاستخدام [+] ")
            print(" ")
            sys.exit(0)

                            # the chois 1 ---> restart ; invaild

         else:
            print(" ")
            print(" ")
            slprint(colors.RED+" [-] مدخل خاطئ "  )
            print(" ")
            slprint(colors.GREEN+" [+]   ...جار التراجع ")
            time.sleep(2)
            os.system('clear')
            start()
                           # the chois 2
                           # the chois 2 ---> 1


     elif chois == "2":
       os.system("clear")
       slprint(colors.ORANGE+list2)
       sllist2c = input(colors.DEFAULT+" اختر الشكل او المعطيات :  ")
       print(" ")
       time.sleep(.2)
       if list2c == "1":
        os.system("clear")
        a21= int(input(colors.ORANGE+" : اكتب الطول  "))
        print(" ")
        b21= int(input(" : اكتب العرض "))
        print(" ")
        c21= int(input(" : اكتب الارتفاع "))
        print(" ")
        time.sleep(.2)
        print(colors.DEFAULT," حجم متوازي المستطيلات "," = "," الطول "," × "," العرض "," × "," الارتفاع "," = " ,a21 * b21 * c21)
        time.sleep(3)
        print(" ")
        start()

       elif list2c == "2":
          os.system("clear")
          d22= int(input(colors.ORANGE+" : اكتب نصف القطر " ))
          print(" ")
          e22= int(input(" : اكتب الارتفاع "))
          print(" ")
          time.sleep(.2)
          print(colors.DEFUALT," حجم الاسطوانة "," = "," مساحة القاعدة "," × "," الارتفاع "," = ",(22/7) * (d22*d22)  * e22)
          time.sleep(3)
          print(" ")
          start()

       elif list2c == "3":
          os.system("clear")
          f23= int(input(colors.ORANGE+" : اكتب طول الحرف " ))
          print(" ")
          time.sleep(.2)
          print(colors.DEFAULT," حجم المكعب "," = "," طول الحرف تكعيب " ," = ",f23*f23*f23)
          time.sleep(3)
          print(" ")
          start()

       elif list2c == "4":
          os.system("clear")
          f24= int(input(colors.ORANGE+" : اكتب نصف القطر  " ))
          print(" ")
          time.sleep(.2)
          print(colors.DEFAULT," حجم الكرة  "," = "," (4/3) "," × "," (22/7) "," × "," طول الحرف تكعيب " ," = ",(4/3) * (22/7) * (f24*f24))
          time.sleep(3)
          print(" ")
          start()

       elif list2c == "5":
          os.system("clear")
          print(" ")
          f25= int(input(colors.ORANGE+" اكتب الكتلة :  " ))
          print(" ")
          f26= int(input(" اكتب الكثافة : "))
          time.sleep(.2)
          print(" ")
          print(colors.DEFAULT," الحجم  "," = "," الكتلة "," / "," الكثافة "," = ",f25 / f26)
          time.sleep(3)
          print(" ")
          start()


       elif list2c == "0":
          print(" ")
          slprint(colors.GREEN+" [+]   ...جار التراجع ")
          time.sleep(2)
          os.system("clear")
          start()

       elif list2c == "x":
          print(" ")
          slprint("-------------------------")
          print(" ")
          slprint(colors.GREEN+" شكرا على الاستخدام [+] ")
          print(" ")
          sys.exit(0)

       elif list2c == "X":
          print(" ")
          slprint("-------------------------")
          print(" ")
          slprint(colors.GREEN+" شكرا على الاستخدام [+] ")
          print(" ")
          sys.exit(0)



       else:
           print(" ")
           print(" ")
           slprint(colors.RED+" [-] مدخل خاطئ "  )
           print(" ")
           slprint(colors.GREEN+" [+]   ...جار التراجع ")
           time.sleep(1)
           os.system("clear")
           start()

                           # the chois 3
                           # the chois 3 ---> 1



     elif chois == "3":
       os.system("clear")
       slprint(colors.ORANGE+list3)
       list3c = input(colors.DEFAULT+" اختر الضلع المفقود : ")
       print(" ")
       time.sleep(.2)
       if list3c == "1":
        os.system("clear")
        a331 = int(input(colors.ORANGE+" اكتب الضلع الاخر : ")) 
        print(" ")
        b331 = int(input(" اكتب الوتر : "))
        print(" ")
        time.sleep(.2)
        print(colors.DEFAULT," الضلع المطلوب "," = "," جذر ","(  الوتر تربيع "," - "," الضلع الاخر تربيع  )"," = ",math.sqrt((b331*b331) - (a331*a331)))
        time.sleep(3)
        print(" ")
        start()


       elif list3c == "2":
          os.system("clear")
          afe = int(input(colors.ORANGE+" اكتب الضلع الاول : ")) 
          print(" ")
          bfe = int(input(" اكتب الضلع الثاني : "))
          print(" ")
          time.sleep(.2)
          print(colors.DEFAULT," الوتر "," = "," جذر ","( الضلع الاول تربيع "," + "," الضلع الثاني تربيع  )"," = ",math.sqrt((afe*afe) + (bfe*bfe)))
          time.sleep(3)
          print(" ")
          start()

       elif list3c == "0":
          print(" ")
          print(" ")
          slprint(colors.GREEN+" [+]   ...جار التراجع ")
          time.sleep(2)
          os.system("clear")
          start()


       elif list3c == "x":
          print(" ")
          slprint("-------------------------")
          print(" ")
          slprint(colors.GREEN+" شكرا على الاستخدام [+] ")
          print(" ")
          sys.exit(0)

       elif list3c == "X":
          print(" ")
          slprint("-------------------------")
          print(" ")
          slprint(colors.GREEN+" شكرا على الاستخدام [+] ")
          print(" ")
          sys.exit(0)


       else:
           print(" ")
           print(" ")
           slprint(colors.RED+" [+] مدخل خاطئ "  )
           print(" ")
           slprint(colors.GREEN+" [+]  ...جار التراجع ")
           time.sleep(2)
           os.system("clear")
           start()

                           # the chois x ---> here the script would closed

     elif chois == "4":
       os.system("clear")
       slprint(colors.ORANGE+list41)
       list41c = input(colors.DEFAULT+" اختر النوع المطلوب :  ")
       print(" ")
       time.sleep(.2)
       if list41c == "1":
        os.system("clear")
        aso1 = int(input(colors.ORANGE+" اكتب مجموع المسافات :  ")) 
        print(" ")
        bso1 = int(input(" اكتب مجموع الازمنة  "))
        print(" ")
        time.sleep(.2)
        print(colors.DEFAULT," السرعة المتوسطة  "," = "," المسافة الكلية "," / "," الزمن الكلي "," = ",aso1 / bso1 )
        time.sleep(3)
        print(" ")
        start()


       elif list41c == "2":
          os.system("clear")
          time.sleep(1)
          slprint(colors.ORANGE+list423)
          print(" ")
          list41c1 = input(colors.DEFAULT+" اختر المعطيات : ")
          if list41c1 == "1":
           os.system("clear")
           print(" ")
           cso2 = int(input(colors.ORANGE+" اكتب المسافة : ")) 
           print(" ")
           dso2 = int(input(" اكتب الزمن : "))
           print(" ")
           time.sleep(.2)
           print(colors.DEFAULT," السرعة القياسية  "," = "," المسافة  "," / "," الزمن "," = ",cso2 / dso2)
           time.sleep(3)
           print(" ")
           start()

          elif list41c1 == "2":
           os.system("clear")
           print(" ")
           eso2 = int(input(colors.ORANGE+" اكتب الكتلة : ")) 
           print(" ")
           fso2 = int(input(" اكتب الطاقة الحركية : "))
           print(" ")
           time.sleep(.2)
           print(colors.DEFAULT," السرعة القياسية "," = "," جذر "," ( 2 × طاقة الحركة  "," / "," الكتلة ) ",math.sqrt((2*fso2) / eso2))
           time.sleep(3)
           print(" ")
           start()


       elif list41c == "3":
          os.system("clear")
          eso3 = int(input(colors.ORANGE+"  اكتب الازاحة : "))
          def rezaha():

              print(" ")
              gso3 = input(colors.ORANGE+" اكتب اتجاهها ( مثال : شمال شرق   ) :   ")
              if gso3 in ("شمال" , "جنوب", "شرق" , "غرب" , "شمال شرق"  , "شمال غرب"  , "جنوب شرق"  , "جنوب غرب" ):
               print(" ")
               fso3 = int(input(" اكتب الزمن : "))
               print(" ")
               time.sleep(.2)
               slprint(colors.DEFAULT," السرعة المتجهة  "," = "," الازاحة  "," / "," الزمن "," = ",eso3 / fso3,gso3)
               time.sleep(3)
               print(" ")
               start()
              else:
                 print(" ")
                 slprint(colors.RED+" [+] الاتجاه خاطئ ")
                 time.sleep(.5)
                 print(" ")
                 slprint(colors.GREEN+" [+]   ...جار التراجع ")
                 time.sleep(1)
                 os.system("clear")
                 print(" ")
                 slprint(colors.ORANGE,"  اكتب الازاحة : ",eso3)
                 print(" ")
                 rezaha()
          rezaha()

       elif list41c == "0":
          print(" ")
          slprint(colors.GREEN+" [+]   ...جار التراجع ")
          time.sleep(2)
          os.system("clear")
          start()

     elif chois =="x":
        print(" ")
        slprint("-------------------------")
        print(" ")
        slprint(colors.GREEN+" شكرا على الاستخدام [+] ")
        print(" ")
        sys.exit(0)

     elif chois =="X":
        print(" ")
        slprint("-------------------------")
        print(" ")
        slprint(colors.GREEN+" شكرا على الاستخدام [+] ")
        print(" ")
        sys.exit(0)


     elif chois == "0":
        print(" ")
        slprint(colors.GREEN+" [+]   ...جار التراجع ")
        time.sleep(1)
        os.system("clear")
        start()
                      # the chois incorrect ---> rastart ; invaild
     else:
        print(" ")
        slprint(colors.RED+" [-] مدخل خاطئ "  )
        print(" ")
        slprint(colors.GREEN+" [+]   ...جار التراجع ")
        time.sleep(2)
        os.system("clear")
        start()

    elif allc =="2":
     os.system("clear")
     slprint(colors.ORANGE+list99)
     normalc = input(colors.DEFAULT+" اختر نوع العملية : ")
     if normalc =="1":
      os.system("clear")
      print(" ")
      gam31 = int(input(colors.ORANGE+" اكتب الرقم الاول : "))
      print(" ")
      gam32 = int(input(" اكتب الرقم الثاني : "))
      print(" ")
      print(colors.DEFAULT,"( قسمة ) " ,gam31," ÷ ",gam32," = ",gam31 / gam32)
      time.sleep(3)
      start()
     elif normalc =="2":
      os.system("clear")
      print(" ")
      gam31 = int(input(colors.ORANGE+" اكتب الرقم الاول : "))
      print(" ")
      gam32 = int(input(" اكتب الرقم الثاني : "))
      print(" ")
      print(colors.DEFAULT,"( جمع ) ",gam31," + ",gam32," = ",gam31 + gam32)
      time.sleep(3)
      start()
     elif normalc =="3":
      os.system("clear")
      print(" ")
      gam31 = int(input(colors.ORANGE+" اكتب الرقم الاول : "))
      print(" ")
      gam32 = int(input(" اكتب الرقم الثاني : "))
      print(" ")
      print(colors.DEFAULT,"( ضرب ) "  ,gam31," × ",gam32," = ",gam31 * gam32)
      time.sleep(3)
      start()
     elif normalc =="4":
      os.system("clear")
      print(" ")
      gam31 = int(input(colors.ORANGE+" اكتب الرقم الاول : "))
      print(" ")
      gam32 = int(input(" اكتب الرقم الثاني : "))
      print(" ")
      print(colors.DEFAULT,"( طرح ) " ,gam31," - ",gam32," = ",gam31 - gam32)
      time.sleep(3)
      start()
     elif normalc == "0":
      print(" ")
      slprint(colors.GREEN+" [+]   ...جار التراجع ") 
      time.sleep(2)
      os.system('clear')
      start()
     elif normalc == "x":
      print(" ")
      slprint("-------------------------")
      print(" ")
      slprint(colors.GREEN+" شكرا على الاستخدام [+] ")
      print(" ")
      sys.exit(0)
     elif normalc == "X":
      print(" ")
      slprint("-------------------------")
      print(" ")
      slprint(colors.GREEN+" شكرا على الاستخدام [+] ")
      print(" ")
      sys.exit(0) 

     else:
        print(" ")
        slprint(colors.RED+" [-] مدخل خاطئ  "  )
        print(" ")
        slprint(colors.GREEN+" [+]   ...جار التراجع ")
        time.sleep(1)
        os.system("clear")
        start()
    elif allc == "x":
       print(" ")
       slprint("-------------------------")
       print(" ")
       slprint(colors.GREEN+" شكرا على الاستخدام [+] ")
       print(" ")
       sys.exit(0)
    elif allc =="X":
       print(" ")
       slprint("-------------------------")
       print(" ")
       slprint(colors.GREEN+" شكرا على الاستخدام [+] ")
       print(" ")
       sys.exit(0)

    else:
       print(" ")
       slprint(colors.RED+" [-] مدخل خاطئ  "  )
       print(" ")
       slprint(colors.GREEN+" [+]   ...جار التراجع ")
       time.sleep(1)
       os.system("clear")
       start()


password()
start()
