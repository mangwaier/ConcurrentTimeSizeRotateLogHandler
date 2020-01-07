import multiprocessing
import os
from time import sleep
import logging
import datetime
from ConcurrentTimeSizeRotateLogHandler import ConcurrentTimedRotatingFileHandler

rootPath = os.getcwd()
_code_log_file = os.path.join(rootPath, 'api_test.log')
_code_log_handler = ConcurrentTimedRotatingFileHandler(filename=_code_log_file, mode="a", maxBytes=10*1024, backupCount=5, when="m", interval=1)
_code_log_formatter = logging.Formatter('%(levelname)s %(asctime)s '
                                        'line:%(lineno)d %(message)s ')
_code_log_handler.setFormatter(_code_log_formatter)
code_log = logging.getLogger()
code_log.setLevel(logging.INFO)
code_log.addHandler(_code_log_handler)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
code_log.addHandler(console)

def job(i):
    sleep(1)
    msg = "===pid={0}==num={1}=".format(os.getpid(), i)
    code_log.info("{0} am working:{1}".format(msg, datetime.datetime.now()))
    # code_log.info("{}, Done: {}".format(i, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

def suma(q):
    if not q.empty():
        sum = q.get()
    else:
        sum = 0
    sum += 1
    q.put(sum)
    return sum

def run(i,q):
    while True:
        try:
            job(i)
            sum = suma(q)
        except Exception as error:
            code_log.info(error)
            sum = q.get()
        # code_log.info("finish task number {}".format(sum))


def main(process_num):
    q = multiprocessing.Manager().Queue()
    pool = multiprocessing.Pool(processes=process_num)
    for i in range(18):
        pool.apply_async(run, (i,q))
    pool.close()
    pool.join()


if __name__ == "__main__":
    main(4)





