prvni_cislo = int(input("vloz prvni cislo: "))
znamenko = input("vloz znak pozadovane matematicke operace (+, -, *, /): ")
druhe_cislo = int(input("vloz druhe coslo: "))

if znamenko == "+":
    print(f"soucet cisel {prvni_cislo} a {druhe_cislo} je {prvni_cislo + druhe_cislo}")
elif znamenko == "-":
    print(f"rozdil cisel {prvni_cislo} a {druhe_cislo} je {prvni_cislo - druhe_cislo}")
elif znamenko == "*":
    print(f"soucin cisel {prvni_cislo} a {druhe_cislo} je {prvni_cislo * druhe_cislo}")
elif znamenko == "/":
    print(f"podil cisel {prvni_cislo} a {druhe_cislo} je {prvni_cislo / druhe_cislo}")
else:
    print(f"zvolil jsi chybnou operaci, program bude ukoncen")
