def main():
    """
    this main function read and display data from a file
    ensure safe file handling
    """
    file = 'ancient_fragment.txt'
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===", end='\n\n')
    print(f"Accessing Storage Vault: {file}")

    try:
        print("Connection established...", end='\n\n')
        f = open('../ancient_fragment.txt')
        print("RECOVERED DATA:")
        print(f.read())
        print()
        f.close()
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")


main()
