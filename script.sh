#!/bin/bash

#$ -cwd
#$ -j y
#$ -q all.q
#$ -t 1-643
#$ -tc 70

fname=$(printf "medline13n%04d.xml.zip" $SGE_TASK_ID)


/usr/bin/python2.6 /mnt/nfs6/wikipedia.proj/odesk/finalscripts/finaldirectoryscript.py  $SGE_TASK_ID


