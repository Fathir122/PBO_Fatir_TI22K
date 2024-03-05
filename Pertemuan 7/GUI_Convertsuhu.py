import tkinter as tk


def konversi_suhu():
    try:
        suhu_input = float(entry_suhu.get())
        satuan_awal = combo_satuan_awal.get()
        satuan_hasil = combo_satuan_hasil.get()

        if satuan_awal == "Celsius" and satuan_hasil == "Fahrenheit":
            hasil = (suhu_input * 9/5) + 32
        elif satuan_awal == "Celsius" and satuan_hasil == "Kelvin":
            hasil = suhu_input + 273.15
        elif satuan_awal == "Fahrenheit" and satuan_hasil == "Celsius":
            hasil = (suhu_input - 32) * 5/9
        elif satuan_awal == "Fahrenheit" and satuan_hasil == "Kelvin":
            hasil = (suhu_input - 32) * 5/9 + 273.15
        elif satuan_awal == "Kelvin" and satuan_hasil == "Celsius":
            hasil = suhu_input - 273.15
        elif satuan_awal == "Kelvin" and satuan_hasil == "Fahrenheit":
            hasil = (suhu_input - 273.15) * 9/5 + 32
        else:
            hasil = suhu_input

        label_hasil.config(text=f"Hasil: {hasil:.2f} {satuan_hasil}")
    except ValueError:
        label_hasil.config(text="Masukkan suhu dalam bentuk angka.")


# Membuat GUI
root = tk.Tk()
root.title("Convert Suhu GUI")
root.configure(background="grey")
root.geometry("270x240")
root.resizable(False, False)

# Label dan Entry untuk input suhu
label_suhu = tk.Label(root, text="Masukkan Suhu:")
label_suhu.grid(row=0, column=0, padx=10, pady=10)
entry_suhu = tk.Entry(root)
entry_suhu.grid(row=0, column=1, padx=10, pady=10)

# Label untuk satuan awal
label_satuan_awal = tk.Label(root, text="Satuan Awal:")
label_satuan_awal.grid(row=1, column=0, padx=10, pady=10)

# Dropdown untuk satuan awal
satuan_awal_options = ["Celsius", "Fahrenheit", "Kelvin"]
combo_satuan_awal = tk.StringVar()
combo_satuan_awal.set(satuan_awal_options[0])
dropdown_satuan_awal = tk.OptionMenu(
    root, combo_satuan_awal, *satuan_awal_options)
dropdown_satuan_awal.grid(row=1, column=1, padx=10, pady=10)

# Label untuk satuan hasil
label_satuan_hasil = tk.Label(root, text="Satuan Hasil:")
label_satuan_hasil.grid(row=2, column=0, padx=10, pady=10)

# Dropdown untuk satuan hasil
satuan_hasil_options = ["Celsius", "Fahrenheit", "Kelvin"]
combo_satuan_hasil = tk.StringVar()
combo_satuan_hasil.set(satuan_hasil_options[1])
dropdown_satuan_hasil = tk.OptionMenu(
    root, combo_satuan_hasil, *satuan_hasil_options)
dropdown_satuan_hasil.grid(row=2, column=1, padx=10, pady=10)

# Tombol konversi
tombol_konversi = tk.Button(root, text="Konversi", command=konversi_suhu)
tombol_konversi.grid(row=3, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil
label_hasil = tk.Label(root, text="")
label_hasil.grid(row=4, column=0, columnspan=2, pady=10)

# Menjalankan GUI
root.mainloop(
