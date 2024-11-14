# #Napište dekorátor @with_password. Funkce, které tento dekorátor mají, se vykonají pouze,
# #pokud uživatel správně zadá heslo (využijte input()).
#
# def with_password(func):
#     password = "prase"
#     if input("vlozte heslo: ") == password:
#         return func
#     else:
#         return wrong_password
#
# def wrong_password(a,b):
#     return f"spatne heslo"
#
#
# @with_password
# def soucet(a,b):
#     return a + b
#
#
#
#
#
# print(soucet(3,5))


def with_password(func):
    def novy_soucet(a, b):
        password = "zirafa"
        if input("vlozte heslo: ") == password:
            return func(a, b)
        else:
            return "Špatné heslo"
    return novy_soucet

@with_password
def soucet(a,b):
    return a + b

print(soucet(3,5))
