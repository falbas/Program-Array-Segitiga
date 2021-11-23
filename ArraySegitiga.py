def cetakarr(arr, n, m):
    gap = 0  # variabel untuk memberi spasi antar elemen
    for i in range(n):
        for j in range(m):
            gap = max(gap, len(arr[i][j])) # mencari nilai maksimal spasi
    gap += 1

    for i in range(n):
        for j in range(m):
            print(arr[i][j], end="") # mencetak elemen array
            for k in range(gap - len(arr[i][j])):
                print(" ", end='') # mencetak spasi sesuai besar variabel gap
        print()


def segitiga1():
    print('''
-----ARRAY SEGITIGA TYPE 1-----
Input
- Array A Upper Triangular berorder N * N
- Array B Lower Triangular berorder (N-1) * (N-1)
Output
- Array A dan Array B disimpan di Array C berorder N * N
''')

    n = 0
    while n < 3 or n > 5:
        n = int(input(f'Masukkan ukuran array (3-5): '))
        if n >= 3 and n <= 5:
            break
        print("Ukuran array harus antara 3-5")

    a = [['0' for i in range(n)] for i in range(n)]
    b = [['0' for i in range(n - 1)] for i in range(n - 1)]
    c = [['0' for i in range(n)] for i in range(n)]
    print()

    for i in range(n):
        for j in range(n):
            if j >= i:
                a[i][j] = input(f'- Masukkan Elemen A[{i+1},{j+1}]: ')
                c[i][j] = a[i][j]

    print(f"\nArray A (Upper Triangular) dengan order {n} * {n}:")
    cetakarr(a, n, n)
    print()

    for i in range(n - 1):
        for j in range(n - 1):
            if j <= i:
                b[i][j] = input((f'- Masukkan Elemen B[{i+1},{j+1}]: '))
                c[i + 1][j] = b[i][j]

    print(f"\nArray B (Lower Triangular) dengan order {n-1} * {n-1}:")
    cetakarr(b, n - 1, n - 1)

    input("\nTekan Enter Untuk Melihat Hasil!\n")
    print("----------- H A S I L -----------")

    print('''
Jadi Array Segitiga Type 1 dari Array A (Upper Triangular) berorder N * N
dan Array B (Lower Triangular) berorder (N-1) * (N-1) adalah Array C berorder N * N
''')
    print(f"Array A (Upper Triangular) dengan order {n} * {n}:")
    cetakarr(a, n, n)

    print(f"\ndan Array B (Lower Triangular) dengan order {n-1} * {n-1}:")
    cetakarr(b, n - 1, n - 1)

    print(f"\nHasil akhirnya adalah Array C dengan order {n} * {n}:")
    cetakarr(c, n, n)


def segitiga2():
    print('''
-----ARRAY SEGITIGA TYPE 2-----
Input
- Array A Upper Triangular berorder N * N
- Array B Lower Triangular berorder N * N
Output
- Array A dan Array B disimpan di Array C berorder N * (N+1)
''')

    n = 0
    while n < 3 or n > 5:
        n = int(input(f'Masukkan ukuran array (3-5): '))
        if n >= 3 and n <= 5:
            break
        print("Ukuran array harus antara 3-5")

    a = [['0' for i in range(n)] for i in range(n)]
    b = [['0' for i in range(n)] for i in range(n)]
    c = [['0' for i in range(n + 1)] for i in range(n)]
    print()

    for i in range(n):
        for j in range(n):
            if j >= i:
                a[i][j] = input(f'- Masukkan Elemen A[{i+1},{j+1}]: ')
                c[i][j + 1] = a[i][j]

    print(f"\nArray A (Upper Triangular) dengan order {n} * {n}:")
    cetakarr(a, n, n)
    print()

    for i in range(n):
        for j in range(n):
            if j <= i:
                b[i][j] = input((f'- Masukkan Elemen B[{i+1},{j+1}]: '))
                c[i][j] = b[i][j]

    print(f"\nArray B (Lower Triangular) dengan order {n} * {n}:")
    cetakarr(b, n, n)

    input("\nTekan Enter Untuk Melihat Hasil!\n")
    print("----------- H A S I L -----------")

    print('''
Jadi Array Segitiga Type 2 dari Array A (Upper Triangular) berorder N * N
dan Array B (Lower Triangular) berorder N * N adalah Array C berorder N * (N+1)
''')
    print(f"Array A (Upper Triangular) dengan order {n} * {n}:")
    cetakarr(a, n, n)

    print(f"\ndan Array B (Lower Triangular) dengan order {n} * {n}:")
    cetakarr(b, n, n)

    print(f"\nHasil akhirnya adalah Array C dengan order {n} * {n+1}:")
    cetakarr(c, n, n + 1)


