str = input("Input string: ")

def kiem_tra_xau_doi_xung(s):
    return s == s[::-1]

result = kiem_tra_xau_doi_xung(str)

print("True" if result else "False")