from pydub import AudioSegment
import os
import glob
import numpy as normalize_path
from pydub import effects  
import numpy as np
normalize_path = '../../../datasets/VCTK-Corpus-removed-silence/wav48/'

# print(os.listdir(normalize_path))
dbfs_list = []
for audio_file in glob.glob(normalize_path+'**/*.wav', recursive=True):
    # print(audio_file)
    dbfs_list.append(AudioSegment.from_file(audio_file).dBFS)


# print(dbfs_list)
target_dbfs = np.array(dbfs_list).mean()
print("Mean DBFS VCTK:", target_dbfs)
