# Uzraksti programmu, kurā  dators izvēlas 100 skaitļus robežās no 101 līdz 500. Izvēlētie skaitļi tiek izvadīti terminālī.

import random

for i in range(100):
    random_skaitlis=random.randint(101,500)
    print(random_skaitlis)
