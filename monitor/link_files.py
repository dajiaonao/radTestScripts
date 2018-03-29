#!/usr/bin/env python
import sys, glob, os
print "test"

pattern = ''
ref = None
N = 5


def force_link(target, des):
    '''if des is linked to target, do nothing, otherwise delete the des and link the target to des'''
    if os.path.exists(des):
        if os.path.islink(des):
            if os.path.realpath(des) == target:
                return
            else:
                print "Deleting", des
                os.remove(des)
#                 delete des
        else:
            print 'File', des, 'already exist. Remove or rename it before running this program...'
            sys.exit(1)
#             raise exception
    #link it here
    print "will link", target, 'to', des
    os.symlink(target, des)

class doMonitor:
    '''Get the links and launch the monitor script'''
    def __init__(self):
        pass
    def start(self):
        ### get the files
        ### make the links
        ### run the monitor is it's not done yet
        pass

def link_files(pattern, n, ref=None, start=None):
    if start is None:
        fs = glob.glob(pattern)
    else:
        t0 = os.path.getctime(start)
        fs = [x for x in glob.glob(pattern) if os.path.getctime(x)>t0] 
#     print fs
    fs_sorted = sorted(fs, key=lambda x:os.path.getctime(x))
#     print fs_sorted
    N = len(fs_sorted)

#     print N
    flist = [fs_sorted[int((1-1./(2**i))*N)] for i in range(n-1)]+[fs_sorted[-2]]
#     print flist
#     print [int((1-1./(2**i))*N) for i in range(n-1)]

#     for i in range(5):
#         print os.path.getctime(fs[i])
       
    for i,f in enumerate(flist):
        force_link(f,'sample_link_'+str(i))

def run_main():
    pattern = '/data/Samples/719/GSMC_script/Morning/period3/2018-03-10_*.dat'
    nP = 5 if len(sys.argv)<2 else int(sys.argv[1])
    link_files(pattern, nP, None, '/data/Samples/719/GSMC_script/Morning/period3/2018-03-10_14_17_48.dat')

if __name__ == '__main__':
    run_main()
