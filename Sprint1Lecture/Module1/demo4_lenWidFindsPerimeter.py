"""
Challenge #4
Create a function that takes lenght and width and finds the perimeter of a rectangle.

Examples:
- find_perimeter(6, 7) -> 26
- find_perimeter(20, 10) -> 60
- find_perimeter(2, 9) -> 22
"""
def find_perimeter(length, width):
    # formula: 2L + 2w
    return 2 * length + 2 * width

print(find_perimeter(6,7))  #26