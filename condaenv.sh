#!/bin/bash
echo -e "Please type the directory where Anaconda is located (ie: /d/donnees/BELKHEIR/AppData): \c "

# read conda path
read  path_conda_user
path_bash="anaconda3/etc/profile.d/conda.sh"
full_path="${path_conda_user}/${path_bash}"
echo "Your path is ${path_conda_user}"

# stop if conda.sh is not found in path
if [ -e $full_path ]; then
	echo "conda.sh is detected in the selected directory"
else 
    echo "conda.sh is no detected in the selected directory"
    echo "Please enter a valid directory"
    exit 1
fi 

# initialize conda in bash
source $full_path

#conda_env=$(conda env list | awk '/yolo_test_env/ {print $1,$4}')

# create and activate env for testing
conda create --name yolo_test_env --file conda_requirements.txt
conda activate yolo_test_env

# test that import works
import_output=$(python -c "
try:
    import pandas
    import pytest
    import numpy
    import sklearn
    print('Python dependencies imported correctly')
except:
    print('abort import')
")


# Create a temporary file
TMPFILE=$(mktemp)
# Add command to activate env and clear cli
echo "source ~/.bashrc" > $TMPFILE
echo "conda activate yolo_test_env" >> $TMPFILE
echo "clear && clear" >> $TMPFILE
echo "rm -f $TMPFILE" >> $TMPFILE

# test that env is ready for use
if [ "$import_output" = "abort import" ] || $(test pytest) false; then
    echo 'Your conda environment is corrupted'
    exit 1
else
    # Start the new bash shell 
    echo "Activating your yolo_test_env"
    bash --rcfile $TMPFILE
fi
