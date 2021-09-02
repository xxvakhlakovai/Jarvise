#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
#   Created by Vakhlakov Alexandr    #

#Jira-api
jira_api_url = 'http://'
jira_api_login = ''
jira_api_pass = ''

#Telegram
tg_token = '1975759826:AAEztk1ZTXmDpWfrftYRmKJ7QGrpeKq5Nyk'
#proxy = {'https': 'http://172.21.38.132:8080'}
tg_proxy = 'https://172.21.38.132:8080'
tg_gpid = ''
tg_url = "https://api.telegram.org/bot"

#tg_messages = "1"
tg_messages_1 = "<b>Появилась новая задача - New issue</b>\n\n" \
              " <b>Issue</b>: <a href='{issue_url}' target='_blank'>{key}</a>\n"
tg_messages_2 = "<b>Сотрудники завели обращение о проблеме - SOS! - New issue</b>\n\n" \
              " <b>Issue</b>: <a href='{issue_url}' target='_blank'>{key}</a>\n"

jql_issue_mon = 'project = MON AND status in ("В работе", "Согласовано для работы", "На паузе", Входящие, Проверка, Frozen, Отложено, "На уточнении") AND component in (EMPTY, AuditMonitoring, BusinessMonitoring, InfraMonitoring, Lifecycle, LocalTask, NetMonitoring, ServerMonitoring, Zabbix) AND created >= -5h'
jql_issue_incident = 'created >= -3h AND issuetype = SOS AND status not in (Resolved, Closed, Закрыт, Решена, "Заявку передали в работу на 2 линию", "Передано 3ей линии", "Передано на 2 линию")'