# Nathanael Long
# 10/05/2025
# IPv4 Address Program

def main():
    """
    A program that requests the user to enter an IP address in the format of (X.X.X.X).
    It checks the provided input each input, in order, against the following conditions...

    1. The IP address must contain 4 octets separated by periods
    2. The octets must be a number and cannot be a letter or symbol
    3. The provided octets must be 0 or higher and less than or equal to 255

    The program repeats until the user enters 'q' or 'Q'.
    """

    ipaddr = input("Please enter an IP address (or type 'q' / 'Q' to quit): ")

    while ipaddr.lower() != 'q':
        octets = ipaddr.split('.')

        if len(octets) != 4:
            print("Sorry, an IP address must have 4 octets separated by periods.")
        else:
            error_flag = False

            for octet in octets:
                if not octet.isdigit():
                    print("Sorry, each octet must be numeric. No letters or symbols allowed.")
                    error_flag = True
                    break

                num = int(octet)
                if num < 0 or num > 255:
                    print("Sorry, each octet must be between 0 and 255.")
                    error_flag = True
                    break

            if not error_flag:
                formatted_ipaddr = ipaddr.replace('.', ':')
                print(f"\nIP address: {formatted_ipaddr}")


        ipaddr = input("\nPlease enter an IP address (or type 'q' / 'Q' to quit): ")


if __name__ == "__main__":
    main()