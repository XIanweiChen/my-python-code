import heapq
G = {1:{1:0,    2:1,    3:12},
     2:{2:0,    3:9,    4:3},
     3:{3:0,    5:5},
     4:{3:4,    4:0,    5:13,   6:15},
     5:{5:0,    6:4},
     6:{6:0}}

def dijkstra(G,start):     ###dijkstra算法
    INF = 999
    dis = dict((key,INF) for key in G)    # 初始化每个点的距离
    dis[start] = 0
    ###堆优化

    dis_un = {}    #存放未访问的点的距离
    pq = []    #存放排序后的值
    for node,d in dis.items():    #构造最小堆
        entry = [d,node]
        dis_un[node] = entry
        heapq.heappush(pq,entry)
    
    print("dis_un:",dis_un)
    print(pq)

    while len(pq)>0:
        v_dis,v = heapq.heappop(pq)    #未访问点中距离最小的点和对应的距离
        for node in G[v]:    #与v直接相连的点
            new_dis = dis[v] + G[v][node]
            if new_dis < dis[node]:    #如果与v直接相连的node通过v到src的距离小于dis中对应的node的值,则用小的值替换
                dis[node] = new_dis    #更新所有点的距离
                dis_un[node][0] = new_dis    #更新未访问的点到start的距离 改变dis_un中的entry从而改变pq
                print("_____________________________") 
                print("dis_un:",dis_un)
                print(pq)

    return dis

print("结果",dijkstra(G,1))


