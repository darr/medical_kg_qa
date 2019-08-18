#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : main.py
# Create date : 2019-08-17 16:49
# Modified date : 2019-08-18 11:07
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from chatbot import ChatBot

def question_chatbot(handler, question):
    print("问题:%s" % question)
    answer = handler.chat_answer(question)
    print("回答:%s\n" % answer)

def test_chatbot():
    handler = ChatBot()
    question_chatbot(handler, "失眠的并发症")
    question_chatbot(handler, "乳腺癌的症状有哪些")
    question_chatbot(handler, "最近老流鼻涕怎么办？")
    question_chatbot(handler, "为什么有的人会失眠？")
    question_chatbot(handler, "失眠有哪些并发症？")
    question_chatbot(handler, "失眠的人不要吃啥？")
    question_chatbot(handler, "耳鸣了吃点啥？")
    question_chatbot(handler, "哪些人最好不好吃蜂蜜？")
    question_chatbot(handler, "鹅肉有什么好处？")
    question_chatbot(handler, "肝病要吃啥药？")
    question_chatbot(handler, "板蓝根颗粒能治啥病？")
    question_chatbot(handler, "脑膜炎怎么才能查出来？")
    question_chatbot(handler, "怎样才能预防肾虚？")
    question_chatbot(handler, "感冒要多久才能好？")
    question_chatbot(handler, "高血压要怎么治？")
    question_chatbot(handler, "白血病能治好吗？")
    question_chatbot(handler, "什么人容易得高血压？")
    question_chatbot(handler, "糖尿病")
    question_chatbot(handler, "全血细胞计数能查出啥来")

def chat_with_chatbot():
    handler = ChatBot()
    while 1:
        question = input('用户:')
        print(question)
        answer = handler.chat_answer(question)
        print('小勇:', answer)

def run():
    test_chatbot()
    chat_with_chatbot()

run()
