#!/usr/bin/env python
import sys, glob, os

isDebug = False

def force_link(target, des):
    '''if des is linked to target, do nothing, otherwise delete the des and link the target to des'''
    if os.path.exists(des):
        if os.path.islink(des):
            if os.path.realpath(des) == target:
                return
            else:
                if isDebug: print "Deleting", des
                os.remove(des)
        else:
            print 'File', des, 'already exist. Remove or rename it before running this program...'
            sys.exit(1)
    #link it here
    if isDebug: print "will link", target, 'to', des
    os.symlink(target, des)

def link_files(pattern, n, ref=None, start=None):
    if start is None:
        fs = glob.glob(pattern)
    else:
        t0 = os.path.getctime(start)
        fs = [x for x in glob.glob(pattern) if os.path.getctime(x)>t0] 
    fs_sorted = sorted(fs, key=lambda x:os.path.getctime(x))

    N = len(fs_sorted)
    flist = [fs_sorted[int((1-1./(2**i))*N)] for i in range(n-1)]+[fs_sorted[-2]]

    if ref is not None and ref not in flist:
        flist.append(ref)

    dir1 = '_links/'
    if not os.path.exists(dir1): os.makedirs(dir1)
    ### create the links for the selected files
    for i,f in enumerate(flist):
        force_link(f,dir1+'sample_'+str(i))

def run_main():
    pattern = '/data/Samples/719/GSMC_script/Morning/period3/2018-03-10_*.dat'
    nP = 5 if len(sys.argv)<2 else int(sys.argv[1])
    link_files(pattern, nP, None, '/data/Samples/719/GSMC_script/Morning/period3/2018-03-10_14_17_48.dat')

if __name__ == '__main__':
    run_main()
