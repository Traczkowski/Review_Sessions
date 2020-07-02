#!/bin/bash
now=$(date +"%Y_%m_%d")
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
/usr/local/bin/papermill /TDirectory/Placeholder.ipynb /TDirectory/output/output$now.ipynb && /usr/local/bin/jupyter nbconvert --to html /TDirectory/output/output$now.ipynb
#/usr/bin/python3 /TDirectory/emailer.py
echo ScriptRun!!!