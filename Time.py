from datetime import datetime 
import time ,os
os.system("cls")

sys_date=time.localtime()
sys_year_miladi=int(sys_date[0] )


def gregorian_to_jalali(gy, gm, gd):
    g_d_m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (gy % 4 == 0 and gy % 100 != 0) or (gy % 400 == 0):
        g_d_m[1] = 29  # اصلاح برای سال کبیسه

    gy -= 1600
    gm -= 1
    gd -= 1

    g_day_no = 365 * gy + (gy // 4) - (gy // 100) + (gy // 400) + 1  # اضافه کردن ۱ روز
    for i in range(gm):
        g_day_no += g_d_m[i]
    g_day_no += gd

    j_day_no = g_day_no - 79
    j_np = j_day_no // 12053
    j_day_no %= 12053

    jy = 979 + 33 * j_np + 4 * (j_day_no // 1461)
    j_day_no %= 1461

    if j_day_no >= 366:
        jy += (j_day_no - 1) // 365
        j_day_no = (j_day_no - 1) % 365

    jm = 0
    days_in_j_month = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]
    while j_day_no >= days_in_j_month[jm]:
        j_day_no -= days_in_j_month[jm]
        jm += 1

    jd = j_day_no + 1  # اینجا مقدار دقیق تنظیم شده است
    return jy, jm + 1, jd #خروجی سال ماه روز شمسی

now = datetime.now()#تاریخ سیستم
gy, gm, gd = now.year, now.month, now.day
jy, jm, jd = gregorian_to_jalali(gy, gm, gd)# تبدیل به تاریخ شمسی
sys_year_miladi_to_shamsi=jy #سال شمسی
# print(F'{jy}/{jm}/{jd}') #سال ماه روز شمسی


print("_" *20)
while True:
    first_entry = (input('1: Convert Solar date to gregorian date. 2: Convert gregorian date Solar date: '))
    list_entry = [1,2]
    if first_entry.isdigit():
        entry = int(first_entry)
        if entry in list_entry:
            if entry == 1:
                print("_" *20)
                def deta_user():
                    while True:
                        print(" " *14, "SHAMSI TO MILADI")
                        print("_" *45)
                        print(f'len 8 > {13450102} >> 1345/01/02 >>> 1966/03/22')
                        print(f'len 6 > {134512:8} >> 1345/01/02 >>> 1966/03/22')
                        print(f'len 7 > {1345012:8} >> 1345/01/02 >>> 1966/03/22')
                        print(f'len 7 > {1345102:8} >> 1345/10/02 >>> 1966/03/22')
                        print("_" *20)
                        user = (input("Enter your Solar 'Shamsi' date number only "))
                        if user.isdigit():
                            user_str = user
                            len_user = len(str(user))
                            if 6 <= len_user < 9:
                                user_str = str(user)
                                if len_user == 8:
                                    print("_" *20)
                                    day = int(user_str[6:])
                                    moon = int(user_str[4:6])
                                    year = int(user_str[:4])
                                    if moon in [1,2,3,4,5,6]:
                                        if (1 <= day <= 31) and (1 <= moon <= 6) and (1 <= year <= sys_year_miladi_to_shamsi):
                                            return(user_str[:4] + "/" + user_str[4:6] + '/' + user_str[6:])
                                    elif moon in [7,8,9,10,11]:
                                        if (1 <= day <= 30) and (7 <= moon <= 11) and (1 <= year <= sys_year_miladi_to_shamsi):
                                            return(user_str[:4] + "/" + user_str[4:6] + '/' + user_str[6:])
                                    else:
                                        if (1 <= day <= 29) and (12 <= moon <= 12) and (1 <= year <= sys_year_miladi_to_shamsi):
                                            return(user_str[:4] + "/" + user_str[4:6] + '/' + user_str[6:]) 
                                elif len_user == 6:
                                    print("_" *20)
                                    day = int(user_str[5:])
                                    moon = int(user_str[4:5])
                                    year = int(user_str[:4])
                                    if 1 <= day <=9 and 1 <= moon <= 9 and 1 <= year <= sys_year_miladi_to_shamsi:
                                        return(f'{year:04}/{moon:02}/{day:02}')
                                else:
                                    print("_" *20)
                                    index_user = int(user_str[4:5])
                                    if index_user == 0:
                                        day = int(user_str[6:])
                                        moon = int(user_str[4:6])
                                        year = int(user_str[:4])
                                        if (moon != 0) and (1 <= year <= sys_year_miladi_to_shamsi):
                                            return(f'{year:04}/{moon:02}/{day:02}')
                                    else:
                                        index_user = int(user_str[5])
                                        if index_user == 0:
                                            day = int(user_str[6])
                                            moon = int(user_str[4:6])
                                            year = int(user_str[:4])
                                            if (moon == 10) and (1 <= year <= sys_year_miladi_to_shamsi):
                                                return(f'{year:04}/{moon:02}/{day:02}')
                                        else:
                                            day = int(user_str[5:])
                                            moon = int(user_str[4:5])
                                            year = int(user_str[:4])
                                            if  (1 <= day <=31) and (1 <= year <= sys_year_miladi_to_shamsi):
                                                return(f'{year:4}/{moon:02}/{day:02}')
                            else:
                                print("_" *20)               
                        else:
                            print("_" *20)
                            pass
                deta_shams = deta_user()# شمسی
                deta_shams1 = "".join(deta_shams.split("/")) # حذف "/"
                def shamsi_to_miladi(jy1,jm1,jd1):
                    jy = int(jy1)
                    jm = int(jm1)
                    jd = int(jd1)
                    gy = jy + 621
                    is_shamsi_leap = (jy % 4 == 3)
                    start_march = 20 if is_shamsi_leap else 21
                    days_in_shamsi_months = [31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]
                    elapsed_days = sum(days_in_shamsi_months[:jm -1]) + jd
                    days_in_miladi_months= [31,29 if (gy % 4 == 0 
                                                      and (gy % 100 != 0 or  gy % 400 == 0)) 
                                                      else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                    miladi_day = start_march
                    miladi_month = 3
                    while elapsed_days > 0:
                        if elapsed_days <= (days_in_miladi_months[miladi_month -1] - miladi_day):
                            miladi_day += elapsed_days
                            break
                        else:
                            elapsed_days -= (days_in_miladi_months[miladi_month -1] - miladi_day + 1)
                            miladi_day = 1
                            miladi_month += 1
                            if miladi_month > 12:
                                miladi_month = 1
                                gy += 1
                    return gy, miladi_month, miladi_day
                def day_moon_year(deta_shams1):
                    day1 = (deta_shams1[6:])
                    moon1 = (deta_shams1[4:6])
                    year1 = (deta_shams1[:4])
                    sh_to_mi = shamsi_to_miladi(year1, moon1, day1)
                    date_miladi = f'{sh_to_mi[0]:04}/{sh_to_mi[1]:02}/{sh_to_mi[2]:02}'
                    return date_miladi
                date_miladi1 = day_moon_year(deta_shams1)
                print(f'date shamsi {deta_shams} to date miladi {date_miladi1}')
                print("_" *20)
            elif entry == 2:
                print("_" *20)
                def deta_user11():
                    while True:
                        print(" " *14, "MILADI TO SHAMSI")
                        print("_" *45)
                        print(f'len 8 > {19450102} >> 1945/01/02 >>> 1323/10/12')
                        print(f'len 6 > {194512:8} >> 1945/01/02 >>> 1323/10/12')
                        print(f'len 7 > {1945012:8} >> 1945/01/02 >>> 1323/10/12')
                        print(f'len 7 > {1945102:8} >> 1945/10/02 >>> 1323/10/12')
                        print("_" *20)
                        user = (input("Enter your Miladi 'Gergorian' date number only "))
                        if user.isdigit():
                            user_str = user
                            len_user = len(str(user))
                            if 6 <= len_user < 9:
                                user_str = str(user)
                                year_user =user_str[:4]
                                if int(year_user) <= sys_year_miladi:
                                    if len_user == 8:
                                        print("_" *20)
                                        day = int(user_str[6:])
                                        moon = int(user_str[4:6])
                                        year = int(user_str[:4])
                                        moon_31 =[1, 3, 5, 7, 8, 10, 12]
                                        moon_30 =[4, 6, 9, 11]
                                        if moon in moon_31:
                                            if (1<= day <=31) and (moon in moon_31) and  (1 <= year <= sys_year_miladi):
                                                return(user_str[:4] + "/" + user_str[4:6] + '/' + user_str[6:])
                                            else:
                                                return(day, moon, year)
                                        if moon in moon_30:
                                            if (1<= day <=30) and (moon in moon_30) and  (1 <= year <= sys_year_miladi):
                                                return(user_str[:4] + "/" + user_str[4:6] + '/' + user_str[6:])
                                        else:
                                            if (1<= day <=28) and (moon == 2) and  (1 <= year <= sys_year_miladi):
                                                return(user_str[:4] + "/" + user_str[4:6] + '/' + user_str[6:])
                                    elif len_user == 6:
                                        print("_" *20)
                                        day = int(user_str[5:])
                                        moon = int(user_str[4:5])
                                        year = int(user_str[:4])
                                        if 1 <= day <=9 and 1 <= moon <= 9 and 1 <= year <= sys_year_miladi:
                                            return(f'{year:04}/{moon:02}/{day:02}')
                                    else:
                                        print("_" *20)
                                        index_user = int(user_str[4:5])
                                        if index_user == 0:
                                            day = int(user_str[6:])
                                            moon = int(user_str[4:6])
                                            year = int(user_str[:4])
                                            if (moon != 0) and 1 <= year <= sys_year_miladi:
                                                return(f'{year:04}/{moon:02}/{day:02}')
                                        else:
                                            index_user = int(user_str[5])
                                            if index_user == 0:
                                                day = int(user_str[6])
                                                moon = int(user_str[4:6])
                                                year = int(user_str[:4])
                                                if (moon == 10) and 1 <= year <= sys_year_miladi:
                                                    return(f'{year:04}/{moon:02}/{day:02}')
                                            else:
                                                day = int(user_str[5:])
                                                moon = int(user_str[4:5])
                                                year = int(user_str[:4])
                                                if  (1 <= day <=31) and 1 <= year < sys_year_miladi:
                                                    return(f'{year:04}/{moon:02}/{day:02}')
                                else:
                                    print("_" *20)                
                            else:
                                print("_" *20)
                                pass 
                date_miladiz = (deta_user11())#

                date_miladi22 = "".join(date_miladiz.split("/"))
                # print(date_miladi22)
                date_shamsi = date_miladi22
                def shamsi_to_miladi(year, month, day):
                    year2 = int(year)
                    month2 = int(month)
                    day2 = int(day)
                    g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

                    days = 355666 + (365 * year2) + ((year2 + 3) // 4)  
                    - ((year2 + 99) // 100) + ((year2 + 399) // 400) + day2 + g_d_m[month2 -1] #کل روز

                    jy =- 1595 + (33 * (days // 12053)) #سال شمسی
                    days %= 12053
                    jy += (4 * (days // 1461))
                    days %= 1461

                    if days > 365:
                        jy += (days -1) // 365
                        days = (days -1) % 365

                    if days < 186:
                        jm = 1 + (days // 31)
                        jd = 1 + (days % 31)
                    else:
                        jm = 7 + ((days - 186) // 30)
                        jd = 1 + ((days - 186) % 30)

                    return jy, jm, jd
                def convert_date(date_shamsi):
                    year = date_shamsi[:4]
                    month = date_shamsi[4:6]
                    day = date_shamsi[6:8]

                    sh_to_mi = shamsi_to_miladi(year, month, day)

                    date_shamsi = f"{sh_to_mi[0]:04d}/{sh_to_mi[1]:02d}/{sh_to_mi[2]:02d}"
                    return date_shamsi
                date_miladi = convert_date(date_shamsi)
                print(f'date shamsi {date_miladiz} to date miladi {date_miladi}')
                print("_" *20)