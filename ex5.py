
# FUNCAO USANDO SLICING
def invert_string(string: str) -> str:
    return string[::-1]


# FUNCAO MANUAL USANDO FOR LOOP
def invert_string_manual(string: str) -> str:
    new_s = ""

    for char in string:
        new_s = char + new_s

    return new_s


print(invert_string_manual(input("Digite uma string: ")))
