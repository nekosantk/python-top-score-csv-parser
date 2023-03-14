import argparse


'''
Primary function of the application which takes in a filename
then reads the file and prints out names of highest scoring players
'''
def main():

    # Argument parser for named arguments
    arg_parser = argparse.ArgumentParser()

    # Add argument options for filename
    arg_parser.add_argument("--filename",
                            help="Specify path to CSV file ie) data/TestData.csv",
                            type=str,
                            required=True)

    # Add argument options for filename
    arg_parser.add_argument("--sorting",
                            help="Specify sorting type ie) alphabetical",
                            type=str,
                            required=False)

    # Parse the arguments
    args = arg_parser.parse_args()

    # Keep track of the highest scoring people
    results = []

    # Keep track of the highest score so far
    best_score = 0

    # Open file
    with open(args.filename) as file:

        # First row of CSV file are the header names ['First Name', 'Second Name', 'Score']
        headers = file.readline().strip().split(',')

        # Columns can be saved in any order as long as header names remain constant [0, 1, 2]
        first_name_index = headers.index("First Name")
        second_name_index = headers.index("Second Name")
        score_col_index = headers.index("Score")

        # Keep track of row number for error message
        row_counter = 0

        # Iteratively read files to accommodate for very large files
        for line in file:

            # Split line of data by comma
            split_line = line.strip().split(',')

            # Increment row counter
            row_counter += 1

            # Check if number of data items matches number of headers
            if len(split_line) != len(headers):
                raise ValueError(f"Mismatch between number of columns and headers in row {row_counter}")

            # Grab values based on previously calculated index
            first_name = split_line[first_name_index]
            second_name = split_line[second_name_index]
            score =  int(split_line[score_col_index])

            # Check if this score is a new best score
            if score > best_score:

                # Clear existing leaderboard data
                results.clear()

                # Add this player's information into the results
                results.append({
                    "first_name": first_name,
                    "second_name": second_name
                })

                # Current score is new best score
                best_score = score

            # Check if this score is tied for best score
            elif score == best_score:

                # Add this player's information into the results
                results.append({
                    "first_name": first_name,
                    "second_name": second_name
                })

    # Check if any data was processed
    if len(results) == 0:
        raise ValueError("No data")

    # Additional sorting options can be added here and passed as arguments to the application
    if args.sorting == 'alphabetical':
        results.sort(key=lambda x: x.get("first_name") + " " + x.get("second_name"), reverse=False)


    # Header for results
    print("==========================")
    print("Results")
    print("==========================")

    # Print out results
    for result in results:
        print(f"{result.get('first_name')} {result.get('second_name')}")

    # Print out best score
    print(f"Score: {best_score}")

    # Footer for results
    print("==========================")


'''
Entry point to program
'''
if __name__ == "__main__":
    main()
