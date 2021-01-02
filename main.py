# Словари

d = {'test': 1, 'test_2': "tes"}
print(d)

a = dict(short='dict', longer='dictionary')
a['short'] = 234
print(a)

b = dict([(23, 34), (56, 87)])
print(b)

c = dict.fromkeys(['a', 'b'], 1)
print(c)

e = {a: a ** 2 for a in range(7)}
print(e)

person = {'name': {'last_name': 'Ivan', 'first_name': 'Ivan',
                   'middle_name': 'Ivanovich'}, 'address': ['city Andreyshkin',
                                                            'st. Vasilkovskaya house 236',
                                                            'ap.12'],
          'phone': {'home_phone': '237-94-88', 'mobile_phone': '8-922-000-85-61',
                    'mobile_phone2': 'No'
                    }}
print(person['phone']['mobile_phone2'])

# person.clear()
# print(person)
