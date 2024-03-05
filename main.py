import os

def print_count_words(text):
    split_text = text.replace('\n', ' ').split(' ')
    split_text = [s for s in split_text if s != '']
    print(len(split_text))

def print_count_distinct_characters(text):
    distinct_character_count = {}
    for c in text.lower():
        distinct_character_count[c] = distinct_character_count.get(c, 0) + 1
    sorted_dict = dict(sorted(distinct_character_count.items(), key=lambda item: item[1], reverse=True))
    for key, val in sorted_dict.items():
        if key.isalpha():
            print(f"- The {key} character was found {val} times")


def main():
    book_dir_path = 'books/'
    if os.path.exists(book_dir_path):
        books = os.listdir(book_dir_path)
        for book in books:
            with open(f'{book_dir_path}/{book}', 'r') as f:
                text = f.read()
                print(f'--- Begin report for {book} ---')
                print('Number of words:')
                print_count_words(text)
                print('Distict character analysis:')
                print_count_distinct_characters(text)
                print('--- End report ---\n')
    else:
        print(f'The books directory ({book_dir_path}) was not found.')
main()