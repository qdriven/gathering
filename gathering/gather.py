#!/usr/bin/env python
# -*- coding:utf-8 -*-
import fire
from gathering.sdks.dltranslator.translate_engine import Translator
"""
Fire support: https://github.com/google/python-fire/blob/master/docs/guide.md
1. class/object
2. pipeline
3. method composition
"""

def main():
    fire.Fire(Translator)


if __name__ == '__main__':
    main()
