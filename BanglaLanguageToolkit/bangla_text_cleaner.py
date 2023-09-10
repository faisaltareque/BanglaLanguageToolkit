import re
import sys
import unicodedata
from ftfy import fix_text
from unicodedata import category, normalize
from emoji import UNICODE_EMOJI, demojize, emojize
from BanglaLanguageToolkit.bangla_character import BanglaCharacter


class BanglaTextCleaner:
    def __init__(
            self,
            fix_unicode=True,
            unicode_norm=True,
            unicode_norm_form="NFKC",
            remove_url=False,
            remove_email=False,
            remove_number=False,
            remove_digits=False,
            remove_emoji=False,
            remove_punct=False,
            replace_with_url="<URL>",
            replace_with_email="<EMAIL>",
            replace_with_number="<NUMBER>",
            replace_with_digit="<DIGIT>",
            replace_with_punct = "<PUNC>"
        ):
        """
        Initialize BanglaTextCleaner class
        """
        self.bangla_character = BanglaCharacter()
        self.regex_patterns = {
            "BANGLA_DIGIT_REGEX" : re.compile(r'[০-৯]+'),
            "EMAIL_REGEX":re.compile(r"(?:^|(?<=[^\w@.)]))([\w+-](\.(?!\.))?)*?[\w+-](@|[(<{\[]at[)>}\]])(?:(?:[a-z\\u00a1-\\uffff0-9]-?)*[a-z\\u00a1-\\uffff0-9]+)(?:\.(?:[a-z\\u00a1-\\uffff0-9]-?)*[a-z\\u00a1-\\uffff0-9]+)*(?:\.(?:[a-z\\u00a1-\\uffff]{2,}))", flags=re.IGNORECASE | re.UNICODE,),
            "URL_REGEX":re.compile(r"(?:^|(?<![\w\/\.]))"    
                                   r"(?:(?:https?:\/\/|ftp:\/\/|www\d{0,3}\.))" # protocol identifier r"(?:(?:https?|ftp)://)"  <-- alt?    
                                   r"(?:\S+(?::\S*)?@)?" r"(?:" # user:pass authentication
                                   r"(?!(?:10|127)(?:\.\d{1,3}){3})"     # IP address exclusion private & local networks
                                   r"(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})"
                                   r"(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})"
                                   r"(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])" # IP address dotted notation octets, excludes loopback network 0.0.0.0, excludes reserved space >= 224.0.0.0 ,excludes network & broadcast addresses, (first & last IP address of each class)
                                   r"(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}"
                                   r"(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))"
                                   r"|"
                                   r"(?:(?:[a-z\\u00a1-\\uffff0-9]-?)*[a-z\\u00a1-\\uffff0-9]+)" # host name
                                   r"(?:\.(?:[a-z\\u00a1-\\uffff0-9]-?)*[a-z\\u00a1-\\uffff0-9]+)*" # domain name
                                   r"(?:\.(?:[a-z\\u00a1-\\uffff]{2,}))" r"|" r"(?:(localhost))" r")"     # TLD identifier
                                   r"(?::\d{2,5})?" # port number    
                                   r"(?:\/[^\)\]\}\s]*)?", # resource path
                                   flags=re.UNICODE | re.IGNORECASE,),
            "DOUBLE_QUOTE_REGEX" : re.compile("|".join(["«", "‹", "»", "›", "„", "“", "‟", "”", "❝", "❞", "❮", "❯", "〝", "〞", "〟", "＂",])),
            "SINGLE_QUOTE_REGEX" : re.compile("|".join(["‘", "‛", "’", "❛", "❜", "`", "´", "‘", "’"]))
        }
        self.fix_unicode = fix_unicode
        self.unicode_norm = unicode_norm
        self.unicode_norm_form = unicode_norm_form
        self.remove_url = remove_url
        self.remove_email = remove_email
        self.remove_number = remove_number
        self.remove_digits = remove_digits
        self.remove_emoji = remove_emoji
        self.remove_punct = remove_punct        
        self.replace_with_url = replace_with_url
        self.replace_with_email = replace_with_email
        self.replace_with_number = replace_with_number
        self.replace_with_digit = replace_with_digit
        self.replace_with_punct = replace_with_punct


    def fix_bad_unicode(self, text, normalization="NFC"):
        """
        Fix bad unicode characters in text
        """
        return fix_text(text, normalization=normalization)
    

    def fix_strange_quotes(self, text):
        """
        Replace strange quotes, i.e., 〞with a single quote ' or a double quote " if it fits better.
        """
        text = self.regex_patterns["SINGLE_QUOTE_REGEX"].sub("'", text)
        text = self.regex_patterns["DOUBLE_QUOTE_REGEX"].sub('"', text)
        return text
    

    def replace_urls(self, text, replace_with=""):
        """
        Replace all URLs in ``text`` str with ``replace_with`` str.
        """
        return self.regex_patterns["URL_REGEX"].sub(replace_with, text)
    

    def replace_emails(self, text, replace_with=""):
        """
        Replace all emails in ``text`` str with ``replace_with`` str.
        """
        return self.regex_patterns["EMAIL_REGEX"].sub(replace_with, text)
    

    def remove_substrings(self, text, to_replace, replace_with=""):
        """
        Remove (or replace) substrings from a text.
        Args:
            text (str): raw text to preprocess
            to_replace (iterable or str): substrings to remove/replace
            replace_with (str): defaults to an empty string but
                you replace substrings with a token.
        """
        if isinstance(to_replace, str):
            to_replace = [to_replace]

        result = text
        for x in to_replace:
            result = result.replace(x, replace_with)
        return result
    

    def remove_emojis(self, text):
        return self.remove_substrings(text, UNICODE_EMOJI["en"])

    def remove_number_or_digit(self, text, replace_with=""):
        return re.sub(self.regex_patterns["BANGLA_DIGIT_REGEX"], replace_with, text)

    def remove_punctuations(self, text, replace_with=""):
        for punc in self.bangla_character.punctuations:
            text = text.replace(punc, replace_with)        
        return text
    
    def clean(self, text: str) -> str:
        if text is None:
            text = ""
        text = str(text)
        text = self.fix_strange_quotes(text)

        if self.fix_unicode:
            text = self.fix_bad_unicode(text)
        if self.unicode_norm:
            text = normalize(self.unicode_norm_form, text)
        if self.remove_url:
            text = self.replace_urls(text, replace_with=self.replace_with_url)
        if self.remove_email:
            text = self.replace_emails(text, replace_with=self.replace_with_email)
        if self.remove_emoji:
            text = self.remove_emojis(text)
        if self.remove_digits:
            text = self.remove_number_or_digit(text, replace_with=self.replace_with_digit)
        if self.remove_number:
            text = self.remove_number_or_digit(text, replace_with=self.replace_with_number)
        if self.remove_punct:
            text = self.remove_punctuations(text, replace_with=self.replace_with_punct)
        return text
    
    def is_bangla_word(self, word: str) -> bool:
        """
        Check if a word is a Bangla word.
        """
        for char in word:
            if not self.bangla_character.is_valid_character(char):
                return False
        return True
    
    def replace_foreign_word(self, word: str, replace_with="<FOREIGN>", keep_special_tokens=False):
        """
        Replace foreign words with ``replace_with`` str.
        """
        if keep_special_tokens:
            if word in ["<URL>", "<EMAIL>", "<NUMBER>", "<DIGIT>", "<PUNC>"]:
                return word
        if not self.is_bangla_word(word):
            return replace_with
        return word
    
    def replace_foreign_words(self, text: str, replace_with="<FOREIGN>", keep_special_tokens=False):
        """
        Replace foreign words with ``replace_with`` str.
        """
        words = text.split()
        words = [self.replace_foreign_word(word, replace_with, keep_special_tokens) for word in words]
        return " ".join(words)