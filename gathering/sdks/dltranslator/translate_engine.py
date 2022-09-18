#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List
from typing import Optional
from typing import Union

import time

from deep_translator import GoogleTranslator
from deep_translator import LingueeTranslator
from deep_translator import MyMemoryTranslator
from deep_translator import PonsTranslator
from deep_translator import YandexTranslator
from deep_translator import batch_detection
from deep_translator import single_detection
from pydantic import BaseModel
from qpyone.builtins import iotools
from qpyone.builtins import listtools


WORDS_LIMITATION = 5000
langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
# output: {arabic: ar, french: fr, english:en etc...}

language_keys = [
    "af",
    "sq",
    "am",
    "ar",
    "hy",
    "az",
    "eu",
    "be",
    "bn",
    "bs",
    "bg",
    "ca",
    "ceb",
    "ny",
    "zh-CN",
    "zh-TW",
    "co",
    "hr",
    "cs",
    "da",
    "nl",
    "en",
    "eo",
    "et",
    "tl",
    "fi",
    "fr",
    "fy",
    "gl",
    "ka",
    "de",
    "el",
    "gu",
    "ht",
    "ha",
    "haw",
    "iw",
    "hi",
    "hmn",
    "hu",
    "is",
    "ig",
    "id",
    "ga",
    "it",
    "ja",
    "jw",
    "kn",
    "kk",
    "km",
    "rw",
    "ko",
    "ku",
    "ky",
    "lo",
    "la",
    "lv",
    "lt",
    "lb",
    "mk",
    "mg",
    "ms",
    "ml",
    "mt",
    "mi",
    "mr",
    "mn",
    "my",
    "ne",
    "no",
    "or",
    "ps",
    "fa",
    "pl",
    "pt",
    "pa",
    "ro",
    "ru",
    "sm",
    "gd",
    "sr",
    "st",
    "sn",
    "sd",
    "si",
    "sk",
    "sl",
    "so",
    "es",
    "su",
    "sw",
    "sv",
    "tg",
    "ta",
    "tt",
    "te",
    "th",
    "tr",
    "tk",
    "uk",
    "ur",
    "ug",
    "uz",
    "vi",
    "cy",
    "xh",
    "yi",
    "yo",
    "zu",
]


class TranslateOption(BaseModel):
    source: Optional[str] = "auto"
    target: Optional[str] = "zh-CN"
    engine: Optional[str] = "google"


## https://deep-translator.readthedocs.io/en/latest/usage.html
class Translater:
    def __init__(self, options=TranslateOption()):
        self.options = options

    def translate_paragraph(self, paragraph: Union[str | List[str]]):
        """
        Translate Paragraph
        """
        result = GoogleTranslator(
            source=self.options.source, target=self.options.target
        ).translate(paragraph)
        return result

    def translate_small_file(self, source_file_path: str, target_file: str):
        """
        translate small files,less than 5000 words
        """
        result = GoogleTranslator(
            source=self.options.source, target=self.options.target
        ).translate_file(source_file_path)
        iotools.write(result, target_file)

    def translate(self, source_file_path: str, target_file: str):
        """
        translate big file, more than 5000 words
        """
        result = iotools.read_as_list(source_file_path)
        print(result)
        batch_words = []
        trans_results = []
        translator = GoogleTranslator(
            source=self.options.source, target=self.options.target
        )
        words_counter = 0
        for line in result:
            words_counter += len(line)
            if words_counter > WORDS_LIMITATION:
                trans_result = translator.translate_batch(batch_words)
                time.sleep(1)
                trans_results.append(trans_result)
                batch_words = []
                words_counter = 0
                batch_words.append(line)
                words_counter += len(line)
            else:
                batch_words.append(line)

        trans_results.append(translator.translate_batch(batch_words))
        iotools.write_lines(listtools.flat(trans_results), target_file)
