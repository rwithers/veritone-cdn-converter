import glob
import sys
import os
from pydub import AudioSegment

dict30Sec = dict()
dict60Sec = dict()

count30 = 0
count60 = 0
code30 = '97004'
code60 = '97005'


for filename in sorted(glob.iglob(sys.argv[1] + '**/*.MP3', recursive=True)):
  pos1 = filename.rfind('/')
  file = filename[pos1 + 1:]
  filepath = filename[0:pos1]
  fileNoExtension = file[0:filename.rfind('.')]
  filenameNoExtension = filename[0:filename.rfind('.')]
  file_stats = os.stat(filename)
  filesizeMB = file_stats.st_size / (1024 * 1024)
  print(file, filename, filepath, filenameNoExtension)

  if (filesizeMB < 1):
    if dict30Sec.get(fileNoExtension) is None:
      dict30Sec[fileNoExtension] = code30 + '.' + format(count30, '03d') 
      print(dict30Sec[fileNoExtension])
      count30 = count30 + 1
      mp3file = AudioSegment.from_file(filename, "mp3")
      mp3file.export(filepath + '/' + dict30Sec[fileNoExtension] + ".wav", "wav")
  else:
    if dict60Sec.get(fileNoExtension) is None:
      dict60Sec[fileNoExtension] = code60 + '.' + format(count60, '03d') 
      print(dict60Sec[fileNoExtension])
      count60 = count60 + 1
      mp3file = AudioSegment.from_file(filename, "mp3")
      mp3file.export(filepath + '/' + dict60Sec[fileNoExtension] + ".wav", "wav")

## Print 30 Second Spots 
keys = dict30Sec.keys()
for key in keys:
  print (key + "\t\t" + dict30Sec[key])

## Print 60 Second Spots 
keys = dict60Sec.keys()
for key in keys:
  print (key + "\t\t" + dict60Sec[key])

