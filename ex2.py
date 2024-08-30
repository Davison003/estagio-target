def fibonacci(num_check: int) -> None:
    a = 0
    b = 1
    c = 0
    while c < num_check:
        # print(c)
        c = a + b
        a = b
        b = c

    if c == num_check:
        print("Fibonacci")
    else: print("Não Fibonacci")


fibonacci(int(input("Digite um número: ")))
