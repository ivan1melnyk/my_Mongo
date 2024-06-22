import json
from datetime import datetime

def update_born_date_format(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:  # Specify UTF-8 encoding
        authors_data = json.load(file)
    
    updated_authors = []
    
    for author in authors_data:
        born_date_str = author.get('born_date', '')
        try:
            # Convert the born_date to YYYY-MM-DD format
            born_date = datetime.strptime(born_date_str, '%B %d, %Y').strftime('%Y-%m-%d')
        except ValueError:
            born_date = born_date_str  # If parsing fails, keep original format
        
        # Update the author dictionary
        author['born_date'] = born_date
        updated_authors.append(author)
    
    # Write the updated data back to the output file
    with open(output_file, 'w', encoding='utf-8') as outfile:  # Specify UTF-8 encoding
        json.dump(updated_authors, outfile, indent=4, ensure_ascii=False)  # ensure_ascii=False for non-ASCII characters

if __name__ == "__main__":
    input_file = 'json/authors.json'
    output_file = 'json/authors_updated.json'
    update_born_date_format(input_file, output_file)
    print(f"Updated authors data with correct born_date format saved to {output_file}")


