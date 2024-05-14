#Source: https://stackoverflow.com/questions/61056708/python-beginner-typeerror-nonetype-object-is-not-iterable-how-to-solve-it
import os
import numpy as np
import math
import random
import re
import csv
import argparse
import sys

from lxml import etree

sys.path.append(os.getcwd())

from tools.clean_text import cleaner
from xlm.utils import bool_flag


def review_extractor(text, category='verbatim', do_lower=False):
    """
    Extract review and label
    """

    tree = etree.fromstring(bytes(text, encoding='utf-8'))
    for e in tree.findall(".//*[@fmc]"):
      label = e.xpath("./@fmc")[0]
      for c in e.findall("./part"):
        # print value of "fmc" attribute and text of child element
        print(c.text, label)
        #print(f"{label:15}{c.text}")
        return c.text, label


def get_review_labels(text, category='verbatim', do_lower=False):
    """
    Input: line
    Returns cleaned review and label
    """
    review_text, label = review_extractor(text, category=category, do_lower=do_lower)
    #review_text = cleaner(review_text, rm_new_lines=True)
    print(review_text, label)
    return review_text, label


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--indir', type=str, help='Path to raw data directory.')
    parser.add_argument('--outdir', type=str, help='Path to processed data directory.')
    parser.add_argument('--do_lower', type=bool_flag, default='False', help='True if do lower case, False otherwise.')
    parser.add_argument('--val_ratio', type=float, default=0.2, help='Ratio to split data for validation.')
    parser.add_argument('--use_hugging_face', type=bool_flag, default='False', help='Prepare data to run fine-tuning using \
                                                                                    Hugging Face Transformer library')

    args = parser.parse_args()

    indir = os.path.expanduser(args.indir)
    outdir = os.path.expanduser(args.outdir)

    category = 'verbatim'
    lang = 'fr'
    val_ratio = args.val_ratio

    train_fname = 'train.tsv' if args.use_hugging_face else 'train_0.tsv' 
    val_fname = 'dev.tsv' if args.use_hugging_face else 'valid_0.tsv' 
    test_fname = 'test.tsv' if args.use_hugging_face else 'test_0.tsv'  

    #for category in categories:
    #print('-'*20)
    path = os.path.join(indir, lang, category)
    splts = ['train', 'test']

    for s in splts:
        review_texts = []
        labels = []
        stats = []


        with open(os.path.join(path, s+'.review'), 'rt', encoding='utf-8') as f_in:
            next(f_in)
            text = f_in.read()
            print(text) # to display whole file


            review_text, label = get_review_labels(text, category=category, do_lower=args.do_lower)
            #review_text, label = review_extractor(text, category=category, do_lower=args.do_lower) 
            review_texts.append(review_text)
            labels.append(label)
            stats.append(len(review_text.split()))



        #assert len(review_texts) == len(labels) == i


        out_path = os.path.join(outdir, category)
        if not os.path.exists(out_path):
            os.makedirs(out_path)




if __name__ == "__main__":
    main()