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
        return self.centroids.tolist()
    
            
        
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
    centroid = processor.process_kmeans()
    return centroid 


@app.route('/grafico')
def grafico():

    data = get_data()

    chart = {
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
            'symbolSize': '20',
            'data': data,
            'type': 'scatter'
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
    