
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from pedalboard.io import AudioFile
import numpy as np

from glob import glob
import os

def get_latest_file():
    files =  glob("./music/*.mp3")
    latest_file = max(files, key=os.path.getctime)
    with AudioFile(latest_file, "r") as f:
        waveform = f.read(f.frames)
        sample_rate = f.samplerate
    return waveform, sample_rate

def make_spectogram():
    waveform, sample_rate = get_latest_file()

    num_channels, num_frames = waveform.shape
    with plt.xkcd():
        figure = Figure() 
        axes = figure.subplots(num_channels, 1)
        if num_channels == 1:
            axes = [axes]
        for c in range(num_channels):
            axes[c].specgram(waveform[c], Fs=sample_rate)
            if num_channels > 1:
                axes[c].set_ylabel(f"Channel {c+1}")
        figure.suptitle("Spectrogram")
    return figure
