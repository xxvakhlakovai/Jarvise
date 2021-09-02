#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
#   Created by Vakhlakov Alexandr    #

#import logging
import requests
from config import *
from jira import JIRA
from dataclasses import dataclass

@dataclass
class MergeRequest:
    id: int
    key: str


class MBJira:
    def __init__(self):
        self.conn = JIRA(jira_api_url, basic_auth=(jira_api_login, jira_api_pass))

    def get_issues(self):
        issues = self.conn.search_issues(jql_issue_mon or jql_issue_incident)
        return issues
#        for issue in issues:
#            return f"{issue.key}:{issue.fields.summary}"

    def get_issue_url(self, issue):
        url = f"{jira_api_url}/browse/{issue.key}"
        return url

def send_to_telegram(text):
    payload = dict(chat_id=tg_gpid, parse_mode='html', text=text)
    requests.post("https://api.telegram.org/bot{}/sendMessage".format(tg_token),
                data=payload
                )