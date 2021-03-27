from pydub import AudioSegment
import os
import glob
import numpy as np
# target_dbfs = -18.5
from pydub import effects  

inp_path = './'
out_path = inp_path



# value returned by get_mean_db_vctk
target_dbfs = -24.632442475923607
print(target_dbfs)

for audio_file in glob.glob(inp_path+'**/*.wav', recursive=True):
    print(audio_file)
    dest_file = audio_file.replace(inp_path, out_path)
    os.makedirs(os.path.dirname(dest_file), exist_ok=True)

    song = AudioSegment.from_file(audio_file)
    change_in_dBFS = target_dbfs - song.dBFS
    normalized_sound = song.apply_gain(change_in_dBFS)


    # print('my normalize:', normalized_sound.dBFS)
    # normalized_sound2 = effects.normalize(song)
    # print('pydub normalize:', normalized_sound2.dBFS)

    normalized_sound.export(dest_file, format=dest_file[-3:])
    
    
