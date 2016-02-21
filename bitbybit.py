def get_and(i, j):
     if i is False or j is False:
          return False
     elif i is None or j is None:
          return None
     else:
          return True

def get_or(i, j):
     if i is True or j is True:
          return True
     elif i is None or j is None:
          return None
     else:
          return False

while True:
     n = int(raw_input())
     if n == 0:
          break
     reg = [None for x in xrange(32)]
     for _ in range(n):
          command = raw_input().split(" ")
          if len(command) is 2:
               i = int(command[1])
               if command[0][0] == "S":
                    reg[i] = True
               else:
                    reg[i] = False
          else:
               i, j = [int(x) for x in command[1:]]
               if command[0][0] == "A":
                    reg[i] = get_and(reg[i], reg[j])
               else:
                    reg[i] = get_or(reg[i], reg[j])
     # Print out the reg
     to_char = lambda x: "?" if x is None else ("1" if x else "0")
     print "".join(to_char(x) for x in reg)[::-1]