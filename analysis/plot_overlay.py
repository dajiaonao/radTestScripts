#!/usr/bin/env python
import os, sys, re, glob
from ROOT import *
from rootUtil import useAtlasStyle, waitRootCmdX, savehistory, mkupHistSimple, get_default_fig_dir
funlist=[]

sDir = get_default_fig_dir()
sTag = 'test_'
sDirectly = False
if gROOT.IsBatch(): sDirectly = True

def checkFirstLine(f):
    with open(f) as f1:
        line1 = f1.readline()
        fs = line1.rstrip().split()
        if float(fs[1])>0.3:
            print f

def plotX1(files, info=None, fields='F1F/F:F2F/F'):
    t0 = None
    for f in glob.glob(files):
        z = os.path.getsize(f)
        if z < 100000:
            print 'skipping small file',f,'with size', z
            continue
        elif z>500000:
            print 'skipping BIG file',f,'with size', z
            continue
#         checkFirstLine(f)
#         return
        print f

        if t0 is not None:
            t0.ReadFile(f)
        else:
            t0 = TTree()
            t0.ReadFile(f,fields)
    m1 = t0.GetMinimum('F1F')
    h1 = TH2D('h1','Waveform;t [ns]; V [V]', 20000,m1,m1+1000,10000,0.10,0.4)
    t0.Draw("F2F:F1F>>h1","","colz")

    if info is not None:
        lt = TLatex()
        lt.DrawLatexNDC(0.2,0.9,info)

    waitRootCmdX()

def test():
    dir0 = os.getenv('SAMPLEDIR_LAMB')
    print dir0
    
    gStyle.SetPadRightMargin(0.16)

#     dir1 = '/data/Samples/719/GSMC_script/Afternoon/fetch_data/'
    dir1 = '/data/Samples/719/GSMC_script/Afternoon/period3/'
    info = '0.8 m'
#     dir1 = '/data/Samples/719/GSMC_script/Morning/period3/'
#     info = '5 m'

#     dir1 = '/data/Samples/719/GSMC_script/Morning/period3b/'
#     info = '5 m, exclude low current part'

    fields = 'F1F/F:F2F/F'
    plotX1(dir1+'2018-03-10_*_*_*.dat', info)
#     plotX1(dir1+'2018-03-10_12_12_*.dat', info)

    ### check every 10 min
    #for i in range(6):
    #    print i
    #    plotX1(dir1+'2018-03-10_15_'+str(i)+'*_*.dat')

    
#     t0.ReadFile(dir1+'2018-03-10_16_58_58.dat','F1F/F:F2F/F')
#     t0.ReadFile(dir1+'2018-03-10_16_59_58.dat')

funlist.append(test)

if __name__ == '__main__':
    savehistory('.')
    useAtlasStyle()
    for fun in funlist: print fun()
