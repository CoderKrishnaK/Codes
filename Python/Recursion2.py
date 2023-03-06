import sys

print(sys.getrecursionlimit())
# prints total no. of stack frams allowed for calling function

# Never Change the recursion limit(Bad programming practice)
# Solid programming Practice
sys.setrecursionlimit(4000)
print(sys.getrecursionlimit())