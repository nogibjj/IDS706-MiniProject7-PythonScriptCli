import argparse


def encrypt(text: str, shift: int) -> str:
    result = []
    for c in text:
        if c.isalpha():
            base = ord('a') if c.islower() else ord('A')
            offset = (ord(c) - base + shift) % 26
            result.append(chr(base + offset))
        else:
            result.append(c)
    return ''.join(result)


def decrypt(text: str, shift: int) -> str:
    return encrypt(text, 26 - shift)


def main():
    parser = argparse.ArgumentParser(description="Encrypt or Decrypt using Caesar cipher.")
    parser.add_argument("plaintext", type=str, help="Plaintext string to be encrypted.")
    parser.add_argument("shift", type=int, help="Shift value for the Caesar cipher.")

    args = parser.parse_args()
    plaintext = args.plaintext
    shift = args.shift

    ciphertext = encrypt(plaintext, shift)
    decrypted_text = decrypt(ciphertext, shift)

    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted text: {decrypted_text}")


if __name__ == "__main__":
    main()
