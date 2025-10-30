SPCMcountryCode = {
    'India' : '0091' ,
    'USA' : '001',
    'Canada' : '0130',
}

print('Country code for India -')
print(SPCMcountryCode.get('India' , 'Not Found'))

print('Country code for UK -')
print(SPCMcountryCode.get('USA' , 'Not Found'))