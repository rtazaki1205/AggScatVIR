#include "colors.inc"
#include "shapes.inc"		
#include "povparam.inc"

light_source
{
    <100,100,-100>
    color rgb <1,1,1> 
    rotate <0,0,0>
    parallel
}

light_source
{
    <100,0,0>
    color rgb <1,1,1> 
    rotate <0,0,0>
    parallel
}

camera
{
    location <camera_distance,0,0> 
    look_at  <0,0,0>
    right <1.0,0,0>
}


text {
    ttf "timrom.ttf" reftext 0, 0
    rotate <0,-90,0>
    scale fontsize
    translate <0,refy+reftext_yoff,-0.5*ref_length+refz>
    pigment { refclr }
}

cylinder{
 <0, 0, -0.5*ref_length>,     
 <0, 0, 0.5*ref_length>,
 ref_barwidth pigment { refclr }
 rotate <0,0,0>
 translate <0,refy,refz>
}

background { color bgcolor }

mesh2{
    #include "coord.dat"
    pigment { parcolor } 
    scale <av_scaled,av_scaled,av_scaled>
    rotate <rotate_x,rotate_y,rotate_z>
    translate<-xc,-yc,-zc>
    finish{
        diffuse 2.0
        specular 0.2
    }
}
