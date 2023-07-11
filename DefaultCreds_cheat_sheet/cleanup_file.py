def filter_file(input_file, output_file, keywords):
    with open(input_file, 'r') as file:
        lines = file.readlines()

        filtered_lines = [line for line in lines if not any(keyword in line for keyword in keywords) and line.count(' ') < 3]

    with open(output_file, 'w') as file:
        file.writelines(filtered_lines)

    print("Filtering complete. Check the output file.")


if __name__ == '__main__':
    input_file = "pw_username_pairs_unique.txt"
    output_file = "cleanedup_pw_username_pairs.txt"
    keywords = ["[", "]", "(", ")", "{", "}", "calculated", "generated", "<<<"]

    filter_file(input_file, output_file, keywords)