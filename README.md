# Incident-Detection
Installation:

	python 3.5 
	Jupyter notebook 


Main Files 
============================================================================================
1) sathon_wide_tls_20160418_edited.add(cover_wholeLane)_withLaneClose_20mins.xml 	- to create incidents in SUMO 

2) sathorn_morning(clusterDetector).py 							- to retrieve data 

3) checkAnomalyOfflineMode_Specific_withFlow.py						- to check anomaly and write file
	
	- writeFileWithAccident()
	- checkAnomaly_WhenWriteFile()
	
	

4) AnomalyDetection.ipynb								- for anomaly detection using support vector machine 


Dataset
============================================================================================
1) IncidentDetection/dataset/LaneClosure/L10130/2 s interval(including2hops)
	- 1 close			- for one-lane closure
	- 1,2 close 		- for two-lane closure
	- 1,2,3 close		- for three-lane closure



Remark
============================================================================================
Here, sumo configurations are same as with the original Chula-SSS. 



Paper
============================================================================================
http://www.wcse.org/content-11-166-1.html
