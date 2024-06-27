import random


def main():
    print("Selamat datang di permainan Tebak Angka!")
    print("Saya telah memilih sebuah angka antara 1 dan 100.")
    print("Coba tebak angka tersebut.")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    number_of_guesses = 0

    while True:
        # Get the user's guess
        try:
            guess = int(input("Masukkan tebakanmu: "))
        except ValueError:
            print("Tolong masukkan angka yang valid.")
            continue

        number_of_guesses += 1

        # Compare the guess to the number
        if guess < number_to_guess:
            print("Terlalu rendah. Coba lagi.")
        elif guess > number_to_guess:
            print("Terlalu tinggi. Coba lagi.")
        else:
            print(
                f"Selamat! Anda telah menebak angka {number_to_guess} dengan benar dalam {number_of_guesses} tebakan.")
            break


if __name__ == "__main__":
    main()
