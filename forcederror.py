from random import randint
import copy

word_dict = {
    'adjective':['selfish','abrasive','grubby','groovy','rich','annoying','disgusting','fast'], 
    'city name':['Chicago','New York','Austin','Houston','Highland','Sugar Land'], 
    'noun':['people','map','music','dog','hamster','ball','hotdog','salad'], 
    'action verb':['programmed','play','laugh','listen','walk','write','drive','executed','controlled'], 
    'sports noun':['ball','mit','puck','uniform','helmet','scoreboard','player']
}

story = (
    "One day my {} friend and I decided to go to the {} game in {}. "+
    "We really wanted to see the {} play the {}. So, we {} our {} "+ 
    "down to the {} and bought some {}s. We got into the game and "+
    "it was a lot of fun. We ate some {} {} and drank some {} {}. "+
    "We had a great time! We plan to go again next year!"
)



def get_word(type, local_dict):
    ''' get a random word from the word_dict based on word type '''
    words = local_dict[type]
    cnt = len(words)-1
    index = randint(0, cnt)
    return local_dict[type].pop(index)


def create_story():
    ''' create a random story from word dict '''
    # create a local copy of the dict so that we can pop words as used
    local_dict = copy.deepcopy(word_dict)
    return story.format(
        get_word('adjective', local_dict), 
        get_word('sports noun', local_dict),
        get_word('city name', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('action verb', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('adjective', local_dict),
        get_word('noun', local_dict),
        get_word('adjective', local_dict),
        get_word('noun', local_dict)
)

def create_story_manual():
    ''' create a story from manual input '''
    return story.format(
        input("Enter adjective: "),
        input("Enter sports noun: "),
        input("Enter city name: "),
        input("Enter noun: "),
        input("Enter noun: "),
        input("Enter action verb: "),
        input("Enter noun: "),
        input("Enter noun: "),
        input("Enter noun: "),
        input("Enter adjective: "),
        input("Enter noun: "),
        input("Enter adjective: "),
        input("Enter noun: ")
    )


def story_automated():
    new_story = 'y'
    while new_story == 'y':
        print(create_story())
        new_story = input("Another story? Y/N: ").lower()

def story_manual():
    new_story = 'y'
    while new_story == 'y':
        print(create_story_manual())
        new_story = input("Another story? Y/N: ").lower()




def main():
    print("Would you like an automated story or manual one? A/M")
    choice = input(">").lower()
    if choice == 'a':
        story_automated()
    elif choice == 'm':
        story_manual()
    else: 
        print("Invalid selection")

main()