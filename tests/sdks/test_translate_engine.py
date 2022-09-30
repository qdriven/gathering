#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os.path

from gathering.sdks.dltranslator.translate_engine import Translator


BASE_PATH = os.path.dirname(__file__).replace("/tests", "")
print(BASE_PATH)
source_prefix = "../../docs/qabase/en"
target_prefix = "../../docs/qabase/cn"
file_name = "6. Completeness.md"
file_list = [
    "org-software.md",
]


def test_translate():
    for file_md_name in file_list:
        print("current file is {}".format(file_md_name))
        Translator().translate(
            source_prefix + "/" + file_md_name, target_prefix + "/" + file_md_name
        )
