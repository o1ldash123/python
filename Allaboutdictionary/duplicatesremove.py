student_data = {
    'id1': {'name': 'Alice', 'age': 20, 'grade': 'A' ,'class': 'V'},
    'id2': {'name': 'Ari', 'age': 14, 'grade': 'A'  ,'class': 'V'} ,
    'id3': {'name': 'John', 'age': 15, 'grade': 'A' ,'class': 'V'},
    'id4': {'name': 'Elliot', 'age': 18, 'grade': 'A' ,'class': 'V'} ,
    'id5': {'name': 'John', 'age': 15, 'grade': 'A' ,'class': 'V'}
}  

result = {
}

for key , value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)


