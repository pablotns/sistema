var dom = document.getElementById('chart-burbuja');
var myChart = echarts.init(dom, null, {
  renderer: 'canvas',
  useDirtyRect: false
});
var app = {};

var option;

option = {
  tooltip: {
    trigger: 'item'
  },
  legend: {
    top: '5%',
    left: 'center'
  },
  series: [
    {
      name: 'Access From',
      type: 'pie',
      radius: ['40%', '70%'],
      avoidLabelOverlap: false,
      itemStyle: {
        borderRadius: 10,
        borderColor: '#fff',
        borderWidth: 2
      },
      label: {
        show: false,
        position: 'center'
      },
      emphasis: {
        label: {
          show: true,
          fontSize: 40,
          fontWeight: 'bold'
        }
      },
      labelLine: {
        show: false
      },
      data: [
        { value: 1048, name: 'PERROS' },
        { value: 735, name: 'GATOS' },
        { value: 580, name: 'HAMSTERS' }
      ]
    }
  ]
};

// Agrega un evento de clic al gráfico
myChart.on('click', function(params) {
    // Redirige a diferentes páginas basadas en la categoría clicada
    var categoryMap = {
      'PERROS': 'categoria'
    };
  
    var categoryPage = categoryMap[params.name];
    if (categoryPage) {
      window.location.href = categoryPage;
    } else {
      alert('Página no encontrada para esta categoría.');
    }
});

if (option && typeof option === 'object') {
  myChart.setOption(option);
}

window.addEventListener('resize', myChart.resize);






