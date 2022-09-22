#!/usr/bin/env python
# -*- coding:utf-8 -*-
from gathering.support.pm.models import PostmanCollection


def test_collection():
    pc = PostmanCollection.parse_file("postman_collections.json")
    assert pc is not None
