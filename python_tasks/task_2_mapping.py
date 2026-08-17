# Task: Dictionary Frequency Mapping
# Instructions: Return a dictionary where keys are categories 
# and values are the count of occurrences.

def count_categories(categories):
    # TODO: Write your logic here
    if not categories:
        return "empty list"
    
    seen = {}
    for i in range(len(categories)):
        if categories[i] not in seen:
            seen[i] = categories[i]
        else:
            seen[categorie[i]] += 1
    return seen

    #we can use hashmap to complete the solution : time complexity: O(n),space complexity : O(n)

# Test Case
data = ['Brakes', 'Engine', 'Brakes', 'Tools', 'Engine', 'Brakes']
# Expected: {'Brakes': 3, 'Engine': 2, 'Tools': 1}
print(count_categories(data))
