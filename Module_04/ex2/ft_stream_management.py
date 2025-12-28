import sys


def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n", end='\n')
    print("Input Stream active. Enter archivist ID: ", end='', flush=True)
    arch_id = sys.stdin.readline().rstrip()
    print("Input Stream active. Enter status report: ", end='', flush=True)
    status_r = sys.stdin.readline().rstrip()
    print("")
    s_out = "{[}STANDARD{]}"
    s_out += ' Archive status from ' + arch_id
    s_out += ': ' + status_r
    sys.stdout.write(s_out)
    sys.stdout.flush()
    s_err = "\n{[}ALERT{]} "
    s_err += "System diagnostic: Communication channels verified\n"
    sys.stderr.write(s_err)
    s_out = "{[}STANDARD{]} "
    s_out = "Data transmission complete\n"
    sys.stdout.write(s_out)
    print("\nThree-channel communication test successful.")


main()
