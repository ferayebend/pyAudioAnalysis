import os, sys
from math import ceil

from sciaudio import audioSegmentation as aS
from sciaudio import audioBasicIO
from optparse import OptionParser

from datetime import datetime, timedelta

import yaml

def getSegmentAnnotations(options):
    audio_file_path = options.audio
    if not options.smoothWindow:
        options.smoothWindow = 0.2
    if not options.Weight:
        options.Weight = 0.1
    Fs, x = audioBasicIO.readAudioFile(audio_file_path)
   
    cuts = optimizeAudioSegments(Fs,x)
    annotations = []
    for cut in cuts:
        print(cut)
        segment = aS.silenceRemoval(x[int(cut[0]):int(cut[1])], int(Fs), 0.040, 0.040, 
                                 smoothWindow = float(options.smoothWindow), 
                                 Weight = float(options.Weight), plot = False)

        annotations += segments2Annotation(segment,offset=float(cut[0])/Fs)
    return annotations

def postProcessAnnotations(annotations, t_limit=3., t_max=15.):
    new_annotations = []
    new_annotations.append(annotations[0])
    for annotation in annotations[1:]:
        diff = float(annotation[0]) - float(new_annotations[-1][0])
        if diff > t_max:
            print('warning: %s vs %s distance too large'\
                   %(str(timedelta(seconds=int(float(new_annotations[-1][0])))),
                     str(timedelta(seconds=int(float(annotation[0]))))))
        if diff > t_limit:
            new_annotations.append(annotation)
    #if the last element not added
    if new_annotations[-1] != annotations[-1]:
        new_annotations.append(annotations[-1])
    return new_annotations
            

def optimizeAudioSegments(Fs, x):
    minutes = len(x)/Fs/60. # in int 
    parts = int(ceil(minutes/20.)) # parts >= 1
    
    step = len(x)/parts - len(x)/parts%Fs # result should be int divisible by Fs
    cuts = [] #  beginning and the end indicies for each cut
    for i in range(parts-1):
        cuts.append((step*i,step*(i+1)))
    cuts.append((step*(parts-1),-1))
    return cuts

def segments2Annotation(segments, offset=0.0):
    return [('%.3f'%(segment[0]+offset),'x') for segment in segments]

def writeAnnotation(annotations,filename):
    with open(filename,'w') as f:
        for a in annotations:
            f.write(','.join(a)+'\n')

def main(options):
    start = datetime.now()

    if not os.path.isfile(options.audio):
        print("ERROR: Cannot open file", options.audio)
        sys.exit()

    annotations = getSegmentAnnotations(options)
    processed_annotations = postProcessAnnotations(annotations)
    #with open(options.audio.replace('.wav','_autosegments.yaml'),'w') as f:
    #    yaml.dump(processed_annotations,f)
    writeAnnotation(processed_annotations,options.audio.replace('.wav','_autosegments.csv'))
    
    end = datetime.now()
    print('it took: ',str(end-start))

if __name__ == "__main__":
    usage = "usage: %prog [-a infile] [option]"
    parser = OptionParser(usage=usage)
    parser.add_option("-a", "--audio", dest="audio", default=None, help="audio file to be segmented", type="string")
    parser.add_option("-s", "--smoothWindow", dest="smoothWindow", default=0.2, help="smoothing window", type="float")
    parser.add_option("-w","--Weight", dest="Weight", default=0.1, help="weight for silenceRemoval [default: %default]")
    (options, args) = parser.parse_args()

    main(options)
