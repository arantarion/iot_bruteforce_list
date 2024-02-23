import os

def process_directory(directory):
    unique_lines = set()
    all_lines = 0
    no_files = 0

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                lines = file.readlines()
                all_lines += len(lines)
                no_files += 1
                for line in lines:
                    line = line.strip()
                    if ":" in line:
                        _, second_part = line.split(":", 1)
                        unique_lines.add(second_part)
                    else:
                        unique_lines.add(line)

    output_list = sorted(list(unique_lines))

    with open("output.txt", 'w') as output_file:
        for line in output_list:
            output_file.write(line + '\n')

    print("Processing complete. Check output.txt file.")
    print("Statistics:")
    print(f"Total lines in all files: {all_lines}")
    print(f"Total unique lines: {len(unique_lines)}")
    print(f"Number of files processed: {no_files}")



if __name__ == '__main__':
    directory = os.getcwd()
    process_directory(directory)