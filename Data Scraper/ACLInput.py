# -*- coding: utf-8 -*-

import json
import instaloader
import argparse
from tqdm import tqdm as tqdm
import re
import requests
from bs4 import BeautifulSoup
import os

JSONfiles = [
'artist.json',
'artistsoninstagram.json',
'art.json',
'artoftheday.json',
'artwork.json',
'beachvibes.json',
'Citytravel.json',
'drawing.json',
'foodphotography.json',
'foodporn.json',
'foodstyling.json',
'Hiking.json',
'instapet.json',
'Luxarytravel.json',
'nature.json',
'pet.json',
'petlover.json',
'petscorner.json',
'petsofinstagram.json',
'petstagram.json',
'solotravel.json',
'tourist.json',
'Travelabout.json',
'traveladdict.json',
'Travelawesome.json',
'travelbook.json',
'travelbug.json',
'travelcaptures.json',
'Traveldeeper.json',
'travelgram.json',
'travelguide.json',
'travelislife.json',
'travel.json',
'travellersnotebook.json']

def preprocess(text):
    text = re.sub(r"(?:\@)\S+", "MENTION", text)
    text = re.sub(r"(?:\@|https?\://)\S+", "URL", text)
    text = re.sub(r'#\w+', "", text)
    text = re.sub(r'[0-9]+', "DIGIT", text)
    text = ' '.join(re.findall('[a-zA-Z ]+',text))
    return text.strip()

resp,data = None, None
path = './Relevant jsons/'
fhc = open('allcomments.txt','a+')
# fhp = open('allposts.txt','a+')
# fht = open('alltags.txt','a+')

for seq in tqdm(range(0,len(JSONfiles))):
  # if seq <= 22:
  #   continue
  # elif seq > 22:
  with open(path + JSONfiles[seq]) as f:
    data = json.load(f)

  L = instaloader.Instaloader()
  instaComments = {}

  allPosts = list(data.keys())

  for idx in tqdm(range(0, len(allPosts))):
    try: 
      post = instaloader.Post.from_shortcode(L.context, allPosts[idx])

      # if post.get_comments(): Missed this
      for eachComment in post.get_comments():
        newText = preprocess(eachComment.text)
        if len(newText.split()) > 1:
          # print(newText)
          fhc.write(newText + ' ')
      fhc.write('\n')

      # newCaption = preprocess(post.caption)
      # fhp.write(newCaption+'\n')

      # for eachTag in post.caption_hashtags:
      #   fht.write(eachTag+';')
      # fht.write('\n')

    except Exception as e:
      continue
fhc.close()
fhp.close()
fht.close()