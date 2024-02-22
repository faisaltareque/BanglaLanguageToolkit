|Version Info| [![Python](https://img.shields.io/badge/python-v3.11.4-green)](https://www.python.org/downloads/release/python-3913/) |
|----|----|

# Bangla Language Processing Toolkit

This is a very basic Bangla language processing toolkit for my personal use.

Most of the code snippets are taken from following open source projects. Please follow these projects for greater details:
- [Normalizer](https://github.com/csebuetnlp/normalizer)
- [BNLP](https://github.com/sagorbrur/bnlp)
- [BLTK](https://github.com/saimoncse19/bltk)

## Installation
Run following command to install
```bash
pip install git+https://github.com/faisaltareque/BanglaLanguageToolkit.git
```

## Usage
### Code
```python
from BanglaLanguageToolkit import BanglaTextCleaner
cleaner = BanglaTextCleaner(remove_emoji=True, remove_email=True, remove_url=True, remove_punct=True)

text = "সে কিভাবে রিগামের সাথে সম্পর্কিত? How is he related to Regum?, www.google.com, demo@gmail.com."
text = cleaner.clean(text)
print(text)
```

### Output
```python
সে কিভাবে রিগামের সাথে সম্পর্কিত <PUNC> How is he related to Regum <PUNC> <PUNC> <URL> <PUNC> <EMAIL> <PUNC>
```

### Code
```python
from BanglaLanguageToolkit import BanglaTextCleaner
cleaner = BanglaTextCleaner(remove_emoji=True, remove_email=True, remove_url=True, remove_punct=True)

text = "সে কিভাবে রিগামের সাথে সম্পর্কিত? How is he related to Regum?, www.google.com, demo@gmail.com."
text = cleaner.clean(text)
text = cleaner.replace_foreign_words(text, keep_special_tokens=True, replace_multiple_foreign_words=False)
```

### Output
```python
সে কিভাবে রিগামের সাথে সম্পর্কিত <PUNC> <FOREIGN> <FOREIGN> <FOREIGN> <FOREIGN> <FOREIGN> <FOREIGN> <PUNC> <PUNC> <URL> <PUNC> <EMAIL> <PUNC>
```