# Strings the sliced text file will be stored in
jfkString = ""
parisString = ""
madridString = ""
amsterdamString = ""
cairoString = ""
airportInfo = ""
johnLennonCode = "LPL"
bournemouthCode = "BOH"

# Distance between overseas airport and Liverpool airport
jfkToLpl = 5326
oryToLpl = 629
madToLpl = 1428
amsToLpl = 526
caiToLpl = 3779

# Distance between overseas airport and Liverpool airport
jfkToBoh = 5486
oryToBoh = 379
madToBoh = 1151
amsToBoh = 489
caiToBoh = 3584

distanceBtwUkAndOverseas = 0

ukCode = ""
overseasCode = ""
aircraft = ""

firstClassSeats = -1
aircraftID = 0
standardSeats = 0

aircraftName = ["MEDIUM NARROW BODY", "LARGE NARROW BODY", "MEDIUM WIDE BODY"]

# Stores the data for each aircraft type
aircraftData = [{"RCS" : 8, "MaxFlightRange" : 2650, "CSSC" : 180, "MNFCS" : 8},
                {"RCS" : 7, "MaxFlightRange" : 5600, "CSSC" : 220,"MNFCS" : 10},
                {"RCS" : 5, "MaxFlightRange" : 4050, "CSSC" : 406, "MNFCS" : 14}]

jfkInfo = {}
parisInfo = {}
madridInfo = {}
amsterdamInfo = {}
cairoInfo = {}
 
# Opens the text file
with open("Airports.txt") as f:
    airportInfo = f.readlines()
    airportInfo = [x.strip() for x in airportInfo] 

jfkString = airportInfo[0]
parisString = airportInfo[1]
madridString = airportInfo[2]
amsterdamString = airportInfo[3]
cairoString = airportInfo[4]

# Slices the relavent string and stores it in a dictionary
jfkInfo = {
    "code" : jfkString[0:3],
    "name" : jfkString[4:32],
    "distanceLPL" : jfkString[33:37],
    "distanceBOH" : jfkString[38:]
    }

parisInfo = {
    "code" : parisString[0:3],
    "name" : parisString[4:14],
    "distanceLPL" : parisString[15:18],
    "distanceBOH" : parisString[18:]
    }

madridInfo = {
    "code" : madridString[0:3],
    "name" : madridString[4:32],
    "distanceLPL" : madridString[33:37],
    "distanceBOH" : madridString[38:]
    }

amsterdamInfo = {
    "code" : amsterdamString[0:3],
    "name" : amsterdamString[4:22],
    "distanceLPL" : amsterdamString[23:26],
    "distanceBOH" : amsterdamString[27:]
    }

cairoInfo = {
    "code" : cairoString[0:3],
    "name" : cairoString[4:23],
    "distanceLPL" : cairoString[24:28],
    "distanceBOH" : cairoString[29:]
    }


# Main Menu
def Menu():
    
    try:
        userChoice = int(input("Enter 1 if you want airport details\n2 if you want flight details"
                               "\n3 if you want to calculate profit"
                               "\n4 if you want to clear all data"
                               "\n5 if you want to quit the program\n>>> "))
    except ValueError:
        print("Invalid input. Please enter a number")
        Menu()
        return  # Sends the user back to the menu if they don't enter a number

    if userChoice > 5:  # The user is sent back to the main menu if the enter an invalid digit
        print("Please enter a number in between 1 and 4")
        Menu()
        return

    # Sends user to which ever function the user chooses
    if userChoice == 1:
        AirportDetails()
    elif userChoice == 2:
        FlightDetails()
    elif userChoice == 3:
        CalculateProfits()
    elif userChoice == 4:
        ClearData()
    else:
        print("Quitting program... ")
        quit()  # Quits the program and displays a suitable message


