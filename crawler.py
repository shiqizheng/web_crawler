#! /usr/bin/env python

import json
import os, os.path
from pprint import pprint
import concurrent.futures

# get all valid addresses
def getAllAddrs(data):
    all_addresses = {}
    for i in range(len(data['pages'])):
        address = data['pages'][i]['address']
        links = data['pages'][i]['links']
        all_addresses[address]= links
    return all_addresses

# read data from Internet directory
def getData(file_path):
    with open(file_path) as data_file:
        data = json.load(data_file)
    data_file.close()
    return data

# perform a dfs search
def crawl(json_data):
    data=json_data
    all_addresses = getAllAddrs(data)
    success = []
    skipped = []
    error = []

    for i in range(len(data['pages'])):
        address = data['pages'][i]['address']
        links = data['pages'][i]['links']
        if address not in success:
            success.append(str(address))
        for j in links:
            if j not in success and j in all_addresses:
                success.append(str(j))
            elif j in success and j not in skipped:
                skipped.append(str(j))
            elif j not in success and j not in skipped:
                error.append(str(j))
            else: continue
    return success,skipped,error

# worker main
def worker(file_path):


    data=getData('Internet/'+file_path) # get data
    success,skipped,error= crawl(data) # process

    # print results
    print('\n'+file_path)
    print("\nSuccess:\n")
    print success
    print("\nSkipped:\n")
    print skipped
    print("\nError:\n")
    print error


def main():
    files=[name for name in os.listdir('Internet') if name.endswith('.json')]
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(files)) as executor:
        crawl = {executor.submit(worker(f)): f for f in files}


if __name__ == '__main__':
    main()
