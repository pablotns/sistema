import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

class DataProcessor:
    def __init__(self):

        self.df = None
        self.df_scaled = None
        self.pca_result = None
        self.kmeans_result = None
        self.centroids = None
        self.labels = None
        self.id = None 
        self.cluster1 = None
        self.cluster2 = None
        self.cluster3 = None
        self.info = pd.read_csv("C:/Users/PC/Desktop/cleaned_data.csv")

    def read_csv(self, file_path):
        self.df = pd.read_csv(file_path)
        self.id = self.df['0']

    def get_tabla(self):
        return self.df

    
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
        return self.centroids.tolist()
    
    def get_transform (self):
        return self.pca_result.tolist()
    
    def get_cluster(self):
        #data = self.pca_result.tolist()
        data = self.df.values.tolist()
        aux = self.labels.tolist()
        tico = self.info.values.tolist()
        #tico = self.df

        cluster1=[]
        cluster2=[]
        cluster3=[]
        dato1 = []
        dato2 = []
        dato3 = []
        for n, a,i in zip(data, aux,tico):
            if a == 0:
                cluster1.append(n)
                dato1.append(i)
                #self.cluster1.append(i)
            elif a == 1:
                cluster2.append(n)
                dato2.append(i)
                #self.cluster2.append(i)
            else:
                cluster3.append(n)
                dato3.append(i)
                #self.cluster3.append(i)

        return cluster1,cluster2,cluster3,dato1,dato2,dato3
    
    


# Ejemplo de uso
if __name__ == "__main__":
    processor = DataProcessor()
    processor.read_csv("C:/Users/PC/Desktop/encoded_data.csv")
    processor.process_data()
    processor.process_kmeans()

    cluster1, cluster2, cluster3, dato1,dato2,dato3 = processor.get_cluster()

    
    print(len(dato1))
    print(len(dato2))
    print(len(dato3))
    #print(cluster2)
    #print(cluster3)

    print(len(cluster1))
    print(len(cluster2))
    print(len(cluster3))

    #print(processor.pca_result.tolist())
    #data = processor.pca_result.tolist()
    #aux = processor.labels.tolist()
    
    #print(len(data))
    #print(len(aux))
    #print(aux)
    #print(processor.get_cluster().tolist)
    #cluster1=[]
    #cluster2=[]
    #cluster3=[]

    """
    for n, a in zip(data, aux):
        if a == 0:
            cluster1.append([n, a])
        elif a == 1:
            cluster2.append([n, a])
        else:
            cluster3.append([n, a])

    
    cluster1,cluster2,cluster3 = processor.get_cluster()

    print(len(cluster1))
    print(len(cluster2))
    print(len(cluster3))
    """
    #print(cluster1)


