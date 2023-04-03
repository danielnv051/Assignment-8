def show_menu():
    print('Welcome to my translator')
    print('1- Translate english to persian')
    print('2- Translate persian to english')
    print('3- Add new word to dictionary')
    print('4- Exit')

def read_from_file():
    global words_bank
    f = open('translate.txt','r')
    temp = f.read().split('\n')
    words_bank = []
    for i in range(0, len(temp), 2):
        my_dict = {"en":temp[i], "fa":temp[i+1]}
        words_bank.append(my_dict) 
    f.close()

def translate_english_to_persian():
    user_text = input("Enter your english text: ")
    user_words = user_text.split(' ')

    for user_word in user_words:
        for word in words_bank:
            if user_word == word['en']:
                print(word['fa'], end=' ')
                break
        else:
            print(user_word, end=' ')

read_from_file()
while True:
    show_menu()
    choice = int(input('enter your choice: '))
    if choice == 1:
        translate_english_to_persian()
    elif choice ==2:
        ...
    elif choice ==3:
        ...
    elif choice ==4:
        exit(0)