import time


class FuncSample:
    @staticmethod
    def get_time() -> str:
        now_time = time.localtime()
        time_str = "现在时间是%s时%s分" % (now_time.tm_hour, now_time.tm_min)
        return time_str
