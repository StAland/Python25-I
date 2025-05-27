def fib_iterativ(n):
    if n < 1:
        print("Bitte eine Zahl von mindestens 1 uebergeben")
        return
    elif n == 1 or n == 2:
        return 1
    fibs = [1, 1]
    for i in range (3, n+1, 1):
        fibs.append(fibs[i-3] + fibs[i-2])
    return fibs[n-1]

def main():
    ergebnis = fib_iterativ(500)
    print(ergebnis)


main()
