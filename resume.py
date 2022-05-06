#/usr/bin/env python
# coding=utf-8

import random
import re


def color(messages):
    color = '\x1B[%d;%dm' % (1,random.randint(30,37))
    return '%s %s\x1B[0m' % (color,messages)


def len_zh(data):
    temp = re.findall('[^a-zA-Z0-9._ ]+', data)
    count = 0
    for i in temp:
        count += len(i)
    return(count)


def colorprint(mes, flag=True):
    def _deco(func):
        def wrapper(*args):
            res = func(*args)
            print color(mes + ':\n')
            if flag:
                for k1, v1 in res.items():
                    zh = len_zh(k1.decode('utf-8'))
                    if not isinstance(v1, dict):
                        print '{0}: {1}'.format(k1.ljust(20+zh), v1)
                    else:
                        print '{0}:'.format(k1.ljust(20+zh))
                        for k2, v2 in v1.items():
                            zh = len_zh(k2.decode('utf-8'))
                            print '    {0}: {1}'.format(k2.ljust(16+zh), v2)
            else:
                for i in res:
                    if not isinstance(i[1], dict):
                        print i
                    else:
                        for k, v in i[1].items():
                            zh = len_zh(k.decode('utf-8'))
                            print '{0}[{1}]: {2}'.format(k.ljust(17+zh), i[0], v)
            print '\n'
            return res
        return wrapper
    return _deco


class Resume(object):

    def __str__(self):
        return color('谢**的Python简历'.center(400))

    @property
    @colorprint('个人信息')
    def personal_information(self):
        return {
            'Name' : '谢**',
            'Tel' : '1807047****',
            'Email' : '***@gmail.com',
            'Education' : {
                'School Name' : '南昌大学共青学院',
                'Major' : '软件技术',
                'Degree' : 'Three-year college',
                'Graduation' : 2018
            },
            'Gender' : 'Male',
            'Born' : [1997, 10, 23],
            'Target Positions' : re.compile(
                "'Python Developer'",re.I|re.M).pattern
        }

    @property
    @colorprint('个人特点')
    def characteristics(self):
        return {
            'is_geek' : True,
            '热衷和喜爱': '热爱IT行业，对新技术充满好奇，关注行业动态',
            '抗压能力强': '具有团队合作精神，良好的编码习惯，工作态度认真负责',
            '自学能力强': '不断探索提高，从不放弃一个解决不了的难题',
        }

    @property
    @colorprint('个人能力')
    def skills(self):
        return {
            'Language' : {
                '熟悉' : ['Python', 'Ruby', 'Bash'],
                '了解' : ['Golang', 'Java']},
            'OS' : ['MacOS', 'Ubuntu', 'Windows'],
            'Tool' : ['Visual Studio Code', 'Vim', 'Git'],
            'DatabaseAndTools' : ['MySQL', 'PostgreSQL', 'Redis', 'SQLAlchemy'],
            'WebFramework' : {
                '熟悉' : ['Flask', 'Django'],
                '了解' : ['Rails']
            },
            'OtherFramework' : [ 'gevent', 'scrapy']
        }

    @property
    @colorprint('工作经验', False)
    def work_experience(self):
        return enumerate([
            {
                'Time period' : '2019.05-2022.05',
                'Company Name' : '广州****科技服务有限公司',
                'Position' : 'Python开发工程师'
            },
            {
                'Time period' : '2018.09-2019.03',
                'Company Name' : '广州***软件开发有限公司',
                'Position' : '后端开发工程师'
            },
        ])

    @property
    @colorprint('项目经验',False)
    def project_experience(self):
        return enumerate([
            {
                'Project' : '**洗车系统',
                'Description' : ('技术栈：Python + Flask + PostgreSQL + Celery，'
                                 '网页端管理后台独立完成，并参与API接口开发、服务器部署维护等')
            },
            {
                'Project' : '车**托管平台',
                'Description' : ('技术栈：Ruby on Rails + PostgreSQL + RabbitMQ，'
                                 '自学了Ruby语言、Ruby on Rails等相关技术，负责该项目后期维护')
            },
            {
                'Project' : '爱海钓',
                'Description' : ('技术栈：Python + Flask + PostgreSQL + Celery，'
                                 '网页端管理后台独立完成，并参与需求分析、数据库设计等')
            },
            {
                'Project' : '医**后勤管理系统',
                'Description': ('技术栈：Golang + MySQL + gRPC + Elasticsearch，'
                                '参与开发了保洁系统、医废系统、质检系统、快捷公告模块等')
            }
        ])

    @property
    @colorprint('@Where', False)
    def findme(self):
        return enumerate([
            {
                'Link' : 'https://www.icenglou.cn',
		        'Description' : '个人技术博客'
            },
            {
                'Link' : 'https://github.com/nnocase',
		        'Description' : 'GitHub'
            }
        ])

    def show(self):
        prolist = [i for i in dir(self) if not i.startswith('_') \
                   and not i.startswith('personal')]
        self.personal_information
        for pro in prolist:
            getattr(self, pro)


if __name__ == '__main__':
    resume = Resume()
    print resume
    resume.show()
