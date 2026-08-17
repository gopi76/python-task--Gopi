# Task: Error Handling & Resilience
# Goal: Calculate a discount safely.

def calculate_discount(price, discount_percent):
    """
    Instructions: Handle cases where discount_percent is 0 
    or if inputs are strings/None. Return 0 for invalid inputs.
    """
    # TODO: Implement logic
    #temp = str(discount_percent)
    
    if discount_percent == 0:
        return 0
    
    if dtype(discount_percent) == "string":
        return "discount should not be string"

    #we can use type of the variable based on that we can write a condition to handle for the strings
    
    
    # we can use try and except concept also
    

# Test Case
print(calculate_discount(100, "10")) # Should return 0 or handle conversion
print(calculate_discount(100, 0))    # Should return 0
