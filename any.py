import shutil
from pytube import YouTube
from pytube import exceptions
import os
import argparse
import csv
import time

parser = argparse.ArgumentParser()
parser.add_argument('--dataset_file', help='url video', default='dataset_csv/vietnam_train.csv', type=str)
parser.add_argument('--is_vn', help='if vietnam dataset',  action='store_true', default=False)
parser.add_argument('--dataset_out', help='folder contain out dataset', default='', type=str)
parser.add_argument('--log_file', help='log_file', default='', type=str)
args = parser.parse_args()

def devideArrayIntoChunks(lst, n) :
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def downloadVideos(arr):
    print(arr)

