from encryption_utils import load_key, encrypt_note

def main():
    key = load_key()  # Load your vault key

    note = input("📝 What do you want to save?: ")
    encrypted_note = encrypt_note(note, key)

    with open("vault.txt", "ab") as vault:
        vault.write(encrypted_note + b"\n")  # Save encrypted text

    print("✅ Your note was encrypted and saved securely!")

if __name__ == "__main__":
    main()

