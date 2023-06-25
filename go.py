#!/usr/bin/env python
import os,sys,subprocess
from sys import exit,argv
from os import popen,system
sys.path.append("/mnt/diskc/1/dauriac/lib")
def w(x):sys.stdout.writelines(x)

import jc2 as jc

files = jc.cmd("ls */rendu*")
D = 0.
for f in files:
    f = f.replace("\n","")
    cmd = "ffmpeg -i "+f+ " 2>&1| grep Duration"
    ans = jc.cmd(cmd)
    ans = ans[0]
    duration = ans.split()[1]
    duration = duration.replace(',','')
    size= jc.cmd("ls -lh "+f)
    size = size[0].replace(',','.')
    aux  = size.split()
    size = aux[4]
    nom = f.split('/')[0]
    if len(nom)<=7:
        nom+='\t'
    print ("%s\t\t%s\t\t%s"%(nom,size,duration))
    aux = list(map(lambda x:float(x),duration.split(':')))
    D += aux[1]*60+aux[2]
m = int(D)//60
s = D-m*60
print("%d clips, duree totale %2d:%02d"%(len(files),m,s))
