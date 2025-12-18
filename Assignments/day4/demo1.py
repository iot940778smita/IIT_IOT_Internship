def km_to_m(distance_km):
    return distance_km * 1000

def m_to_cm(distance_m):
    return distance_m * 100

def cm_to_mm(distance_cm):
    return distance_cm * 10

def feet_to_inches(distance_feet):
    return distance_feet * 12

def inches_to_cm(distance_inches):
    return distance_inches * 2.54


def distance_converter(distance, conversion_type_str, conversion_func):
   
    converted_distance = conversion_func(distance)
    print(f"{distance} {conversion_type_str.split(' to ')[0]} is equal to {converted_distance:.2f} {conversion_type_str.split(' to ')[1]}.")


if __name__ == "__main__":
    try:
  
        distance_input = float(input("Enter a distance (e.g., 5.5): "))

        print("\n--- All Conversions using the input distance ---")

        
        distance_converter(distance_input, "km to m", km_to_m)
        distance_converter(distance_input, "m to cm", m_to_cm)
        distance_converter(distance_input, "cm to mm", cm_to_mm)
        distance_converter(distance_input, "feet to inches", feet_to_inches)
        distance_converter(distance_input, "inches to cm", inches_to_cm)

    except ValueError:
        print("Invalid input. Please enter a numerical value for distance.")

