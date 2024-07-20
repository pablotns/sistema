
// See https://github.com/ecomfe/echarts-stat
echarts.registerTransform(ecStat.transform.clustering);

const getOptionChart = async () => {
  try{
    const response = await fetch("http://127.0.0.1:5000/grafico");
    return await response.json();
  } catch(ex){
      alert(ex);
  }
}

const initChart = async() => {
    const myChart = echarts.init(document.getElementById('chart-torta'));
    myChart.setOption(await getOptionChart());
    myChart.resize();
};

window.addEventListener('load',async()=>{
  await initChart();
});