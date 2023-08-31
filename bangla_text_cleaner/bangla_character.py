class BanglaCharacter:
    def __init__(self):
        self.vowels = ["অ", "আ", "ই", "ঈ", "উ", "ঊ", "ঋ", "ঌ", "এ", "ঐ", "ও", "ঔ"]
        self.vowels_unicode = ["\u0985", "\u0986", "\u0987", "\u0988", "\u0989", "\u098A", "\u098B", "\u098C", "\u098F", "\u0990", "\u0993", "\u0994"]
        self.vowel_signs = ["া", "ি", "ী", "ু", "ূ", "ৃ", "ৄ", "ে", "ৈ", "ো", "ৌ"]
        self.vowel_signs_unicode = ["\u09BE", "\u09Bf", "\u09C0", "\u09C1", "\u09C2", "\u09C3", "\u09C4", "\u09C7", "\u09C8", "\u09CB", "\u09CC"]
        self.digits = ["০", "১", "২", "৩", "৪", "৫", "৬", "৭", "৮", "৯"]
        self.digit_unicode = ["\u09E6", "\u09E7", "\u09E8", "\u09E9", "\u09EA", "\u09EB", "\u09EC", "\u09ED", "\u09EE", "\u09EF"]
        self.consonants = ["ক", "খ", "গ", "ঘ", "ঙ", "চ", "ছ", "জ", "ঝ", "ঞ", 
                           "ট", "ঠ", "ড", "ঢ", "ণ", "ত", "থ", "দ", "ধ", "ন", 
                           "প", "ফ", "ব", "ভ", "ম", "য", "র", "ল", "শ", "ষ", 
                           "স", "হ", "ড়", "ঢ়", "য়", "ৎ", "ং", "ঃ", "ঁ"]
        self.consonant_unicode = ["\u0995", "\u0996", "\u0997", "\u0998", "\u0999", "\u099A", "\u099B","\u099C",
                            "\u099D", "\u099E", "\u099F", "\u09A0", "\u09A1", "\u09A2", "\u09A3", "\u09A4",
                            "\u09A5", "\u09A6", "\u09A7", "\u09A8", "\u09AA", "\u09AB", "\u09AC", "\u09AD",
                            "\u09AE", "\u09AF", "\u09B0", "\u09B2", "\u09B6", "\u09B7", "\u09B8", "\u09B9",
                            "\u09DC", "\u09DD", "\u09DF", "\u09CE", "\u0982", "\u0983", "\u0981"]
        self.punctuations = ["।", ",", ";", ":", "?", "!", "'", ".", "\"", "-", "[", "]", "{", "}", "(", ")", '–', "—", "―", "~"]
        self.punctuation_unicode = ["\u0964", "\u002C", "\u003B", "\u003A", "\u003F", "\u0021",
                            "\u0027", "\u002E", "\u0022", "\u002D", "\u005B", "\u005D",
                            "\u007B", "\u007D", "\u0028", "\u0029", "\u2013", "\u2014",
                            "\u2015", "\u007E"]
        self.operators = ["=", "+", "-", "*", "/", "%", "<", ">", "×", "÷"]
        self.unicode_operators = ["\u003D", "\u002B", "\u002D", "\u002A", "\u002F", "\u0025", "\u003C",
                            "\u003E", "\u00D7", "\u00F7"]
        self.others = ["৳", "৺", '্', "ঀ", "ঽ", "#", "$", "◌়"]
        self.unicode_others = ["\u09F3", "\u09FA", "\u09CD", "\u0980", "\u09BD", "\u0023", "\u0024", "\u09BC"]

    def is_valid_character(self, char: str) -> bool:
        if len(char) > 1:
            raise ValueError("Input character must be a single character")
        if char in self.vowels or char in self.vowel_signs or char in self.digits or char in self.consonants or char in self.punctuations or char in self.operators or char in self.others:
            return True
        return False