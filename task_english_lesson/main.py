def add():
    help_verb_past_simple = ['was', 'were']
    help_verb_present_simple = ['am', 'is', 'are']
    help_verb_future_simple = ['shall be', 'will be']
    help_verb_past_continious = [word + ' being' for word in help_verb_past_simple]
    help_verb_present_continious = [word + ' being' for word in help_verb_present_simple]
    help_verb_past_perfect = ['had been']
    help_verb_present_perfect = ['has been', 'have been']
    help_verb_future_perfect = ['shall have been', 'will have been']
    type_of_passive = ['Past Simple', 'Present Simple', 'Future Simple', 'Past Continious',
                       'Present Continious', 'Past Perfect', 'Present Perfect', 'Future Perfect']
    example_sentence = {'past simple':'My neighbour’s bike was stolen.', 'present simple':'She is said to have a boyfriend.', 'future simple':'New fitness center will be opened next week.',
                        'past continious':'The exam was being taken yesterday morning', 'present continious':'The car is being refueled now.', 'present perfect':'The flowers have already been watered.',
                        'past perfect':'The pizza had been delivered when he came back home.', 'future perfect':'The article will have been rewritten by tomorrow morning.'}

    print('Hello!\nIf you want to know the type of passive voice - print your sentence,\nif you want to see examples of sentences in the passive voice - press 1,\nif you want to end the program - press 0!')
    verbs = []
    with open('verbs.txt', 'r') as f:
        line = f.readline()
        while line:
            line = line.replace('\n', '')
            verbs.append(line)
            line = f.readline()
    while True:
        sentence = str(input('Print here: '))
        if sentence == '0':
            break
        elif sentence == '1':
            sentence = str(input('Print type of Passive Voice here: ')).lower()
            try:
                print(example_sentence[sentence])
            except:
                print('Incorrect input')
        else:
            sent = sentence
            sentence = sentence.split(' ')
            type_of_sentence = ''
            index = ''
            if len(sentence) <= 1:
                pass
            else:
                for word in range(len(sentence) - 1):
                    if list(filter(lambda x: x in sent, help_verb_future_perfect)) != []:
                        type_of_sentence = type_of_passive[7]
                        index = word + 2
                    elif sentence[word] + ' ' + sentence[word + 1] in help_verb_present_perfect:
                        type_of_sentence = type_of_passive[6]
                        index = word + 1
                    elif sentence[word] + ' ' + sentence[word + 1] in help_verb_past_perfect:
                        type_of_sentence = type_of_passive[5]
                        index = word + 1
                    elif sentence[word] + ' ' + sentence[word + 1] in help_verb_present_continious:
                        type_of_sentence = type_of_passive[4]
                        index = word + 1
                    elif sentence[word] + ' ' + sentence[word + 1] in help_verb_past_continious:
                        type_of_sentence = type_of_passive[3]
                        index = word + 1
                    elif sentence[word] + ' ' + sentence[word + 1] in help_verb_future_simple:
                        type_of_sentence = type_of_passive[2]
                        index = word + 1
                    elif sentence[word] in help_verb_past_simple:
                        type_of_sentence = type_of_passive[0]
                        index = word
                    elif sentence[word] in help_verb_present_simple:
                        type_of_sentence = type_of_passive[1]
                        index = word
                    if type_of_sentence:
                        break
            try:
                sentence[index + 1]
            except:
                type_of_sentence = ''
            if type_of_sentence and (sentence[index + 1] in verbs or sentence[index + 1][-2:] == 'ed'):
                print(f"It is {type_of_sentence}")
                continue
            else:
                print('This is not a passive sentence')
                continue

if __name__ == '__main__':
    add()