def AirportDetails():

    # Checking if the UK code is valid
    ukCodeInput = input("Enter the three letter airport code for the UK airport\n>>> ")
    global ukCode
    ukCode = ukCodeInput.upper()

    if ukCode == johnLennonCode or ukCode == bournemouthCode:
        overseasCodeInput = input("Please enter the three letter code for the overseas airport\n>>> ")
        global overseasCode
        overseasCode = overseasCodeInput.upper()  # Converts the variable to upper case
        
        # Checking if the overseas code is valid        
        if overseasCode in jfkInfo.values():
            print(jfkInfo.get("name"))
            Menu()  # Displays the full name of the airport that the user entered
        elif overseasCode in parisInfo.values():
            print(parisInfo.get("name"))
            Menu()
        elif overseasCode in madridInfo.values():
            print(madridInfo.get("name"))
            Menu()
        elif overseasCode in amsterdamInfo.values():
            print(amsterdamInfo.get("name"))
            Menu()
        elif overseasCode in cairoInfo.values():
            print(cairoInfo.get("name"))
            Menu()
        else:
            print("The code '" + overseasCode + "' is invalid")
            Menu()  # Sends the user back to the main menu and displays a suitable message if the overseas code is invalid

    else:
        print("The code you entered in invalid")
        Menu()  # Sends the user back to the main menu if UK code is invalid
                
    

# Calculates the details such as number of first class and standard seats
def FlightDetails():

    # Checking the aircraft type
    global aircraftID

    aircraftInput = input("Please enter the type of aircraft being used\n>>> ")
    global aircraft
    aircraft = aircraftInput.upper()  # Converts the variable to upper case

    if aircraft not in aircraftName:  # If "aircraft" isn't in "aircraftName", the user will be sent to the menu
        print("Aircraft type not found")
        Menu()
        return
    
    if aircraft == aircraftName[0]:
        print(aircraftData[0])
        aircraftID = 0  # aircraftID is updated based on which aircraft the user enters
    elif aircraft == aircraftName[1]:
        print(aircraftData[1])
        aircraftID = 1
    else:
        print(aircraftData[2])
        aircraftID = 2

    # Checking the number of first class seats
    global firstClassSeats
    firstClassSeats = int(input("Enter the number of first class seats the aircraft has\n>>> "))

    if firstClassSeats == 0:
        print("The number of seats must be greater than zero")
        Menu()
        return  # If the user enters an invalid digit, they will get sent back to the main menu

    if firstClassSeats < aircraftData[aircraftID]["MNFCS"]:
        print("The number of first class seats is too small")
        Menu()
        return   

    if firstClassSeats > aircraftData[aircraftID]["CSSC"] / 2:
        print("The number of first class seats is too big")
        Menu()
        return
    # If the "Capacity if all seats are standard-class" is smaller than "firstClassSeats"
    # The user is sent to the main menu

    

    # Calculating the number of standard class seats
    global standardSeats
    standardSeats = aircraftData[aircraftID]["CSSC"] - firstClassSeats * 2
    print("There are", standardSeats, "standard seats on this aircraft")
    
    Menu()

def CalculateProfits():

    # Checking if the required information has been entered
    if not ukCode or not overseasCode:
        print("You have not entered the UK Code or the Overseas Code")
        Menu()
        return

    if not aircraft:
        print("You have not entered the aircraft type")
        Menu()
        return

    if firstClassSeats == -1:
        print("You have not entered the number of first class seats")
        Menu()
        return

    # Checking whether or not the distance between the overseas airport and the UK ariport is bigger than the
    # Aircraft's max flight range
    IsDistanceBetweenAirportsTooBig(ukCode, overseasCode)

    # Calculating the flight cost, flight cost per seat, flight income and flight profit
    standardSeatPrice = int(input("Enter the price of a standard class seat\n>>> "))
    firstClassPrice = int(input("Enter the price of a first class seat\n>>> "))

    # Flight cost per seat
    flightCostPerSeat = aircraftData[aircraftID]["RCS"] * distanceBtwUkAndOverseas / 100

    # Flight cost
    flightCost = flightCostPerSeat * (firstClassSeats + standardSeats)
    
    # Flight income
    flightIncome = firstClassSeats * firstClassPrice + standardSeats * standardSeatPrice
    
    # Flight profit
    flightProfit = flightIncome - flightCost
    flightProfitRounded = round(flightProfit, 2)

    # Outputs all relevent information
    print("The flight cost per seat is :", flightCostPerSeat,"\nThe flight cost is :", flightCost,"\nThe flight income is :", flightIncome,"\nThe flight profit is :", flightProfitRounded)

