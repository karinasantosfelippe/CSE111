import random

def main():
    sort_list = ['fish', 'catfish', 'giraffe', 'whale', 'turtle', 'alligator', 'baboon', 'bird', 'urchin', 'lion', 'tuiuiu', 'toucan', 'ostrith', 'ant', 'orangutan', 'kong', 'spider', 'shark', 'tiger', 'butterfly', 'wild dog']
    print(sort_list)
    
    while len(sort_list) > 0:
        _ = input("Are you ready? (press enter)")
        word = random.choice(sort_list)
        print(word)
        sort_list.remove(word)
        print(sort_list)

if __name__ == "__main__":
    main()