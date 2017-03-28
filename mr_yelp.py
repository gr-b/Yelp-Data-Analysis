from mrjob.job import MRJob
import json, nltk
from nltk.stem.snowball import SnowballStemmer
undesirables = ['CC','IN','TO','DT']
stemmer = SnowballStemmer('english')

class MRWordScore(MRJob):

    def mapper(self, _, line):
        review = json.loads(line.strip())
        cleaned_text = clean_text(review['text'])
        clean_words = cleaned_text.split()
        cleaner_text = remove_unecessary_pos(cleaned_text).split()
        #stemmed_words = [stemmer.stem(word) for word in cleaner_text.split()]
        score = float(review['stars'])
        for word in cleaner_text:
            yield (word, score)

    '''def combiner(self, word, counts):
        length = len(list(counts))
        if length == 0:
            yield (word, 0)
        yield (word, int(sum(counts)/length)) # Average score'''

    def reducer(self, word, counts):
        total = 0
        count = 0
        for num in counts:
            total += num
            count += 1
        #if count == 0:
        #    yield (word, (0, count))
        if count < 10:
            return
        yield (word, {'score':total/count, 'count':count}) # Average score

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


#dataset = open('yelp_academic_dataset_review.json','r')

#clean_reviews = []

def write_data(clean_reviews):
    with open('clean_reviews.json','a') as outfile:
        print 'Writing {0} reviews to file.'.format(len(clean_reviews))
        [outfile.write(json.dumps(review) + '\n') for review in clean_reviews]
        #outfile.write(json.dumps(clean_reviews))
        outfile.close()
'''
# Clean and sort reviews by business_id
i = 0
for line in dataset:
    review = json.loads(line.strip())
    cleaned_text = clean_text(review['text'])
    cleaner_text = remove_unecessary_pos(cleaned_text)
    stemmed_words = [stemmer.stem(word) for word in cleaner_text.split()])
    print stemmed_string

    i += 1
    if i > 5:
        break'''

MRWordScore.run()
dataset.close()
    



