import random
random_int=random.randint(1,10)
print(f"Random integer between 1 and 10:{random_int}")

#
random_float=random.random()
print(f"Random float between 0 and 1:{random_float}")


#
items=[1,2,3,4,5]
random.shuffle(items)
print(f"Shuffeled list:{items}")
