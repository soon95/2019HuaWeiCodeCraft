# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:56:38 2019

@author: Leon Song
"""
import pandas as pd


# 道路类
class Road:  
    
    def __init__(self,road_id,road_length,road_speed,road_channel,road_from,road_to):
        self.road_id=road_id
        self.road_length=road_length
        self.road_speed=road_speed
        self.road_channel=road_channel
        self.road_from=road_from
        self.road_to=road_to
    
    
# 车辆类
class Car:
    
    def __init__(self,car_id,car_start,car_end,car_speed,car_start_time):
        self.car_id=car_id
        self.car_start=car_start
        self.car_end=car_end
        self.car_speed=car_speed
        self.car_start_time=car_start_time


# 路口类
class Cross:
    
    def __init__(self,cross_id,road_up,road_right,road_down,road_left):
        self.cross_id=cross_id
        self.road_up=road_up
        self.road_right=road_right
        self.road_down=road_down
        self.road_left=road_left
        
        
 
    


def load_data(file_path,obj):
    """
    读取数据
    
    参数：
        file_name:字符串
        obj:字符串
    输出:
        data:
    
    e.g.:读取路径下车辆表信息
        file_path='F:/2019HWcode/code/SDK_python/CodeCraft-2019/config'
        obj='car'
        data=load_data(file_path,obj)
    """
    data=pd.read_csv(file_path+'/'+obj+'.txt')
    if obj is 'cross':
        data.columns=['id','up','right','down','left']
    else:
        data.columns=data.columns.str.strip('#?(?)?')
        
    data[data.columns[0]]=data[data.columns[0]].str.lstrip('(').apply(pd.to_numeric)
    data[data.columns[data.columns.size-1]]=data[data.columns[data.columns.size-1]].str.rstrip(')').apply(pd.to_numeric)
    
    return data

    


if __name__=='__main__':
    
    
    file_path='F:/2019HWcode/code/SDK_python/CodeCraft-2019/config'
    obj='cross'
    data=load_data(file_path,obj)























