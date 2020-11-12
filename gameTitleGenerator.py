import random

# make titles in one of many ways:
# http://www.ashley-bovan.co.uk/words/partsofspeech.html

one_nouns = set()
two_nouns = set()
one_verbs = set()
two_verbs = set()

with open("pos-files/nouns/1syllablenouns.txt") as f:
    raw_nouns = f.readlines()
    one_nouns = [n.strip() for n in raw_nouns]

with open("pos-files/nouns/2syllablenouns.txt") as f:
    raw_nouns = f.readlines()
    two_nouns = [n.strip() for n in raw_nouns]

with open("pos-files/verbs/1syllableverbs.txt") as f:
    raw_verbs = f.readlines()
    one_verbs = [v.strip() for v in raw_verbs]

with open("pos-files/verbs/2syllableverbs.txt") as f:
    raw_verbs = f.readlines()
    two_verbs = [v.strip() for v in raw_verbs]    

def generateTitle(titleType):
    # 0 Noun
    if titleType == 0:
        title = capitalise(pickSyllables(one_nouns, two_nouns))
    # 1 Noun Verb
    if titleType == 1:
        title = capitalise(pickSyllables(one_nouns, two_nouns)) + random.choice(one_verbs)
    # 2 Verb Noun
    if titleType == 2:
        title = capitalise(pickSyllables(one_verbs, two_verbs)) + random.choice(one_nouns)
    # 3 Noun Noun
    if titleType == 3:
        title = capitalise(pickSyllables(one_nouns, two_nouns)) + random.choice(one_nouns)
    # 4 Verb of the Noun
    if titleType == 4:
        title = capitalise(pickSyllables(one_verbs, two_verbs)) + " of the " + capitalise(pickSyllables(one_nouns, two_nouns))
    # 5 Verb of Noun
    if titleType == 5:
        title = capitalise(pickSyllables(one_verbs, two_verbs)) + " of " + capitalise(pickSyllables(one_nouns, two_nouns))
    # 6 Noun + craft    
    if titleType == 6:
        title = capitalise(pickSyllables(one_nouns, two_nouns)) + "craft"
    # 7 Noun and Noun
    if titleType == 7:
        title = capitalise(pickSyllables(one_nouns, two_nouns)) + " and " + capitalise(pickSyllables(one_nouns, two_nouns))

    return title

def capitalise(word):
    first_letter = word[0]
    rest = word[1:]
    return first_letter.upper() + rest

def pickSyllables(one, two): 
    if random.random() > 0.5:
        return random.choice(one)
    else:
        return random.choice(two)

def selectPlatforms():
    platform_string = ''
    platforms = ['Windows', 'Mac', 'Linux']
    amount = random.randint(1, 3)
    for i in range(amount):
        platform_string += platforms[i]
        if i < amount-1:
            platform_string += ", "
    return platform_string

def selectPrice():
    price = ''
    if random.random() > 0.1:
        price = "$" + str(random.randint(0, 59))
        if random.random() > 0.5:
            price += ".99"
    else:
        price = 'Free'
    return price

def selectReviewScore():
    score = random.randint(0, 100)
    review_colour = ''
    if score >= 75:
        review_colour = 'positive'
    elif score < 75 and score >= 50:
        review_colour = 'mixed'
    else:
        review_colour = 'negative'
    return [score, review_colour]

# for i in range(10):
    # print(generateTitle(random.randint(0, 7)))
    # print(generateTitle(1))