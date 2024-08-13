from flask import Flask, render_template,jsonify

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
            
        
app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/categoria1')
def categoria1():
    return render_template('cat1.html')

@app.route('/categoria2')
def categoria2():
    datos = {
        'titulo': 'Página de gráficos',
        'descripcion': 'Esta página muestra gráficos interactivos.',
        'grafico1': 'Gráfico de Dispersión',
        'grafico2': 'Gráfico de Torta',
        'valores': [
            {'id': 1, 'nombre': 'Item 1', 'valor': 10},
            {'id': 2, 'nombre': 'Item 2', 'valor': 20},
            {'id': 3, 'nombre': 'Item 3', 'valor': 30},
            {'id': 4, 'nombre': 'Item 4', 'valor': 40},
            {'id': 5, 'nombre': 'Item 5', 'valor': 50}
        ]
    }
    return render_template('cat2.html', datos=datos)

@app.route('/categoria3')
def categoria3():
    datos = {
        'titulo': 'Página de gráficos',
        'descripcion': 'Esta página muestra gráficos interactivos.',
        'grafico1': 'Gráfico de Dispersión',
        'grafico2': 'Gráfico de Torta',
        'valores': [
            {'id': 1, 'nombre': 'Item 1', 'valor': 10},
            {'id': 2, 'nombre': 'Item 2', 'valor': 20},
            {'id': 3, 'nombre': 'Item 3', 'valor': 30},
            {'id': 4, 'nombre': 'Item 4', 'valor': 40},
            {'id': 5, 'nombre': 'Item 5', 'valor': 50}
        ]
    }
    return render_template('cat3.html', datos=datos)

@app.route('/pruebachart')
def pruebachart():
    return render_template('charts.html')


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

@app.route('/tabla')
def tabla():
    processor = DataProcessor()
    processor.read_csv("C:/Users/PC/Desktop/encoded_data.csv")
    dataset = processor.get_tabla()
    dataset = dataset.values.tolist()
    return jsonify(dataset)

@app.route('/puntos')
def puntos():
    dataxx , cluster1,cluster2,cluster3 = get_data()

    v1 = len(cluster1)
    v2 = len(cluster2)
    v3 = len(cluster3)

    data = [
            { 'value': v1, 'name': 'CLUSTER1' },
            { 'value': v2, 'name': 'CLUSTER2' },
            { 'value': v3, 'name': 'CLUSTER3' }
        ]
    
    chart = {
        'tooltip': {
            'trigger': 'item'
        },
        'legend': {
            'top': '5%',
            'left': 'center'
        },
        'series': [
            {
            'name': 'Result',
            'type': 'pie',
            'radius': ['40%', '70%'],
            'avoidLabelOverlap': 'false',
            'padAngle': '5',
            'itemStyle': {
                'borderRadius': '10'
            },
            'data': data
            }
        ]
    }
    
    return jsonify(chart)



if __name__ == '__main__':
    app.run(debug=True,port=5000)
    