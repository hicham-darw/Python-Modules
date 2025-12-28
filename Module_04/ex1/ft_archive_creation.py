def main():
    file = 'new_discovery.txt'
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===", end='\n\n')
    try:
        print(f"Initializing new storage unit: {file}")
        f = open(file, "w")
        print('Storage unit created successfully...', end='\n\n')
        print('Inscribing preservation data...')
        f.write('{[}ENTRY 001{]} New quantum algorithm discovered\n')
        print("{[}ENTRY 001{]} New quantum algorithm discovered")
        f.write('{[}ENTRY 002{]} Efficiency increased by 347%\n')
        print("{[}ENTRY 002{]} Efficiency increased by 347%")
        f.write('{[}ENTRY 003{]} Archived by Data Archivist trainee\n')
        print("{[}ENTRY 003{]} Archived by Data Archivist trainee", end='\n\n')
        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive '{file}' ready for long-term preservation.")
    except Exception as e:
        print(e)


main()
