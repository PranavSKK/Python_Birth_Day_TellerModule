date=int(input("enter your birth date\n"))
month_inp=input("enter your birth month\n")
year=(input("enter your birth year\n"))
month=(month_inp[0:3]).lower()
check1=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
check2=['1','2','3','4','5','6','7','8','9','10','11','12','01','02','03','04','05','06','07','08','09']
s=4
y=year[2:]
int_year=int(year)
if (len(year)==4 and date<=31 and month in check1) or (len(year)==4 and date<=31 and month_inp in check2):
    if month=='jan' or month_inp=='1' or month_inp=='01':
        m=0
    elif month=='feb' or month_inp=='2' or month_inp=='02':
        m=3
    elif month=='mar' or month_inp=='3' or month_inp=='03':
        m=3
    elif month=='apr' or month_inp=='4' or month_inp=='04':
        m=6
    elif month=='may' or month_inp=='5' or month_inp=='05':
        m=1
    elif month=='jun' or month_inp=='6' or month_inp=='06':
        m=4
    elif month=='jul' or month_inp=='7' or month_inp=='07':
        m=6
    elif month=='aug' or month_inp=='8' or month_inp=='08':
        m=2
    elif month=='sep' or month_inp=='9' or month_inp=='09':
        m=5
    elif month=='oct' or month_inp=='10':
        m=0
    elif month=='nov' or month_inp=='11':
        m=3
    elif month=='dec' or month_inp=='12':
        m=5                    
    if 1600<=int_year<=1699 :
        quot,rem=divmod(int(y),s)
        sum=(quot+date+m+6+int(y))
      
        if(int_year%4==0 and int_year%100!=0 or int_year%400==0):
            if(month=='jan' or month=='feb'):
                if sum%7==0:
                    print("saturday")
                elif sum%7==1:
                    print("sunday")
                elif sum%7==2:
                    print("monday")
                elif sum%7==3:
                    print("tuesday")
                elif sum%7==4:
                    print("wednesday")
                elif sum%7==5:
                    print("thursday")
                elif sum%7==6:
                    print("friday")

            else:
                if sum%7==0:
                    print("sunday")
                elif sum%7==1:
                    print("monday")
                elif sum%7==2:
                    print("tuesday")
                elif sum%7==3:
                    print("wednesday")
                elif sum%7==4:
                    print("thursday")
                elif sum%7==5:
                    print("friday")
                elif sum%7==6:
                    print("saturday")

        else:
            if sum%7==0:
                print("sunday")
            elif sum%7==1:
                print("monday")
            elif sum%7==2:
                print("tuesday")
            elif sum%7==3:
                print("wednesday")
            elif sum%7==4:
                print("thursday")
            elif sum%7==5:
                print("friday")
            elif sum%7==6:
                print("saturday")
    if 1700<=int_year<=1799 :
            quot,rem=divmod(int(y),s)
            sum=(quot+date+m+4+int(y))
            if(int_year%4==0 and int_year%100!=0 or int_year%400==0):
                if(month=='jan' or month=='feb'):
                    if sum%7==0:
                        print("saturday")
                    elif sum%7==1:
                        print("sunday")
                    elif sum%7==2:
                        print("monday")
                    elif sum%7==3:
                        print("tuesday")
                    elif sum%7==4:
                        print("wednesday")
                    elif sum%7==5:
                        print("thursday")
                    elif sum%7==6:
                        print("friday")

                else:
                    if sum%7==0:
                        print("sunday")
                    elif sum%7==1:
                        print("monday")
                    elif sum%7==2:
                        print("tuesday")
                    elif sum%7==3:
                        print("wednesday")
                    elif sum%7==4:
                        print("thursday")
                    elif sum%7==5:
                        print("friday")
                    elif sum%7==6:
                        print("saturday")

            else:
                if sum%7==0:
                    print("sunday")
                elif sum%7==1:
                    print("monday")
                elif sum%7==2:
                    print("tuesday")
                elif sum%7==3:
                    print("wednesday")
                elif sum%7==4:
                    print("thursday")
                elif sum%7==5:
                    print("friday")
                elif sum%7==6:
                    print("saturday")
    if 1800<=int_year<=1899 :
        quot,rem=divmod(int(y),s)
        sum=(quot+date+m+2+int(y))
        if(int_year%4==0 and int_year%100!=0 or int_year%400==0):
            if(month=='jan' or month=='feb'):
                if sum%7==0:
                    print("saturday")
                elif sum%7==1:
                    print("sunday")
                elif sum%7==2:
                    print("monday")
                elif sum%7==3:
                    print("tuesday")
                elif sum%7==4:
                    print("wednesday")
                elif sum%7==5:
                    print("thursday")
                elif sum%7==6:
                    print("friday")

            else:
                if sum%7==0:
                    print("sunday")
                elif sum%7==1:
                    print("monday")
                elif sum%7==2:
                    print("tuesday")
                elif sum%7==3:
                    print("wednesday")
                elif sum%7==4:
                    print("thursday")
                elif sum%7==5:
                    print("friday")
                elif sum%7==6:
                    print("saturday")

        else:
            if sum%7==0:
                print("sunday")
            elif sum%7==1:
                print("monday")
            elif sum%7==2:
                print("tuesday")
            elif sum%7==3:
                print("wednesday")
            elif sum%7==4:
                print("thursday")
            elif sum%7==5:
                print("friday")
            elif sum%7==6:
                print("saturday")           
    if 1900<=int_year<=1999 :
        quot,rem=divmod(int(y),s)
        sum=(quot+date+m+0+int(y))
        if(int_year%4==0 and int_year%100!=0 or int_year%400==0):
            if(month=='jan' or month=='feb'):
                if sum%7==0:
                    print("saturday")
                elif sum%7==1:
                    print("sunday")
                elif sum%7==2:
                    print("monday")
                elif sum%7==3:
                    print("tuesday")
                elif sum%7==4:
                    print("wednesday")
                elif sum%7==5:
                    print("thursday")
                elif sum%7==6:
                    print("friday")

            else:
                if sum%7==0:
                    print("sunday")
                elif sum%7==1:
                    print("monday")
                elif sum%7==2:
                    print("tuesday")
                elif sum%7==3:
                    print("wednesday")
                elif sum%7==4:
                    print("thursday")
                elif sum%7==5:
                    print("friday")
                elif sum%7==6:
                    print("saturday")

        else:
            if sum%7==0:
                print("sunday")
            elif sum%7==1:
                print("monday")
            elif sum%7==2:
                print("tuesday")
            elif sum%7==3:
                print("wednesday")
            elif sum%7==4:
                print("thursday")
            elif sum%7==5:
                print("friday")
            elif sum%7==6:
                print("saturday")            
    if 2000<=int_year<=2099 :
        quot,rem=divmod(int(y),s)
        sum=(quot+date+m+6+int(y))
        if(int_year%4==0 and int_year%100!=0 or int_year%400==0):
            if(month=='jan' or month=='feb'):
                if sum%7==0:
                    print("saturday")
                elif sum%7==1:
                    print("sunday")
                elif sum%7==2:
                    print("monday")
                elif sum%7==3:
                    print("tuesday")
                elif sum%7==4:
                    print("wednesday")
                elif sum%7==5:
                    print("thursday")
                elif sum%7==6:
                    print("friday")

            else:
                if sum%7==0:
                    print("sunday")
                elif sum%7==1:
                    print("monday")
                elif sum%7==2:
                    print("tuesday")
                elif sum%7==3:
                    print("wednesday")
                elif sum%7==4:
                    print("thursday")
                elif sum%7==5:
                    print("friday")
                elif sum%7==6:
                    print("saturday")

        else:
            if sum%7==0:
                print("sunday")
            elif sum%7==1:
                print("monday")
            elif sum%7==2:
                print("tuesday")
            elif sum%7==3:
                print("wednesday")
            elif sum%7==4:
                print("thursday")
            elif sum%7==5:
                print("friday")
            elif sum%7==6:
                print("saturday")
else:
    print("invalid Input's")


