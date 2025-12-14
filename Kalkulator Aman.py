def kalkulator():
    try:
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua: "))

        operator = input("Masukkan operator (+, -, *, /): ")

        if operator == "+":
            hasil = angka1 + angka2
        elif operator == "-":
            hasil = angka1 - angka2
        elif operator == "*":
            hasil = angka1 * angka2
        elif operator == "/":
            if angka2 == 0:
                raise ZeroDivisionError("Tidak bisa membagi dengan nol!")
            hasil = angka1 / angka2
        else:
            raise Exception(f"Operator '{operator}' tidak valid!")

        print(f"Hasil: {hasil}")

    except ValueError:
        print("Error: Input harus berupa angka!")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    kalkulator()