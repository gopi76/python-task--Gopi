# Task: String Formatting
# Goal: Transform a raw SKU into a readable title.

def format_sku(sku_string):
    """
    Instructions: Convert 'engine-oil-10w30' to 'Engine Oil 10w30'.
    """
    # TODO: Implement logic
    if not sku_string:
        return "empty string"
    result = []
    sku_string = sku_string.strip("-")
    print(sku_string)
    for i in range(len(sku_string)):
        if sku_string[i]=="-":
            result.append(sku_string[:i])

    return ''.join(result)

# we can use one loop - O(n) - time complexity. lower - we cna use .lower() or .upper()
 #for upper case

# or we cna use ord(stirng_character) >=65 and  <= 90. we can keep upper. and ord() 122 to 148 can use lowercase




sku_string = 'engine-oil-10w30'

print(format_sku(sku_string))

# Test: format_sku("brake-pads-ceramic") -> "Brake Pads Ceramic"
