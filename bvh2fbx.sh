#!/bin/bash

for file in `ls | grep .bvh`
do
  echo $file
  `blender -b --python ./convert_fbx.py -- $file`
done
