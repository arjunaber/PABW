for i in range(1, 101):
    print(i)

for i in range(1, 101):
    if i % 2 == 1:
        print(i)
    else:
        continue

def cek_genap_ganjil(n):
    if n % 2 == 0:
        return "genap"
    else:
        return "ganjil"