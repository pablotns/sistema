from flask import Flask, render_template,jsonify

import pandas as pd
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

    def read_csv(self, file_path):
        self.df = pd.read_csv(file_path)

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
        data = self.pca_result.tolist()
        aux = self.labels.tolist()
        cluster1=[]
        cluster2=[]
        cluster3=[]
        for n, a in zip(data, aux):
            if a == 0:
                cluster1.append(n)
            elif a == 1:
                cluster2.append(n)
            else:
                cluster3.append(n)

        return cluster1,cluster2,cluster3
            
        
app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/categoria')
def categoria():
    return render_template('cat1.html')


def get_data():
    
    processor = DataProcessor()
    processor.read_csv("C:/Users/PC/Desktop/encoded_data.csv")
    processor.process_data()
    # Cambio por cluster 
    #dataset = processor.get_transform() 
    centroid = processor.process_kmeans()
    cluster1, cluster2, cluster3 = processor.get_cluster()
    return centroid, cluster1, cluster2, cluster3

@app.route('/grafico')
def grafico():

    data , cluster1,cluster2,cluster3 = get_data()

    chart = {
        'tooltip': {
            'show':'true',
            'trigger':'item',
            'formatter': ' {a}<br/>{c0}'
        },
        'xAxis':
        {
            'scale': 'true'    
        },
        'yAxis': 
        {
            'scale': 'true'
        },
        'series': [
            {
            'name': 'Cluster: 1',
            'symbolSize': '8',
            'data': cluster1,
            'type': 'scatter',
            'color': '#5470c6'
            }
            ,
            {
            'name': 'Cluster: 2',
            'symbolSize': '8',
            'data': cluster2,
            'type': 'scatter',
            'color': '#91cc75'
            }
            ,
            {
            'name': 'Cluster: 3',
            'symbolSize': '8',
            'data': cluster3,
            'type': 'scatter',
            'color': '#fac858'
            },
            {
            'name': 'Centroids',
            'type': 'effectScatter',
            'symbolSize': '12',
            'data': data,
            'color':'#ee6666'
            }
        ]
    }
    return jsonify(chart)

@app.route('/puntos')
def puntos():
    
    data = [
            { 'value': 1048, 'name': 'PERROS' },
            { 'value': 735, 'name': 'TOS' },
            { 'value': 580, 'name': 'HAMSTERS' }
        ]
    
    chart = {
        'series': [
            {
            'name': 'Access From',
            'type': 'pie',
            'radius': '50%',
            'data': data
            }
        ]
    }
    return jsonify(chart)



if __name__ == '__main__':
    app.run(debug=True,port=5000)
    