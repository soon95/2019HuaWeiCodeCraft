# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:56:38 2019

@author: Leon Song
"""
import pandas as pd
from queue import PriorityQueue
import collections

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
        return self.length <= other.length


         
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

# ====================================================================
class Graph:
    '''
    地图类
    成员变量：
        adj：存放于道路起点相连的所有道路，数据类型：dict(),key:起点路口编号,value：set([与起点相连的道路类集合])
    成员函数：
        dijkstra(self,origin,destination)：搜索最短路径
    '''        
    def __init__(self,roads):
        '''
        构造方法
        参数：
            roads:道路数据，数据类型：pandas.DataFrame
        '''
        self.adj=collections.defaultdict(set)
        for _,road in roads.iterrows():
            if road['isDuplex']==1:
                self.adj[road['to']].add(Road(road['length'],road['to'],road['from']))
            self.adj[road['from']].add(Road(road['length'],road['from'],road['to']))


    def dijkstra(self,origin,destination):
        '''
        搜索最短路径
        参数：
            origin:起点路口编号
            destination:目的地路口编号
        输出：
            path：最短路径，数据类型：dict()
        '''
        edge_to=dict()      #最短路径 key:to value:from
        edge_to[origin]=origin

        routes=PriorityQueue(100)       #优先队列最大容量，默认设置：100
        for road in self.adj[origin]:
            routes.put(road)
        
        visited=set()
        visited.add(origin)

        while routes:
            
            road=routes.get()       #最短的一段路径
            if road.road_to in visited:     #如果已经访问，则进入下一轮
                continue
            
            edge_to[road.road_to]=road.road_from
            if road.road_to == destination:     #达到终点
                path=dict()
                path_to=destination
                while path_to != origin:
                    path[path_to]=edge_to[path_to]
                    path_to=edge_to[path_to]
                return path
            
            for neighbor in self.adj[road.road_to]:     #将新加入节点的邻接元素加入优先队列
                if neighbor not in visited:
                    routes.put(neighbor)
            visited.add(road.road_to)

        print('访问路径不存在！')
        return dict()       #返回空
#==============================================================================        

  

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

    graph=Graph(roads)
    path=graph.dijkstra(1,2)
    print(path)