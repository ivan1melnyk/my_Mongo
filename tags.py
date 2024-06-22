import json

def get_unique_tags(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    tags = set()
    
    for quote in data:
        for tag in quote.get('tags', []):
            tags.add(tag)
    
    return list(tags)

if __name__ == "__main__":
    json_file = 'json/quotes.json'
    unique_tags = get_unique_tags(json_file)
    print("Unique tags:", unique_tags)

    with open('json/tags.json', 'w') as json_file:
        json.dump(unique_tags, json_file, indent=4)

    print("Tags have been written to tags.json")