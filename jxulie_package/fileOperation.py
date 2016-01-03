#-*- coding:UTF-8 -*-
'''
Created on 2016年1月3日

@author: Bo Xu <mailto:bolang1988@gmail.com>

@version: 1.0

@summary: 

'''
def merge_path2path(in_path_list, out_path):
    out_file = open(out_path, 'w', encoding = "utf-8")
    for in_path in in_path_list:
        in_file = open(in_path, 'r', encoding = "utf-8")
        out_file.write(in_file.read())
        in_file.close()
    out_file.close()

def statistic_b1s1_path2path(in_path, out_path, cols, big_position, small_position, delimiter = "t"):
    ''' b1s1 means we need to statistic 1 big item with 1 small item
        path2path means we read from file and write to file
        in_path is the input file path
        out_path is the output file path
        cols means how many cols in each line
        big position means the position of big item
        small position means the position of small item 
        t means the delimiter is \t, b means the delimiter is blank
    '''
    statistic_dict = dict()
    in_file = open(in_path, 'r', encoding = "utf-8")
    lines = in_file.readlines()
    for line in lines:
        line = line.rstrip()
        words = None
        if delimiter == "t":
            words = line.split("\t")
        elif delimiter == "b":
            words = line.split(" ")
        else:
            print("error delimiter")
            break
        small_item = words[small_position]
        big_item = words[big_position]
    
        if big_item not in statistic_dict:
            statistic_dict[big_item] = set()
        statistic_dict[big_item].add(small_item)

    out_file = open(out_path, 'w', encoding = "utf-8")
    
    for big_statistic, small_set in sorted(statistic_dict.items(), key = lambda k:len(k[1]), reverse = True):
        out_file.write(big_statistic + "\t" + str(len(small_set)) + "\n")
        
        
def statistic_b2s1_path2path(in_path, out_path, cols, big_position1, big_position2, small_position, delimiter = "t"):
    ''' b2s1 means we need to statistic 2 big item with 1 small item
        path2path means we read from file and write to file
        in_path is the input file path
        out_path is the output file path
        cols means how many cols in each line
        big position means the position of big item
        small position means the position of small item 
        t means the delimiter is \t, b means the delimiter is blank
    '''
    statistic_dict = dict()
    in_file = open(in_path, 'r', encoding = "utf-8")
    lines = in_file.readlines()
    for line in lines:
        line = line.rstrip()
        words = None
        if delimiter == "t":
            words = line.split("\t")
        elif delimiter == "b":
            words = line.split(" ")
        else:
            print("error delimiter")
            break
        small_item = words[small_position]
        big_item1 = words[big_position1]
        big_item2 = words[big_position2]
        big_item = big_item1 + "_" + big_item2
    
        if big_item not in statistic_dict:
            statistic_dict[big_item] = set()
        statistic_dict[big_item].add(small_item)

    out_file = open(out_path, 'w', encoding = "utf-8")
    
    for big_statistic, small_set in sorted(statistic_dict.items(), key = lambda k:len(k[1]), reverse = True):
        out_file.write(big_statistic + "\t" + str(len(small_set)) + "\n")