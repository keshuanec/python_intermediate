#Napište dekorátor @with_password. Funkce, které tento dekorátor mají, se vykonají pouze,
#pokud uživatel správně zadá heslo (využijte input()).

def with_password(func):
    def password_check():
        password = "prase"
        if input("vlozte heslo: ") == password:
            return func
        else:
            print("zadal jste nespravne heslo")
    return password_check()

@with_password
def soucet(a,b):
    return a + b



print(soucet(3,5))