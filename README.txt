[1]依赖于ConcurrentLogHandler第三方库
pip3 install ConcurrentLogHandler

[2]问题
日志文件流关闭后，第一次重命名存在bug，程序会再一次尝试重命名，直到重命名成功。该问题不影响多进程写入。

[3]改进
如何保留缓存的日志文件可以根据个人喜好，修改getFilesToDelete函数。

[4]格式问题
vim xxx.sh
:set ff
如果出现fileforma＝dos。
:set fileformat=unix
