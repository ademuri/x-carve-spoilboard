f = open("speed-test.nc", "w")

distance = 150
spacing = 10
safe_height = 5
plunge_speed = 100

speeds = [1600, 2000, 2400, 2800, 3200, 3600, 4000]

f.write("; Speed test\n\n")
f.write("G21\n")
forward = True

x = spacing
y = 0
f.write(f"G00 Z{safe_height}\n")
f.write(f"G00 X{x} Y{y}\n\n")

for speed in speeds:
    f.write(f"G01 Z0 F{plunge_speed}\n")
    if forward:
        x -= spacing
    else:
        x += spacing
    f.write(f"G01 X{x} Y{y} F{speed}\n")

    if forward:
        y += distance
    else:
        y -= distance
    f.write(f"G01 X{x} Y{y} F{speed}\n")
    f.write(f"G00 Z{safe_height}\n")

    if forward:
        x += spacing / 2
    else:
        x += spacing * 1.5

    f.write(f"G00 X{x} Y{y}\n\n")
    forward = not forward

f.write(f"G00 Z{safe_height}\n")
f.write(f"G00 X0 Y0\n")

f.close()
