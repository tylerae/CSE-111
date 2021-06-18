import random

def main():
    print(f'{get_determiner}, {get_noun}, {get_verb}.')

def get_determiner(quantity):
    if quantity == 1:
        words = ["the", "one"]
    else:
        words = ["some", "many"]
    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == 1:
        words = ['dog' , 'cat' , 'mom' , 'Tyler' , 'dad']
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    if quantity == 1:
        words = ['runs' , 'talks' , 'yells' , 'plays' , 'sits' , 'sleeps']
    else:
        words = ['ran' , 'talked' , 'yelled' , 'played' , "sat" , 'slept']
    word = random.choice(words)
    return word



