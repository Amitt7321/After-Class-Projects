def binary_to_decimal(binary_str):
    """Converts a binary string to a decimal integer."""

    binary_str = str(binary_str)
    decimal_value = 0
    reversed_binary = binary_str[::-1]
    
    for index, digit in enumerate(reversed_binary):

        if digit == '1': 
            decimal_value += 2 ** index
            
    return decimal_value

def decimal_to_binary(decimal_num):
    """Converts a decimal integer to a binary string."""
    if decimal_num == 0:

        return "0" 

    binary_str = "" 
    
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_str = str(remainder) + binary_str
        decimal_num = decimal_num // 2
        
    return binary_str

if __name__ == "__main__": 

    print("--- Binary to Decimal Conversion ---")
    binary_examples = [1101, 1000]
    
    for b in binary_examples:
        print(f"Binary: {b}₂ -> Decimal: {binary_to_decimal(b)}₁₀")

    print("\n--- Decimal to Binary Conversion ---")
    decimal_examples = [13, 8]
    
    for d in decimal_examples:
        print(f"Decimal: {d}₁₀ -> Binary: {decimal_to_binary(d)}₂")
