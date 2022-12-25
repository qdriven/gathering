#!/usr/bin/env python
# -*- coding:utf-8 -*-

from qpyone.clients.http.client import AsyncHttpClient
from qpyone.clients.http.client import BaseHttpClient
from qpyone.clients.http.client import HttpClient
from qpyone.clients.http.client import HttpClientOption
from qpyone.config import configs

from .api.notion_endpoint import *


base_url_v1: str = "https://api.notion.com/v1"
auth = {"Authorization": f"Bearer {configs.notion_token}"}

notion_options = HttpClientOption(auth=auth, headers={"Notion-Version": "2022-02-22"})


class NotionSdk:
    def __init__(
        self, client: BaseHttpClient = HttpClient(options=notion_options), **kwargs
    ):
        self.http_client = client
        self.options = kwargs if kwargs else {}
        self.blocks = BlocksEndpoint(invoker=client, **kwargs)
        self.databases = DatabasesEndpoint(invoker=client, **kwargs)
        self.users = UsersEndpoint(invoker=client, **kwargs)
        self.pages = PagesEndpoint(invoker=client, **kwargs)
        self.search = SearchEndpoint(invoker=client, **kwargs)


notion_sdk = NotionSdk(base_url=base_url_v1)
async_notion_sdk = NotionSdk(client=AsyncHttpClient(options=notion_options))
