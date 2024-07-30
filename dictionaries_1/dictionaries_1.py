a = (input("Введите имя питомца "))
pets = {
	a : {
		'Вид питомца' : ' ',
		'Возраст питомца' : ' ',
		'Имя владельца' : ' '
	}
}
pets['Вид питомца'] = input('Введите вид питомца ' )	
pets['Возраст питомца'] = int(input('Введите возраст питомца '))
pets['Имя владельца'] = input('Введите имя владельца ' )
vid = list(pets.values())[1]
vid1 = list(pets.values())[2]
vid2 = list(pets.values())[3]
years = ()
if (vid1 >= 5 and vid1 <= 20) or (vid1 >= 25 and vid1 <= 35):
	years = "лет"
elif (vid1 >= 2 and vid1 <= 4):
	years = "года"
else:
	years = "год"
print(f"Это {vid} по кличке \"{a}\". Возраст питомца: {vid1} {years}. Имя владельца: {vid2}")