def main():
    a, b = map(int, input("Введите числа(example: '24 2'): ").split())

    print(f"НОД для чисел {a} and {b} = ", end="")

    if a != b:
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        print(a + b)
    else:
        print(a)
main()