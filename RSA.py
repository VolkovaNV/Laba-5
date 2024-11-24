from sympy import isprime, randprime
import random
import tkinter as tk

bits = 8 

public_key = private_key = None

def generate_keys():
    global public_key, private_key
    public_key, private_key = pari(bits)

def zashifr():
    plaintext = text_entry.get()
    key, n = public_key  # Используем публичный ключ
    cipher = [(ord(char) ** key) % n for char in plaintext]
    formatted_cipher = ' '.join(map(str, cipher))
    Res.delete(1.0, tk.END)
    Res.insert(tk.END, formatted_cipher)
    return formatted_cipher

def rashifr():
    cipher_text = text_entry.get()
    cipher = list(map(int, cipher_text.split()))
    key, n = private_key  # Используем приватный ключ
    plain = [chr((char ** key) % n) for char in cipher]
    Res.delete(1.0, tk.END)
    Res.insert(tk.END, ''.join(plain))
    return ''.join(plain)

def obrat(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def NOD(a, b): # НОД алг. Евклида
    while b != 0:
        a, b = b, a % b
    return a

def pari(bits):
    p = randprime(2**(bits-1), 2**bits)
    q = randprime(2**(bits-1), 2**bits)
    phi = (p - 1) * (q - 1)
    n = p * q

    e = random.randrange(2, phi)
    g = NOD(e, phi)
    while g != 1:
        e = random.randrange(2, phi)
        g = NOD(e, phi)

    d = obrat(e, phi)
    return ((e, n), (d, n))

root = tk.Tk()
root.title("Лабораторная №5")

generate_keys()

text_label = tk.Label(root, text="Введите сообщение:")
text_label.grid(row=0, column=0)
result_label = tk.Label(root, text="Результат:")
result_label.grid(row=3, column=0)
text_entry = tk.Entry(root)
text_entry.grid(row=0, column=1)
Res = tk.Text(root, height=5, width=50)
Res.grid(row=3, column=1)

Zah_button = tk.Button(root, text="Зашифровать", command=zashifr)
Zah_button.grid(row=2, column=0)
Rah_button = tk.Button(root, text="Расшифровать", command=rashifr)
Rah_button.grid(row=2, column=1)

root.mainloop()
