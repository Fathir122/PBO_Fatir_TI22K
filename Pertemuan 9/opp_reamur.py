class KonversiToReamur:
    def _init_(self, celsius):
        self.celsius = celsius

    def konversi(self):
        reamur = self.celsius * 4/5
        return reamur


def main():
    celsius_input = float(input("Masukkan suhu dalam Celsius: "))
    konversi_reamur = KonversiToReamur(celsius_input)
    hasil_reamur = konversi_reamur.konversi()
    print(f"{celsius_input}°C sama dengan {hasil_reamur}°Re")


if _name_ == "_main_":
    main()
