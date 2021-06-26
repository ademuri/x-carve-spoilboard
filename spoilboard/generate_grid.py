f = open("grid.nc", "w")

width = 700
height = 700
grid_spacing = 10
major_label_spacing = 50
tick_height = 5

offset_x = 14
offset_y = 18

feed_rate = 1500
z_high = 5
z_low = 0

f.write("; Y lines\n")
forward = True
for x in range(offset_x, width + offset_x + grid_spacing, grid_spacing):
    f.write(f"G00 Z{z_high}\n")
    y_start = offset_y
    feed = feed_rate
    if (x - offset_x) % major_label_spacing == 0:
        y_start = y_start - tick_height
        feed = feed_rate * 0.3
    if forward:
        f.write(f"G00 X{x} Y{y_start}\n")
        f.write(f"G01 Z{z_low} F{feed_rate}\n")
        f.write(f"G01 X{x} Y{offset_y + height} F{feed}\n")
    else:
        f.write(f"G00 X{x} Y{offset_y + height}\n")
        f.write(f"G01 Z{z_low} F{feed_rate}\n")
        f.write(f"G01 X{x} Y{y_start} F{feed}\n")
    f.write(f"G00 Z{z_high}\n")
    f.write("\n")
    forward = not forward

f.write("\n; X lines\n")
for y in range(offset_y, height + offset_y + grid_spacing, grid_spacing):
    f.write(f"G00 Z{z_high}\n")
    x_start = offset_x
    feed = feed_rate
    if (y - offset_y) % major_label_spacing == 0:
        x_start = x_start - tick_height
        feed = feed_rate * 0.3
    if forward:
        f.write(f"G00 X{x_start} Y{y}\n")
        f.write(f"G01 Z{z_low} F{feed}\n")
        f.write(f"G01 X{offset_x + width} Y{y} F{feed}\n")
    else:
        f.write(f"G00 X{offset_x + width} Y{y}\n")
        f.write(f"G01 Z{z_low} F{feed_rate}\n")
        f.write(f"G01 X{x_start} Y{y} F{feed}\n")
    f.write(f"G00 Z{z_high}\n")
    f.write("\n")
    forward = not forward

f.close()
