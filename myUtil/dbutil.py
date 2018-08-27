# -*-coding:utf-8-*-
import MySQLdb


# 数据库工具类
class DB(object):
    # 链接数据库
    def __init__(self, ip, db, user='root', pwd='', tb=''):
        self.ip = ip
        self.db = db
        self.user = user
        self.pwd = pwd
        self.conn = MySQLdb.connect(ip, user, pwd, db, charset='utf8')
        self.cur = self.conn.cursor()
        self.table = tb

    # 数据库重新链接
    def reconnection(self):
        self.conn = MySQLdb.connect(self.ip, self.user, self.pwd, self.db, charset='utf8')
        self.cur = self.conn.cursor()

    # 删除表
    def delete(self):
        self.cur.execute('DROP TABLE IF EXISTS `%s`;' % self.table)

    # 创建表
    def create(self, *args):
        sql = "create table IF NOT EXISTS `%s`(" \
              "id INT PRIMARY KEY auto_increment," % self.table
        for arg in args:
            sql += arg + " text(255),"
        sql = str(sql).rstrip(',') + ") ENGINE=InnoDB DEFAULT CHARSET=utf8;"
        print sql
        self.cur.execute(sql)

    # 插入表
    def insert(self, *args):
        try:
            if args is not None:
                num = len(args)
                sql = 'insert into `%s` VALUES (0,' % self.table
                for i in range(0, num):
                    sql += '%s,'
                sql = str(sql).rstrip(',') + ')'
                print sql % args
                self.cur.execute(sql, args)
                self.conn.commit()
        except BaseException, e:
            print e
            print 'reconnection:'
            self.reconnection()
            self.insert(*args)

    def select(self, wheredic={}):
        try:
            if wheredic is not None:
                sql = 'select * from `%s` WHERE' % self.table
                for where in wheredic:
                    sql += ' %s = \'%s\' and' % (where, wheredic[where])
                sql = str(sql)[0:-3] + ';'
                print sql
                i = self.execute(sql)
                return i
        except BaseException, e:
            print e

    def execute(self, sql):
        i = self.cur.execute(sql)
        self.conn.commit()
        return i

    def result(self):
        return self.cur.fetchall()

    # 删除记录
    # def delete(self, dic={}):
    #     print 'delete table rows',dic
    #
    # 修改记录
    # def update(self, dic={}):
    #     print 'update table rows',dic

    def __del__(self):
        self.table = ''
        self.cur.close()
        self.conn.commit()
        self.conn.close()
