def crisis_response(file):
    """
    Runs a series of archive access attempts to simulate crisis scenarios, 
    demonstrating proper handling of missing files -security restrictions 
    and normal operations.
    """
    try:
        print(f"CRISIS ALERT: Attempting access to '{file}'...")
        with open(file, 'r') as f:
            data = f.read()
        print(f"SUCCESS: Archive recovered - ''{data}''")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    else:
        print("STATUS: Normal operations resumed")


def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    crisis_response('lost_archive.txt')
    print()
    crisis_response('classified_data.txt')
    print()
    crisis_response('standard_archive.txt')
    print()
    print("All crisis scenarios handled successfully. Archives secure.")


main()
