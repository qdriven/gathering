#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List
from typing import Optional
from typing import Union

import time

from deep_translator import GoogleTranslator
from pydantic import BaseModel
from qpyone.builtins import iotools
from qpyone.builtins import listtools


WORDS_LIMITATION = 5000
langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)


# output: {arabic: ar, french: fr, english:en etc...}


class TranslateOption(BaseModel):
    source: Optional[str] = "auto"
    target: Optional[str] = "zh-CN"
    engine: Optional[str] = "google"
    source_file: Optional[str] = ""
    target_file: Optional[str] = ""


## https://deep-translator.readthedocs.io/en/latest/usage.html
class Translator:
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
