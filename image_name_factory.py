class ImageNameFactory:
  def get_canonical_image_names(self, subject, count):
    seeds = range(1, count + 1)
    return [get_simple_image_name(s) if count < 1000 else get_volumetric_image_name(s) for s in seeds]

  def get_simple_image_name(self, subject, ordinal):
    return "{}{:03d}.jpg".format(subject, ordinal)

  def get_volumetric_image_name(self, subject, ordinal):
    vol = (ordinal // 1000) + 1
    return "vol{:03d}/{}{:03d}.jpg".format(vol, subject, ordinal)
  