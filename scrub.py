import sys

def output_to_stdout(msg):
  print msg

if len(sys.argv) > 1:
  target = sys.argv[1]
else:
