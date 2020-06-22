#!/usr/bin/env python3
import zhihu
from zhihu.models import answer
from zhihu.models import user
from zhihu.models import question
from zhihu.models import column
from zhihu.models import account
from zhihu.models import collection

__author__ = 'liuzhijun'
__license__ = 'MIT'

__all__ = ["Answer", "User", "Question", "Column", "Account"]

User = zhihu.models.Zhihu
Answer = answer.Answer
User = user.User
Question = question.Question
Column = column.Column
Account = account.Account
Collection = collection.Collection
