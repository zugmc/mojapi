from datetime import datetime


def currenttimemillis_to_python_datetime(currenttimemillis):
    return datetime.fromtimestamp(currenttimemillis/1000)