from flair.models import TextClassifier
from flair.data import Sentence

classifier = TextClassifier.load('en-sentiment')
sentence = Sentence('I think climate change is bunk, climate change is bunk, climate change is bunk, climate change is bunk, climate change is bunk, climate change is bunk, climate change is bunk, climate change is bunk, climate change is bunk!')
classifier.predict(sentence)
# print sentence with predicted labels
print('Sentence above is: ', sentence.labels)
# print(sentence.category)