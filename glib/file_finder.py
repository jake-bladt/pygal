import glob
import os

class FileFinder:
  def __init__(self, path):
    self.path = path

  def get_files(self, pattern):
    search_pattern = os.path.join(self.path, pattern)
    return glob.glob(search_pattern)
