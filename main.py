from lib import coordinate_mapper
from lib import grind

mapper = coordinate_mapper.CoordinateMapper('C:\\dev\\python\\rbot\\images\\buttons')
grinder = grind.Grind(mapper.map_buttons())