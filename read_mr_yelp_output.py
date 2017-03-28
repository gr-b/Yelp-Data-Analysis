import sys, json, math, nltk
undesirables = ['CC','IN','TO','DT']

words = {}
wordlist = open('output.txt','r')
for line in wordlist:
    firstspace = line.strip().index('{')
    word = line[0:firstspace]
    info = line[firstspace-1:]
    infoDict = json.loads(info.strip())
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

for line in sys.stdin:
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
        continue
    print 'Our score: {0:.2f} | Their score: {}'.format(total/count, review['stars']) 
            
