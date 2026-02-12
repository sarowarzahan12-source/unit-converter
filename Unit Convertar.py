print("WELCOME TO UNIT CONVERTER")
while True:
    try:
        print("CHOOSE CATEGORY\n1.LENGTH\n2.TEMPERATURE\n3.WEIGHT\n4.AREA\n5.VOLUME\n6.EXIT")
        u=int(input("ENTER YOUR CHOICE(DON'T WRITE INSTEAD WRITE NUMBER)\n"))
        if u==1:
            while True:
                try:
                    print("CHOOSE\n1.KM TO MILE\n2.MILE TO KM\n3.METER TO INCH\n4.INCH TO METER\n5.MILLIMETER TO CENTIMETER\n6.CENTIMETER TO MILLIMETER\n7.METR TO KILOMETER\n8.KILOMETER TO METER\n9.FEET TO METER\n10.METER TO FEET\n11.YARD TO METER\n12.METER TO YARD\n13.MILE TO FEET\n14.FEET TO MILE\n15.MILE TO YARD\n16.YARD TO MILE\n17.INCH TO CENTIMETER\n18.CENTIMETER TO INCH\n19.MILLIMETER TO INCH\n20.INCH TO MILLIMETER\n21.BACK")
                    u=int(input("YOUR CHOICE(DONT WRITE INSTEAD WRITE NUMBER)\n"))
                    if u==1:
                        try:
                            k=float(input("ENTER KM\n"))
                            r=k*0.621371
                            print(f"RESULT = {r} MILE\n")
                        except ValueError:
                            print("INVALID ENTER KM\n")
                            continue
                    elif u==2:
                        try:
                            m=float(input("ENTER MILE\n"))
                            re=m/0.621371
                            print(f"RESULT = {re} KM\n")
                        except ValueError:
                            print("INVALID ENTER MILE\n")
                            continue
                    elif u==3:
                        try:
                            me=float(input("ENTER METER\n"))
                            res=me*39.3701
                            print(f"RESULT = {res} INCH\n")
                        except ValueError:
                            print("INVALID ENTER METER\n")
                            continue
                    elif u==4:
                        try:
                            i=float(input("ENTER INCH\n"))
                            resu=i/39.3701
                            print(f"RESULT = {resu} METER\n")
                        except ValueError:
                            print("INVALID ENTER INCH\n")
                            continue
                    elif u==5:
                        try:
                            mm = float(input("ENTER MILLIMETER\n"))
                            cm = mm / 10
                            print(f"RESULT = {cm} CENTIMETER\n")
                        except ValueError:
                            print("INVALID ENTER MILLIMETER\n")
                            continue
                    elif u==6:
                        try:
                            cm = float(input("ENTER CENTIMETER\n"))
                            mm = cm * 10
                            print(f"RESULT = {mm} MILLIMETER\n")
                        except ValueError:
                            print("INVALID ENTER CENTIMETER\n")
                            continue
                    elif u==7:
                        try:
                            m = float(input("ENTER METER\n"))
                            km = m / 1000
                            print(f"RESULT = {km} KILOMETER\n")
                        except ValueError:
                            print("INVALID ENTER METER\n")
                            continue
                    elif u==8:
                        try:
                            km = float(input("ENTER KILOMETER\n"))
                            m = km * 1000
                            print(f"RESULT = {m} METER\n")
                        except ValueError:
                            print("INVALID ENTER KILOMETER\n")
                            continue
                    elif u==9:
                        try:
                            ft = float(input("ENTER FEET\n"))
                            m = ft * 0.3048
                            print(f"RESULT = {m} METER\n")
                        except ValueError:
                            print("INVALID ENTER FEET\n")
                            continue
                    elif u==10:
                        try:
                            m = float(input("ENTER METER\n"))
                            ft = m / 0.3048
                            print(f"RESULT = {ft} FEET\n")
                        except ValueError:
                            print("INVALID ENTER METER\n")
                            continue
                    elif u==11:
                        try:
                            yd = float(input("ENTER YARD\n"))
                            m = yd * 0.9144
                            print(f"RESULT = {m} METER\n")
                        except ValueError:
                            print("INVALID ENTER YARD\n")
                            continue
                    elif u==12:
                        try:
                            m = float(input("ENTER METER\n"))
                            yd = m / 0.9144
                            print(f"RESULT = {yd} YARD\n")
                        except ValueError:
                            print("INVALID ENTER METER\n")
                            continue
                    elif u==13:
                        try:
                            mile = float(input("ENTER MILE\n"))
                            ft = mile * 5280
                            print(f"RESULT = {ft} FEET\n")
                        except ValueError:
                            print("INVALID ENTER MILE\n")
                            continue
                    elif u==14:
                        try:
                            ft = float(input("ENTER FEET\n"))
                            mile = ft / 5280
                            print(f"RESULT = {mile} MILE\n")
                        except ValueError:
                            print("INVALID ENTER FEET\n")
                            continue
                    elif u==15:
                        try:
                            mile = float(input("ENTER MILE\n"))
                            yd = mile * 1760
                            print(f"RESULT = {yd} YARD\n")
                        except ValueError:
                            print("INVALID ENTER MILE\n")
                            continue
                    elif u==16:
                        try:
                            yd = float(input("ENTER YARD\n"))
                            mile = yd / 1760
                            print(f"RESULT = {mile} MILE\n")
                        except ValueError:
                            print("INVALID ENTER YARD\n")
                            continue
                    elif u==17:
                        try:
                            inch = float(input("ENTER INCH\n"))
                            cm = inch * 2.54
                            print(f"RESULT = {cm} CENTIMETER\n")
                        except ValueError:
                            print("INVALID ENTER INCH\n")
                            continue
                    elif u==18:
                        try:
                            cm = float(input("ENTER CENTIMETER\n"))
                            inch = cm / 2.54
                            print(f"RESULT = {inch} INCH\n")
                        except ValueError:
                            print("INVALID ENTER CENTIMETER\n")
                            continue
                    elif u==19:
                        try:
                            mm = float(input("ENTER MILLIMETER\n"))
                            inch = mm / 25.4
                            print(f"RESULT = {inch} INCH\n")
                        except ValueError:
                            print("INVALID ENTER MILLIMETER\n")
                            continue
                    elif u==20:
                        try:
                            inch = float(input("ENTER INCH\n"))
                            mm = inch * 25.4
                            print(f"RESULT = {mm} MILLIMETER\n")
                        except ValueError:
                            print("INVALID ENTER INCH\n")
                            continue
                    elif u==21:
                        print("BACKING...\n")
                        break
                    else:
                        print("INVALID ENTER CHOICE\n")
                        continue
                except ValueError:
                    print("INVALID INPUT, TRY AGAIN\n")
                    continue
        elif u==3:
            while True:
                try:
                    print("CHOICE\n1.KILO TO POUND\n2.POUND TO KILO\n3.GRAM TO OUNCE\n4.OUNCE TO GRAM\n5.BACK")
                    u=int(input("YOUR CHOICE(DONT WRITE INSTEAD WRITE NUMBER)\n"))
                    if u==1:
                        try:
                            K=float(input("ENTER KILO\n"))
                            rE=K*2.20462
                            print(f"RESULT = {rE} POUND\n")
                        except ValueError:
                            print("INVALID ENTER KILO\n")
                            continue
                    elif u==2:
                        try:
                            p=float(input("ENTER POUND\n"))
                            REs=p/2.20462
                            print(f"RESULT = {REs} KILO\n")
                        except ValueError:
                            print("INVALID ENTER POUND\n")
                            continue
                    elif u==3:
                        try:
                            g=float(input("ENTER GRAM\n"))
                            RES=g/28.3495
                            print(f"RESULT = {RES} OUNCE\n")
                        except ValueError:
                            print("INVALID ENTER GRAM\n")
                            continue
                    elif u==4:
                        try:
                            o=float(input("ENTER OUNCE\n"))
                            ReS=o*28.3495
                            print(f"RESULT = {ReS} GRAM\n")
                        except ValueError:
                            print("INVALID ENTER OUNCE\n")
                            continue
                    elif u==5:
                        print("BACKING...\n")
                        break
                    else:
                        print("INVALID ENTER CHOICE\n")
                        continue
                except ValueError:
                    print("INVALID INPUT, TRY AGAIN\n")
                    continue
        elif u==2:
            while True:
                try:
                    print("CHOOSE \n1.CELSIUS TO FAHRENHEIT\n2.FAHRENHEIT TO CELSIUS\n3.CELSIUS TO KELVIN\n4.KELVIN TO CELSIUS\n5.BACK")
                    u=int(input("YOUR CHOICE (DONT WRITE INSTEAD WRITE NUMBER)\n"))
                    if u==1:
                        try:
                            c=float(input("ENTER CELSIUS\n"))
                            R=c*9/5+32
                            print(f"RESULT = {R} FAHRENHEIT\n")
                        except ValueError:
                            print("INVALID ENTER CELSIUS\n")
                            continue
                    elif u==2:
                        try:
                            f=float(input("ENTER FAHRENHEIT\n"))
                            Re=(f-32)*5/9
                            print(f"RESULT = {Re} CELSIUS\n")
                        except ValueError:
                            print("INVALID ENTER FAHRENHEIT\n")
                            continue
                    elif u==3:
                        try:
                            ce=float(input("ENTER CELSIUS\n"))
                            RE=ce+273.15
                            print(f"RESULT = {RE} KELVIN\n")
                        except ValueError:
                            print("INVALID ENTER CELSIUS\n")
                            continue
                    elif u==4:
                        try:
                            k=float(input("ENTER KELVIN\n"))
                            R=k-273.15
                            print(f"RESULT = {R} CELSIUS\n")
                        except ValueError:
                            print("INVALID ENTER KELVIN\n")
                            continue
                    elif u==5:
                        print("BACKING...\n")
                        break
                    else:
                        print("INVALID ENTER CHOICE\n")
                        continue
                except ValueError:
                    print("INVALID INPUT, TRY AGAIN\n")
                    continue
        elif u==4:
            while True:
                try:
                    print("CHOICE\n1.ACRE TO SQUARE METER\n2.SQUARE METER TO ACRE\n3.BACK")
                    u=int(input("YOUR CHOICE(DON'T WRITE INSTEAD WRITE NUMBER)\n"))
                    if u==1:
                        try:
                            a=float(input("ENTER ACRE\n"))
                            RESu=a*4046.86
                            print(f"RESULT = {RESu} SQUARE METER\n")
                        except ValueError:
                            print("INVALID ENTER ACRE\n")
                            continue
                    elif u==2:
                        try:
                            s=float(input("ENTER SQUARE METER\n"))
                            RESU=s/4046.86
                            print(f"RESULT = {RESU} ACRE\n")
                        except ValueError:
                            print("INVALID ENTER SQUARE METER\n")
                            continue
                    elif u==3:
                        print("BACKING...\n")
                        break
                    else:
                        print("INVALID ENTER CHOICE\n")
                        continue
                except ValueError:
                    print("INVALID INPUT, TRY AGAIN\n")
                    continue
        elif u==5:
            while True:
                try:
                    print("CHOOSE\n1.LITER TO GALLON\n2.GALLON TO LITER\n3.BACK")
                    u=int(input("YOUR CHOICE(DONT WRITE INSTEAD WRITE NUMBER)\n"))
                    if u==1:
                        try:
                            l=float(input("ENTER LITER\n"))
                            result=l/3.78541
                            print(f"RESULT = {result} GALLON\n")
                        except ValueError:
                            print("INVALID ENTER LITER\n")
                            continue
                    elif u==2:
                        try:
                            g=float(input("ENTER GALLON\n"))
                            result=g*3.78541
                            print(f"RESULT = {result} LITER\n")
                        except ValueError:
                            print("INVALID ENTER GALLON\n")
                            continue
                    elif u==3:
                        print("BACKING...\n")
                        break
                    else:
                        print("INVALID ENTER CHOICE\n")
                        continue
                except ValueError:
                    print("INVALID INPUT, TRY AGAIN\n")
                    continue
        elif u==6:
            print("OK, THANKS")
            break
        else:
            print("INVALID CHOICE, TRY AGAIN\n")
            continue
    except ValueError:
        print("INVALID INPUT, TRY AGAIN\n")
        continue