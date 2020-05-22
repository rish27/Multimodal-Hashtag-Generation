import argparse
import os

parser = argparse.ArgumentParser(description='Get stats for each hashtag topic')
parser.add_argument('path', type=str, help='path required topic based hashtag')
args = parser.parse_args()
path = args.path

for dir_name in os.listdir(path):
	# print(dir_name)
	if os.path.isdir(path + '/' + dir_name):
		
		dir_path = path + '/' + dir_name
		print(os.listdir(dir_path))
		print(dir_path,len([i for i in os.listdir(dir_path) if os.path.isdir(dir_path + '/' + i)]))