import os
import shutil
import psutil
from datetime import datetime, timedelta
from time import mktime


def old_files(files, max_time):
    yield from (name for name in files if os.stat(name).st_mtime < max_time)


def clearing(delay):
    max_time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    max_time -= timedelta(days=delay)
    max_time = mktime(max_time.timetuple()) 
    for name in old_files(source, max_time):
        new_name = os.path.join(dst, os.path.relpath(name, source))
        shutil.move(os.path.join(source, name), os.path.join(dst, name))


source = '/Загрузочная'
dst = '/old'
delay = 90
clearing(delay)
usage = psutil.disk_usage(source)

while int(usage) >= 95:
    delay = delay-1
    clearing(delay)
    usage = psutil.disk_usage(source)
