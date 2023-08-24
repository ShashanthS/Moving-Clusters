import numpy as np

def hms_to_deg(input):
    temp = input.split()
    # print(temp[0], temp[1], temp[2])
    return float(temp[0]) * 15 + float(temp[1]) * .25 + float(temp[2]) * 0.0042


def dms_to_deg(dms_val):
    temp = dms_val.split()
    return float(temp[0]) + float(temp[1]) * (1/60) + float(temp[2]) * (1/3600)


print(hms_to_deg('03 46 24.2'))
print(dms_to_deg('24 06 50'))