Cena_za_kg_konfet = float(input("Vvedite cenu za 1 kg: "))
for i in range(1, 11):
    cost = i * Cena_za_kg_konfet
    print(f"{i} kilogram konfet stoit {cost}")