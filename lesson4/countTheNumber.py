Amount = int(input('please enter amount for withdraw'))
note_1 = Amount//100
note_2 = (Amount%100)//5
note_3 = ((Amount%100)%50)//10

print('There are three notes . \n The following are ' ,'note1- $100', note_1 ,'note2-$50 ', note_2 ,'note3-$40 ' , note_3)