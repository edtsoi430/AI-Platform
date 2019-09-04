# Still under development. Created by Edmond Tsoi @ 2019. 
import six
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

client = language.LanguageServiceClient()

with open("comments.txt", "r") as file:
    line = file.readline()
    while line:
        # print("Line {}".format(line.strip()))
        line = file.readline()
        text = line.strip()
        s = text.split()
        if(len(s) > 20):
            document = types.Document(
                content=text.encode('utf-8'),
                type=enums.Document.Type.PLAIN_TEXT)
            
            categories = client.classify_text(document).categories
            for category in categories:
                print(u'=' * 20)
                print(u'{:<16}: {}'.format('text', text))
                print(u'{:<16}: {}'.format('name', category.name))
                print(u'{:<16}: {}'.format('confidence', category.confidence))