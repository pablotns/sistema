import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

class DataProcessor:
    def __init__(self):

        self.df = pd.read_csv("C:/Users/PC/Desktop/encoded_data.csv")
        self.info = pd.read_csv("C:/Users/PC/Desktop/cleaned_data.csv")
        self.df_scaled = None
        self.pca_result = None
        self.kmeans_result = None
        self.centroids = None
        self.labels = None
        self.cantCluster1 = None
        self.cantCluster2 = None
        self.cantCluster3 = None
        
        
    def process_data (self, n_components=2):
        scaler = MinMaxScaler()
        self.df_scaled = pd.DataFrame(scaler.fit_transform(self.df), columns=self.df.columns)
        pca = PCA(n_components=n_components)
        self.pca_result = pca.fit_transform(self.df_scaled)
        
    def process_kmeans(self, n_clusters=3):   
        kmeans = KMeans(n_clusters=n_clusters)
        self.kmeans_result = kmeans.fit(self.pca_result)
        self.centroids = kmeans.cluster_centers_
        self.labels = kmeans.labels_
    
    def get_cluster(self):
        coordenadas = self.pca_result.tolist()
        puntaje = self.df.values.tolist()
        etiqueta = self.labels.tolist()
        descripcion = self.info.values.tolist()
        
        coor_cluster1=[]
        coor_cluster2=[]
        coor_cluster3=[]

        cluster1=[]
        cluster2=[]
        cluster3=[]

        dato1 = []
        dato2 = []
        dato3 = []

        for n, a, i ,c in zip(puntaje, etiqueta,descripcion,coordenadas):
            if a == 0:
                cluster1.append(n)
                dato1.append(i)
                coor_cluster1.append(c)
            elif a == 1:
                cluster2.append(n)
                dato2.append(i)
                coor_cluster2.append(c)
            else:
                cluster3.append(n)
                dato3.append(i)
                coor_cluster3.append(c)

        self.cantCluster1 = len(coor_cluster1)
        self.cantCluster2 = len(coor_cluster2)
        self.cantCluster3 = len(coor_cluster3)

        return cluster1,cluster2,cluster3,dato1,dato2,dato3,coor_cluster1,coor_cluster2,coor_cluster3

    def get_tabla(self):
        return self.df

    def get_tablaDesc(self):
        return self.info
    
    def get_centroids (self):
        return self.centroids.tolist()
    
    def get_transform (self):
        return self.pca_result.tolist()
    
    def get_coordenadas(self):
        return self.cantCluster1, self.cantCluster2, self.cantCluster3


processor = DataProcessor()


# Ejemplo de uso
if __name__ == "__main__":
    processor = DataProcessor()
    processor.process_data()
    processor.process_kmeans()

    cluster1, cluster2, cluster3, dato1,dato2,dato3,coor1,coor2,coor3 = processor.get_cluster()