def ClearData():

    # Clearing data that has been collected
    distanceBtwUkAndOverseas = 0
    ukCode = ""
    overseasCode = ""
    aircraft = ""
    firstClassSeats = -1
    aircraftID = 0
    standardSeats = 0 

    print("All data has been cleared")
    Menu()

def IsDistanceBetweenAirportsTooBig(ukAirport, overseasAirport):
    # Checking if the distance between the airports is bigger than the max flight range
    global distanceBtwUkAndOverseas
    
    if ukAirport == "BOH":  # Checks which UK airport the user entered

        if overseasAirport == "JFK":  # Checks which overseas airport the user entered

            if aircraftData[aircraftID]["MaxFlightRange"] < jfkToBoh:  # Checks if the aircraft is suitable for the flight
                print("The airport is too far away for this particular aircraft")
                Menu()  # If not, the user is sent to the main menu
            else:
                distanceBtwUkAndOverseas = jfkToBoh             
                return  # If so, the distanceBtwUkAndOverseas is updated

        elif overseasAirport == "ORY":

            if aircraftData[aircraftID]["MaxFlightRange"] < oryToBoh:
                print("The airport is too far away for this particular aircraft")
                Menu()
            else:
                distanceBtwUkAndOverseas = oryToBoh
                return

        elif overseasAirport == "MAD":

            if aircraftData[aircraftID]["MaxFlightRange"] < madToBoh:
                print("The airport is too far away for this particular aircraft")
                Menu()
            else:
                distanceBtwUkAndOverseas = madToBoh
                return

        elif overseasAirport == "AMS":

            if aircraftData[aircraftID]["MaxFlightRange"] < amsToBoh:
                print("The airport is too far away for this particular aircraft")
                Menu()
            else:
                distanceBtwUkAndOverseas = amsToBoh
                return

        else: 
            if aircraftData[aircraftID]["MaxFlightRange"] < caiToBoh:
                print("The airport is too far away for this particular aircraft")
                Menu()
            else:
                distanceBtwUkAndOverseas = caiToBoh
                return

    else:

        if overseasAirport == "JFK":

            if aircraftData[aircraftID]["MaxFlightRange"] < jfkToLpl:
                print("The airport is too far away for this particular aircraft")
                Menu()
            else:
                distanceBtwUkAndOverseas = jfkToLpl
                return

        elif overseasAirport == "ORY":

            if aircraftData[aircraftID]["MaxFlightRange"] < oryToLpl:
                print("The airport is too far away for this particular aircraft")
                Menu()
            else:
                distanceBtwUkAndOverseas = oryToLpl
                return

        elif overseasAirport == "MAD":

            if aircraftData[aircraftID]["MaxFlightRange"] < madToLpl:
                print("The airport is too far away for this particular aircraft")
                Menu()
            else:
                distanceBtwUkAndOverseas = madToLpl
                return

        elif overseasAirport == "AMS":

            if aircraftData[aircraftID]["MaxFlightRange"] < amsToLpl:
                print("The airport is too far away for this particular aircraft")
                Menu()
            else:
                distanceBtwUkAndOverseas = amsToLpl
                return

        else: 
            if aircraftData[aircraftID]["MaxFlightRange"] < caiToLpl:
                print("The airport is too far away for this particular aircraft")
                Menu()
            else:
                distanceBtwUkAndOverseas = caiToLpl
                return
                
        
Menu()
