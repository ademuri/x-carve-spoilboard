
width = 753;
height = 766;
spacing = 75;
diameter = 6.75;

for (x = [0 : spacing : width]) {
    for (y = [0 : spacing : height]) {
        translate([x, y]) {
            circle(d = diameter);
        }
    }
}