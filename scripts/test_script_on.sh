#!/bin/bash

# Max Kessler <max.e.kessler@gmail.com>
# test if the wemo emulation is working in an esay way

TIME=$(date +%d/%m/%Y\ %H:%M:%S)
FTIME=$(date +%d_%m_%Y_%H_%M_%S)
FILE=on-${FTIME}.txt

echo "on test at $TIME" > ~/${FILE}
