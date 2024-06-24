def find_duplicate_names(names):
    seen = set()
    duplicates = set()
    
    for name in names:
        if name in seen:
            duplicates.add(name)
        else:
            seen.add(name)
    
    return duplicates

# Example usage
names_list = ["Tom", "Jerry", "Mike", "Tom"]
result = find_duplicate_names(names_list)
print(result)  # Output: {'Tom'}
