import sys
import os

# Function to convert "\xXX" format to "0xXX" format
def convert_to_0x(input_data, output):
    byte_count = 0  # Counter for bytes written in the current line
    first_byte = True  # Flag to handle comma placement correctly

    idx = 0
    while idx < len(input_data):
        if input_data[idx] == '\\' and idx + 1 < len(input_data) and input_data[idx + 1] == 'x':
            idx += 2  # Skip "\x"
            if idx + 1 < len(input_data):
                if byte_count > 0 or not first_byte:
                    output.write(", ")  # Add a comma and space before each new byte
                output.write(f"0x{input_data[idx]}{input_data[idx + 1]}")
                byte_count += 1
                first_byte = False

                # Check if we've written 16 bytes; if so, add a newline
                if byte_count % 16 == 0:
                    output.write(",\n")  # Add a comma and newline after every 16 bytes
                    byte_count = 0  # Reset byte count after line break
                idx += 2  # Skip the two characters after "\x"
        else:
            output.write(input_data[idx])  # Copy other characters as is
            idx += 1

    # If there were bytes written, add a final newline
    if byte_count > 0:
        output.write("\n")

# Function to convert "0xXX" format to "\xXX" format
def convert_to_xX(input_data, output):
    byte_count = 0  # Counter for bytes written in the current line
    idx = 0

    while idx < len(input_data):
        if input_data[idx] == ',' or input_data[idx] == ' ':
            idx += 1
            continue

        if input_data[idx:idx + 2] == "0x":
            idx += 2  # Skip "0x"
            if idx + 1 < len(input_data):
                output.write(f"\\x{input_data[idx]}{input_data[idx + 1]}")
                byte_count += 1

                # Check if we've written 16 bytes; if so, add a newline
                if byte_count % 16 == 0:
                    output.write("\n")  # Add a newline after every 16 bytes
                    byte_count = 0
                idx += 2  # Move past the two hex characters
        else:
            output.write(input_data[idx])
            idx += 1

    # If there were bytes written, add a final newline
    if byte_count > 0:
        output.write("\n")

# Function to handle the file conversion
def convert_file(input_file, output_file, conversion_flag):
    try:
        with open(input_file, "r") as input, open(output_file, "w") as output:
            for line in input:
                line = line.strip()  # Remove any trailing newline characters

                if conversion_flag == "-xX":
                    convert_to_0x(line, output)
                elif conversion_flag == "-0x":
                    convert_to_xX(line, output)
                else:
                    print(f"Invalid conversion flag: {conversion_flag}")
                    sys.exit(1)
        print(f"Conversion completed. Output written to {output_file}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

# Main function to handle command line arguments
if __name__ == "__main__":
    if len(sys.argv) < 5:
        print(f"Usage: {sys.argv[0]} -xX|-0x <input_file> -out <output_file>")
        sys.exit(1)

    conversion_flag = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[4]

    convert_file(input_file, output_file, conversion_flag)
