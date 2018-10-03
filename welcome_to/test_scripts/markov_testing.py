import random
# import custom_markov as cmarkov

total_daesien = open('text_corpuses/totaldeasiean.txt', encoding='utf8').read()
corpus = total_daesien.split()

def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])

pairs = make_pairs(corpus)

word_dict = {}
for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

first_word = random.choice(corpus)
while first_word.islower():
    first_word = random.choice(corpus)
chain = [first_word]
n_words = 30

for i in range(n_words):
    chain.append(random.choice(word_dict[chain[-1]]))

# print(' '.join(chain))


# print(cmarkov.one_word_markov_slide_seed(corpus,20,"My special hyperventilating"))


def process_seeds(slide_seed):
    single_lines = slide_seed.splitlines()
    if not single_lines:
        good_seed = "What a beautiful image"
    else:
        single_lines = [line for line in single_lines if line != '']
        choosen_line = random.choice(single_lines)
        # print(choosen_line)
        good_seed = choosen_line.split()
    return(good_seed)

the_seed = '''
RESOURCES

The Best Code is No Code At All

increase the
productivity
expressive power of the code . Less

code to do the same thing (and possibly better).



@theburningmonk
'''

# print(process_seeds(the_seed))


def one_word_markov_slide_seed(corpus,num_words,slide_seed):
    pairs = make_pairs(corpus)

    word_dict = {}
    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]

    first_words = process_seeds(slide_seed)
    chain = first_words
    print(chain)
    n_words = num_words

    for i in range(n_words):
        if word_dict.get(chain[-1]) == None:
            new_seed = random.choice(corpus)
            while new_seed.isupper():
                new_seed = random.choice(corpus)
            chain.append(new_seed)
        else:
            chain.append(random.choice(word_dict[chain[-1]]))

    return(' '.join(chain))


print(one_word_markov_slide_seed(corpus,20,the_seed))
