def hitung_diskon(total_belanja):
    if total_belanja >= 250000:
        diskon = total_belanja * 50 / 100
        print("Diskon yang diberikan adalah Rp.", diskon)
    else:
        print("Anda tidak mendapatkan diskon karena total belanjaan tidak mencapai Rp. 250.000.")

def main():
    total_belanja = float(input("Masukkan total belanjaan Anda: Rp. "))
    hitung_diskon(total_belanja)

if __name__ == "__main__":
    main()