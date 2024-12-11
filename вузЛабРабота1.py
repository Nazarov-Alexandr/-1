def f(numbers, aim, current_summ=0, result=''):
    if not numbers:
        if current_summ == aim:
            return result + "=" + str(aim)
        else:
            return "No solution"
    a = f(numbers[1:], aim, current_summ + numbers[0], f"{result}+{numbers[0]}")
    if a != "No solution":
        return a
    b = f(numbers[1:], aim, current_summ - numbers[0], f"{result}-{numbers[0]}")
    if b != "No solution":
        return b
    return "No solution"


if __name__ == "__main__":
    with open("input.txt") as file:
        inp = file.read()
    inp = list(map(int, inp.split()))
    N = inp[0]
    x = inp[1:-1]
    S = inp[-1]
    print(N, x, S)
    if N == len(x):
        c = f(x, S)
        if c[0] == "+":
            c = c[1:]
            print(c)
        with open("output.txt", "w") as file:
            inp = file.write(c)
    else:
        print("Не корректные входные данные")
        exit(1)
