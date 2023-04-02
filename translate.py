
def read_from_file():
    global words_bank
    f = open('translate.txt','r')
    temp = f.read().split('\n')
    words_bank = []
    for i in range(0, len(temp), 2):
        my_dict = {"en":temp[i], "fa":temp[i+1]}
        words_bank.append(my_dict) 
    f.close()

read_from_file()

user_text = input("Enter your english text: ")
user_words = user_text.split(' ')

for user_word in user_words:
    for word in words_bank:
        if user_word == word['en']:
            print(word['fa'], end=' ')
            break



