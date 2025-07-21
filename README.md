# 2025 ZJU Comprehensive_Course_Experiment
### Title:

  Aggregate Carbon Emissions by Sector in the World’s Major Emitting Countries in Recent Years

### Data source:

https://www.carbonmonitor.org.cn/ (Global real-time carbon data, Carbon Monitor)

### Data-processing approach:

  A Python script built with pandas is used to ingest and cleanse the large, granular dataset. The pivot function is then applied to reshape the table so that sectors become columns (or indices) and countries/years become rows (or columns), facilitating subsequent visualization.
