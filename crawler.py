#! /usr/bin/env python

import json
import argparse
from pprint import pprint

def getAllAddrs(data):
    all_addresses = {}
    for i in range(len(data['pages'])):
        address = data['pages'][i]['address']
        links = data['pages'][i]['links']
        all_addresses[address]= links
    return all_addresses

def getData(file_path):
    with open(file_path) as data_file:
        data = json.load(data_file)
    data_file.close()
    return data

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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-file',type=str,action='store',default='Internet/Internet_1.json',
                        help='file path')
    args = parser.parse_args()


    data=getData(args.file)
    success,skipped,error= crawl(data)

    print("\nSuccess:\n")
    print success
    print("\nSkipped:\n")
    print skipped
    print("\nError:\n")
    print error


if __name__ == '__main__':
    main()
