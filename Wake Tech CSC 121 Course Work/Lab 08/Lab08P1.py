# Nathanael Long
# 10/28/2025
# program.log.txt File reader program

def main():

    """
    A program that checks for the program.log.txt file and reads the contents.
    It then tallies up the number of each kind of message in the log.
    It then returns the number of criticals, errors, warnings, informationals, and unknowns
    within the file. If it doesn't find the file, it says it cannot find the file.
    """

    # Set counters to zero
    CRITICAL = 0
    ERROR = 0
    WARNING = 0
    INFO = 0
    UNKNOWN = 0

    try:
        # Open program.log.txt
        with open("program.log.txt", "r") as log_file:
            for line in log_file:
                parts = line.strip().split()
                if len(parts) < 5:
                    UNKNOWN += 1
                    continue

                category = parts[3].upper()

                # Update the counts as needed
                if category == "CRITICAL":
                    CRITICAL += 1
                elif category == "ERROR":
                    ERROR += 1
                elif category == "WARNING":
                    WARNING += 1
                elif category == "INFO":
                    INFO += 1
                else:
                    UNKNOWN += 1

        # print the updated counts
        print(f'Here are the counts from the log file...')
        print(f"Critical: {CRITICAL}")
        print(f"Error: {ERROR}")
        print(f"Warning: {WARNING}")
        print(f"Informational: {INFO}")
        print(f"Unknown: {UNKNOWN}")

    except FileNotFoundError:
        print("Sorry, but I couldn't find a ' program.log.txt ' to open.")

if __name__ == "__main__":
    main()
