import tkinter as tk


def hitung_luas_volume():
    try:
        # Ambil panjang sisi dari input pengguna
        panjang_sisi = float(sisi_entry.get())

        # Hitung luas permukaan dan volume kubus
        luas_permukaan = 6 * panjang_sisi ** 2
        volume = panjang_sisi ** 3

        # Update label hasil
        luas_permukaan_var.set(f"Luas Permukaan Kubus: {luas_permukaan:.2f}")
        volume_var.set(f"Volume Kubus: {volume:.2f}")
    except ValueError:
        luas_permukaan_var.set("Masukkan angka valid")
        volume_var.set("Masukkan angka valid")


# Membuat jendela tkinter
window = tk.Tk()
window.title("Menghitung Luas Permukaan dan Volume Kubus")

# Frame utama
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Label panjang sisi
sisi_label = tk.Label(frame, text="Panjang Sisi Kubus:")
sisi_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Input panjang sisi
sisi_entry = tk.Entry(frame)
sisi_entry.grid(row=0, column=1, padx=10, pady=10)

# Tombol hitung
hitung_button = tk.Button(frame, text="Hitung", command=hitung_luas_volume)
hitung_button.grid(row=1, column=0, columnspan=2,
                   padx=10, pady=10, sticky="we")

# Hasil luas permukaan dan volume
luas_permukaan_var = tk.StringVar()
luas_permukaan_label = tk.Label(frame, textvariable=luas_permukaan_var)
luas_permukaan_label.grid(row=2, column=0, columnspan=2,
                          padx=10, pady=10, sticky="w")

volume_var = tk.StringVar()
volume_label = tk.Label(frame, textvariable=volume_var)
volume_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="w")

window.mainloop()
