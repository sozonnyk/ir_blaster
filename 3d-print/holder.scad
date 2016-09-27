btm_h = 7;
btm_rad = 30;
btm_thik = 4;

low_leg_width = 40;
low_leg_length = 76;

hi_leg_h = 70;
hi_leg_thik = 5;

side_leg_width = 76; //From circle center
side_leg_h = 30;

holder_thik=1;
holder_rad=5.7;
holder_h=30;

$fn=90;

difference() {
    union() {
      cylinder(btm_h, btm_rad + btm_thik, btm_rad + btm_thik, false);
        translate([0,-low_leg_width/2,0])
          #cube([low_leg_length,low_leg_width,btm_h]);
    }
    cylinder(btm_h, btm_rad , btm_rad , false);
    
    linear_extrude(height=height+2) {
         polygon(points=[[0,0.6*btm_rad],[0,-0.6*btm_rad],[-1.2*btm_rad,-1.2*btm_rad],[-1.2*btm_rad,1.2*btm_rad]]);  }
}

translate([low_leg_length,-low_leg_width/2,0])
cube([hi_leg_thik,low_leg_width,hi_leg_h]);

translate([low_leg_length,0,hi_leg_h-side_leg_h])
cube([hi_leg_thik,side_leg_width,side_leg_h]);

translate([low_leg_length-holder_rad+holder_thik,side_leg_width-holder_rad,hi_leg_h-side_leg_h])
    difference() {
    cylinder(holder_h,holder_rad,holder_rad,false);
    cylinder(holder_h,holder_rad-holder_thik,holder_rad-holder_thik,false);
      linear_extrude(height=holder_h) {
        polygon(points=[[0,0.6*holder_rad],[0,-0.6*holder_rad],[-1.2*holder_rad,-1.2*holder_rad],[-1.2*holder_rad,1.2*holder_rad]]);  
      }
    }