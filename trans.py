import argparse

# Setup argparse to receive command-line arguments
parser = argparse.ArgumentParser(description='Transfer hex values from input to output.')
parser.add_argument('input_file', type=str, help='Path to the input file.')
parser.add_argument('--split', action='store_true', help='Split output into header.txt and data.txt')
args = parser.parse_args()

# Read input_file specified as command-line argument
input_file = args.input_file

with open(input_file, 'r') as file:
    hex_values = file.read().splitlines()

code_values = [chr(int(hex_value, 16)) for hex_value in hex_values]

# Check if the split flag is set
if args.split:
    header_values = code_values[:143]
    data_values = code_values[143:]

    with open('header.txt', 'wb') as file:
        for code_value in header_values:
            file.write(code_value.encode('ISO-8859-1'))
    
    with open('data.txt', 'wb') as file:
        for code_value in data_values:
            file.write(code_value.encode('ISO-8859-1'))
else:
    # Modify output file name if needed
    output_file = './output.txt'

    with open(output_file, 'wb') as file:
        for code_value in code_values:
            file.write(code_value.encode('ISO-8859-1'))
