// Ensure 'essos' theme is registered before this code, e.g., via:
// <script src="path/to/echarts.js"></script>
// <script src="path/to/essos.js"></script>
var myChart = echarts.init(document.getElementById('Energy'), 'essos');

var option = {
  title: {
    text: 'Global Energy Consumption 2023',
    subtext: 'Percentage of Different Energy Sources',
    left: 'center'
  },
  tooltip: {
    trigger: 'item',
    formatter: '{a} <br/>{b} : {c} EJ ({d}%)' // Added percentage and unit
  },
  legend: {
    left: 'center',
    top: 'bottom',
    data: [
      'Fossil Fuels',
      'Renewables (excl. Hydro)',
      'Nuclear',
      'Hydro'
    ] // Removed 'Land Use Change'
  },
  toolbox: {
    show: true,
    feature: {
      mark: { show: true },
      dataView: { show: true, readOnly: false },
      restore: { show: true },
      saveAsImage: { show: true }
    }
  },
  series: [
    {
      name: 'Access From',
      type: 'pie',
      radius: ['40%', '70%'],
      avoidLabelOverlap: false,
      padAngle: 5,
      itemStyle: {
        borderRadius: 10
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
        { value: 505, name: 'Fossil Fuels' },
        { value: 50.84, name: 'Renewables (excl. Hydro)' },
        { value: 24.48, name: 'Nuclear' },
        { value: 39.68, name: 'Hydro' }
      ]
    }
  ]
};

myChart.setOption(option);