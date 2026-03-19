txt = ["niba", "nima", "hiba"]
name = input("Enter a name: ")

for x in txt:
    print(x)
    if x == name:
        print("Match mil gaya!")
    else:
        print("Match nhi mil gya!")
        break