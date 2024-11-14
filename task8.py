#Napište dekorátor @with_password. Funkce, které tento dekorátor mají, se vykonají pouze,
#pokud uživatel správně zadá heslo (využijte input()).

print("test")
def with_password(func):
    password = "prase"
    if input("vlozte heslo") == password:
        return func
    else:
        print("zadal jste nespravne heslo")


@with_password
def soucet(a,b):
    return a + b



print(soucet(3,5))