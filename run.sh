# Step.1 Download audio
mkdir ./raw_audio
python download_thesound_audio.py

# Step.2 split audio
mkdir test_set
./split_audio.sh
