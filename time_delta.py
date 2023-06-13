#!/bin/python3

import os
import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):
    time_format = "%a %d %b %Y %H:%M:%S %z"
    time1 = datetime.datetime.strptime(t1, time_format).timestamp()
    time2 = datetime.datetime.strptime(t2, time_format).timestamp()
    return str(int(abs(time1 - time2)))


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + "\n")

    fptr.close()
