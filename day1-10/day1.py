"""
Requirements

1. Create a greeting for your program
2. Ask the user for the city that they grew up in
3. Ask the user for the name of a pet 
4. Combine the name of their city and pet and show them their band name
5. Make sure the input cursor shows on a newline
"""

def greeting() -> None:
    print("Hello and welcome to the Band Name Generator!")

def get_city() -> str:
    print("What city did you grow up in?")
    city = input()
    return city 

def get_pet() -> str:
    print("What is the name of your pet?")
    pet = input()
    return pet 

def generate_band_name(city: str, pet: str) -> str:
    band_name = city + ' ' + pet
    return band_name 

def again() -> bool:
    print("Would you like to generate another band name? (Y|N)")
    while (ans := input().lower()) not in {'y','n'}:
        print("Errr. I don't know what you mean")
        print("Would you like to generate another band name? (Y|N)")
    if ans == 'y':
        return True
    return False 

def loop() -> None:
    playing = True
    while playing:
        greeting()
        print("")
        city = get_city()
        pet = get_pet()
        band = generate_band_name(city,pet)
        print(f"\nYour band name is {band}\n")
        playing = again()
    print("\n")
    print("Thanks for playing!")

if __name__ == "__main__":
    loop()
