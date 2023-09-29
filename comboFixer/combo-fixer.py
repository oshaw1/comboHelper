import sys

def process_line(line):
    parts = line.split()
    formatted_parts = []

    for part in parts:
        if len(part) > 4:
            formatted_parts.append(part)
        else:
            if formatted_parts:
                return ':'.join(formatted_parts)

    return None

def main():
    if len(sys.argv) != 3:
        print("Usage: python combo-fixer.py input_file.txt output_file.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            formatted_parts = []
            for line in infile:
                username_password = process_line(line)
                if username_password:
                    outfile.write(username_password + '\n')
                formatted_parts = []  # Reset formatted_parts for the next line

        print(f"Processing completed. Result saved in '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The input file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
