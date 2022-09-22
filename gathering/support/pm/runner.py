#!/usr/bin/env python
# -*- coding:utf-8 -*-
from gathering.support.pm.models import PostmanCollection


class PostmanRunner:
    """
    To Run the requests in collections
    1. call request
    2. bath run requests
    3. getting context and environment variables
    4. run some javascripts
    """

    def __init__(self, postman_collection_path: str):
        self.pc = PostmanCollection.parse_file(postman_collection_path)

    def get_request_by_name(self):
        pass

    def get_request(self):
        pass

    def run(self, key, **kwargs):
        pass
