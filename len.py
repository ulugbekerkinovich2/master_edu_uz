import json

# Load the JSON data from a file
with open('new_cleaned_data_lex_uz_masters.json', 'r', encoding='utf-8-sig') as file:
    data_magistr_latest = json.load(file)

# Calculate the number of objects
object_count = len(data_magistr_latest)

# Print the result
print("Number of objects:", object_count)
