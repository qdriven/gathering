#!/usr/bin/env python
# -*- coding:utf-8 -*-
from gql import gql


STAR_QUERY = gql(
    """
        query ($username: String!, $after: String) {
        user(login: $username) {
            starredRepositories(first: 100, after: $after, orderBy: {direction: DESC, field: STARRED_AT}) {
              totalCount
              nodes {
                name
                nameWithOwner
                description
                url
                stargazerCount
                forkCount
                isPrivate
                pushedAt
                updatedAt
                languages(first: 1, orderBy: {field: SIZE, direction: DESC}) {
                  edges {
                    node {
                      id
                      name
                    }
                  }
                }
                repositoryTopics(first: 100) {
                  nodes {
                    topic {
                      name
                      stargazerCount
                    }
                  }
                }
              }
              pageInfo {
                endCursor
                hasNextPage
              }
            }
          }
        }
        """
)
