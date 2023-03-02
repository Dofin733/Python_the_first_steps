#simplified inputs с помощью f - строка, метод .format и конкатенация

w = 0.2
animal = 'newt'

new_var = f'{w} kg is the weight of the {animal}'
print(new_var) 

new_var = "{} kg is the weight of the {}".format(w, animal)
print(new_var) 


print(str(w) + "kg is the weight of the " + animal) 

