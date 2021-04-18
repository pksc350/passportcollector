class Stamp:
  def __init__(self, country, date, color, shape):
    self.country = country
    self.date = date
    self.color = color
    self.shape = shape

stamps = [
  Stamp('Bahamas', 'Dec 18, 2017', 'Black', 'Rectangle'),
  Stamp('Indonesia', 'Dec 13 2019', 'Green', 'Square'),
  Stamp('Thailand', 'Dec 31 2019', 'Blue', 'Triangle')
]
