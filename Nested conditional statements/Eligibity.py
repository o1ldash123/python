medicalCause = input('did you have a medical cause Y or N:  ')

atten = int(input('enteer the attendance of the student: '))

if medicalCause == 'Y' :
    print('You are not allowed')
else:
    if atten >= 75 :
        print('Allowed')
    else:
        print('Not allowed')