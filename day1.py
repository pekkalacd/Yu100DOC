"""
Requirements

1. create a greeting for your program
2. ask the user for the city that they grew up in
3. ask the user for the name of a pet
4. combine the name of their city and pet and show them their band name
5. make sure the input cursor shows on a newline.
"""

def greet() -> None:
    print("Hello and welcome to the Band-Generator!\n")

def get_city() -> str:
    print("What is the name of the city you grew up in?")
    city = input()
    return city

def get_pet() -> str:
    print("What is the name of your pet?")
    pet = input()
    return pet 

def generate_band_name(city: str, pet: str) -> str:
    band_name = city + ' ' + pet 
    return band_name 

def play_again() -> bool:
    print("Would you like to generate another band name? (Y|N)")
    while (ans := input().lower()) not in {'y','n'}:
        print("Err. I don't understand what you mean")
        print("Would you like to generate another band name? (Y|N)")
    if ans == 'y':
        return True
    return False 

def loop():
    playing = True 
    while playing:
        greet()
        city = get_city()
        pet = get_pet()
        band_name = generate_band_name(city,pet)
        print(f"\nYour band name is {band_name}\n")
        playing = play_again()
    print("\nThanks for playing!")


if __name__ == "__main__":
    loop()
