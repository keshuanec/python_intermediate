# #Napište dekorátor @with_password. Funkce, které tento dekorátor mají, se vykonají pouze,
# #pokud uživatel správně zadá heslo (využijte input()).
#
# def with_password(func):
#     password = "prase"
#     if input("vlozte heslo: ") == password:
#         return func
#     else:
#         return "wrong_password"
#


#


def with_password(func):
    def pass_protected(*args, **kwargs):
        password = "prase"
        if input(f"vlozte heslo pro funkci \"{func.__name__}\": ") == password:
            return f"vysledek volani funkce \"{func.__name__}\" je: {func(*args, **kwargs)}"
        else:
            return f"Pro funkci \"{func.__name__}\" bylo zadano Špatné heslo"
    return pass_protected

@with_password
def soucetAB(a,b):
    return a + b

@with_password
def soucetABC(a,b,c):
    return a+b+c

@with_password
def soucet_all(*args):
    soucet = 0
    for i in args:
        soucet += i
    return soucet




print(soucetAB(3,5))
print(soucetABC(3,4,5))
print(soucet_all(5,2,4,3,4,8,5))