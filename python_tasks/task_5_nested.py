# Task: Deep Dictionary Navigation
# Instructions: Extract 'year'. If any key is missing, return "Unknown".

def get_vehicle_year(data):
    # TODO: Write your logic here safely
    
    # we can through a loop from starting to end of data;
    # then check for the the year in keys(). if we found out return "we have all data" else " return key is missing or unknown" Time complexity: O(n), no need of space : o(1)

# Test Case
vehicle = {'specs': {'model_info': {'year': 2024}}}
# Expected: 2024
print(get_vehicle_year(vehicle))
