from typing import Union

def banner() -> None:
    print("Welcome to Treasure Island")
    print("Your mission is to find the treasure.")

def verify(*options: str) -> str:
    msg = ' or '.join(options) + '? '
    print(msg)
    while (ans := input().lower()) not in set(options):
        print("Invalid response, looking for one of", end=" ")
        print(*options,end=" ")
        print("\nTry again")
        print(msg)
    return ans 

def left_right() -> str:
    return verify('left','right')

def swim_wait() -> str:
    return verify('swim','wait')

def door() -> str:
    return verify('red','blue','yellow','any')

def again() -> bool:
    print("Would you like to play again? (Y|N)")
    while (ans := input().lower()) not in {'y','n'}:
        print("Err. I didn't catch that...")
        print("Would you like to play again? (Y|N)")
    if ans == 'y':
        return True
    return False 

def loop():
    playing = True
    while playing:
        stage_one = left_right()
        if stage_one == 'right':
            print("You fell into a hole. Game Over!")
        else:
            stage_two = swim_wait()
            if stage_two == 'swim':
                print("You were attacked by a trout. Game over!")
            else:
                stage_three = door()
                if stage_three == 'red':
                    print("You were burned by a fire. Game over!")
                elif stage_three == 'blue':
                    print("You were eaten by beasts. Game over!")
                elif stage_three == 'any':
                    print("idk what happened. but...Game over!")
                else:
                    print("You win!")
        playing = again()

if __name__ == "__main__":
    loop()

