# Nathanael Long
# 10/28/2025
# sales.txt File reader program


def main():
    """
    A program that checks for the sales.txt file and reads the contents.
    It then checks the contents of the file and removes parts it doesn't need.
    It gets the totals of sales in monetary terms and then outputs it to a new file
    called daily_reports.txt and tells the user in the console what the output is.
    If it doesn't find the sales.txt file, it says it cannot find the file in the console.
    """
    # Set the counts to zero
    total_books = 0.0
    total_dvds = 0.0
    total_games = 0.0

    try:
        with open("sales.txt", "r") as sales_file:
            line_number = 0

            for line in sales_file:
                line_number += 1
                # Get rid of blank spaces
                line = line.strip()

                # Skip the lines with no content
                if not line:
                    continue

                parts = [p.strip() for p in line.split(",")]

                # Look for only date and time, category, & price
                if len(parts) != 3:
                    print(f"Sorry, there's an error on line {line_number}: Format is not valid.")
                    continue

                _, category, price_str = parts

                try:
                    price = float(price_str)
                except ValueError:
                    print(f'Sorry, there is an error on line {line_number}: I was not able convert "{price_str}" to the proper format')
                    continue

                category = category.lower()

                # Total everything up
                if category == "book":
                    total_books += price
                elif category == "dvd":
                    total_dvds += price
                elif category == "game":
                    total_games += price
                else:
                    continue

        # Create and add the data to a file called daily_report.txt
        with open("daily_report.txt", "w") as dailyreport:
            dailyreport.write(f"Books: ${total_books:.2f}\n")
            dailyreport.write(f"DVDs: ${total_dvds:.2f}\n")
            dailyreport.write(f"Games: ${total_games:.2f}\n")
            print("Done! the daily_report.txt file has been created.")
            print(f" You will find that the contents of the file is :: Books: ${total_books:.2f}, DVDs: ${total_dvds:.2f}, Games: ${total_games:.2f}")

    except FileNotFoundError:
        print("Sorry, but I couldn't find a ' sales.txt ' to open.")

if __name__ == "__main__":
    main()