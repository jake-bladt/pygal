import os
import sys

from 'glib/file_finder' import FileFinder

gallery_root = os.environ['GALLERY_ROOT']

if len(sys.argv) > 1:
  gallery_path = os.path.join(gallery_root, sys.argv[1])
  print(gallery_path)
  finder = FileFinder(gallery_path)
  files = finder.find_files('*.jpg')
  print('found {} file(s).'.format(len.files))
else:
  "loop through all galleries"
  pass
