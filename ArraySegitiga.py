def cetakarr(arr, n, m):
    gap = 0
    for i in range(n):
        for j in range(m):
            gap = max(gap, len(arr[i][j]))
    gap += 1

    for i in range(n):
        for j in range(m):
            print(arr[i][j], end="")
            for k in range(gap - len(arr[i][j])):
                print(" ", end='')
        print()


def segitiga1():
    print("\n-----ARRAY SEGITIGA TIPE 1-----\n")
    n = int(input(f'Masukan Ukuran Array (Integer): '))
    a = [['0' for i in range(n)] for i in range(n)]
    b = [['0' for i in range(n - 1)] for i in range(n - 1)]
    c = [['0' for i in range(n)] for i in range(n)]
    print()

    for i in range(n):
        for j in range(n):
            if j >= i:
                a[i][j] = input(f'- Masukkan Elemen A[{i+1},{j+1}]: ')
                c[i][j] = a[i][j]

    print(f"\nArray A (Upper Triangular) dengan order {n}*{n}:")
    cetakarr(a, n, n)
    print()

    for i in range(n - 1):
        for j in range(n - 1):
            if j <= i:
                b[i][j] = input((f'- Masukkan Elemen B[{i+1},{j+1}]: '))
                c[i + 1][j] = b[i][j]

    print(f"\nArray B (Lower Triangular) dengan order {n-1}*{n-1}:")
    cetakarr(b, n - 1, n - 1)

    input("\nTekan Enter Untuk Melihat Hasil!\n")
    print("----------- H A S I L -----------")

    print("\nJadi array segitiga tipe 1 dari")
    print(f"array A (Upper Triangular) dengan order {n}*{n}:")
    cetakarr(a, n, n)

    print(f"\ndan array B (Lower Triangular) dengan order {n-1}*{n-1}:")
    cetakarr(b, n - 1, n - 1)

    print(f"\nHasil akhirnya adalah array dengan order {n}*{n}:")
    cetakarr(c, n, n)


def segitiga2():
    print("\n-----ARRAY SEGITIGA TIPE 2-----\n")
    n = int(input(f'Masukan Ukuran Array (Integer): '))
    a = [['0' for i in range(n)] for i in range(n)]
    b = [['0' for i in range(n)] for i in range(n)]
    c = [['0' for i in range(n + 1)] for i in range(n)]
    print()

    for i in range(n):
        for j in range(n):
            if j >= i:
                a[i][j] = input(f'- Masukkan Elemen A[{i+1},{j+1}]: ')

    for i in range(n):
        for j in range(n):
            c[i][j + 1] = a[i][j]

    print(f"\nArray A (Upper Triangular) dengan order {n}*{n}:")
    cetakarr(a, n, n)
    print()

    for i in range(n):
        for j in range(n):
            if j <= i:
                b[i][j] = input((f'- Masukkan Elemen B[{i+1},{j+1}]: '))

    for i in range(n):
        for j in range(n):
            if j <= i:
                c[i][j] = b[i][j]

    print(f"\nArray B (Lower Triangular) dengan order {n}*{n}:")
    cetakarr(b, n, n)

    input("\nTekan Enter Untuk Melihat Hasil!\n")
    print("----------- H A S I L -----------")

    print("\nJadi array segitiga tipe 2 dari")
    print(f"array A (Upper Triangular) dengan order {n}*{n}:")
    cetakarr(a, n, n)

    print(f"\ndan array B (Lower Triangular) dengan order {n}*{n}:")
    cetakarr(b, n, n)

    print(f"\nHasil akhirnya adalah array dengan order {n}*{n+1}:")
    cetakarr(c, n, n + 1)


def segitiga3():
    print("\n-----ARRAY SEGITIGA TIPE 3-----\n")
    n = int(input(f'Masukan Ukuran Array (Integer): '))
    a = [['0' for i in range(n)] for i in range(n)]
    b = [['0' for i in range(n)] for i in range(n)]
    c = [['0' for i in range(n + 1)] for i in range(n)]
    print()

    for i in range(n):
        for j in range(n):
            if j >= i:
                a[i][j] = input(f'- Masukkan Elemen A[{i+1},{j+1}]: ')

    for i in range(n):
        for j in range(n):
            c[i][j + 1] = a[i][j]

    print(f"\nArray A (Upper Triangular) dengan order {n}*{n}:")
    cetakarr(a, n, n)
    print()

    for i in range(n):
        for j in range(n):
            if j >= i:
                b[i][j] = input((f'- Masukkan Elemen B[{i+1},{j+1}]: '))

    print(f"\nArray B (Upper Triangular) dengan order {n}*{n}:")
    cetakarr(b, n, n)

    for i in range(n):
        for j in range(n):
            if j >= i:
                b[i][j], b[j][i] = b[j][i], b[i][j]

    print(f"\nTranspose Array B (Lower Triangular) dengan order {n}*{n}:")
    cetakarr(b, n, n)

    for i in range(n):
        for j in range(n):
            if j <= i:
                c[i][j] = b[i][j]

    input("\nTekan Enter Untuk Melihat Hasil!\n")
    print("----------- H A S I L -----------")

    print("\nJadi array segitiga tipe 3 dari")
    print(f"array A (Upper Triangular) dengan order {n}*{n}:")
    cetakarr(a, n, n)

    print(f"\ndan transpose array B (Lower Triangular) dengan order {n}*{n}:")
    cetakarr(b, n, n)

    print(f"\nHasil akhirnya adalah array dengan order {n}*{n+1}:")
    cetakarr(c, n, n + 1)


def segitiga4():
    print("Array Segitiga 4 Coming Soon")


def menu():
    print("\n-----PROGRAM ARRAY SEGITIGA-----")
    print("1. Array Segitiga Tipe 1")
    print("2. Array Segitiga Tipe 2")
    print("3. Array Segitiga Tipe 3")
    print("4. Array Segitiga Tipe 4")
    pilihan = input("Pilih jenis array segitiga: ")

    if pilihan == "1":
        segitiga1()
    elif pilihan == "2":
        segitiga2()
    elif pilihan == "3":
        segitiga3()
    elif pilihan == "4":
        segitiga4()
    else:
        print("Tidak ada dalam pilihan")


stop = False
while stop == False:
    menu()

    ask = True
    while(ask == True):
        repeat = input("\nApakah Anda Ingin Mengulang? (Y/N): ").lower()
        if repeat == "n":
            stop = True
            ask = False
        elif repeat == "y":
            stop = False
            ask = False
        else:
            ask = True

print("\nTerima Kasih & Keep Healthy!\n")
