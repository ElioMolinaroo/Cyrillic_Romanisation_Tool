"""Transliterator for languages using the cyrillic alphabet.

Supported languages: Russian
"""

RUSSIAN_TRANSLITERATION_TABLE = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "ë",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "ĭ",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "kh",
    "ц": "ts",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ъ": '"',
    "ы": "y",
    "ь": "'",
    "э": "ė",
    "ю": "iu",
    "я": "ia",
}


class Transliterator:
    def __init__(self, transliteration_table: dict):
        self.transliteration_table = transliteration_table

    def transliterate_character(self, char: str) -> str:
        # Check if the char argument is only one character long
        if len(char) != 1:
            raise ValueError(
                f"The argument char only takes one character, you gave it {len(char)}."
            )
        # Check if the character is a letter
        if char.isalpha() is True:
            # If the character is uppercase, make it lowercase and then back to uppercase
            if char.isupper() is True:
                lower_trans_char = self.transliteration_table[char.lower()]
                return lower_trans_char.capitalize()
            # Otherwise just transliterate it
            else:
                return self.transliteration_table[char]
        else:
            return char

    def transliterate_text(self, text: str) -> str:
        transliterated_text = ""
        for char in text:
            transliterated_text += self.transliterate_character(char)
        return transliterated_text


if __name__ == "__main__":
    russian_transliterator = Transliterator(transliteration_table=RUSSIAN_TRANSLITERATION_TABLE)
    result = russian_transliterator.transliterate_text(text=input("Your text in Russian: \n"))
    print(f"\n{result}")
