print("masukan angka di luar bulan untuk berhenti")
bulan = int(input("bulan (1-12): "))
ganjil = "ada 31 hari" 
genap = "ada 30 hari"
hari = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if bulan < 0 or bulan > 12:
    print("masukan bulan yang valid")

while bulan > 0 and bulan < 13:
    if bulan == 2:
        tahun = int(input("tahun: "))
        if tahun % 4 == 0:
            hari[1] = 29

    print(f"ada {hari[bulan-1]} hari")
    bulan = int(input("bulan (1-12): "))
    
print("bye bye :3")