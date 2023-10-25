def encode():
    raw_password = input("Please enter your password to encode: ")
    # Loop through each digit and add 3 to it
    encoded = ""
    for i in range(len(raw_password)):
        # Modulo 10 gets the last digit.
        encoded += str((int(raw_password[i]) + 3) % 10)
    return encoded

def decode():
    encoded_password = input("Please enter your password to encode: ")
    # Loop through each digit and add 3 to it
    decoded = ""
    for i in range(len(encoded_password)):
        # Modulo 10 gets the last digit.
        decoded += str((int(encoded_password[i]) - 3) % 10)
    return decoded

def main():
    stored_password = ""
    while True():
        print("""Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n""")
        selection = input("Please enter an option: ")
        match selection:
            case 1:
                stored_password = encode()
                print("Your password has been encoded and stored!")
            case 2:
                decoded_password = decode()
                print("The encoded password is {[]}")

if __name__ == "__main__":
    main()