# ALGORITMA Persamaan Linear (a*x + b = c)
# Input nilai a, b, dan c
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))
# Memastikan nilai a tidak nol untuk menghindari pembagian dengan nol
if a != 0:
    temp = c - b
    x = temp / a
    print(f"Nilai x adalah: {x}")
else:
    print("Nilai 'a' tidak boleh nol!")
