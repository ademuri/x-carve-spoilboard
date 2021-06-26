line_width = 1;

width = 700;
height = 700;
grid_spacing = 10;
major_label_spacing = 50;
tick_height = 5;
label_font_size = 10;


for (x = [0 : grid_spacing : width]) {
    translate([x, 0]) {
        //square([line_width, height]);
    }
}
for (x = [0 : major_label_spacing : width]) {
    translate([x, -tick_height]) {
        //square([line_width, tick_height]);
    }
    translate([x, -(tick_height + 2)]) {
        text(text = str(x / 10), size = label_font_size, halign = "center", valign = "top");
    }
}


for (y = [0 : grid_spacing : height]) {
    translate([0, y]) {
        //square([width, line_width]);
    }   
}
for (y = [0 : major_label_spacing : height]) {
    translate([-tick_height, y]) {
        //square([tick_height, line_width]);
    }
    translate([-(tick_height + 2), y]) {
        text(text = str(y / 10), size = label_font_size, halign = "right", valign = "center");
    }
}