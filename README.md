# gimpPlugin-animation to spritesheet


 aligns different layers of an image into one image.
 since gimp outputs the result of animations into several layers, it is sometimes useful to put all of these layers into 
 one image that can be used as a spritesheet, in game development for instance.

just a little gimp plugin i created to turn multiple layers into one image by juxtaposing every layer next to eachother.
     _____________
    |             |              ________________________________________
  | |             |             |             :             :            |
| | |             |  ------->   |             :             :            |
| | |             |             |             :             :            |
| | |____________ |             |             :             :            |
| |____________|                |_____________:_____________:____________|
|____________|

MULTIPLE LAYERS    ==========> one layer with all layers next to eachother in a NEW IMAGE (so it doesn't touch you original image)

This script must be placed in ~/.gimp-n.m/plug-ins

# (c) doryfor 2022 
# this is just a very simple script to turn multiple layers into one image
# by pasting them next to eachother. this was quite useful to turn animations made
# by gimp into one single image with all the frames present on the same layer. 

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

# This script must be placed in ~/.gimp-n.m/plug-ins
