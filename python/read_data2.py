# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 13:43:40 2018

@author: dholtsch
"""

import pandas as pd
import numpy  as np
import csv


def peak_stats(site):
    beg_pos  = data.find(site)
    print(beg_pos)
    sta_name = data[beg_pos + 10: beg_pos + 52].strip()
    print(sta_name)
    beg_pos  = beg_pos + data[beg_pos: len(data)].find('Number of peaks in record            =')
    beg_pos  = beg_pos + 38
    inc_pos  = data[beg_pos : beg_pos + 80].find('\n')
    no_peaks = int(data[beg_pos : beg_pos + inc_pos])
    print(no_peaks)
    beg_pos  = beg_pos + data[beg_pos: len(data)].find('Beginning Year                       =')
    beg_pos  = beg_pos + 38
    inc_pos  = data[beg_pos : beg_pos + 80].find('\n')
    beg_year = int(data[beg_pos : beg_pos + inc_pos])
    print(beg_year)
    beg_pos  = beg_pos + data[beg_pos: len(data)].find('Ending Year                          =')
    beg_pos  = beg_pos + 38
    inc_pos  = data[beg_pos : beg_pos + 80].find('\n')
    end_year = int(data[beg_pos : beg_pos + inc_pos])
    print(end_year)
    beg_pos  = beg_pos + data[beg_pos: len(data)].find('Type of analysis                      ')
    beg_pos  = beg_pos + 38
    inc_pos  = data[beg_pos : beg_pos + 80].find('\n')
    type_anal= data[beg_pos : beg_pos + inc_pos].strip()
    print(type_anal)
    beg_pos  = beg_pos + data[beg_pos: len(data)].find('             SYSTEMATIC RECORD  ')
    beg_pos  = beg_pos + 31
    inc_pos  = data[beg_pos : beg_pos + 80].find('\n')
    my_list  = data[beg_pos : beg_pos + inc_pos].split()
    ken_tau       = float(my_list[0])
    ken_p_value   = float(my_list[1])
    ken_med_slope = float(my_list[2])
    ken_no_peaks  = int(my_list[3])
    print(ken_tau, ken_p_value, ken_med_slope, ken_no_peaks)
    beg_pos  = beg_pos + data[beg_pos: len(data)].find('   0.1000 ')
    beg_pos  = beg_pos + 12
    inc_pos  = data[beg_pos : beg_pos + 80].find('\n')
    my_list  = data[beg_pos : beg_pos + inc_pos].split()
    q_100_est = float(my_list[0])
    q_100_l95 = float(my_list[3])
    q_100_u95 = float(my_list[4])
    print(q_100_est, q_100_l95, q_100_u95)
    beg_pos  = beg_pos + data[beg_pos: len(data)].find('   0.0200 ')
    beg_pos  = beg_pos + 12
    inc_pos  = data[beg_pos : beg_pos + 80].find('\n')
    my_list  = data[beg_pos : beg_pos + inc_pos].split()
    q_020_est = float(my_list[0])
    q_020_l95 = float(my_list[3])
    q_020_u95 = float(my_list[4])
    print(q_020_est, q_020_l95, q_020_u95)
    beg_pos  = beg_pos + data[beg_pos: len(data)].find('   0.0100 ')
    beg_pos  = beg_pos + 12
    inc_pos  = data[beg_pos : beg_pos + 80].find('\n')
    my_list  = data[beg_pos : beg_pos + inc_pos].split()
    q_010_est = float(my_list[0])
    q_010_l95 = float(my_list[3])
    q_010_u95 = float(my_list[4])
    print(q_010_est, q_010_l95, q_010_u95)
    beg_pos  = beg_pos + data[beg_pos: len(data)].find('   0.0020 ')
    beg_pos  = beg_pos + 12
    inc_pos  = data[beg_pos : beg_pos + 80].find('\n')
    my_list  = data[beg_pos : beg_pos + inc_pos].split()
    print(my_list)
    q_002_est = float(my_list[0])
    q_002_l95 = float(my_list[3])
    q_002_u95 = float(my_list[4])
    print(q_002_est, q_002_l95, q_002_u95)   
    return(site, sta_name, no_peaks, beg_year, end_year, type_anal, ken_tau, 
           ken_p_value, ken_med_slope, ken_no_peaks, 
           q_100_est, q_100_l95, q_100_u95,
           q_020_est, q_020_l95, q_020_u95, 
           q_010_est, q_010_l95, q_010_u95,
           q_002_est, q_002_l95, q_002_u95)
    

sta_list = ['04096015', '04096405', '04096515', '04097500', '04097540',
            '04099000', '04101500', '04102500', '04104945', '04105000',
            '04105500', '04106000', '04106400', '04109000', '04111000',
            '04111379', '04112000', '04112500', '04113000', '04116000',
            '04117500', '04119000']

# Open Weaverset_2017_EMA_STA_MGB.prt file
# filename = 'C:\Home\SW_Specialist\Floods\WY_2018\WeaverSet_2017_EMA_STA_MGB.prt'
# filename = 'C:\Home\SW_Specialist\Floods\WY_2018\WeaverSet_2018_EMA_STA_MGB.prt'
# filename = 'C:\Home\SW_Specialist\Floods\WY_2018\WeaverSet_2017_B17B_WGT_MGB.prt'
filename = 'C:\Home\SW_Specialist\Floods\WY_2018\WeaverSet_2018_B17B_WGT_MGB.prt'
with open(filename, 'rt') as myfile:
    data=myfile.read()



# f = open('WeaverSet_2017_EMA_STA_MGB.out', 'wt')
# f = open('WeaverSet_2018_EMA_STA_MGB.out', 'wt')
# 

# f = open('WeaverSet_2017_B17B_WGT_MGB.out', 'wt')
f = open('WeaverSet_2018_B17B_WGT_MGB.out', 'wt')

writer  = csv.writer(f, delimiter='\t')
writer.writerow( ('sta_no', 'sta_name', 'no_peaks', 'beg_year', 'end_year', 
                  'type_anal', 'ken_tau', 'ken_p_value', 'ken_med_slope', 
                  'ken_no_peaks',
                  'q_100_est', 'q_100_l95', 'q_100_u95', 'q_020_est', 
                  'q_020_l95', 'q_020_u95', 'q_010_est', 'q_010_l95', 
                  'q_010_u95', 'q_002_est', 'q_002_l95', 'q_002_u95') )
for sta in sta_list:
    t = peak_stats(sta)
    writer.writerow(t)
f.close()


    