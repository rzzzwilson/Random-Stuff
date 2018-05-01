import os
import time

root = "."

def get_last_write_time(filename):
    st = os.stat(filename)
    convert_time_to_human_readable = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(st.st_mtime))
    return convert_time_to_human_readable

timestr = time.strftime("%Y%m%d_%H%M%S")

for path, dirs, files in os.walk(os.path.join(root, dir)):
    for f in files:
       if any([f.endswith(x) for x in config[camID]["media_file"]]):
           print("os.rename('%s', '%s')" % (os.path.join(path, f),
                                            os.path.join(path, "%s" % timestr+'__'+f)))
#           os.rename(os.path.join(path, f), os.path.join(path, "%s" % timestr+'__'+f))
