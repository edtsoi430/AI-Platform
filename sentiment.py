# Still under development. Created by Edmond Tsoi @ 2019. 
import signal
import sys
from google.cloud import language
from google.api_core.exceptions import InvalidArgument
import os

print('Credendtials from environ: {}'.format(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')))
# create a Google Cloud Natural Languague API Python client
client = language.LanguageServiceClient()


# a function which takes a block of text and returns its sentiment and magnitude
def detect_sentiment(text):
    """Detects sentiment in the text."""

    document = language.types.Document(
        content=text,
        type=language.enums.Document.Type.PLAIN_TEXT)

    sentiment = client.analyze_sentiment(document).document_sentiment

    return sentiment.score, sentiment.magnitude


# keep track of count of total comments and comments with each sentiment
count = 0
positive_count = 0
neutral_count = 0
negative_count = 0


def print_summary():
    print()
    print('Total comments analysed: {}'.format(count))
    print('Positive : {} ({:.2%})'.format(positive_count, positive_count / count))
    print('Negative : {} ({:.2%})'.format(negative_count, negative_count / count))
    print('Neutral  : {} ({:.2%})'.format(neutral_count, neutral_count / count))


# register a signal handler so that we can exit early
def signal_handler(signal, frame):
    print('KeyboardInterrupt')
    print_summary()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

# read our comments.txt file
with open('comments.txt', encoding='utf-8') as f:
    for line in f:
        # use a try-except block since we occasionally get language not supported errors
        try:
            score, mag = detect_sentiment(line)
        except InvalidArgument as e:
            # skip the comment if we get an error
            print('Skipped 1 comment: ', e.message)
            continue

        # increment the total count
        count += 1

        # depending on whether the sentiment is positve, negative or neutral, increment the corresponding count
        if score > 0:
            positive_count += 1
        elif score < 0:
            negative_count += 1
        else:
            neutral_count += 1

        # calculate the proportion of comments with each sentiment
        positive_proportion = positive_count / count
        neutral_proportion = neutral_count / count
        negative_proportion = negative_count / count

        print(
            'Count: {}, Positive: {:.3f}, Neutral: {:.3f}, Negative: {:.3f}'.format(
                count, positive_proportion, neutral_proportion, negative_proportion))

print_summary()