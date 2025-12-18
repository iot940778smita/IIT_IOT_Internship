tonnes_to_kg = lambda tonnes: tonnes * 1000


kg_to_gm = lambda kg: kg * 1000

gm_to_mg = lambda gm: gm * 1000


mg_to_lbs = lambda mg: mg * 2.20462e-6

try:
    tonnes_input = float(input("Enter weight in tonnes: "))

    
    kilograms = tonnes_to_kg(tonnes_input)
    grams = kg_to_gm(kilograms)
    milligrams = gm_to_mg(grams)
    pounds = mg_to_lbs(milligrams)

    print(f"\n{tonnes_input} tonnes is equal to:")
    print(f"{kilograms:.4f} kg")
    print(f"{grams:.4f} gm")
    print(f"{milligrams:.4f} mg")
    print(f"{pounds:.8f} lbs")

except ValueError:
    print("Invalid input. Please enter a numerical value.")