def segitiga3():
    print('''
-----ARRAY SEGITIGA TYPE 3-----
Input
- Array A Upper Triangular berorder N * N
- Array B Upper Triangular berorder N * N
- Transpose Array B menjadi Lower Triangular berorder N * N
Output
- Array A dan Array B disimpan di Array C berorder N * (N+1)
''')

    n = 0
    while n < 3 or n > 5:
        n = int(input(f'Masukkan ukuran array (3-5): '))
        if n >= 3 and n <= 5:
            break
        print("Ukuran array harus antara 3-5")

    a = [['0' for i in range(n)] for i in range(n)]
    b = [['0' for i in range(n)] for i in range(n)]
    c = [['0' for i in range(n + 1)] for i in range(n)]
    print()

    for i in range(n):
        for j in range(n):
            if j >= i:
                a[i][j] = input(f'- Masukkan Elemen A[{i+1},{j+1}]: ')
                c[i][j + 1] = a[i][j]

    print(f"\nArray A (Upper Triangular) dengan order {n} * {n}:")
    cetakarr(a, n, n)
    print()

    for i in range(n):
        for j in range(n):
            if j >= i:
                b[i][j] = input((f'- Masukkan Elemen B[{i+1},{j+1}]: '))

    print(f"\nArray B (Upper Triangular) dengan order {n} * {n}:")
    cetakarr(b, n, n)

    for i in range(n):
        for j in range(n):
            if j >= i:
                b[i][j], b[j][i] = b[j][i], b[i][j]
            if j <= i:
                c[i][j] = b[i][j]

    print(f"\nTranspose Array B (Lower Triangular) dengan order {n} * {n}:")
    cetakarr(b, n, n)

    input("\nTekan Enter Untuk Melihat Hasil!\n")
    print("----------- H A S I L -----------")

    print('''
Jadi Array Segitiga Type 3 dari Array A (Upper Triangular) berorder N * N
dan Array B (Upper Triangular) berorder N * N, kemudian Array B di Transpose menjadi
Lower Triangular. Hasilnya adalah Array C berorder N * (N+1)
''')
    print(f"array A (Upper Triangular) dengan order {n} * {n}:")
    cetakarr(a, n, n)

    print(f"\ndan Transpose Array B (Lower Triangular) dengan order {n}*{n}:")
    cetakarr(b, n, n)

    print(f"\nHasil akhirnya adalah Array C dengan order {n} * {n+1}:")
    cetakarr(c, n, n + 1)


def segitiga4():
    print('''
-----ARRAY SEGITIGA TYPE 4-----
Input
- Array A Upper Triangular berorder N * N
- Array B Upper Triangular berorder N * N
- Transpose Array A menjadi Lower Triangular berorder N * N
Output
- Array A dan Array B disimpan di Array C berorder N * (N+1)
''')

    n = 0
    while n < 3 or n > 5:
        n = int(input(f'Masukkan ukuran array (3-5): '))
        if n >= 3 and n <= 5:
            break
        print("Ukuran array harus antara 3-5")

    a = [['0' for i in range(n)] for i in range(n)]
    b = [['0' for i in range(n)] for i in range(n)]
    c = [['0' for i in range(n + 1)] for i in range(n)]
    print()

    for i in range(n):
        for j in range(n):
            if j >= i:
                a[i][j] = input(f'- Masukkan Elemen A[{i+1},{j+1}]: ')

    print(f"\nArray A (Upper Triangular) dengan order {n} * {n}:")
    cetakarr(a, n, n)

    for i in range(n):
        for j in range(n):
            if j >= i:
                a[i][j], a[j][i] = a[j][i], a[i][j]
            if j <= i:
                c[i][j] = a[i][j]

    print(f"\nTranspose Array A (Lower Triangular) dengan order {n} * {n}:")
    cetakarr(a, n, n)
    print()

    for i in range(n):
        for j in range(n):
            if j >= i:
                b[i][j] = input(f'- Masukkan Elemen B[{i+1},{j+1}]: ')
                c[i][j + 1] = b[i][j]

    print(f"\nArray B (Upper Triangular) dengan order {n} * {n}:")
    cetakarr(b, n, n)

    input("\nTekan Enter Untuk Melihat Hasil!\n")
    print("----------- H A S I L -----------")

    print('''
Jadi Array Segitiga Type 4 dari Array A (Upper Triangular) berorder N * N
dan Array B (Upper Triangular) berorder N * N, kemudian Array A di Transpose menjadi
Lower Triangular. Hasilnya adalah Array C berorder N * (N+1)
''')
    print(f"Transpose array A (Upper Triangular) dengan order {n} * {n}:")
    cetakarr(a, n, n)

    print(f"\ndan array B (Lower Triangular) dengan order {n} * {n}:")
    cetakarr(b, n, n)

    print(f"\nHasil akhirnya adalah array C dengan order {n} * {n+1}:")
    cetakarr(c, n, n + 1)


def menu():
    print("\n-----PROGRAM ARRAY SEGITIGA-----")
    print("1. Array Segitiga Type 1 order N * N")
    print("2. Array Segitiga Type 2 order N * (N+1)")
    print("3. Array Segitiga Type 3 order N * (N+1)")
    print("4. Array Segitiga Type 4 order N * (N+1)")
    pilihan = input("Pilih jenis Array Segitiga: ")

    if pilihan == "1":
        segitiga1()
    elif pilihan == "2":
        segitiga2()
    elif pilihan == "3":
        segitiga3()
    elif pilihan == "4":
        segitiga4()
    else:
        print("Nomor tersebut tidak ada dalam pilihan")


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
