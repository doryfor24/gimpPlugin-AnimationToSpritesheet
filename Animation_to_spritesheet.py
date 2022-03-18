#!/usr/bin/python

# -*- coding: utf-8 -*-


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

from gimpfu import *

 
def myPlugin(image,layer):
  # extract visible layers AND count the amount of layers on the image
  layers=[l for l in image.layers if l.visible]
  #take the image size
  width = image.layers[0].width
  height = image.layers[0].height
  # Make a new image. Size 10x10 for now -- we'll resize later.
  img = gimp.Image(1, 1, RGB)
  # Create a new layer 
  layer = gimp.Layer(img, "animation layer", len(layers)*width, height,RGBA_IMAGE, 100, NORMAL_MODE)
  #add layer to image
  img.add_layer(layer,0)
  # Resize the image to the size of the layer
  img.resize(layer.width, layer.height, 0, 0)
  #display a message for no good reason
  pdb.gimp_message( "info : %d layers found. this will take a few seconds." % len(layers) )
  
 
  
  #copy and paste whatever is on the layer to the correct place on the image
  i=0
  for l in image.layers:
    
   
    buffer_index = pdb.gimp_edit_copy (l)
    floating = pdb.gimp_edit_paste(img.layers[0],buffer_index)
    pdb.gimp_layer_set_offsets(floating, width*(len(layers)-1-i), 0)
    pdb.gimp_floating_sel_anchor(floating)
    i = i +1
    
    
  # Create a new image window
  gimp.Display(img)
  # Show the new image window
  gimp.displays_flush()
register(
  "animation_to_spritesheet",
  "aligns different layers of an image into one image. \n since gimp outputs the result of animations into several layers, it is sometimes useful to put all of these layers into \n one image that can be used as a spritesheet, in game development for instance.",
  "aligns different layers of an image into one image",
  "doryfor",
  "doryfor",
  "2020",
  "<Image>/Spritesheets/animation_to_spritesheet",
  "*",
  [],
  [],
  myPlugin)
 
main()