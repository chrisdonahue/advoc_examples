# import os
# from shutil import copyfile

# experiment_name = "/data2/advoc/userstudy/Waveforms/"
# exp_sub_name = "Jokes_Tacotron2_R9Y9_Mel80"
# experiment_name += exp_sub_name


# # methods = ["srezNoBN", "srez_small_NoBN", "waveglow", "WaveNetVocoder", "LWS", "Original"]
# methods = ["srezNoBN", "srez_small_NoBN", "waveglow", "WaveNetVocoder", "LWS"]
# name_maps = {
#     'srezNoBN' : 'Advoc',
#     'srez_small_NoBN' : 'Advoc_small',
#     'waveglow' : 'Waveglow',
#     'WaveNetVocoder' : 'Wavenet',
#     'LWS' : 'Pinv',
#     'Original' : 'Real'
# }

# # file_names = ["LJ050-0185.wav", "LJ050-0040.wav", "LJ048-0188.wav", "LJ049-0205.wav"]
# file_names = ["Jokes-0002.wav", "Jokes-0007.wav", "Jokes-0018.wav", "Jokes-0029.wav"]

# dest_base = "/data2/paarth/advocWeb"
# dest_dir = "{}/{}".format(dest_base, exp_sub_name)

# if not os.path.isdir(dest_dir):
#     os.makedirs(dest_dir)

# for method in methods:
#     dest_dir = "{}/{}".format(dest_base, exp_sub_name)
#     dest_dir = "{}/{}".format(dest_dir, name_maps[method])
#     if not os.path.isdir(dest_dir):
#         os.makedirs(dest_dir)
#     for fidx, file_name in enumerate(file_names):
#         if method != "Original":
#             source_file_name = "{}_{}/{}".format(experiment_name, method, file_name)
#         else:
#             source_file_name = "{}/{}".format("/data2/advoc/userstudy/Waveforms/LJSpeechTest_Real_Original", file_name)
#         dest_file_name = "{}/{}.wav".format(dest_dir, fidx + 1)
#         copyfile(source_file_name, dest_file_name)
#         print("Done", method, fidx)

# print("Done")



import os
from shutil import copyfile

experiment_name = "/data2/advoc/userstudy/Waveforms/"
# exp_sub_name = "Jokes_Tacotron2_R9Y9_Mel80"
# experiment_name += exp_sub_name


# methods = ["srezNoBN", "srez_small_NoBN", "waveglow", "WaveNetVocoder", "LWS", "Original"]
methods = [
    "LJSpeechTest_Real_R9Y9_Mel20_GL60", 
    "LJSpeechTest_Real_R9Y9_Mel20_LWS", 
    "LJSpeechTest_Real_R9Y9_Mel20_srezNoBN", 
    "LJSpeechTest_Real_R9Y9_Mel40_GL60", 
    "LJSpeechTest_Real_R9Y9_Mel40_LWS", 
    "LJSpeechTest_Real_R9Y9_Mel40_srezNoBN", 
    "LJSpeechTest_Real_R9Y9_Mel80_GL60", 
    "LJSpeechTest_Real_R9Y9_Mel80_LWS", 
    "LJSpeechTest_Real_R9Y9_Mel80_srezNoBN"
]

name_maps = {
    "LJSpeechTest_Real_Original" : "Real",
    'LJSpeechTest_Real_R9Y9_Mel20_GL60' : 'mel20_gl',
    "LJSpeechTest_Real_R9Y9_Mel20_LWS" : 'mel20_lws' , 
    "LJSpeechTest_Real_R9Y9_Mel20_srezNoBN" : 'mel20_advoc', 
    "LJSpeechTest_Real_R9Y9_Mel40_GL60": 'mel40_gl',
    "LJSpeechTest_Real_R9Y9_Mel40_LWS": 'mel40_lws', 
    "LJSpeechTest_Real_R9Y9_Mel40_srezNoBN": 'mel40_advoc', 
    "LJSpeechTest_Real_R9Y9_Mel80_GL60": 'mel80_gl',
    "LJSpeechTest_Real_R9Y9_Mel80_LWS": 'mel80_lws', 
    "LJSpeechTest_Real_R9Y9_Mel80_srezNoBN": 'mel80_advoc', 
}

file_names = ["LJ050-0185.wav", "LJ050-0040.wav", "LJ048-0188.wav", "LJ049-0205.wav"]
# file_names = ["Jokes-0002.wav", "Jokes-0007.wav", "Jokes-0018.wav", "Jokes-0029.wav"]

dest_base = "/data2/paarth/advocWeb"
dest_dir = "{}/{}".format(dest_base, "compression")

if not os.path.isdir(dest_dir):
    os.makedirs(dest_dir)

for method in methods:
    dest_dir = "{}/{}".format(dest_base, "compression")
    dest_dir = "{}/{}".format(dest_dir, name_maps[method])
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)
    for fidx, file_name in enumerate(file_names):
        if method != "Original":
            source_file_name = "{}/{}/{}".format(experiment_name, method, file_name)
        else:
            source_file_name = "{}/{}".format("/data2/advoc/userstudy/Waveforms/LJSpeechTest_Real_Original", file_name)
        dest_file_name = "{}/{}.wav".format(dest_dir, fidx + 1)
        copyfile(source_file_name, dest_file_name)
        print("Done", method, fidx)

print("Done")