import os
import sys

gallery_root = os.environ['GALLERY_ROOT']

if len(sys.argv) > 1:
  gallery_path = os.path.join(gallery_root, sys.argv[1])
  print(gallery_path)
else:
  "loop through all galleries"
  pass
