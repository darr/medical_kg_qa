#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : chatbot_graph.py
# Create date : 2019-08-16 23:08
# Modified date : 2019-08-17 17:43
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from question_classifier import QuestionClassifier
from question_parser import QuestionPaser
from answer_search import AnswerSearcher

class ChatBot:
    '''问答类'''
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_answer(self, sent):
        answer = '才疏学浅，未知如何作答。'
        res_classify = self.classifier.classify(sent)
        if not res_classify:
            return answer
        res_sql = self.parser.parser_main(res_classify)
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers:
            return answer
        else:
            return '\n'.join(final_answers)

#import chardet

if __name__ == '__main__':
    handler = ChatBot()
    question = "失眠的并发症"
    answer = handler.chat_answer(question)
    print('小勇:', answer)
    while 1:
        question = input('用户:')
        print(question)
        answer = handler.chat_answer(question)
        print('小勇:', answer)
