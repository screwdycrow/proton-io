

def main(script,myDir,mySel,magickExec,composeType,background,scale,size,quality,outName,outDir) :
    import subprocess
    #print script,myDir,mySel,aerenderExec,compName,startf,endf,outName,outDir
    print script,myDir,mySel,magickExec,composeType,background,scale,size,quality,outName,outDir
    mySel = open(mySel,"r")
    mySel = mySel.read()
    mySel = mySel.split(',')

    #start creating the arguments list
    args = []
    #resolving the magick executable
    if magickExec == 'None':
        scriptDir = os.path.dirname(__file__)
        magickPath = os.path.join(scriptDir,'..','..','libs','magick.exe')
        magickPath = os.path.realpath(magickPath)
        args.extend([magickPath])
    else:
        args.extend([magickExec])

    #start creating the other arguments
    args.extend(['convert',mySel[0],mySel[1]])

    #resolving file name from source
    pre, ext = os.path.splitext(mySel[0])
    print ("compose type = " + composeType)
    outFile = pre + '_{}.jpeg'.format(composeType)

    args.extend(['-compose',composeType])
    #args.extend(['-flatten'])

    #check if arguments exist to add
    if background != 'None':
        args.extend(['-background',background])
    if scale != 'None':
        args.extend(['-scale',scale])
    if size != 'None':
        args.extend(['-size',size])
    if quality != 'None':
        args.extend(['-quality',quality])
    if (outDir != 'None'):
        #create the directory if it doesn't exist
        if not os.path.exists(outDir):
            os.makedirs(outDir)
        outRender = os.path.join(outDir,outFile)
        args.extend(["-composite",outRender])
    else:
        args.extend(["-composite",outFile])

    print args
    #execute the args
    subprocess.Popen(args)



if __name__ == '__main__':
            import os
            import sys
            import re

            try:
                main(*sys.argv)
                raw_input("Press ENTER to exit")
            except:
                print sys.exc_info()[0]
                import traceback
                print traceback.format_exc()
                print "Press Enter to continue ..."
                raw_input("Press ENTER to exit")
