def main():
    """
    reads a secure archive and writes it to a new file, ensuring safe access
    and preservation
    """
    file = "classified_data.txt"
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    try:
        with open('../' + file, "r") as file:
            print("Initiating secure vault access...")
            print("Vault connection established with failsafe protocols\n")
            data = file.read()
            print("SECURE EXTRACTION:")
            print(data, end='\n\n')
    except Exception as e:
        print(e)
    try:
        with open("../security_protocols.txt", "w") as file:
            print("SECURE PRESERVATION:")
            file.write(data)
            print("{[}CLASSIFIED{]} New security protocols archived")
            print("Vault automatically sealed upon completion")
    except Exception as e:
        print(e)
    finally:
        print("\nAll vault operations completed with maximum security.")


main()
