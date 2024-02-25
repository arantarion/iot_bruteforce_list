import csv

def process_csv(filename):
    unique_pairs = set()

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Skip the header row

        # Find the index of the "productvendor" column
        productvendor_index = headers.index("productvendor")

        for row in reader:
            # Replace "<blank>" with an empty string
            row = [cell if cell != "<blank>" else "" for cell in row]

            # Get the elements in the row excluding the "productvendor" column
            elements = [cell for i, cell in enumerate(row) if i != productvendor_index]

            # Generate pairs
            pairs = [":".join([str(cell1), str(cell2)]) for cell1 in elements for cell2 in elements]

            # Add the pairs to the set
            unique_pairs.update(pairs)

    with open("pw_username_pairs_unique.txt", 'w') as output_file:
        for pair in unique_pairs:
            output_file.write(pair + '\n')

    print("Processing complete. Check pw_username_pairs_unique.txt file.")


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print('Usage: python script.py <filename>')
    else:
        filename = sys.argv[1]
        process_csv(filename)
