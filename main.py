#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
#   Created by Vakhlakov Alexandr    #


#import logging
#import requests
from config import *
from tasks import MBJira
from tasks import send_to_telegram

jira = MBJira()
m = jira.get_issues()
for new_issue in m:
    msg = tg_messages_2.format(
        key=new_issue.key,
        issue_url=jira.get_issue_url(new_issue)
    )

    send_to_telegram(msg)