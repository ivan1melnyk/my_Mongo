import json


def seach_by_name(value):
    quotes_list = list()
    with open('json/quotes.json', encoding='utf-8') as file:
        quotes = json.load(file)
        for quote in quotes:
            if quote["author"] == value:
                quotes_list.append(quote["quote"])
        return quotes_list


def seach_by_tags(comand, value):
    if comand == 'tag':
        with open('json/quotes.json', encoding='utf-8') as file:
            quotes = json.load(file)
            for quote in quotes:
                if value in quote["tags"]:
                    return quote["quote"]
    else:
        tags = value.split(',')
        quotes_list = list()
        with open('json/quotes.json', encoding='utf-8') as file:
            quotes = json.load(file)
            for quote in quotes:
                if any(tag in quote["tags"] for tag in tags):
                    quotes_list.append(quote["quote"])
            return quotes_list


def show_result(result):
    if isinstance(result, list):
        for item in result:
            print(item)
    else:
        print(result)


while True:
    user_input = input('команда: значення << ')
    if user_input == 'exit':
        break

    comand, value = [part.strip() for part in user_input.split(':')]

    if comand == 'name':
        show_result(seach_by_name(value))
    elif comand == 'tag':
        show_result(seach_by_tags(comand, value))
    elif comand == 'tags':
        show_result(seach_by_tags(comand, value))
    else:
        print('Command not found')
