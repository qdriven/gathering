#!/usr/bin/env python
# -*- coding:utf-8 -*-
from github3.repos import Repository
from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport

from .queries import STAR_QUERY


class GithubGqlClient:
    API_URL = "https://api.github.com/graphql"

    def __init__(self, token):
        self.token = token
        headers = {"Authorization": f"Bearer {token}"}
        self.transport = AIOHTTPTransport(url=self.API_URL, headers=headers)
        self.client = Client(transport=self.transport, fetch_schema_from_transport=True)

    def get_user_starred_by_username(
        self, user_name: str, after: str = "", topic_stars_count: int = 0
    ):
        items = []
        result = self.client.execute(
            STAR_QUERY, variable_values={"username": user_name, "after": after}
        )
        has_next = result["user"]["starredRepositories"]["pageInfo"]["hasNextPage"]
        end_cursor = result["user"]["starredRepositories"]["pageInfo"]["endCursor"]
        for repo in result["user"]["starredRepositories"]["nodes"]:
            name = repo["nameWithOwner"]
            description = repo["description"] if repo["description"] else ""
            language = (
                repo["languages"]["edges"][0]["node"]["name"]
                if repo["languages"]["edges"]
                else ""
            )
            url = repo["url"]
            stargazer_count = repo["stargazerCount"]
            is_private = repo["isPrivate"]
            topics = [
                tag["topic"]["name"]
                for tag in repo["repositoryTopics"]["nodes"]
                if tag["topic"]["stargazerCount"] >= topic_stars_count
            ]
            items.append(
                Repository(
                    name,
                    description,
                    language,
                    url,
                    stargazer_count,
                    is_private,
                    topics,
                )
            )

        if has_next:
            items.extend(
                self.get_user_starred_by_username(
                    user_name, end_cursor, topic_stars_count
                )
            )
        return items
