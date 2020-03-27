import nltk
import re
import string

from nltk.tokenize import sent_tokenize
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
from nltk import SnowballStemmer
from nltk.stem import WordNetLemmatizer


def to_lower_case(text):
    return text.lower()


def tokenize_paragraph(paragraph):
    # Tokenise paragraphs to sentences
    return sent_tokenize(paragraph)


def tokenize_sentence(sentence):
    # Tokenise sentences to words
    return TreebankWordTokenizer().tokenize(sentence)


def remove_numbers(text):
    return re.sub(r"\d+", "", text)


def remove_punctuation(words):
    return [w for w in words if w not in string.punctuation]


def remove_stopwords(words):
    return [w for w in words if w not in stopwords.words("english")]


def remove_whitespaces(text):
    return "".join(text.split())


def stemming(word):
    # Fast algorithm to get almost every word stem - sometimes the result is no word anymore
    return SnowballStemmer("english").stem(word)


def lemmatize(word):
    # Correct algorithm to get word stem (by dictionary)
    return WordNetLemmatizer().lemmatize(word)


class TextPreProcessor:

    def __init(self):
        nltk.download("punkt")
        nltk.download("stopwords")
        nltk.download("wordnet")

    def pre_process_text(self, text):
        lower_text = to_lower_case(text)
        sentences = tokenize_paragraph(lower_text)
        sentences_words = [tokenize_sentence(sentence) for sentence in sentences]
        # flatten list
        words = [word for sentence in sentences_words for word in sentence]
        number_free_words = [remove_numbers(word) for word in words]
        punctuation_free_words = remove_punctuation(number_free_words)
        stopwords_free_words = remove_stopwords(punctuation_free_words)
        whitespace_free_words = [remove_whitespaces(word) for word in stopwords_free_words]
        lemmas = list({lemmatize(word) for word in whitespace_free_words})
        lemmas.sort()
        return lemmas


if __name__ == "__main__":
    text = """FinTechExplained3465 aims to explain how text processing works. 213 Once we have gathered the text, the 
    next stage is about cleaning and consolidating the text. It is important to ensure the text is standardised and the 
    noise is removed 09654     so that efficient analysis can be performed on the text to derive meaningful insights."""

    text_pre_processor = TextPreProcessor()
    print(text_pre_processor.pre_process_text(text))
