def main():
    """
    A program that requests the user to enter an IP address in the format of (X.X.X.X).
    It checks the provided input each input, in order, against the following conditions...

      1. The IP address must contain 4 octets separated by periods
      2. The octets must be a number and cannot be a letter or symbol
      3. The provided octets must be 0 or higher and less than or equal to 255

    If the IP address is valid...
        - Replaces periods with colons
        - Prints the formatted IP address
        - Prints the class of the IP address
        - Prints the default subnet mask
        - Prints whether the IP address is public or private

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
                first_octet = int(octets[0])  # <-- Fixed: define first_octet before using it
                second_octet = int(octets[1])

                # Determine the class and subnet mask
                if 1 <= first_octet <= 126:
                    ip_class = "Class A"
                    subnet_mask = "255.0.0.0"
                elif 128 <= first_octet <= 191:
                    ip_class = "Class B"
                    subnet_mask = "255.255.0.0"
                elif 192 <= first_octet <= 223:
                    ip_class = "Class C"
                    subnet_mask = "255.255.255.0"
                elif 224 <= first_octet <= 239:
                    ip_class = "Class D (Multicast)"
                    subnet_mask = "N/A"
                elif 240 <= first_octet <= 255:
                    ip_class = "Class E (Experimental)"
                    subnet_mask = "N/A"
                else:
                    ip_class = "Invalid"
                    subnet_mask = "N/A"

                # Format subnet mask as X:X:X:X if applicable
                subnet_mask_formatted = subnet_mask.replace('.', ':') if subnet_mask != "N/A" else subnet_mask

                # Determine if IP is public or private
                if first_octet == 10:
                    ip_type = "Private"
                elif first_octet == 172 and 16 <= second_octet <= 31:
                    ip_type = "Private"
                elif first_octet == 192 and second_octet == 168:
                    ip_type = "Private"
                else:
                    ip_type = "Public"

                # Output as requested
                print(f"{ipaddr}   {subnet_mask_formatted}")
                print(f"{ip_class} - {ip_type}")

        ipaddr = input("\n Please enter an IP address (or type 'q' / 'Q' to quit): ")


if __name__ == "__main__":
    main()
