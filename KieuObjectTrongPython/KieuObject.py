users = {}
account = {
    'username': 'XuanHoai',
    'password': '848028',
    'age': 25
}

# Truy xuất age = 25 và truy xuất username = 'XuanHoai'
print(account['age'])
print(account['username'])

account['test'] = 'Test'
print(account.values())
print(account.keys())

for i in account.values():
    print(i)

if 'age' not in account.keys():
    print('Không có')
else:
    print('Có')
