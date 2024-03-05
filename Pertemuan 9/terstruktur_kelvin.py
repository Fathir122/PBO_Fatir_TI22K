def konversi_ke_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin


def main():
    celsius_input = float(input("Masukkan suhu dalam Celsius: "))
    hasil_kelvin = konversi_ke_kelvin(celsius_input)
    print(f"{celsius_input}°C sama dengan {hasil_kelvin}K")


if _name_ == "_main_":
    main()
