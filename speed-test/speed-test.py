f = open("speed-test.nc", "w")

distance = 150
spacing = 10
safe_height = 5
plunge_speed = 100

speeds = [1600, 2000, 2400, 2800, 3200]

f.write("; Speed test\n\n")
f.write("G21\n")
forward = True

x = 0
y = distance
f.write(f"G00 Z{safe_height}\n")
f.write(f"G00 X{x} Y{y}\n\n")

for speed in speeds:
    f.write(f"G01 Z0 F{plunge_speed}\n")
    if forward:
        y -= distance
    else:
        x -= distance
    f.write(f"G01 X{x} Y{y} F{speed}\n")

    if forward:
        x += distance
    else:
        y += distance
    f.write(f"G01 X{x} Y{y} F{speed}\n")
    f.write(f"G00 Z{safe_height}\n")

    x += spacing
    y += spacing

    f.write(f"G00 X{x} Y{y}\n\n")
    forward = not forward

f.write(f"G00 Z{safe_height}\n")
f.write(f"G00 X0 Y0\n")

f.close()
