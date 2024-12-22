import random

# Fonksiyon: 1024 bitlik rastgele bir ikili dizisi üretir
def generate_binary_string(length=1024):
    return ''.join(random.choice('01') for _ in range(length))

# 100 tane 1024 bitlik ikili dizesi üret
binary_strings = [generate_binary_string() for _ in range(100)]

# Sonuçları yazdır
for binary_string in binary_strings:
    print(f"[{', '.join(binary_string)}],")
