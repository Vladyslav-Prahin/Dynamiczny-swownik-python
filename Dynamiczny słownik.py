definicje = {}





while 1 ==1:
    print("1: Dodaj definicję")
    print("2: Szukaj definicję")
    print("3: Usuń definicję")
    print("4: Zakończ")
    
    wybor = input("Co chcesz zrobić? ")
    if (wybor == "1"):
        klucze =input("Podaj słowo do zdefiniowania: ")
        definicja = input("Podaj definicję: ")
        definicje[klucze] = definicja
        print(definicje)
    elif (wybor == "2"):
        klucz = input("Jakiej definicji szukasz? ")
        if klucz in definicje:
            print(definicje[klucz])
        else:
            print("Takiej definicji nie ma")
    elif (wybor == "3"):
        klucz = input("Jaką definicję chcesz usunąć? ")
        if klucz in definicje:
            del(definicje[klucz])
            print("Usunięta")
        else:
            print("Definicji o nazwie", klucz, "Nie ms")
    elif (wybor == "4"):
        print("No to pa")
        break
    else:
        print("Podana zła wartość!")
