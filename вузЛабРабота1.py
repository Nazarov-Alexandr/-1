def f(numbers, aim, current_summ=0, result=''):
    if not numbers:
        # проверка на то, что были использованы все числа и дальнейшая проверка
        # на соответствие получившегося результата с целью
        if current_summ == aim:
            return result + "=" + str(aim)
        else:
            return "No solution"
    a = f(numbers[1:], aim, current_summ + numbers[0], f"{result}+{numbers[0]}")  # запуск рекурсии с числом, которое имеет положительный знак
    if a != "No solution":
        # выбор наиболее подходящего варианта числа с положительным знаком
        return a
    b = f(numbers[1:], aim, current_summ - numbers[0], f"{result}-{numbers[0]}")  # запуск рекурсии с числом, которое имеет отрицательный знак
    if b != "No solution":
        # выбор наиболее подходящего варианта числа с отрицательным знаком
        return b
    return "No solution"


if __name__ == "__main__":
    with open("input.txt") as file:
        inp = file.read()
    inp = list(map(int, inp.split()))  # занесение чисел в отдельный список
    N = inp[0]  # количество чисел
    x = inp[1:-1]  # заданные числа
    S = inp[-1]  # ожидаемый результат
    print(N, x, S)
    if N == len(x):
        # поиск решения
        c = f(x, S)
        if c[0] == "+":
            # если выражение начинается со знака "+", то его необходимо убрать
            c = c[1:]
            print(c)
        with open("output.txt", "w") as file:
            inp = file.write(c)  # запись в файл результата
    else:
        print("Не корректные входные данные")
        exit(1)
