import os
os.system("color 09")
xl = 1
lx = 1
ly = 1
xt = 1
tx = 1
ty = 1
xtp = 1
tpx = 1
tpy = 1
px = 1
# Seconds -> Y
def stm(xt):
    return xt / 60
def sth(xt):
    return xt / 3600
def std(xt):
    return xt / 3600 / 24
def stw(xt):
    return xt / 3600 / 24 / 7
#  Minutes -> Y
def mts(xt):
    return xt * 60
def mth(xt):
    return xt / 60
def mtd(xt):
    return xt / 60 / 24
def mtw(xt):
    return xt / 60 / 24 / 7
# Hours -> Y
def hts(xt):
    return xt * 3600
def htm(xt):
    return xt * 60
def htd(xt):
    return xt / 24
def htw(xt):
    return xt / 24 / 7
# Days -> Y
def dts(xt):
    return xt * 24 * 60 * 60
def dtm(xt):
    return xt * 24 * 60
def dth(xt):
    return xt * 24
def dtw(xt):
    return xt / 7
# Weeks -> Y
def wts(xt):
    return xt * 7 * 24 * 3600
def wtm(xt):
    return xt * 7 * 24 * 60
def wth(xt):
    return xt * 7 * 24
def wtd(xt): 
    return xt * 7
# Kilometer -> Y
def kmtmt(xl):
    return xl * 1000
def kmtcm(xl):
    return xl * 100000
def kmtmm(xl):
    return xl * 1e+6
def kmtmi(xl):
    return xl / 1.609
def kmty(xl):
    return xl * 1094
def kmtf(xl):
    return xl * 3281
def kmti(xl):
    return xl * 39370
# Meter -> Y
def mttkm(xl):
    return xl / 1000
def mttcm(xl):
    return xl * 100
def mttmm(xl):
    return xl * 1000
def mttmi(xl):
    return xl / 1609
def mtty(xl):
    return xl * 1.094
def mttf(xl):
    return xl * 3.281
def mtti(xl):
    return xl * 39.37
# Centimeter -> Y
def cmtkm(xl):
    return xl / 100000
def cmtmt(xl):
    return xl / 100
def cmtmm(xl):
    return xl * 10
def cmtmi(xl):
    return xl / 160934
def cmty(xl):
    return xl / 91.44
def cmtf(xl):
    return xl / 30.48
def cmti(xl):
    return xl / 2.54
# Millimeter -> Y
def mmtkm(xl):
    return xl / 1e+6
def mmtmt(xl):
    return xl / 1000
def mmtcm(xl):
    return xl / 10
def mmtmi(xl):
    return xl / 1.609e+6
def mmty(xl):
    return xl / 914
def mmtf(xl):
    return xl / 305
def mmti(xl):
    return xl / 25.4
# Mile -> Y
def mitkm(xl):
    return xl * 1.609
def mitmt(xl):
    return xl * 1609
def mitcm(xl):
    return xl * 160934
def mitmm(xl):
    return xl * 1.609e+6
def mity(xl):
    return xl * 1760
def mitf(xl):
    return xl * 5280
def miti(xl):
    return xl / 63360
# Yard -> Y
def ytkm(xl):
    return xl / 1094
def ytmt(xl):
    return xl / 1.094
def ytcm(xl):
    return xl * 91.44
def ytmm(xl):
    return xl * 914
def ytmi(xl):
    return xl / 1760
def ytf(xl):
    return xl * 3
def yti(xl):
    return xl * 36
# Foot -> Y
def ftkm(xl):
    return xl / 3281
def ftmt(xl):
    return xl / 3.281
def ftcm(xl):
    return xl * 30.48
def ftmm(xl):
    return xl * 305
def ftmi(xl):
    return xl / 5280
def fty(xl):
    return xl / 3
def fti(xl):
    return xl * 12
# Inch -> Y
def itkm(xl):
    return xl / 39370
def itmt(xl):
    return xl / 39.37
def itcm(xl):
    return xl * 2.54
def itmm(xl):
    return xl * 25.4
def itmi(xl):
    return xl / 63360
def ity(xl):
    return xl / 36
def itf(xl):
    return xl / 12
def far(xtp):
    return (float(xtp) / 5) * 9 + 32
def cel(xtp):
    return (float(xtp) - 32) * 5 / 9
