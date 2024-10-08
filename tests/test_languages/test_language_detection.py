from pathlib import Path

from release.cyrillic_romanisation_tool import Language


DATABASE_PATH = Path("tests/test_database").absolute()


def get_file_content(filepath: Path):
    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()
    file.close()
    return text


def test_detect_russian():
    # Get the russian database text
    russian_text = get_file_content(filepath=DATABASE_PATH / "russian.txt")

    # Try detecting the language
    lang_obj = Language()
    detected_language = lang_obj.detect_language(text=russian_text)

    assert detected_language == "russian"


def test_detect_ukrainian():
    # Get the ukrainian database text
    ukrainian_text = get_file_content(filepath=DATABASE_PATH / "ukrainian.txt")

    # Try detecting the language
    lang_obj = Language()
    detected_language = lang_obj.detect_language(text=ukrainian_text)

    assert detected_language == "ukrainian"


def test_detect_uzbek():
    # Get the uzbek database text
    uzbek_text = get_file_content(filepath=DATABASE_PATH / "uzbek.txt")

    # Try detecting the language
    lang_obj = Language()
    detected_language = lang_obj.detect_language(text=uzbek_text)

    assert detected_language == "uzbek"


def test_detect_kazakh():
    # Get the kazakh database text
    kazakh_text = get_file_content(filepath=DATABASE_PATH / "kazakh.txt")

    # Try detecting the language
    lang_obj = Language()
    detected_language = lang_obj.detect_language(text=kazakh_text)

    assert detected_language == "kazakh"


def test_detect_serbian():
    # Get the serbian database text
    serbian_text = get_file_content(filepath=DATABASE_PATH / "serbian.txt")

    # Try detecting the language
    lang_obj = Language()
    detected_language = lang_obj.detect_language(text=serbian_text)

    assert detected_language == "serbian"


def test_detect_bulgarian():
    # Get the bulgarian database text
    bulgarian_text = get_file_content(filepath=DATABASE_PATH / "bulgarian.txt")

    # Try detecting the language
    lang_obj = Language()
    detected_language = lang_obj.detect_language(text=bulgarian_text)

    assert detected_language == "bulgarian"


def test_detect_belarusian():
    # Get the belarusian database text
    belarusian_text = get_file_content(filepath=DATABASE_PATH / "belarusian.txt")

    # Try detecting the language
    lang_obj = Language()
    detected_language = lang_obj.detect_language(text=belarusian_text)

    assert detected_language == "belarusian"


def test_detect_tajik():
    # Get the tajik database text
    tajik_text = get_file_content(filepath=DATABASE_PATH / "tajik.txt")

    # Try detecting the language
    lang_obj = Language()
    detected_language = lang_obj.detect_language(text=tajik_text)

    assert detected_language == "tajik"


def test_detect_kyrgyz():
    # Get the kyrgyz database text
    kyrgyz_text = get_file_content(filepath=DATABASE_PATH / "kyrgyz.txt")

    # Try detecting the language
    lang_obj = Language()
    detected_language = lang_obj.detect_language(text=kyrgyz_text)

    assert detected_language == "kyrgyz"


def test_detect_turkmen():
    # Get the turkmen database text
    turkmen_text = get_file_content(filepath=DATABASE_PATH / "turkmen.txt")

    # Try detecting the language
    lang_obj = Language()
    detected_language = lang_obj.detect_language(text=turkmen_text)

    assert detected_language == "turkmen"


def test_detect_macedonian():
    # Get the macedonian database text
    macedonian_text = get_file_content(filepath=DATABASE_PATH / "macedonian.txt")

    # Try detecting the language
    lang_obj = Language()
    detected_language = lang_obj.detect_language(text=macedonian_text)

    assert detected_language == "macedonian"


def test_detect_chechen_ingush():
    # Get the chechen database text
    chechen_text = get_file_content(filepath=DATABASE_PATH / "chechen.txt")

    # Try detecting the language
    lang_obj = Language()
    detected_language = lang_obj.detect_language(text=chechen_text)

    assert detected_language == "chechen/ingush"


def test_detect_montenegrin():
    # Get the montenegrin database text
    montenegrin_text = get_file_content(filepath=DATABASE_PATH / "montenegrin.txt")

    # Try detecting the language
    lang_obj = Language()
    detected_language = lang_obj.detect_language(text=montenegrin_text)

    assert detected_language in ("montenegrin", "serbian")


def test_detect_ossetian():
    # Get the ossetian database text
    ossetian_text = get_file_content(filepath=DATABASE_PATH / "ossetian.txt")

    # Try detecting the language
    lang_obj = Language()
    detected_language = lang_obj.detect_language(text=ossetian_text)

    assert detected_language == "ossetian"


def test_detect_abkhaz():
    # Get the abkhaz database text
    abkhaz_text = get_file_content(filepath=DATABASE_PATH / "abkhaz.txt")

    # Try detecting the language
    lang_obj = Language()
    detected_language = lang_obj.detect_language(text=abkhaz_text)

    assert detected_language == "abkhaz"
