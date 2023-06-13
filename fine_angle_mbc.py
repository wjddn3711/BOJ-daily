# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = int(input())
BC = int(input())

MC = math.sqrt(AB**2 + BC**2)
print(f"{round(math.degrees(math.acos(BC/MC)))}{chr(0xB0)}")
