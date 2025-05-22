import random

def main():
    number = random.randint(1, 100)
    tries = 0

    print("Zgadnij liczbę od 1 do 100")

    while True:
        try:
            guess = int(input("Twoja próba: "))
            tries += 1

            if guess < number:
                print("Za mało!")
            elif guess > number:
                print("Za dużo!")
            else:
                print(f"Brawo! Zgadłeś w {tries} próbach.")
                break
        except ValueError:
            print("Wpisz liczbę całkowitą.")

if __name__ == "__main__":
    main()
