#!/bin/bash
# untar your R installation
#tar -xzf R402.tar.gz
#tar -xzf packages_FITSio_tidyverse.tar.gz

file=$(echo $1 | cut -d"/" -f6 | cut -d"." -f1)
ext1=.tsv
ext2=.gz
wget $1
gzip -d $file$ext1$ext2

# make sure the script will use your python installation, 
# and the working directory as its home location
export PATH=$PWD/python/bin:$PATH
export PYTHONPATH=$PWD/packages
export HOME=$PWD

#find . ! -name '*[!0-9]*' -type d
#mv ./imm6010.zip $PWD/packages/afinn/
# run your script
python3 amazonML.py $file # note: the two actual command-line arguments
                          # are in myscript.sub's "arguments = " line

rm $file$ext1
#rm $file$ext1$ext2
