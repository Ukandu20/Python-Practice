# Description: Converts CAD to Japanese Yen

def convert_cad_to_yen(cad_value, conversion_rate):
    return cad_value * conversion_rate

def main():

    conversion_rate = 97.78

    print("CAD to Japanese Yen Converter")
    print(f"Conversion rate: 1 CAD = {conversion_rate} Japanese Yen")

    while True:
        try:
            cad_value = float(input("Enter the amount in CAD (0 to exit): "))
            if cad_value == 0:
                break
            yen_value = convert_cad_to_yen(cad_value, conversion_rate)
            print(f"{cad_value} CAD = {yen_value:.2f} Japanese Yen")
        except ValueError:
            print("Invalid input. Please enter a valid number for CAD value.")

if __name__ == "__main__":
    main()
