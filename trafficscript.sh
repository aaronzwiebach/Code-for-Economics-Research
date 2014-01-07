fname=$(printf "medline13n%04d.xml.zip" $SGE_TASK_ID)


/usr/bin/python2.6 /mnt/nfs6/wikipedia.proj/odesk/gettrafficinfo.py  $SGE_TASK_ID




