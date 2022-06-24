book_name = input()
number_book = 0
is_book_found = False
book = (input())
while book != 'No More Books':
    if book == book_name:
        is_book_found = True
        print(f'You checked {number_book} books and found it.')
        break
    number_book += 1
    book = input()
if not is_book_found:
    print(f'The book you search is not here!')
    print(f'You checked {number_book} books.')

