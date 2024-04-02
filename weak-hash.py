import argparse

def calc_weak_hash(input_string):
    """A deliberately weak hash function for educational purposes.
    This function computes a hash by summing the ASCII values of the characters
    in the input string, then takes that sum modulo 256."""
    # Compute the sum of ASCII values
    ascii_sum = sum(ord(char) for char in input_string)
    # Return the sum modulo 256
    return ascii_sum % 256
    
def main():
    parser = argparse.ArgumentParser(description='Calculate the sum of ASCII values of the input string.')
    parser.add_argument('-i', '--input', type=str, required=True, help='Input string')
    
    args = parser.parse_args()
    
    sum_result = calc_weak_hash(args.input)
    print(f"The sum of the ASCII values: {sum_result}")

if __name__ == "__main__":
    main()

