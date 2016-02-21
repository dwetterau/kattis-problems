import fileinput

def process_line(line):
    nums = [long(x) for x in line.split(" ")]
    print abs(nums[0] - nums[1])

for line in fileinput.input():
    process_line(line)
