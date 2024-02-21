def hitung_berat_badan(tinggi_badan, bmi_harap):
    berat_badan = bmi_harap * (tinggi_badan ** 2)
    return berat_badan

def main():
    tinggi_badan = float(input("Masukkan tinggi badan Anda (dalam meter): "))
    bmi_harap = float(input("Masukkan nilai BMI yang diharapkan: "))

    berat_badan_diperlukan = hitung_berat_badan(tinggi_badan, bmi_harap)

    print(f"Berat badan yang diperlukan untuk BMI {bmi_harap} dan tinggi badan {tinggi_badan} meter adalah: {berat_badan_diperlukan} kilogram")

if __name__ == "__main__":
    main()