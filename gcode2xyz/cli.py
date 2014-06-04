#!/usr/bin/env python
""" Command Line Tool for converting gcode from sli3r into 3w file for xyz davinci printer."""
import os
import sys
import os.path
import base64

header = """; filename = composition.3w
; machine = daVinciF10
; material = default
; layer_height = 0.2
; fill_density = 0.10
; shells = 3
; speed = 60
; total_layers = 124
; total_filament = 2116.02
; dimension = 50.00:50.00:50.00
; extruder = 1

"""


def convert_gcode_to_3w(input_filename):
  data = header # start with the default header
  input_file = open(input_filename,'rb')
    
  input_file.readline() # discard the first line  
  
  data += input_file.read() # append the rest of the file
  
  filename_base, extension = os.path.splitext(input_filename)
  output_filename = filename_base + '.3w'
  out_file = open(output_filename, 'wb')
  out_file.write(base64.b64encode(data))
  #out_file.write(data)
  return


def main():
  if (len(sys.argv) < 2):    
    print  """ Command Line Tool for converting gcode from sli3r into 3w file for xyz davinci printer. 
    Usage: <input_file>.gcode  
    """
    return 1
  filename = sys.argv[1]
  
  print 'converting %s' % (filename)
  
  convert_gcode_to_3w(filename)
  
    
  return

if __name__ == "__main__":
    main()