def port(px):
    while True:
        print("                     ")
        print("Choose Type of Unit")
        print("1.Time")
        print("2.Length")
        print("3.Temperature")
        px = input("1|2|3 : ")
        if px in ("1", "2", "3"):
            if px == "1":
                calctim(xt, tx, ty)
            elif px == "2":
                calclen(xl, lx, ly)
            elif px == "3":
                calctp(xtp, tpx)
        else:
            print("Invalid Input")
def calclen(xl, lx, ly):
    while True:
        print("                     ")
        print("There Will be 2 inputs, X to Y")
        print("0.Kilometer")
        print("1.Meter")
        print("2.Centimeter")
        print("3.Millimeter")
        print("4.Mile")
        print("5.Yard")
        print("6.Foot")
        print("7.Inch")
        lx = input("0|1|2|3|4|5|6|7 X: ")
        ly = input("0|1|2|3|4|5|6|7 Y: ")
        if lx in ("0", "1", "2", "3", "4", "5", "6", "7"):
            if ly in ("0", "1", "2", "3", "4", "5", "6", "7"):
                try:
                    xl = input("Value of X:")
                    xl = float(xl)
                    if lx == "0" and ly == "0":
                        print("I think you already know the answer to that question is ", xl)
                    elif lx == "0" and ly == "1":
                        print(xl, " Converted to Meter is ", kmtmt(xl))
                        break
                    elif lx == "0" and ly == "2":
                        print(xl, " Converted to Centimeter is ", kmtcm(xl))
                        break
                    elif lx == "0" and ly == "3":
                        print(xl, " Converted to Millimeter is ", kmtmm(xl))
                        break
                    elif lx == "0" and ly == "4":
                        print(xl, " Converted to Mile is ", kmtmi(xl))
                        break
                    elif lx == "0" and ly == "5":
                        print(xl, " Converted to Yard is ", kmty(xl))
                        break
                    elif lx == "0" and ly == "6":
                        print(xl, " Converted to Foot is ", kmtf(xl))
                        break
                    elif lx == "0" and ly == "7":
                        print(xl, " Converted to Inch is ", kmti(xl))
                        break
                    elif lx == "1" and ly == "0":
                        print(xl, " Converted to Kilometer is ", mttkm(xl))
                        break
                    elif lx == "1" and ly == "1":
                        print("I think you already know the answer to that question is ", xl)
                    elif lx == "1" and ly == "2":
                        print(xl, " Converted to Centimeter is ", mttcm(xl))
                        break
                    elif lx == "1" and ly == "3":
                        print(xl, " Converted to Millimeter is ", mttmm(xl))
                        break
                    elif lx == "1" and ly == "4":
                        print(xl, " Converted to Mile is ", mttmi(xl))
                        break
                    elif lx == "1" and ly == "5":
                        print(xl, " Converted to Yard is ", mtty(xl))
                        break
                    elif lx == "1" and ly == "6":
                        print(xl, " Converted to Foot is ", mttf(xl))
                        break
                    elif lx == "1" and ly == "7":
                        print(xl, " Converted to Inch is ", mtti(xl))
                        break
                    elif lx == "2" and ly == "0":
                        print(xl, " Converted to Kilometer is ", cmtkm(xl))
                        break
                    elif lx == "2" and ly == "1":
                        print(xl, " Converted to Meter is ", cmtmt(xl))
                        break
                    elif lx == "2" and ly == "2":
                        print("I think you already know the answer to that question is ", xl)
                    elif lx == "2" and ly == "3":
                        print(xl, " Converted to Millimeter is ", cmtmm(xl))
                        break
                    elif lx == "2" and ly == "4":
                        print(xl, " Converted to Mile is ", cmtmi(xl))
                        break
                    elif lx == "2" and ly == "5":
                        print(xl, " Converted to Yard is ", cmty(xl))
                        break
                    elif lx == "2" and ly == "6":
                        print(xl, " Converted to Foot is ", cmtf(xl))
                        break
                    elif lx == "2" and ly == "7":
                        print(xl, " Converted to Inch is ", cmti(xl))
                        break
                    elif lx == "3" and ly == "0":
                        print(xl, " Converted to Kilometer is ", mmtkm(xl))
                        break
                    elif lx == "3" and ly == "1":
                        print(xl, " Converted to Meter is ", mmtmt(xl))
                        break
                    elif lx == "3" and ly == "2":
                        print(xl, " Converted to Centimeter is ", mmtcm(xl))
                        break
                    elif lx == "3" and ly == "3":
                        print("I think you already know the answer to that question is ", xl)
                    elif lx == "3" and ly == "4":
                        print(xl, " Converted to Mile is ", mmtmi(xl))
                        break
                    elif lx == "3" and ly == "5":
                        print(xl, " Converted to Yard is", mmty(xl))
                        break
                    elif lx == "3" and ly == "6":
                        print(xl, " Converted to Foot is ", mmtf(xl))
                        break
                    elif lx == "3" and ly == "7":
                        print(xl, " Converted to Inch is ", mmti(xl))
                        break
                    elif lx == "4" and ly == "0":
                        print(xl, " Converted to Kilometer is ", mitkm(xl))
                        break
                    elif lx == "4" and ly == "1":
                        print(xl, " Converted to Meter is ", mitmt(xl))
                        break
                    elif lx == "4" and ly == "2":
                        print(xl, " Converted to Centimeter is ", mitcm(xl))
                        break
                    elif lx == "4" and ly == "3":
                        print(xl, " Converted to Millimeter is ", mitmm(xl))
                        break
                    elif lx == "4" and ly == "4":
                        print("I think you already know the answer to that question is ", xl)
                    elif lx == "4" and ly == "5":
                        print(xl, " Converted to Yard is", mity(xl))
                        break
                    elif lx == "4" and ly == "6":
                        print(xl, " Converted to Foot is ", mity(xl))
                        break
                    elif lx == "4" and ly == "7":
                        print(xl, " Converted to Inch is ", miti(xl))
                        break
                    elif lx == "5" and ly == "0":
                        print(xl, " Converted to Kilometer is ", ytkm(xl))
                        break
                    elif lx == "5" and ly == "1":
                        print(xl, " Converted to Meter is ", ytmt(xl))
                        break
                    elif lx == "5" and ly == "2":
                        print(xl, " Converted to Centimeter is ", ytcm(xl))
                        break
                    elif lx == "5" and ly == "3":
                        print(xl, " Converted to Millimeter is ", ytmm(xl))
                        break
                    elif lx == "5" and ly == "4":
                        print(xl, " Converted to Mile is ", ytmi(xl))
                        break
                    elif lx == "5" and ly == "5":
                        print("I think you already know the answer to that question is ", xl)
                    elif lx == "5" and ly == "6":
                        print(xl, " Converted to Foot is ", ytf(xl))
                        break
                    elif lx == "5" and ly == "7":
                        print(xl, " Converted to Inch is ", yti(xl))
                        break
                    elif lx == "6" and ly == "0":
                        print(xl, " Converted to Kilometer is ", ftkm(xl))
                        break
                    elif lx == "6" and ly == "1":
                        print(xl, " Converted to Meter is ", ftmt(xl))
                        break
                    elif lx == "6" and ly == "2":
                        print(xl, " Converted to Centimeter is ", ftcm(xl))
                        break
                    elif lx == "6" and ly == "3":
                        print(xl, " Converted to Millimeter is ", ftmm(xl))
                        break
                    elif lx == "6" and ly == "4":
                        print(xl, " Converted to Mile is ", ftmi(xl))
                        break
                    elif lx == "6" and ly == "5":
                        print(xl, " Converted to Yard is ", fty(xl))
                        break
                    elif lx == "6" and ly == "6":
                        print("I think you already know the answer to that question is ", xl)
                    elif lx == "6" and ly == "7":
                        print(xl, " Converted to Inch is ", fti(xl))
                        break
                    elif lx == "7" and ly == "0":
                        print(xl, " Converted to Kilometer is ", itkm(xl))
                        break
                    elif lx == "7" and ly == "1":
                        print(xl, " Converted to Meter is ", itmt(xl))
                        break
                    elif lx == "7" and ly == "2":
                        print(xl, " Converted to Centimeter is ", itcm(xl))
                        break
                    elif lx == "7" and ly == "3":
                        print(xl, " Converted to Millimeter is ", itmm(xl))
                        break
                    elif lx == "7" and ly == "4":
                        print(xl, " Converted to Mile is ", itmi(xl))
                        break
                    elif lx == "7" and ly == "5":
                        print(xl, " Converted to Yard is ", ity(xl))
                        break
                    elif lx == "7" and ly == "6":
                        print(xl, " Converted to Foot is ", itf(xl))
                        break
                    elif lx == "7" and ly == "7":
                        print("I think you already know the answer to that question is ", xl)
                except ValueError:
                    print("Invalid Input")
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")
def calctim(xt, tx, ty):
    while True:
        print("                             ")
        print("There Will be 2 inputs, X to Y")
        print("1.Seconds")
        print("2.Minutes")
        print("3.Hours")
        print("4.Days")
        print("5.Weeks")
        tx = input("1|2|3|4|5 X: ")
        ty = input("1|2|3|4|5 Y: ")
        if tx in ("1", "2", "3", "4", "5"):
            if ty in ("1", "2", "3", "4", "5"):
                try:
                    xt = input("Value of X: ")
                    xt = float(xt)
                    if tx == "1" and ty == "1":
                        print("I think you already know the answer to that question is ", xt)
                    elif tx == "1" and ty == "2":
                        print(xt, " Converted to Minute is ", stm(xt))
                        break
                    elif tx == "1" and ty == "3":
                        print(xt, " Converted to Hour is ", sth(xt))
                        break
                    elif tx == "1" and ty == "4":
                        print(xt, " Converted to Day is ", std(xt))
                        break
                    elif tx == "1" and ty == "5":
                        print(xt, " Converted to Week is ", stw(xt))
                        break
                    elif tx == "2" and ty == "1":
                        print(xt, " Converted to Second is ", mts(xt))
                        break
                    elif tx == "2" and ty == "2":
                        print("I think you already know the answer to that question is ", xt)
                    elif tx == "2" and ty == "3":
                        print(xt, " Converted to Hour is ", mth(xt))
                        break
                    elif tx == "2" and ty == "4":
                        print(xt, " Converted to Day is ", mtd(xt))
                        break
                    elif tx == "2" and ty == "5":
                        print(xt, " Converted to Week is ", mtw(xt))
                        break
                    elif tx == "3" and ty == "1":
                        print(xt, " Converted to Second is ", hts(xt))
                        break
                    elif tx == "3" and ty == "2":
                        print(xt, " Converted to Minute is ", htm(xt))
                        break
                    elif tx == "3" and ty == "3":
                        print("I think you already know the answer to that question is ", xt)
                        break
                    elif tx == "3" and ty == "4":
                        print(xt, " Converted to Day is ", htd(xt))
                        break
                    elif tx == "3" and ty == "5": 
                        print(xt, " Converted to Week is ", htw(xt))
                        break
                    elif tx == "4" and ty == "1":
                        print(xt, " Converted to Second is ", dts(xt))
                        break
                    elif tx == "4" and ty == "2":
                        print(xt, " Converted to Minute is ", dtm(xt))
                        break
                    elif tx == "4" and ty == "3":
                        print(xt, " Converted to Hour is ", dth(xt))
                        break
                    elif tx == "4" and ty == "4":
                        print("I think you already know the answer to that question is ", xt)
                    elif tx == "4" and ty == "5":
                        print(xt, " Converted to Week is ", dtw(xt))
                        break
                    elif tx == "5" and ty == "1":
                        print(xt, " Converted to Second is ", wts(xt))
                        break
                    elif tx == "5" and ty == "2":
                        print(xt, " Converted to Minute is ", wtm(xt))
                        break
                    elif tx == "5" and ty == "3":
                        print(xt, " Converted to Hour is ", wth(xt))
                        break
                    elif tx == "5" and ty == "4":
                        print(xt, " Converted to Day is ", wtd(xt))
                        break
                    elif tx == "5" and ty == "5":
                        print("I think you already know the answer to that question is ", xt)
                except ValueError:
                    print("Invalid Input")        
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")
def calctp(xtp, tpx):
    while True:
        print("                             ")
        print("1.Fahrenheit -> Celsius")
        print("2.Fahrenheit <- Celsius")
        tpx = input("1|2: ")

        if tpx in ("1", "2"):
            xtp = input("Starting Temp: ")
            try:
                xtp = float(xtp)
                if tpx == "1":
                    print(xtp, "converted to Celsius is ", cel(xtp))
                    break 
                elif tpx == "2":
                    print(xtp, "converted to Fahrenheit is ", far(xtp))
                    break
                else:
                    print("Invalid Input")
            except ValueError:
                print("Invalid Input")
while True:
    port(px)