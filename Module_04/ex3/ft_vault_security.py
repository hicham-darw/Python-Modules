def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    try:
        with open('file.txt', "r") as file:
            print("Initiating secure vault access...")
            print("Vault connection established with failsafe protocols\n")
            data = file.read()
            print("SECURE EXTRACTION:")
            print(data)
            print("{[}CLASSIFIED{]} Archive integrity: 100%\n")

    except Exception as e:
        print(e)
    try:
        with open("file.txt", "w") as file:
            print("SECURE PRESERVATION:")
            file.write('{[}CLASSIFIED{]} Quantum encryption keys recovered')
            print('{[}CLASSIFIED{]} Quantum encryption keys recovered')
            print("Vault automatically sealed upon completion")
        print("\nAll vault operations completed with maximum security.")
    except Exception as e:
        print(e)


main()
