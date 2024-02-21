def hitung_fungsi(x):
    a = 2 * x**3 + 2 * x + 15 / x
    return a

def main():
    x = int(input("Masukkan bilangan bulat untuk x: "))
    a = hitung_fungsi(x)
    print("Hasil dari fungsi f(x) =", a)

if __name__ == "__main__":
    main()
