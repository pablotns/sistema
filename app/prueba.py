import globals

globals.processor.process_data()
globals.processor.process_kmeans()

cluster1, cluster2, cluster3, dato1,dato2,dato3,coor1,coor2,coor3 = globals.processor.get_cluster()

print(globals.processor.get_centroids())
