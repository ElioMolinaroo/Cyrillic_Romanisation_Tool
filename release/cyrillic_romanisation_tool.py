"""Transliterator for languages using the cyrillic alphabet.

Supported languages: Russian
                     Ukrainian
                     Uzbek
"""

LANGUAGES_TABLES = {
    "common": {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
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
        "ь": "'",
        "ю": "iu",
        "я": "ia",
    },
    "russian": {"ё": "ë", "ъ": '"', "ы": "y", "э": "ė"},
    "ukrainian": {"г": "h", "ґ": "g", "є": "ie", "и": "y", "і": "i", "ї": "ï"},
    "uzbek": {"ё": "ë", "э": "ė", "ғ": "gh", "қ": "q", "ў": "ŭ", "ҳ": "ḣ", "ъ": '"'},
}


class Language:

    def __init__(self):
        self.supported_languages = ("russian", "ukrainian", "uzbek")
        self.RESOLUTION_ORDER = (
            "russian",
            "ukrainian",
            "uzbek",
            # "kazakh",
            # "serbian",
            # "bulgarian",
            # "belarusian",
            # "tajiki",
            # "kyrgyz",
            # "turkmen",
            # "bosnian",
            # "macedonian",
            # "chechen",
            # "montenegrin",
            # "ossetian",
            # "ingush",
            # "abkhazian",
        )

    def detect_language(self, text: str) -> str:
        detected_language = None
        potential_languages = {}

        # Iterate over the languages
        for lang in self.RESOLUTION_ORDER:
            # Get the language table
            language_table = LANGUAGES_TABLES[lang]
            total_specific_chars = len(LANGUAGES_TABLES[lang])
            wrong_language = False
            detection_probability = 0.0
            matching_chars_list = []

            # Iterate over each character in the text
            for char in text:
                # Check if the character is a letter
                if char.isalpha() is False:
                    continue

                char = char.lower()

                # If the character is in the common table, go to the next character
                if char in LANGUAGES_TABLES["common"]:
                    continue

                # If the character is not in the common language table and not in the tested language table, skip to the next language
                elif (
                    char not in LANGUAGES_TABLES["common"]
                    and char not in language_table
                ):
                    wrong_language = True
                    break

                # If the character is in the tested language table, check the proportion of found character
                elif char in language_table:
                    if char not in matching_chars_list:
                        matching_chars_list.append(char)
                        found_chars_proportion = (
                            len(matching_chars_list) / total_specific_chars
                        )

                        # If proportion is higher than 75% declare the language detected
                        if found_chars_proportion >= 0.75:
                            detected_language = lang
                            break

            # If the language has been found quit the loop
            if detected_language is not None:
                break

            # If the language is wrong, go to the next one
            if wrong_language is True:
                continue

            # When at the end of the text if it hasn't been detected as uncompatible, add it to potential_languages dict
            potential_languages[lang] = found_chars_proportion

        # When we've gone through all the languages pick the one in the potential languages with the highest probability
        if len(potential_languages) > 0:
            detected_language = max(potential_languages, key=potential_languages.get)

        if detected_language is None:
            raise RuntimeError("The given input wasn't detected as a known language")
        else:
            return detected_language

    def create_language_table(self, language: str) -> dict:
        return {**LANGUAGES_TABLES["common"], **LANGUAGES_TABLES[language]}


class Transliterator:
    """this is a test"""

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

    close = False

    while close is False:
        # User wants transliterate or detect language
        chosen_proc = None
        while chosen_proc not in ("", "1", "2", "3", "4"):
            chosen_proc = input(
                "\033[1m- Transliterate text (1)\033[0m\n- Detect language (2)\n- List of supported languages (3)\n- exit (4): \n"
            )

        # Transliterate text
        if chosen_proc == "1" or chosen_proc == "":
            # Get the user input text
            user_text = input("Your text in Cyrillic: \n")

            # Find the source language
            language_obj = Language()
            source_lang = language_obj.detect_language(text=user_text)

            # Create the language table
            lang_table = language_obj.create_language_table(source_lang)

            # Transliterate the text
            transliterator_obj = Transliterator(transliteration_table=lang_table)
            result = transliterator_obj.transliterate_text(text=user_text)

            # Print the results
            print(f"\n\n{result}\n")

        # Detect language
        elif chosen_proc == "2":
            # Get the user input text
            user_text = input("Your text in Cyrillic: \n")

            # Find the source language
            language_obj = Language()
            source_lang = language_obj.detect_language(text=user_text)

            print(f"\n This text is written in {source_lang.capitalize()}. \n")

        # List of supported languages
        elif chosen_proc == "3":
            lang_obj = Language()
            print(f"\nSupported languages:\n")
            for lang in lang_obj.supported_languages:
                print("- " + lang.capitalize())
            print("\n")

        # Exit the program
        elif chosen_proc == "4":
            close = True
