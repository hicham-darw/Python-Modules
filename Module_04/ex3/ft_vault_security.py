def main():
    """
    reads a secure archive and writes it to a new file, ensuring safe access
    and preservation
    """
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    try:
        with open('../security_protocols.txt', "r") as file:
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
            file.write(data)
            print(data)
            print("Vault automatically sealed upon completion")
        print("\nAll vault operations completed with maximum security.")
    except Exception as e:
        print(e)


main()
