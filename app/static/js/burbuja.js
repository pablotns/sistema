// See https://github.com/ecomfe/echarts-stat
echarts.registerTransform(ecStat.transform.clustering);

const getOptionChart2 = async () => {
  try {
    const response = await fetch("http://127.0.0.1:5000/puntos");
    return await response.json();
  } catch(ex) {
    alert(ex);
  }
}

const initChart2 = async() => {
  const myChart = echarts.init(document.getElementById('chart-burbuja'));
  myChart.setOption(await getOptionChart2());
  myChart.on('click', function(params) {
    var categoryMap = {
      'CLUSTER1': 'categoria1',
      'CLUSTER2': 'categoria2',
      'CLUSTER3': 'categoria3'
    };
  
    var categoryPage = categoryMap[params.name];
    if (categoryPage) {
      window.location.href = categoryPage;
    } else {
      alert('Página no encontrada para esta categoría.');
    }
   });
  
  myChart.resize();
};

window.addEventListener('load', async () => {
  await initChart2();
});

