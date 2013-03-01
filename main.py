from lib import coordinate_mapper

root_dir = 'C:\\dev\\python\\rbot\\images\\buttons'

mapper = coordinate_mapper.CoordinateMapper(root_dir)
mapper.map_buttons()

print mapper.button_coords