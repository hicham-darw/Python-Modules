def main():
    """
    this main function read and display data from a file
    ensure safe file handling
    """
    file = 'ancient_fragment.txt'
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===", end='\n\n')
    print(f"Accessing Storage Vault: {file}")
    print("Connection established...", end='\n\n')
    f = open('../' + file)
    print("RECOVERED DATA:")
    print(f.read())
    print()
    f.close()
    print("Data recovery complete. Storage unit disconnected.")
    print("ERROR: Storage vault not found.")


main()
