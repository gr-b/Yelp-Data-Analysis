import sys, json, math, nltk, random
undesirables = ['CC','IN','TO','DT']

def log(n):
    return math.log(n) - 1.3

def calcscore(score):
    if score < 24.17:
        return 1
    elif score < 24.75:
        return 2
    elif score < 25.2:
        return 3
    elif score < 25.45:
        return 4
    else:
        return 5

words = {}
wordlist = open(sys.argv[1],'r')
for line in wordlist:
    firstspace = line.strip().index('{')
    word = line[0:firstspace][1:-2]
    info = line[firstspace-1:]
    infoDict = json.loads(info.strip())
    score = infoDict['score']
    count = infoDict['count']
    infoDict['score'] = score*log(count)
    words[word] = infoDict
    #print word, '{0:.2f}'.format(infoDict['score'])

'''sorted_words = sorted(words, key=lambda x: x['score'], reverse=True)

for wordDict in sorted_words:
    score = wordDict['score']
    count = wordDict['count']
    print wordDict['word'], '{0:.2f}'.format(wordDict['score'])'''

def clean_text(text):
    # Get rid of all bad characters, and uppercase.
    new_text = ''
    for c in text:
        if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            new_text += c.lower()
        elif c in 'abcdefghijklmnopqrstuvwxyz ':
            new_text += c
    return new_text

def remove_unecessary_pos(text):
    pos_list = nltk.pos_tag(text.split())
    #print pos_list
    new_text = ''
    for pos in pos_list:
        if pos[1] in undesirables:
            pass
        else:
            new_text += pos[0] + ' '
    return new_text


scores = {}

i = 0
for line in open(sys.argv[2], 'r'):
    review = json.loads(line.strip())
    cleaned_text = clean_text(review['text'])
    cleaner_words = remove_unecessary_pos(cleaned_text).split()
    total = 0
    count = 0
    for word in cleaner_words:
        if word in words.keys():
            total += words[word]['score']
            count += 1
        if count == 0:
            print 'Continuing ' + word
    if count == 0:
        continue
    score = total/count
    print 'Our score: {0:.2f} | Their score: {1}'.format(int(calcscore(score)), review['stars'])
    #scores += (score, int(review['stars']))
    if review['stars'] not in scores.keys():
        scores[review['stars']] = []
    scores[review['stars']] += [score]
    i += 1
    if i > 50:
        break

for key, scorelist in scores.items():
    total = 0
    for score in scorelist:
        total += score
    print 'Average for {} : {}'.format(key, total/len(scorelist))





            
