def totalCalc(billAmount , tipPerc) :
    total = billAmount * ( 1 + 0.01 * tipPerc)
    total = round(total, 2)
    print(f"Please pay ${total}")

totalCalc(10000 , 20)