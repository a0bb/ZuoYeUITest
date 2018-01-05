# coding:utf8

import time
import os
import sched
import sys
import datetime

# 初始化sched模块的scheduler类
# 第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。
schedule = sched.scheduler(time.time, time.sleep)

sys.path.append(sys.prefix + "\\Lib\\MyWheels")
reload(sys)
sys.setdefaultencoding('utf8')
start_time = 0
end_time = 0
class mytimer(object):
    # 被周期性调度触发的函数
    def execute_command(self, cmd, inc):
        start_time = datetime.datetime.now()
        os.system(cmd)
        time.sleep(3)
        end_time = datetime.datetime.now()
        delay = round((end_time-start_time).total_seconds())
        print
        print u'mytimer => 开始时间：%s' % start_time
        print u'mytimer => 耗时:%smin' %(delay/60)
        schedule.enter(int(inc-delay), 0, self.execute_command, (cmd, inc))
        print u'mytimer => 结束时间：%s' % end_time

    def cmd_timer(self, cmd, time_str, inc=60):
        # cmd：windows中命令行代码
        # time_str：哪一个时间点开始第一次执行
        # inc：两次执行的间隔时间
        # enter四个参数分别为：间隔时间、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数，
        # 给该触发函数的参数（tuple形式）
        now = datetime.datetime.now()
        schedule_time = datetime.datetime.strptime(time_str,'%H:%M').replace(year=now.year,month=now.month,day=now.day)
        if schedule_time < now:
            schedule_time = schedule_time + datetime.timedelta(days=1)
        time_before_start = int(round((schedule_time-datetime.datetime.now()).total_seconds()))
        print u'mytimer => 还有%s秒开始任务' %time_before_start
        schedule.enter(time_before_start, 0, self.execute_command, (cmd, inc))
        schedule.run()

if __name__ == '__main__':
    mytimer = mytimer()
    mytimer.cmd_timer("robot --pythonpath C:\\Git\\ZuoYeUITest --test *0001 C:\\Git\\ZuoYeUITest\\tc", '23:00', 86400)