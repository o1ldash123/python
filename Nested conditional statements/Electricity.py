units = int(input('please enter Number of units you consumed:-  '))
  

if(units < 50) :
    amount = units * 2.60
    surCharge = 25

elif(units <=100) :
    amount = 130 + ((units - 50) * 3.25)
    surCharge = 35

elif (units <= 200) :
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surCharge = 75

    total = amount + surCharge
    print('\nElectricity BILL = %.2F' %total)