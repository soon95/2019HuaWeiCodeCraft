# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:56:38 2019

@author: Leon Song
"""
import pandas as pd
from queue import PriorityQueue
#==============================================================================
# 道路类
# =============================================================================
class Road:  
    '''
    加权有向路
    '''
    def __init__(self,length,road_from,road_to):
         self.length=length
         self.road_from=road_from
         self.road_to=road_to

    def __lt__(self,other):
        '''
        用于优先队列中排序比较
        '''
        return self.length<other.length

         
# =============================================================================
    
    
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
    
    def __init__(self,cross_id):
        self.cross_id=cross_id
#        self.road_up=road_up
#        self.road_right=road_right
#        self.road_down=road_down
#        self.road_left=road_left

class Graph:
             
    def __init__(self,roads,crosses):
        self.adj=dict()     #邻接矩阵 存放的是一个道路类集合
        self.cross_num=crosses.shape[0]
        
        for i in range(self.cross_num):
           self.adj[crosses['id'][i]]=set()
        
        for _,road in roads.iterrows():
            if road['isDuplex']==1:
                self.adj[road['to']].add(Road(road['length'],road['to'],road['from']))
            self.adj[road['from']].add(Road(road['length'],road['from'],road['to']))
        

#==============================================================================        

class Shortest_path:
    '''
    最短路径
    '''
    def __init__(self, g, car_from, car_to):

        self.edge_to=dict()     #最短路径 key:to value:from
        self.dist_to=dict()
        self.pq=PriorityQueue()     #存放道路

        self.edge_to[car_from]=car_from
        self.add_roads(g.adj[car_from])

        while car_to not in self.edge_to.keys():
            road=self.pq.get()
            self.edge_to[road.road_to]=road.road_from
            self.add_roads(g.adj[road.road_from])


    def add_roads(self,s):
        '''
        将邻接表中的路径添加到优先队列中
        '''
        for road in s:      #s 道路集合
            if road.road_to not in self.edge_to.keys():
                self.pq.put(road)




   

#==============================================================================

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
  
# ================================================================================

if __name__=='__main__':
    file_path='F:/2019HWcode/code/SDK_python/CodeCraft-2019/config'
    obj1='road'
    roads=load_data(file_path,obj1)
    
    obj2='cross'
    crosses=load_data(file_path,obj2)

    graph=Graph(roads,crosses)

    sp=Shortest_path(graph,1,5)
    print(sp.edge_to)



    




















