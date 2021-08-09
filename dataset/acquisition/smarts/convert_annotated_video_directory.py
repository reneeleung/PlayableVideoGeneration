import os
import multiprocessing as mp
from pathlib import Path

from PIL import Image

from dataset.video import Video
import re

frames_extension = "png"
root_directory = "tmp"
output_directory = "tmp/smarts_ours"
frameskip = 0
#frameskip = 4
processes = 8

target_size = [256, 256]


def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def acquire_sequence(video_path: str, output_path: str):
    '''
    Acquires the video sequence and saves it to output_path
    :param video_path: path which contains all frames from the current input video
    :param output_path: path at which to save the captured sequence
    '''

    images = []
    actions = []
    frames = sorted(os.listdir(video_path), key=natural_keys)
    capture_index = 0
    end_frame = len(frames)
    while capture_index < end_frame:
        frame = frames[capture_index]
        assert int(frame.split('_')[0]) == capture_index, f"Error on {video_path}"
        # Read PIL image
        current_image = Image.open(os.path.join(video_path, frames[capture_index]))
        images.append(current_image)
        actions.append(int(frame.split('_')[1][:1])) # first char after _

        # Skip the specified number of frames between frames to acquire
        last_index = capture_index
        capture_index += frameskip+1

    frames_count = len(images)
    #actions = [None] * frames_count
    rewards = [None] * frames_count
    dones = [None] * frames_count
    metadata = [None] * frames_count

    # Saves the acquired video in the dataset format
    acquired_video = Video()
    acquired_video.add_content(images, actions, rewards, metadata, dones)
    acquired_video.save(output_path, frames_extension)


def acquire_video(args):
    video_path, idx = args

    print(f"- Acquiring {video_path}")

    output_path = os.path.join(output_directory, f"{idx:05d}")
    acquire_sequence(video_path, output_path)


if __name__ == "__main__":

    # Creates the output directory
    Path(output_directory).mkdir(parents=True, exist_ok=True)
    
    # Samples from data
    ids = os.listdir(root_directory)

    work_items = []
    index = 0
    for identity in ids:
        video_path = os.path.join(root_directory, identity)
        num_frames = len(os.listdir(video_path))
        # Only sample frames of length at least 15
        if num_frames >= 15:
            work_items.append((video_path, index))
            print(f"{index}, {identity}")
            index += 1

    pool = mp.Pool(processes)
    pool.map(acquire_video, work_items)
    pool.close()



























