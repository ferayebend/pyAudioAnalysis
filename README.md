
# <img src="icon.png" align="left" height="130"/> A Python library for audio feature extraction, classification, segmentation and applications

*This doc contains general info. Click [here](https://github.com/tyiannak/pyAudioAnalysis/wiki) for the complete wiki*

This is a fork of [pyAudioAnalysis](https://github.com/tyiannak/pyAudioAnalysis/), which is intended to be a lightweight, packageable version which complies with PEP8 and works in python3.

## News
 * [BK] Ported to Python3 
 * [TG ]Check out [paura](https://github.com/tyiannak/paura) a python script for realtime recording and analysis of audio data
 * [TG] January 2017: *mp3* files are also supported for single file feature extraction, classification and segmentation (using pydub library)
 * [TG] September 2016: New segment classifiers (from sklearn): random forests, extra trees and gradient boosting
 * [TG] August 2016: Update: mlpy no longer used. SVMs, PCA, etc performed through scikit-learn 
 * [TG] August 2016: Update: Dependencies have been simplified 
 * [TG] January 2016: [PLOS-One Paper regarding pyAudioAnalysis] (http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0144610) *(please cite!)*

## General
pyAudioAnalysis is a Python library covering a wide range of audio analysis tasks. Through pyAudioAnalysis you can:
 * Extract audio *features* and representations (e.g. mfccs, spectrogram, chromagram)
 * *Classify* unknown sounds
 * *Train*, parameter tune and *evaluate* classifiers of audio segments
 * *Detect* audio events and exclude silence periods from long recordings
 * Perform *supervised segmentation* (joint segmentation - classification)
 * Perform *unsupervised segmentation* (e.g. speaker diarization)
 * Extract audio *thumbnails*
 * Train and use *audio regression* models (example application: emotion recognition)
 * Apply dimensionality reduction to *visualize* audio data and content similarities

## Installation
 * via pip
 ```
 pip install git+https://github.com/ferayebend/sciaudio.git
 ```
 * via setup.py
 ```
 python3 setup.py install 
 ``` 
 * In the case of numpy/scipy dependency problems:
 ```
 pip install numpy scipy
 ```
 * via the Dockerfile
 ```
 docker build -t sciaudio .
 ```
 * Clone the source of this library: 
 ```
 git clone https://github.com/ferayebend/sciaudio.git
 ```

## Further reading
Apart from the current README file and [the wiki] (https://github.com/tyiannak/pyAudioAnalysis/wiki), a more general and theoretic description of the adopted methods (along with several experiments on particular use-cases) is presented [in this publication] (http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0144610). Please use the following citation when citing pyAudioAnalysis in your research work:
```
@article{giannakopoulos2015pyaudioanalysis,
  title={pyAudioAnalysis: An Open-Source Python Library for Audio Signal Analysis},
  author={Giannakopoulos, Theodoros},
  journal={PloS one},
  volume={10},
  number={12},
  year={2015},
  publisher={Public Library of Science}
}
```

Finally, for Matlab-related audio analysis material check  [this book](http://www.amazon.com/Introduction-Audio-Analysis-MATLAB%C2%AE-Approach/dp/0080993885).

## Author
<img src="http://cgi.di.uoa.gr/~tyiannak/image.jpg" align="left" height="100"/>

[Theodoros Giannakopoulos] (http://www.di.uoa.gr/~tyiannak), 
Postdoc researcher at NCSR Demokritos, 
Athens,
Greece


