#!/usr/bin/env python
# -*- coding:utf-8 -*-
from gathering.sdks.notion.notion import async_notion_sdk
from gathering.sdks.notion.notion import notion_sdk
from qpyone.config import configs


class TestNotionSdk:
    def test_secret_loading(self):
        assert configs.notion_token is not None

    def test_notion_sdk(self):
        assert notion_sdk is not None
        assert async_notion_sdk is not None

    def test_notion_database(self):
        assert notion_sdk.databases is not None
        result = notion_sdk.databases.list()
        print(result)

    def test_search(self):
        result = notion_sdk.search()
        print(result)

    def test_create_db(self):
        pass

    def test_upload_files(self):
        pass

