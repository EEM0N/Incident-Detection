#https://stackoverflow.com/questions/45577255/plotly-plot-multiple-figures-as-subplots
import plotly
import plotly.offline as py
import plotly.graph_objs as go
import csv
import os
import pandas as pd
import plotly.io as pio


#************************************************Model******************************************************
def findUpStream(accidentLink):

    allHopList=[]
    zeroHopList=[]
    zeroHopList.append(accidentLink)
    #https://www.reddit.com/r/learnpython/comments/7qrywv/how_to_read_a_specific_cell_of_a_csv_file_in/
    names = ["Lane Name","One Hop","Two Hop","Three Hop","Four Hop"]
    dirpath = os.getcwd()
    with open(dirpath+'\\upAndDown\\up.csv', 'r', newline='') as csvDataFile:
        csvReader = csv.DictReader(csvDataFile)
        for index, row in enumerate(csvReader):
            if (row['Lane Name']==accidentLink):
                #print(index)

                oneHop=row['One Hop']
                oneHopList=oneHop.split(",")

                twoHop=row['Two Hop']
                twoHopList=twoHop.split(",")

                threeHop=row['Three Hop']
                threeHopList=threeHop.split(",")

                fourHop=row['Four Hop']
                fourHopList=fourHop.split(",")

                allHopList.append(zeroHopList)
                allHopList.append(oneHopList)
                allHopList.append(twoHopList)
                allHopList.append(threeHopList)
                allHopList.append(fourHopList)

                break

    return allHopList

def findDownStream(accidentLink):
    allHopList=[]
    zeroHopList=[]
    zeroHopList.append(accidentLink)
    #https://www.reddit.com/r/learnpython/comments/7qrywv/how_to_read_a_specific_cell_of_a_csv_file_in/
    names = ["Lane Name","One Hop","Two Hop","Three Hop","Four Hop"]
    dirpath = os.getcwd()
    with open(dirpath+'\\upAndDown\\down.csv', 'r', newline='') as csvDataFile:
        csvReader = csv.DictReader(csvDataFile)
        for index, row in enumerate(csvReader):
            if (row['Lane Name']==accidentLink):
                #print(index)

                oneHop=row['One Hop']
                oneHopList=oneHop.split(",")

                twoHop=row['Two Hop']
                twoHopList=twoHop.split(",")

                threeHop=row['Three Hop']
                threeHopList=threeHop.split(",")

                fourHop=row['Four Hop']
                fourHopList=fourHop.split(",")

                allHopList.append(zeroHopList)
                allHopList.append(oneHopList)
                allHopList.append(twoHopList)
                allHopList.append(threeHopList)
                allHopList.append(fourHopList)

                break
    return allHopList
#*************************************************************************************************************




#************************************************View********************************************************
def showMeanSpeedForUpstream(accLink,upstreamList,duration):
    dirpath = os.getcwd()
    fichier_html_graphs=open(dirpath+"/AccHappendLink/meanSpeed/"+accLink+" Upstream DashBoard.html",'w')
    fichier_html_graphs.write("<html><head></head><body style=\"margin:0\">"+"\n")
    fichier_html_graphs.write("<h3>============================================Upstream Links of "+accLink+"===========================================</h3> ")

    names1 =  ["Time","Edge ID","Edge Length","NumberOfLane","Lane Name","Jam Length","Density","Mean Speed","Mean Occupancy","Flow","Road State(basedOnJamLength)"]
    names2= ["Time","Edge ID","Edge Length","NumberOfLane","Lane Name","Jam Length","Density","Mean Speed","Mean Occupancy","Flow","Road State(basedOnJamLength)","Road State(basedOnFlow)"]

    grid=[]
    zeroHop=upstreamList[0]
    oneHop=upstreamList[1]
    twoHop=upstreamList[2]
    threeHop=upstreamList[3]
    fourHop=upstreamList[4]
    if(duration==20):
        start1=2
        end1=6
        start2=11
        end2=15
        start3=20
        end3=24
        start4=29
        end4=33
    if(duration==10):
        start1=2
        end1=4
        start2=11
        end2=13
        start3=20
        end3=22
        start4=29
        end4=31
    if(duration==15):
        start1=2
        end1=5
        start2=11
        end2=14
        start3=20
        end3=23
        start4=29
        end4=32

    #Plotting for zero plot
    #==========================================================================================
    fichier_html_graphs.write("<h3>================================================Zero Hop===============================================</h3> ")
    if len(zeroHop)!=0:
        for hop in zeroHop:
            dirpath = os.getcwd()
            withoutAccLocationPath=dirpath+'\\dataset\\NormalCase\\seed50_Correct_5min\\'+hop+'.csv'
            withAccLocationPath1=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1 close\\'+hop+'.csv'
            withAccLocationPath2=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2 close\\'+hop+'.csv'
            withAccLocationPath3=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2,3 close\\'+hop+'.csv'

            print(withAccLocationPath1)

            if os.path.isfile(withoutAccLocationPath) and os.path.isfile(withAccLocationPath1)\
                    and os.path.isfile(withAccLocationPath2) and os.path.isfile(withAccLocationPath3):


                df = pd.read_csv(withoutAccLocationPath,names=names1, header=None,skiprows=1)
                df1 = pd.read_csv(withAccLocationPath1, names=names2, header=None,skiprows=1)
                df2 = pd.read_csv(withAccLocationPath2, names=names2, header=None,skiprows=1)
                df3 = pd.read_csv(withAccLocationPath3, names=names2, header=None,skiprows=1)


                trace0 = go.Scatter(x=df['Time'], y=df['Mean Speed'], mode = 'lines',name='Normal Case',
                                     line = dict(color =  ('rgb(0, 0, 255)'),width = 2)
                                    )
                trace1 = go.Scatter(x=df1['Time'], y=df1['Mean Speed'], mode = 'lines',name='One-Lane Closure',
                                     line = dict(color =  ('rgba(16, 112, 2, 0.8)'),width = 2)
                                    )
                trace2 = go.Scatter(x=df2['Time'], y=df2['Mean Speed'], mode = 'lines',name='Two-Lane Closure',
                                     line = dict(color =  ('rgb(255, 0, 0)'),width = 2)
                                    )
                trace3 = go.Scatter(x=df3['Time'], y=df3['Mean Speed'], mode = 'lines',name='Three-Lane Closure',
                                     line = dict(color =  ('rgba(80, 26, 80, 0.8)'),width = 2)
                                    )
                data = [trace0,trace1,trace2,trace3]

                if (0 <= df2['Mean Speed'].astype(float).max() <= 4):
                    max_range = 4
                elif (4 <= df2['Mean Speed'].astype(float).max() <= 10):
                    max_range = 10
                elif (df2['Mean Speed'].astype(float).max() >= 10):
                    max_range = 12

                # Edit the layout
                layout = go.Layout(title = '<b>Edge '+hop+'</b>',
                              titlefont=dict(
                                family='Courier New, monospace',
                                size=22,
                                color='#000000'
                                ),
                              legend=dict(traceorder='normal',font=dict(family='sans-serif',size=22,color='#000')),
                              xaxis = dict(title = 'Time (min)',tickangle=-45,color='#000000',
                                           tickfont=dict(family='sans-serif',size=19,color='#000'), tickmode = 'linear',dtick = 2),
                              yaxis = dict(title = 'Mean Speed (m/min)',color='#000000',range=[0,max_range],dtick = 2,
                                            tickfont=dict(family='sans-serif',size=19,color='#000'),
                                           ),
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)',
                                shapes= [
                                    # highlight first accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start1],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end1],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight second accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start2],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end2],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight third accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start3],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end3],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight fourth accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start4],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end4],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    }
                                ]
                              )
                fig = go.Figure(data=data, layout=layout)

                plotly.offline.plot(fig, filename=dirpath+'/AccHappendLink/meanSpeed/'+hop+'.html',auto_open=False)

                # Save image
                pio.write_image(fig, dirpath+'\\AccHappendLink\\meanSpeed\\images\\'+hop+'.png',width=1800, height=700)
                fichier_html_graphs.write("  <object data=\""+hop+'.html'+"\" width=\"1800\" height=\"400\" style=\"margin: 0px 0px\"></object>")

            else:
                print('Zero Hop: '+hop+'File Not Found')
                fichier_html_graphs.write("  <object data='AccHappendLink/meanSpeed/FileNotFound.html' width=\"750\" height=\"400\">"+hop+"File Not Found</object>")
    #==========================================================================================



    #Plotting for one hop
    #==========================================================================================

    fichier_html_graphs.write("<h3>================================================One Hop===============================================</h3> ")
    if len(oneHop)!=0:
        for hop in oneHop:
            dirpath = os.getcwd()
            withoutAccLocationPath=dirpath+'\\dataset\\NormalCase\\seed50_Correct_5min\\'+hop+'.csv'
            withAccLocationPath1=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1 close\\'+hop+'.csv'
            withAccLocationPath2=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2 close\\'+hop+'.csv'
            withAccLocationPath3=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2,3 close\\'+hop+'.csv'



            if os.path.isfile(withoutAccLocationPath) and os.path.isfile(withAccLocationPath1)\
                    and os.path.isfile(withAccLocationPath2) and os.path.isfile(withAccLocationPath3):


                df = pd.read_csv(withoutAccLocationPath,names=names1, header=None,skiprows=1)
                df1 = pd.read_csv(withAccLocationPath1, names=names2, header=None,skiprows=1)
                df2 = pd.read_csv(withAccLocationPath2, names=names2, header=None,skiprows=1)
                df3 = pd.read_csv(withAccLocationPath3, names=names2, header=None,skiprows=1)


                trace0 = go.Scatter(x=df['Time'], y=df['Mean Speed'], mode = 'lines',name='Normal Case',
                                     line = dict(color =  ('rgb(0, 0, 255)'),width = 2)
                                    )
                trace1 = go.Scatter(x=df1['Time'], y=df1['Mean Speed'], mode = 'lines',name='One-Lane Closure',
                                     line = dict(color =  ('rgba(16, 112, 2, 0.8)'),width = 2)
                                    )
                trace2 = go.Scatter(x=df2['Time'], y=df2['Mean Speed'], mode = 'lines',name='Two-Lane Closure',
                                     line = dict(color =  ('rgb(255, 0, 0)'),width = 2)
                                    )
                trace3 = go.Scatter(x=df3['Time'], y=df3['Mean Speed'], mode = 'lines',name='Three-Lane Closure',
                                     line = dict(color =  ('rgba(80, 26, 80, 0.8)'),width = 2)
                                    )
                data = [trace0,trace1,trace2,trace3]
                if (0 <= df2['Mean Speed'].astype(float).max() <= 4):
                    max_range = 4
                elif (4 <= df2['Mean Speed'].astype(float).max() <= 10):
                    max_range = 10
                elif (df2['Mean Speed'].astype(float).max() >= 10):
                    max_range = 12

                # Edit the layout
                layout = go.Layout(title = '<b>Edge '+hop+'</b>',
                              titlefont=dict(
                                family='Courier New, monospace',
                                  size=22,
                                color='#000000'
                                ),
                              legend=dict(traceorder='normal',
                                               font=dict(family='sans-serif', size=22, color='#000')),
                              xaxis = dict(title = 'Time (min)',tickangle=-45,color='#000000',
                                           tickfont=dict(family='sans-serif',size=19,color='#000'),tickmode = 'linear',dtick = 2),
                              yaxis = dict(title = 'Mean Speed (m/min)',color='#000000',range=[0,max_range],dtick = 2,
                                           tickfont=dict(family='sans-serif',size=19,color='#000')),
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)',
                                   shapes= [
                                    # highlight first accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start1],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end1],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight second accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start2],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end2],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight third accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start3],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end3],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight fourth accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start4],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end4],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    }
                                ]
                              )
                fig = go.Figure(data=data, layout=layout)
                pio.write_image(fig, dirpath+'\\AccHappendLink\\meanSpeed\\images\\'+hop+'.png',width=1800, height=700)
                plotly.offline.plot(fig, filename=dirpath+'/AccHappendLink/meanSpeed/'+hop+'.html',auto_open=False)
                fichier_html_graphs.write("  <object data=\""+hop+'.html'+"\" width=\"1800\" height=\"400\" style=\"margin: 0px 0px\"></object>")

            else:
                print('One Hop: '+hop+'File Not Found')
                fichier_html_graphs.write("  <object data='AccHappendLink/meanSpeed/FileNotFound.html' width=\"750\" height=\"400\">"+hop+"File Not Found</object>")
    #==========================================================================================




    #Plotting for two hop
    #==========================================================================================

    fichier_html_graphs.write("<h3>================================================Two Hop===============================================</h3> ")
    if len(twoHop)!=0:
        twoHopPlot=[]
        for hop in twoHop:

            dirpath = os.getcwd()
            withoutAccLocationPath=dirpath+'\\dataset\\NormalCase\\seed50_Correct_5min\\'+hop+'.csv'
            withAccLocationPath1=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1 close\\'+hop+'.csv'
            withAccLocationPath2=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2 close\\'+hop+'.csv'
            withAccLocationPath3=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2,3 close\\'+hop+'.csv'



            if os.path.isfile(withoutAccLocationPath) and os.path.isfile(withAccLocationPath1)\
                    and os.path.isfile(withAccLocationPath2) and os.path.isfile(withAccLocationPath3):


                df = pd.read_csv(withoutAccLocationPath,names=names1, header=None,skiprows=1)
                df1 = pd.read_csv(withAccLocationPath1, names=names2, header=None,skiprows=1)
                df2 = pd.read_csv(withAccLocationPath2, names=names2, header=None,skiprows=1)
                df3 = pd.read_csv(withAccLocationPath3, names=names2, header=None,skiprows=1)


                trace0 = go.Scatter(x=df['Time'], y=df['Mean Speed'], mode = 'lines',name='Normal Case',
                                     line = dict(color =  ('rgb(0, 0, 255)'),width = 2)
                                    )
                trace1 = go.Scatter(x=df1['Time'], y=df1['Mean Speed'], mode = 'lines',name='One-Lane Closure',
                                     line = dict(color =  ('rgba(16, 112, 2, 0.8)'),width = 2)
                                    )
                trace2 = go.Scatter(x=df2['Time'], y=df2['Mean Speed'], mode = 'lines',name='Two-Lane Closure',
                                     line = dict(color =  ('rgb(255, 0, 0)'),width = 2)
                                    )
                trace3 = go.Scatter(x=df3['Time'], y=df3['Mean Speed'], mode = 'lines',name='Three-Lane Closure',
                                     line = dict(color =  ('rgba(80, 26, 80, 0.8)'),width = 2)
                                    )
                data = [trace0,trace1,trace2,trace3]
                if (0 <= df2['Mean Speed'].astype(float).max() <= 4):
                    max_range = 4
                elif (4 <= df2['Mean Speed'].astype(float).max() <= 10):
                    max_range = 10
                elif (df2['Mean Speed'].astype(float).max() >= 10):
                    max_range = 12

                # Edit the layout
                layout = go.Layout(title = '<b>Edge '+hop+'</b>',
                              titlefont=dict(
                                family='Courier New, monospace',
                                  size=22,
                                color='#000000'
                                ),
                              legend=dict(traceorder='normal',
                                               font=dict(family='sans-serif', size=22, color='#000')),
                              xaxis = dict(title = 'Time (min)',tickangle=-45,color='#000000',
                                           tickfont=dict(family='sans-serif',size=19,color='#000'),tickmode = 'linear',dtick = 2),
                              yaxis = dict(title = 'Mean Speed (m/min)',color='#000000',range=[0,max_range],dtick = 2,
                                           tickfont=dict(family='sans-serif',size=19,color='#000')),
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)',
                                   shapes= [
                                    # highlight first accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start1],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end1],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight second accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start2],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end2],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight third accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start3],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end3],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight fourth accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start4],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end4],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    }
                                ]
                              )
                fig = go.Figure(data=data, layout=layout)
                pio.write_image(fig, dirpath+'\\AccHappendLink\\meanSpeed\\images\\'+hop+'.png',width=1800, height=700)
                plotly.offline.plot(fig, filename=dirpath+'/AccHappendLink/meanSpeed/'+hop+'.html',auto_open=False)
                fichier_html_graphs.write("  <object data=\""+hop+'.html'+"\" width=\"1800\" height=\"400\" style=\"margin: 0px 0px\"></object>")

            else:
                print('Two Hop: '+hop+'File Not Found')
                fichier_html_graphs.write("  <object data='AccHappendLink/meanSpeed/FileNotFound.html' width=\"750\" height=\"400\">"+hop+"File Not Found</object>")
    #==========================================================================================


    #Plotting for three hop
    #==========================================================================================

    fichier_html_graphs.write("<h3>================================================Three Hop===============================================</h3> ")
    if len(threeHop)!=0:
        threeHopPlot=[]

        for hop in threeHop:
            dirpath = os.getcwd()
            withoutAccLocationPath=dirpath+'\\dataset\\NormalCase\\seed50_Correct_5min\\'+hop+'.csv'
            withAccLocationPath1=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1 close\\'+hop+'.csv'
            withAccLocationPath2=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2 close\\'+hop+'.csv'
            withAccLocationPath3=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2,3 close\\'+hop+'.csv'



            if os.path.isfile(withoutAccLocationPath) and os.path.isfile(withAccLocationPath1)\
                    and os.path.isfile(withAccLocationPath2) and os.path.isfile(withAccLocationPath3):


                df = pd.read_csv(withoutAccLocationPath,names=names1, header=None,skiprows=1)
                df1 = pd.read_csv(withAccLocationPath1, names=names2, header=None,skiprows=1)
                df2 = pd.read_csv(withAccLocationPath2, names=names2, header=None,skiprows=1)
                df3 = pd.read_csv(withAccLocationPath3, names=names2, header=None,skiprows=1)


                trace0 = go.Scatter(x=df['Time'], y=df['Mean Speed'], mode = 'lines',name='Normal Case',
                                     line = dict(color =  ('rgb(0, 0, 255)'),width = 2)
                                    )
                trace1 = go.Scatter(x=df1['Time'], y=df1['Mean Speed'], mode = 'lines',name='One-Lane Closure',
                                     line = dict(color =  ('rgba(16, 112, 2, 0.8)'),width = 2)
                                    )
                trace2 = go.Scatter(x=df2['Time'], y=df2['Mean Speed'], mode = 'lines',name='Two-Lane Closure',
                                     line = dict(color =  ('rgb(255, 0, 0)'),width = 2)
                                    )
                trace3 = go.Scatter(x=df3['Time'], y=df3['Mean Speed'], mode = 'lines',name='Three-Lane Closure',
                                     line = dict(color =  ('rgba(80, 26, 80, 0.8)'),width = 2)
                                    )
                data = [trace0,trace1,trace2,trace3]
                if (0 <= df2['Mean Speed'].astype(float).max() <= 4):
                    max_range = 4
                elif (4 <= df2['Mean Speed'].astype(float).max() <= 10):
                    max_range = 10
                elif (df2['Mean Speed'].astype(float).max() >= 10):
                    max_range = 12
                # Edit the layout
                layout = go.Layout(title = '<b>Edge '+hop+'</b>',
                              titlefont=dict(
                                family='Courier New, monospace',
                                size=22,
                                color='#000000'
                                ),
                              legend=dict(traceorder='normal',
                                               font=dict(family='sans-serif', size=22, color='#000')),
                              xaxis = dict(title = 'Time (min)',tickangle=-45,color='#000000',
                                           tickfont=dict(family='sans-serif',size=19,color='#000'),tickmode = 'linear',dtick = 2),
                              yaxis = dict(title = 'Mean Speed (m/min)',color='#000000',range=[0,max_range],dtick = 2,
                                           tickfont=dict(family='sans-serif',size=19,color='#000')),
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)',
                                   shapes= [
                                    # highlight first accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start1],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end1],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight second accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start2],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end2],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight third accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start3],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end3],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight fourth accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start4],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end4],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    }
                                ]
                              )
                fig = go.Figure(data=data, layout=layout)
                pio.write_image(fig, dirpath+'\\AccHappendLink\\meanSpeed\\images\\'+hop+'.png',width=1800, height=700)
                plotly.offline.plot(fig, filename=dirpath+'/AccHappendLink/meanSpeed/'+hop+'.html',auto_open=False)
                fichier_html_graphs.write("  <object data=\""+hop+'.html'+"\" width=\"1800\" height=\"400\" style=\"margin: 0px 0px\"></object>")
            else:
                print('Three Hop: '+hop+'File Not Found')
                fichier_html_graphs.write("  <object data='AccHappendLink/meanSpeed/FileNotFound.html' width=\"750\" height=\"400\">"+hop+"File Not Found</object>")
    #==========================================================================================



    #Plotting for four hop
    #==========================================================================================

    fichier_html_graphs.write("<h3>================================================Four Hop===============================================</h3> ")
    if len(fourHop)!=0:
        fourHopPlot=[]
        for hop in fourHop:
            dirpath = os.getcwd()
            withoutAccLocationPath=dirpath+'\\dataset\\NormalCase\\seed50_Correct_5min\\'+hop+'.csv'
            withAccLocationPath1=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1 close\\'+hop+'.csv'
            withAccLocationPath2=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2 close\\'+hop+'.csv'
            withAccLocationPath3=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2,3 close\\'+hop+'.csv'



            if os.path.isfile(withoutAccLocationPath) and os.path.isfile(withAccLocationPath1)\
                    and os.path.isfile(withAccLocationPath2) and os.path.isfile(withAccLocationPath3):


                df = pd.read_csv(withoutAccLocationPath,names=names1, header=None,skiprows=1)
                df1 = pd.read_csv(withAccLocationPath1, names=names2, header=None,skiprows=1)
                df2 = pd.read_csv(withAccLocationPath2, names=names2, header=None,skiprows=1)
                df3 = pd.read_csv(withAccLocationPath3, names=names2, header=None,skiprows=1)


                trace0 = go.Scatter(x=df['Time'], y=df['Mean Speed'], mode = 'lines',name='Normal Case',
                                     line = dict(color =  ('rgb(0, 0, 255)'),width = 2)
                                    )
                trace1 = go.Scatter(x=df1['Time'], y=df1['Mean Speed'], mode = 'lines',name='One-Lane Closure',
                                     line = dict(color =  ('rgba(16, 112, 2, 0.8)'),width = 2)
                                    )
                trace2 = go.Scatter(x=df2['Time'], y=df2['Mean Speed'], mode = 'lines',name='Two-Lane Closure',
                                     line = dict(color =  ('rgb(255, 0, 0)'),width = 2)
                                    )
                trace3 = go.Scatter(x=df3['Time'], y=df3['Mean Speed'], mode = 'lines',name='Three-Lane Closure',
                                     line = dict(color =  ('rgba(80, 26, 80, 0.8)'),width = 2)
                                    )
                data = [trace0,trace1,trace2,trace3]
                if (0 <= df2['Mean Speed'].astype(float).max() <= 4):
                    max_range = 4
                elif (4 <= df2['Mean Speed'].astype(float).max() <= 10):
                    max_range = 10
                elif (df2['Mean Speed'].astype(float).max() >= 10):
                    max_range = 12
                # Edit the layout
                layout = go.Layout(title = '<b>Edge '+hop+'</b>',
                              titlefont=dict(
                                family='Courier New, monospace',
                                size=22,
                                color='#000000'
                                ),
                              legend=dict(traceorder='normal',
                                               font=dict(family='sans-serif', size=22, color='#000')),
                              xaxis = dict(title = 'Time (min)',tickangle=-45,color='#000000',
                                           tickfont=dict(family='sans-serif',size=19,color='#000'),tickmode = 'linear',dtick = 2),
                              yaxis = dict(title = 'Mean Speed (m/min)',color='#000000',range=[0,max_range],dtick = 2,
                                           tickfont=dict(family='sans-serif',size=19,color='#000')),
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)',
                                   shapes= [
                                    # highlight first accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start1],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end1],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight second accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start2],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end2],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight third accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start3],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end3],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight fourth accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start4],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end4],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    }
                                ]
                              )
                fig = go.Figure(data=data, layout=layout)
                pio.write_image(fig, dirpath+'\\AccHappendLink\\meanSpeed\\images\\'+hop+'.png',width=1800, height=700)
                plotly.offline.plot(fig, filename=dirpath+'/AccHappendLink/meanSpeed/'+hop+'.html',auto_open=False)
                fichier_html_graphs.write("  <object data=\""+hop+'.html'+"\" width=\"1800\" height=\"400\" style=\"margin: 0px 0px\"></object>")
            else:
                print('Four Hop: '+hop+'File Not Found')
                fichier_html_graphs.write("  <object data='AccHappendLink/meanSpeed/FileNotFound.html' width=\"750\" height=\"400\">"+hop+"File Not Found</object>")
    #==========================================================================================


    fichier_html_graphs.write("</body></html>")
    print("CHECK YOUR DASHBOARD.html In the current directory")





def showMeanSpeedForDownstream(accLink,downstreamList,duration):
    dirpath = os.getcwd()
    fichier_html_graphs=open(dirpath+"/AccHappendLink/meanSpeed/"+accLink+" Downstream DashBoard.html",'w')
    fichier_html_graphs.write("<html><head></head><body style=\"margin:0 auto\">"+"\n")
    fichier_html_graphs.write("<h3>============================================Downstream Links of "+accLink+"===========================================</h3> ")
    names1 =  ["Time","Edge ID","Edge Length","NumberOfLane","Lane Name","Jam Length","Density","Mean Speed","Mean Occupancy","Flow","Road State(basedOnJamLength)"]
    names2= ["Time","Edge ID","Edge Length","NumberOfLane","Lane Name","Jam Length","Density","Mean Speed","Mean Occupancy","Flow","Road State(basedOnJamLength)","Road State(basedOnFlow)"]
    grid=[]
    zeroHop=downstreamList[0]
    oneHop=downstreamList[1]
    twoHop=downstreamList[2]
    threeHop=downstreamList[3]
    fourHop=downstreamList[4]
    if (duration == 20):
        start1 = 2
        end1 = 6
        start2 = 11
        end2 = 15
        start3 = 20
        end3 = 24
        start4 = 29
        end4 = 33
    if (duration == 10):
        start1 = 2
        end1 = 4
        start2 = 11
        end2 = 13
        start3 = 20
        end3 = 22
        start4 = 29
        end4 = 31
    if (duration == 15):
        start1 = 2
        end1 = 5
        start2 = 11
        end2 = 14
        start3 = 20
        end3 = 23
        start4 = 29
        end4 = 32
    #Plotting for zero plot
    #==========================================================================================

    fichier_html_graphs.write("<h3>================================================Zero Hop===============================================</h3> ")
    if len(zeroHop)!=0:
        for hop in zeroHop:


            withoutAccLocationPath=dirpath+'\\dataset\\NormalCase\\seed50_Correct_5min\\'+hop+'.csv'
            withAccLocationPath1=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1 close\\'+hop+'.csv'
            withAccLocationPath2=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2 close\\'+hop+'.csv'
            withAccLocationPath3=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2,3 close\\'+hop+'.csv'



            if os.path.isfile(withoutAccLocationPath) and os.path.isfile(withAccLocationPath1)\
                    and os.path.isfile(withAccLocationPath2) and os.path.isfile(withAccLocationPath3):


                df = pd.read_csv(withoutAccLocationPath,names=names1, header=None,skiprows=1)
                df1 = pd.read_csv(withAccLocationPath1, names=names2, header=None,skiprows=1)
                df2 = pd.read_csv(withAccLocationPath2, names=names2, header=None,skiprows=1)
                df3 = pd.read_csv(withAccLocationPath3, names=names2, header=None,skiprows=1)


                trace0 = go.Scatter(x=df['Time'], y=df['Mean Speed'], mode = 'lines',name='Normal Case',
                                     line = dict(color =  ('rgb(0, 0, 255)'),width = 2)
                                    )
                trace1 = go.Scatter(x=df1['Time'], y=df1['Mean Speed'], mode = 'lines',name='One-Lane Closure',
                                     line = dict(color =  ('rgba(16, 112, 2, 0.8)'),width = 2)
                                    )
                trace2 = go.Scatter(x=df2['Time'], y=df2['Mean Speed'], mode = 'lines',name='Two-Lane Closure',
                                     line = dict(color =  ('rgb(255, 0, 0)'),width = 2)
                                    )
                trace3 = go.Scatter(x=df3['Time'], y=df3['Mean Speed'], mode = 'lines',name='Three-Lane Closure',
                                     line = dict(color =  ('rgba(80, 26, 80, 0.8)'),width = 2)
                                    )
                data = [trace0,trace1,trace2,trace3]
                if (0 <= df2['Mean Speed'].astype(float).max() <= 4):
                    max_range = 4
                elif (4 <= df2['Mean Speed'].astype(float).max() <= 10):
                    max_range = 10
                elif (df2['Mean Speed'].astype(float).max() >= 10):
                    max_range = 12
                # Edit the layout
                layout = go.Layout(title = '<b>Edge '+hop+'</b>',
                              titlefont=dict(
                                family='Courier New, monospace',
                                size=22,
                                color='#000000'
                                ),
                              legend=dict(traceorder='normal',
                                               font=dict(family='sans-serif', size=22, color='#000')),
                              xaxis = dict(title = 'Time (min)',tickangle=-45,color='#000000',
                                           tickfont=dict(family='sans-serif',size=19,color='#000'),tickmode = 'linear',dtick = 2),
                              yaxis = dict(title = 'Mean Speed (m/min)',color='#000000',range=[0,max_range],tickmode = 'linear',dtick = 2,
                                           tickfont=dict(family='sans-serif',size=19,color='#000')),
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)',
                                   shapes= [
                                    # highlight first accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start1],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end1],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight second accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start2],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end2],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight third accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start3],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end3],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight fourth accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start4],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end4],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    }
                                ]
                              )
                fig = go.Figure(data=data, layout=layout)
                pio.write_image(fig, dirpath+'\\AccHappendLink\\meanSpeed\\images\\'+hop+'.png',width=1800, height=700)
                plotly.offline.plot(fig, filename=dirpath+'/AccHappendLink/meanSpeed/'+hop+'.html',auto_open=False)
                fichier_html_graphs.write("  <object data=\""+hop+'.html'+"\" width=\"1800\" height=\"400\" style=\"margin: 0px 0px\"></object>")

            else:
                print('Zero Hop: '+hop+'File Not Found')
                fichier_html_graphs.write("  <object data='AccHappendLink/meanSpeed/FileNotFound.html' width=\"750\" height=\"400\">"+hop+"File Not Found</object>")
    #==========================================================================================



    #Plotting for one plot
    #==========================================================================================

    fichier_html_graphs.write("<h3>================================================One Hop===============================================</h3> ")
    if len(oneHop)!=0:
        for hop in oneHop:

            dirpath = os.getcwd()
            withoutAccLocationPath=dirpath+'\\dataset\\NormalCase\\seed50_Correct_5min\\'+hop+'.csv'
            withAccLocationPath1=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1 close\\'+hop+'.csv'
            withAccLocationPath2=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2 close\\'+hop+'.csv'
            withAccLocationPath3=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2,3 close\\'+hop+'.csv'



            if os.path.isfile(withoutAccLocationPath) and os.path.isfile(withAccLocationPath1)\
                    and os.path.isfile(withAccLocationPath2) and os.path.isfile(withAccLocationPath3):


                df = pd.read_csv(withoutAccLocationPath,names=names1, header=None,skiprows=1)
                df1 = pd.read_csv(withAccLocationPath1, names=names2, header=None,skiprows=1)
                df2 = pd.read_csv(withAccLocationPath2, names=names2, header=None,skiprows=1)
                df3 = pd.read_csv(withAccLocationPath3, names=names2, header=None,skiprows=1)


                trace0 = go.Scatter(x=df['Time'], y=df['Mean Speed'], mode = 'lines',name='Normal Case',
                                     line = dict(color =  ('rgb(0, 0, 255)'),width = 2)
                                    )
                trace1 = go.Scatter(x=df1['Time'], y=df1['Mean Speed'], mode = 'lines',name='One-Lane Closure',
                                     line = dict(color =  ('rgba(16, 112, 2, 0.8)'),width = 2)
                                    )
                trace2 = go.Scatter(x=df2['Time'], y=df2['Mean Speed'], mode = 'lines',name='Two-Lane Closure',
                                     line = dict(color =  ('rgb(255, 0, 0)'),width = 2)
                                    )
                trace3 = go.Scatter(x=df3['Time'], y=df3['Mean Speed'], mode = 'lines',name='Three-Lane Closure',
                                     line = dict(color =  ('rgba(80, 26, 80, 0.8)'),width = 2)
                                    )
                data = [trace0,trace1,trace2,trace3]
                if (0 <= df2['Mean Speed'].astype(float).max() <= 4):
                    max_range = 4
                elif (4 <= df2['Mean Speed'].astype(float).max() <= 10):
                    max_range = 10
                elif (df2['Mean Speed'].astype(float).max() >= 10):
                    max_range = 12
                if hop=='L10189':
                    max_range=6
                # Edit the layout
                layout = go.Layout(title = '<b>Edge '+hop+'</b>',
                              titlefont=dict(
                                family='Courier New, monospace',
                                size=22,
                                color='#000000'
                                ),
                              legend=dict(traceorder='normal',
                                               font=dict(family='sans-serif', size=22, color='#000')),
                              xaxis = dict(title = 'Time (min)',tickangle=-45,color='#000000',
                                           tickfont=dict(family='sans-serif',size=19,color='#000'),tickmode = 'linear',dtick = 2),
                              yaxis = dict(title = 'Mean Speed (m/min)',color='#000000',range=[0,max_range],dtick = 2,
                                           tickfont=dict(family='sans-serif',size=19,color='#000')),
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)',
                                   shapes= [
                                    # highlight first accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start1],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end1],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight second accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start2],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end2],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight third accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start3],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end3],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight fourth accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start4],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end4],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    }
                                ]
                              )
                fig = go.Figure(data=data, layout=layout)
                pio.write_image(fig, dirpath+'\\AccHappendLink\\meanSpeed\\images\\'+hop+'.png',width=1800, height=700)
                plotly.offline.plot(fig, filename=dirpath+'/AccHappendLink/meanSpeed/'+hop+'.html',auto_open=False)
                fichier_html_graphs.write("  <object data=\""+hop+'.html'+"\" width=\"1800\" height=\"400\" style=\"margin: 0px 0px\"></object>")

            else:
                print('One Hop: '+hop+'File Not Found')
                fichier_html_graphs.write("  <object data='AccHappendLink/meanSpeed/FileNotFound.html' width=\"750\" height=\"400\">"+hop+"File Not Found</object>")
    #==========================================================================================




    #Plotting for two plot
    #==========================================================================================

    fichier_html_graphs.write("<h3>================================================Two Hop===============================================</h3> ")
    if len(twoHop)!=0:
        twoHopPlot=[]
        for hop in twoHop:

            dirpath = os.getcwd()
            withoutAccLocationPath=dirpath+'\\dataset\\NormalCase\\seed50_Correct_5min\\'+hop+'.csv'
            withAccLocationPath1=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1 close\\'+hop+'.csv'
            withAccLocationPath2=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2 close\\'+hop+'.csv'
            withAccLocationPath3=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2,3 close\\'+hop+'.csv'



            if os.path.isfile(withoutAccLocationPath) and os.path.isfile(withAccLocationPath1)\
                    and os.path.isfile(withAccLocationPath2) and os.path.isfile(withAccLocationPath3):


                df = pd.read_csv(withoutAccLocationPath,names=names1, header=None,skiprows=1)
                df1 = pd.read_csv(withAccLocationPath1, names=names2, header=None,skiprows=1)
                df2 = pd.read_csv(withAccLocationPath2, names=names2, header=None,skiprows=1)
                df3 = pd.read_csv(withAccLocationPath3, names=names2, header=None,skiprows=1)


                trace0 = go.Scatter(x=df['Time'], y=df['Mean Speed'], mode = 'lines',name='Normal Case',
                                     line = dict(color =  ('rgb(0, 0, 255)'),width = 2)
                                    )
                trace1 = go.Scatter(x=df1['Time'], y=df1['Mean Speed'], mode = 'lines',name='One-Lane Closure',
                                     line = dict(color =  ('rgba(16, 112, 2, 0.8)'),width = 2)
                                    )
                trace2 = go.Scatter(x=df2['Time'], y=df2['Mean Speed'], mode = 'lines',name='Two-Lane Closure',
                                     line = dict(color =  ('rgb(255, 0, 0)'),width = 2)
                                    )
                trace3 = go.Scatter(x=df3['Time'], y=df3['Mean Speed'], mode = 'lines',name='Three-Lane Closure',
                                     line = dict(color =  ('rgba(80, 26, 80, 0.8)'),width = 2)
                                    )
                data = [trace0,trace1,trace2,trace3]
                if (0 <= df2['Mean Speed'].astype(float).max() <= 4):
                    max_range = 4
                elif (4 <= df2['Mean Speed'].astype(float).max() <= 10):
                    max_range = 10
                elif (df2['Mean Speed'].astype(float).max() >= 10):
                    max_range = 12
                # Edit the layout
                layout = go.Layout(title = '<b>Edge '+hop+'</b>',
                              titlefont=dict(
                                family='Courier New, monospace',
                                size=22,
                                color='#000000'
                                ),
                              legend=dict(traceorder='normal',
                                               font=dict(family='sans-serif', size=22, color='#000')),
                              xaxis = dict(title = 'Time (min)',tickangle=-45,color='#000000',
                                           tickfont=dict(family='sans-serif',size=19,color='#000'),tickmode = 'linear',dtick = 2),
                              yaxis = dict(title = 'Mean Speed (m/min)',color='#000000',range=[0,max_range],dtick = 2,
                                           tickfont=dict(family='sans-serif',size=19,color='#000')),
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)',
                                   shapes= [
                                    # highlight first accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start1],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end1],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight second accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start2],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end2],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight third accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start3],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end3],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight fourth accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start4],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end4],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    }
                                ]
                              )
                fig = go.Figure(data=data, layout=layout)
                pio.write_image(fig, dirpath+'\\AccHappendLink\\meanSpeed\\images\\'+hop+'.png',width=1800, height=700)
                plotly.offline.plot(fig, filename=dirpath+'/AccHappendLink/meanSpeed/'+hop+'.html',auto_open=False)
                fichier_html_graphs.write("  <object data=\""+hop+'.html'+"\" width=\"1800\" height=\"400\" style=\"margin: 0px 0px\"></object>")

            else:
                print('Two Hop: '+hop+'File Not Found')
                fichier_html_graphs.write("  <object data='AccHappendLink/meanSpeed/FileNotFound.html' width=\"750\" height=\"400\">"+hop+"File Not Found</object>")
    #==========================================================================================


    #Plotting for three plot
    #==========================================================================================

    fichier_html_graphs.write("<h3>================================================Three Hop===============================================</h3> ")
    if len(threeHop)!=0:
        threeHopPlot=[]
        for hop in threeHop:

            dirpath = os.getcwd()
            withoutAccLocationPath=dirpath+'\\dataset\\NormalCase\\seed50_Correct_5min\\'+hop+'.csv'
            withAccLocationPath1=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1 close\\'+hop+'.csv'
            withAccLocationPath2=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2 close\\'+hop+'.csv'
            withAccLocationPath3=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2,3 close\\'+hop+'.csv'



            if os.path.isfile(withoutAccLocationPath) and os.path.isfile(withAccLocationPath1)\
                    and os.path.isfile(withAccLocationPath2) and os.path.isfile(withAccLocationPath3):


                df = pd.read_csv(withoutAccLocationPath,names=names1, header=None,skiprows=1)
                df1 = pd.read_csv(withAccLocationPath1, names=names2, header=None,skiprows=1)
                df2 = pd.read_csv(withAccLocationPath2, names=names2, header=None,skiprows=1)
                df3 = pd.read_csv(withAccLocationPath3, names=names2, header=None,skiprows=1)


                trace0 = go.Scatter(x=df['Time'], y=df['Mean Speed'], mode = 'lines',name='Normal Case',
                                     line = dict(color =  ('rgb(0, 0, 255)'),width = 2)
                                    )
                trace1 = go.Scatter(x=df1['Time'], y=df1['Mean Speed'], mode = 'lines',name='One-Lane Closure',
                                     line = dict(color =  ('rgba(16, 112, 2, 0.8)'),width = 2)
                                    )
                trace2 = go.Scatter(x=df2['Time'], y=df2['Mean Speed'], mode = 'lines',name='Two-Lane Closure',
                                     line = dict(color =  ('rgb(255, 0, 0)'),width = 2)
                                    )
                trace3 = go.Scatter(x=df3['Time'], y=df3['Mean Speed'], mode = 'lines',name='Three-Lane Closure',
                                     line = dict(color =  ('rgba(80, 26, 80, 0.8)'),width = 2)
                                    )
                data = [trace0,trace1,trace2,trace3]
                if (0 <= df2['Mean Speed'].astype(float).max() <= 4):
                    max_range = 4
                elif (4 <= df2['Mean Speed'].astype(float).max() <= 10):
                    max_range = 10
                elif (df2['Mean Speed'].astype(float).max() >= 10):
                    max_range = 12
                # Edit the layout
                layout = go.Layout(title = '<b>Edge '+hop+'</b>',
                              titlefont=dict(
                                family='Courier New, monospace',
                                size=22,
                                color='#000000'
                                ),
                              legend=dict(traceorder='normal',
                                               font=dict(family='sans-serif', size=22, color='#000')),
                              xaxis = dict(title = 'Time (min)',tickangle=-45,color='#000000',
                                           tickfont=dict(family='sans-serif',size=19,color='#000'),tickmode = 'linear',dtick = 2),
                              yaxis = dict(title = 'Mean Speed (m/min)',color='#000000',range=[0,max_range],dtick = 2,
                                           tickfont=dict(family='sans-serif',size=19,color='#000')),
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)',
                                   shapes= [
                                    # highlight first accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start1],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end1],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight second accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start2],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end2],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight third accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start3],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end3],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight fourth accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start4],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end4],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    }
                                ]
                              )
                fig = go.Figure(data=data, layout=layout)
                pio.write_image(fig, dirpath+'\\AccHappendLink\\meanSpeed\\images\\'+hop+'.png',width=1800, height=700)
                plotly.offline.plot(fig, filename=dirpath+'/AccHappendLink/meanSpeed/'+hop+'.html',auto_open=False)
                fichier_html_graphs.write("  <object data=\""+hop+'.html'+"\" width=\"1800\" height=\"400\" style=\"margin: 0px 0px\"></object>")
            else:
                print('Three Hop: '+hop+'File Not Found')
                fichier_html_graphs.write("  <object data='AccHappendLink/meanSpeed/FileNotFound.html' width=\"750\" height=\"400\">"+hop+"File Not Found</object>")
    #==========================================================================================



    #Plotting for four plot
    #==========================================================================================

    fichier_html_graphs.write("<h3>================================================Four Hop===============================================</h3> ")
    if len(fourHop)!=0:
        fourHopPlot=[]
        for hop in fourHop:

            dirpath = os.getcwd()
            withoutAccLocationPath=dirpath+'\\dataset\\NormalCase\\seed50_Correct_5min\\'+hop+'.csv'
            withAccLocationPath1=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1 close\\'+hop+'.csv'
            withAccLocationPath2=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2 close\\'+hop+'.csv'
            withAccLocationPath3=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2,3 close\\'+hop+'.csv'



            if os.path.isfile(withoutAccLocationPath) and os.path.isfile(withAccLocationPath1)\
                    and os.path.isfile(withAccLocationPath2) and os.path.isfile(withAccLocationPath3):


                df = pd.read_csv(withoutAccLocationPath,names=names1, header=None,skiprows=1)
                df1 = pd.read_csv(withAccLocationPath1, names=names2, header=None,skiprows=1)
                df2 = pd.read_csv(withAccLocationPath2, names=names2, header=None,skiprows=1)
                df3 = pd.read_csv(withAccLocationPath3, names=names2, header=None,skiprows=1)


                trace0 = go.Scatter(x=df['Time'], y=df['Mean Speed'], mode = 'lines',name='Normal Case',
                                     line = dict(color =  ('rgb(0, 0, 255)'),width = 2)
                                    )
                trace1 = go.Scatter(x=df1['Time'], y=df1['Mean Speed'], mode = 'lines',name='One-Lane Closure',
                                     line = dict(color =  ('rgba(16, 112, 2, 0.8)'),width = 2)
                                    )
                trace2 = go.Scatter(x=df2['Time'], y=df2['Mean Speed'], mode = 'lines',name='Two-Lane Closure',
                                     line = dict(color =  ('rgb(255, 0, 0)'),width = 2)
                                    )
                trace3 = go.Scatter(x=df3['Time'], y=df3['Mean Speed'], mode = 'lines',name='Three-Lane Closure',
                                     line = dict(color =  ('rgba(80, 26, 80, 0.8)'),width = 2)
                                    )
                data = [trace0,trace1,trace2,trace3]
                if (0 <= df2['Mean Speed'].astype(float).max() <= 4):
                    max_range = 4
                elif (4 <= df2['Mean Speed'].astype(float).max() <= 10):
                    max_range = 10
                elif (df2['Mean Speed'].astype(float).max() >= 10):
                    max_range = 12
                # Edit the layout
                layout = go.Layout(title = '<b>Edge '+hop+'</b>',
                              titlefont=dict(
                                family='Courier New, monospace',
                                size=22,
                                color='#000000'
                                ),
                              legend=dict(traceorder='normal',
                                               font=dict(family='sans-serif', size=22, color='#000')),
                              xaxis = dict(title = 'Time (min)',tickangle=-45,color='#000000',
                                           tickfont=dict(family='sans-serif',size=19,color='#000'),tickmode = 'linear',dtick = 2),
                              yaxis = dict(title = 'Mean Speed (m/min)',color='#000000',range=[0,max_range],dtick = 2,
                                           tickfont=dict(family='sans-serif',size=19,color='#000')),
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)',
                                   shapes= [
                                    # highlight first accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start1],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end1],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight second accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start2],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end2],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight third accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start3],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end3],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight fourth accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start4],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end4],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    }
                                ]
                              )
                fig = go.Figure(data=data, layout=layout)
                pio.write_image(fig, dirpath+'\\AccHappendLink\\meanSpeed\\images\\'+hop+'.png',width=1800, height=700)
                plotly.offline.plot(fig, filename=dirpath+'/AccHappendLink/meanSpeed/'+hop+'.html',auto_open=False)
                fichier_html_graphs.write("  <object data=\""+hop+'.html'+"\" width=\"1800\" height=\"400\" style=\"margin: 0px 0px\"></object>")
            else:
                print('Four Hop: '+hop+'File Not Found')
                fichier_html_graphs.write("  <object data='AccHappendLink/meanSpeed/FileNotFound.html' width=\"750\" height=\"400\">"+hop+"File Not Found</object>")
    #==========================================================================================


    fichier_html_graphs.write("</body></html>")
    print("CHECK YOUR DASHBOARD.html In the current directory")
#=============================================================================================================




def showFlowForUpstream(accLink,upstreamList,duration):
    dirpath = os.getcwd()
    fichier_html_graphs=open(dirpath+"/AccHappendLink/flow/"+accLink+" Upstream DashBoard.html",'w')
    fichier_html_graphs.write("<html><head></head><body style=\"margin:0\">"+"\n")

    fichier_html_graphs.write("<h3>============================================Upstream Links of "+accLink+"===========================================</h3> ")
    names1 =  ["Time","Edge ID","Edge Length","NumberOfLane","Lane Name","Jam Length","Density","Mean Speed","Mean Occupancy","Flow","Road State(basedOnJamLength)"]
    names2= ["Time","Edge ID","Edge Length","NumberOfLane","Lane Name","Jam Length","Density","Mean Speed","Mean Occupancy","Flow","Road State(basedOnJamLength)","Road State(basedOnFlow)"]

    grid=[]
    zeroHop=upstreamList[0]
    oneHop=upstreamList[1]
    twoHop=upstreamList[2]
    threeHop=upstreamList[3]
    fourHop=upstreamList[4]

    if (duration == 20):
        start1 = 2
        end1 = 6
        start2 = 11
        end2 = 15
        start3 = 20
        end3 = 24
        start4 = 29
        end4 = 33
    if (duration == 10):
        start1 = 2
        end1 = 4
        start2 = 11
        end2 = 13
        start3 = 20
        end3 = 22
        start4 = 29
        end4 = 31
    if (duration == 15):
        start1 = 2
        end1 = 5
        start2 = 11
        end2 = 14
        start3 = 20
        end3 = 23
        start4 = 29
        end4 = 32

    #Plotting for zero plot
    #==========================================================================================

    fichier_html_graphs.write("<h3>================================================Zero Hop===============================================</h3> ")
    if len(zeroHop)!=0:
        for hop in zeroHop:


            withoutAccLocationPath=dirpath+'\\dataset\\NormalCase\\seed50_Correct_5min\\'+hop+'.csv'
            withAccLocationPath1=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1 close\\'+hop+'.csv'
            withAccLocationPath2=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2 close\\'+hop+'.csv'
            withAccLocationPath3=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2,3 close\\'+hop+'.csv'



            if os.path.isfile(withoutAccLocationPath) and os.path.isfile(withAccLocationPath1)\
                    and os.path.isfile(withAccLocationPath2) and os.path.isfile(withAccLocationPath3):


                df = pd.read_csv(withoutAccLocationPath,names=names1, header=None,skiprows=1)
                df1 = pd.read_csv(withAccLocationPath1, names=names2, header=None,skiprows=1)
                df2 = pd.read_csv(withAccLocationPath2, names=names2, header=None,skiprows=1)
                df3 = pd.read_csv(withAccLocationPath3, names=names2, header=None,skiprows=1)


                trace0 = go.Scatter(x=df['Time'], y=df['Flow'], mode = 'lines',name='Normal Case',
                                     line = dict(color =  ('rgb(0, 0, 255)'),width = 2)
                                    )
                trace1 = go.Scatter(x=df1['Time'], y=df1['Flow'], mode = 'lines',name='One-Lane Closure',
                                     line = dict(color =  ('rgba(16, 112, 2, 0.8)'),width = 2)
                                    )
                trace2 = go.Scatter(x=df2['Time'], y=df2['Flow'], mode = 'lines',name='Two-Lane Closure',
                                     line = dict(color =  ('rgb(255, 0, 0)'),width = 2)
                                    )
                trace3 = go.Scatter(x=df3['Time'], y=df3['Flow'], mode = 'lines',name='Three-Lane Closure',
                                     line = dict(color =  ('rgba(80, 26, 80, 0.8)'),width = 2)
                                    )
                data = [trace0,trace1,trace2,trace3]
                if (0 <= df2['Flow'].astype(float).max() <= 200):
                    max_range = 200
                elif (200 <= df2['Flow'].astype(float).max() <= 400):
                    max_range = 400
                elif (400 <= df2['Flow'].astype(float).max() <= 800):
                    max_range = 800
                elif (df2['Flow'].astype(float).max() >= 800):
                    max_range = 900
                # Edit the layout
                layout = go.Layout(title = '<b>Edge '+hop+'</b>',
                              titlefont=dict(
                                family='Courier New, monospace',
                                  size=22,
                                color='#000000'
                                ),
                              legend=dict(traceorder='normal',
                                               font=dict(family='sans-serif', size=22, color='#000')),
                              xaxis = dict(title = 'Time (min)',tickangle=-45,color='#000000',
                                           tickfont=dict(family='sans-serif',size=19,color='#000'),tickmode = 'linear',dtick = 2),
                              yaxis = dict(title = 'Flow (veh/min)',color='#000000',range=[0,max_range],dtick=max_range/4,
                                           tickfont=dict(family='sans-serif',size=19,color='#000')),
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)',
                                shapes= [
                                    # highlight first accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start1],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end1],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight second accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start2],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end2],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight third accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start3],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end3],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight fourth accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start4],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end4],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    }
                                ]
                              )
                fig = go.Figure(data=data, layout=layout)
                pio.write_image(fig, dirpath+'\\AccHappendLink\\flow\\images\\'+hop+'.png',width=1800, height=700)
                plotly.offline.plot(fig, filename=dirpath+'/AccHappendLink/flow/'+hop+'.html',auto_open=False)
                fichier_html_graphs.write("  <object data=\""+hop+'.html'+"\" width=\"1800\" height=\"400\" style=\"margin: 0px 0px\"></object>")

            else:
                print('Zero Hop: '+hop+'File Not Found')
                fichier_html_graphs.write("  <object data='AccHappendLink/flow/FileNotFound.html' width=\"750\" height=\"400\">"+hop+"File Not Found</object>")
    #==========================================================================================



    #Plotting for one plot
    #==========================================================================================

    fichier_html_graphs.write("<h3>================================================One Hop===============================================</h3> ")
    if len(oneHop)!=0:
        for hop in oneHop:

            dirpath = os.getcwd()
            withoutAccLocationPath=dirpath+'\\dataset\\NormalCase\\seed50_Correct_5min\\'+hop+'.csv'
            withAccLocationPath1=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1 close\\'+hop+'.csv'
            withAccLocationPath2=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2 close\\'+hop+'.csv'
            withAccLocationPath3=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2,3 close\\'+hop+'.csv'



            if os.path.isfile(withoutAccLocationPath) and os.path.isfile(withAccLocationPath1)\
                    and os.path.isfile(withAccLocationPath2) and os.path.isfile(withAccLocationPath3):


                df = pd.read_csv(withoutAccLocationPath,names=names1, header=None,skiprows=1)
                df1 = pd.read_csv(withAccLocationPath1, names=names2, header=None,skiprows=1)
                df2 = pd.read_csv(withAccLocationPath2, names=names2, header=None,skiprows=1)
                df3 = pd.read_csv(withAccLocationPath3, names=names2, header=None,skiprows=1)


                trace0 = go.Scatter(x=df['Time'], y=df['Flow'], mode = 'lines',name='Normal Case',
                                     line = dict(color =  ('rgb(0, 0, 255)'),width = 2)
                                    )
                trace1 = go.Scatter(x=df1['Time'], y=df1['Flow'], mode = 'lines',name='One-Lane Closure',
                                     line = dict(color =  ('rgba(16, 112, 2, 0.8)'),width = 2)
                                    )
                trace2 = go.Scatter(x=df2['Time'], y=df2['Flow'], mode = 'lines',name='Two-Lane Closure',
                                     line = dict(color =  ('rgb(255, 0, 0)'),width = 2)
                                    )
                trace3 = go.Scatter(x=df3['Time'], y=df3['Flow'], mode = 'lines',name='Three-Lane Closure',
                                     line = dict(color =  ('rgba(80, 26, 80, 0.8)'),width = 2)
                                    )
                data = [trace0,trace1,trace2,trace3]

                if (0 <= df2['Flow'].astype(float).max() <= 200):
                    max_range = 200
                elif (200 < df2['Flow'].astype(float).max() <= 400):
                    max_range = 400
                elif (400 < df2['Flow'].astype(float).max() <= 800):
                    max_range = 800
                elif (df2['Flow'].astype(float).max() >= 800):
                    max_range = 900
                if hop=='L49':
                    max_range=400
                # Edit the layout
                layout = go.Layout(title = '<b>Edge '+hop+'</b>',
                              titlefont=dict(
                                family='Courier New, monospace',
                                size=22,
                                color='#000000'
                                ),
                              legend=dict(traceorder='normal',
                                               font=dict(family='sans-serif', size=22, color='#000')),
                              xaxis = dict(title = 'Time (min)',tickangle=-45,color='#000000',
                                           tickfont=dict(family='sans-serif',size=19,color='#000'),tickmode = 'linear',dtick = 2),
                              yaxis = dict(title = 'Flow (veh/min)',color='#000000',range=[0,max_range],dtick=max_range/4,
                                           tickfont=dict(family='sans-serif',size=19,color='#000')),
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)',
                                   shapes= [
                                    # highlight first accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start1],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end1],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight second accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start2],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end2],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight third accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start3],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end3],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight fourth accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start4],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end4],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    }
                                ]
                              )
                fig = go.Figure(data=data, layout=layout)
                pio.write_image(fig, dirpath+'\\AccHappendLink\\flow\\images\\'+hop+'.png',width=1800, height=700)
                plotly.offline.plot(fig, filename=dirpath+'/AccHappendLink/flow/'+hop+'.html',auto_open=False)
                fichier_html_graphs.write("  <object data=\""+hop+'.html'+"\" width=\"1800\" height=\"400\" style=\"margin: 0px 0px\"></object>")

            else:
                print('One Hop: '+hop+'File Not Found')
                fichier_html_graphs.write("  <object data='AccHappendLink/flow/FileNotFound.html' width=\"750\" height=\"400\">"+hop+"File Not Found</object>")
    #==========================================================================================




    #Plotting for two plot
    #==========================================================================================

    fichier_html_graphs.write("<h3>================================================Two Hop===============================================</h3> ")
    if len(twoHop)!=0:
        twoHopPlot=[]
        for hop in twoHop:

            dirpath = os.getcwd()
            withoutAccLocationPath=dirpath+'\\dataset\\NormalCase\\seed50_Correct_5min\\'+hop+'.csv'
            withAccLocationPath1=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1 close\\'+hop+'.csv'
            withAccLocationPath2=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2 close\\'+hop+'.csv'
            withAccLocationPath3=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2,3 close\\'+hop+'.csv'



            if os.path.isfile(withoutAccLocationPath) and os.path.isfile(withAccLocationPath1)\
                    and os.path.isfile(withAccLocationPath2) and os.path.isfile(withAccLocationPath3):


                df = pd.read_csv(withoutAccLocationPath,names=names1, header=None,skiprows=1)
                df1 = pd.read_csv(withAccLocationPath1, names=names2, header=None,skiprows=1)
                df2 = pd.read_csv(withAccLocationPath2, names=names2, header=None,skiprows=1)
                df3 = pd.read_csv(withAccLocationPath3, names=names2, header=None,skiprows=1)


                trace0 = go.Scatter(x=df['Time'], y=df['Flow'], mode = 'lines',name='Normal Case',
                                     line = dict(color =  ('rgb(0, 0, 255)'),width = 2)
                                    )
                trace1 = go.Scatter(x=df1['Time'], y=df1['Flow'], mode = 'lines',name='One-Lane Closure',
                                     line = dict(color =  ('rgba(16, 112, 2, 0.8)'),width = 2)
                                    )
                trace2 = go.Scatter(x=df2['Time'], y=df2['Flow'], mode = 'lines',name='Two-Lane Closure',
                                     line = dict(color =  ('rgb(255, 0, 0)'),width = 2)
                                    )
                trace3 = go.Scatter(x=df3['Time'], y=df3['Flow'], mode = 'lines',name='Three-Lane Closure',
                                     line = dict(color =  ('rgba(80, 26, 80, 0.8)'),width = 2)
                                    )
                data = [trace0,trace1,trace2,trace3]
                if (0 <= df2['Flow'].astype(float).max() <= 200):
                    max_range = 200
                elif (200 < df2['Flow'].astype(float).max() <= 400):
                    max_range = 400
                elif (400 < df2['Flow'].astype(float).max() <= 800):
                    max_range = 800
                elif (df2['Flow'].astype(float).max() >= 800):
                    max_range = 900
                # Edit the layout
                layout = go.Layout(title = '<b>Edge '+hop+'</b>',
                              titlefont=dict(
                                family='Courier New, monospace',
                                size=22,
                                color='#000000'
                                ),
                              legend=dict(traceorder='normal',
                                               font=dict(family='sans-serif', size=22, color='#000')),
                              xaxis = dict(title = 'Time (min)',tickangle=-45,color='#000000',
                                           tickfont=dict(family='sans-serif',size=19,color='#000'),tickmode = 'linear',dtick = 2),
                              yaxis = dict(title = 'Flow (veh/min)',color='#000000',range=[0,max_range],dtick=max_range/4,
                                           tickfont=dict(family='sans-serif',size=19,color='#000')),
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)',
                                   shapes= [
                                    # highlight first accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start1],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end1],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight second accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start2],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end2],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight third accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start3],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end3],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight fourth accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start4],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end4],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    }
                                ]
                              )
                fig = go.Figure(data=data, layout=layout)
                pio.write_image(fig, dirpath+'\\AccHappendLink\\flow\\images\\'+hop+'.png',width=1800, height=700)
                plotly.offline.plot(fig, filename=dirpath+'/AccHappendLink/flow/'+hop+'.html',auto_open=False)
                fichier_html_graphs.write("  <object data=\""+hop+'.html'+"\" width=\"1800\" height=\"400\" style=\"margin: 0px 0px\"></object>")

            else:
                print('Two Hop: '+hop+'File Not Found')
                fichier_html_graphs.write("  <object data='AccHappendLink/flow/FileNotFound.html' width=\"750\" height=\"400\">"+hop+"File Not Found</object>")
    #==========================================================================================


    #Plotting for three plot
    #==========================================================================================

    fichier_html_graphs.write("<h3>================================================Three Hop===============================================</h3> ")
    if len(threeHop)!=0:
        threeHopPlot=[]
        for hop in threeHop:

            dirpath = os.getcwd()
            withoutAccLocationPath=dirpath+'\\dataset\\NormalCase\\seed50_Correct_5min\\'+hop+'.csv'
            withAccLocationPath1=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1 close\\'+hop+'.csv'
            withAccLocationPath2=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2 close\\'+hop+'.csv'
            withAccLocationPath3=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2,3 close\\'+hop+'.csv'



            if os.path.isfile(withoutAccLocationPath) and os.path.isfile(withAccLocationPath1)\
                    and os.path.isfile(withAccLocationPath2) and os.path.isfile(withAccLocationPath3):


                df = pd.read_csv(withoutAccLocationPath,names=names1, header=None,skiprows=1)
                df1 = pd.read_csv(withAccLocationPath1, names=names2, header=None,skiprows=1)
                df2 = pd.read_csv(withAccLocationPath2, names=names2, header=None,skiprows=1)
                df3 = pd.read_csv(withAccLocationPath3, names=names2, header=None,skiprows=1)


                trace0 = go.Scatter(x=df['Time'], y=df['Flow'], mode = 'lines',name='Normal Case',
                                     line = dict(color =  ('rgb(0, 0, 255)'),width = 2)
                                    )
                trace1 = go.Scatter(x=df1['Time'], y=df1['Flow'], mode = 'lines',name='One-Lane Closure',
                                     line = dict(color =  ('rgba(16, 112, 2, 0.8)'),width = 2)
                                    )
                trace2 = go.Scatter(x=df2['Time'], y=df2['Flow'], mode = 'lines',name='Two-Lane Closure',
                                     line = dict(color =  ('rgb(255, 0, 0)'),width = 2)
                                    )
                trace3 = go.Scatter(x=df3['Time'], y=df3['Flow'], mode = 'lines',name='Three-Lane Closure',
                                     line = dict(color =  ('rgba(80, 26, 80, 0.8)'),width = 2)
                                    )
                data = [trace0,trace1,trace2,trace3]
                if (0 <= df2['Flow'].astype(float).max() <= 200):
                    max_range = 200
                elif (200 < df2['Flow'].astype(float).max() <= 400):
                    max_range = 400
                elif (400 < df2['Flow'].astype(float).max() <= 800):
                    max_range = 800
                elif (df2['Flow'].astype(float).max() >= 800):
                    max_range = 900
                # Edit the layout
                layout = go.Layout(title = '<b>Edge '+hop+'</b>',
                              titlefont=dict(
                                family='Courier New, monospace',
                                size=22,
                                color='#000000'
                                ),
                              legend=dict(traceorder='normal',
                                               font=dict(family='sans-serif', size=22, color='#000')),
                              xaxis = dict(title = 'Time (min)',tickangle=-45,color='#000000',
                                           tickfont=dict(family='sans-serif',size=19,color='#000'),tickmode = 'linear',dtick = 2),
                              yaxis = dict(title = 'Flow (veh/min)',color='#000000',range=[0,max_range],dtick=max_range/4,
                                           tickfont=dict(family='sans-serif',size=19,color='#000')),
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)',
                                   shapes= [
                                    # highlight first accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start1],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end1],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight second accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start2],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end2],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight third accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start3],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end3],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight fourth accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start4],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end4],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    }
                                ]
                              )
                fig = go.Figure(data=data, layout=layout)
                pio.write_image(fig, dirpath+'\\AccHappendLink\\flow\\images\\'+hop+'.png',width=1800, height=700)
                plotly.offline.plot(fig, filename=dirpath+'/AccHappendLink/flow/'+hop+'.html',auto_open=False)
                fichier_html_graphs.write("  <object data=\""+hop+'.html'+"\" width=\"1800\" height=\"400\" style=\"margin: 0px 0px\"></object>")
            else:
                print('Three Hop: '+hop+'File Not Found')
                fichier_html_graphs.write("  <object data='AccHappendLink/flow/FileNotFound.html' width=\"750\" height=\"400\">"+hop+"File Not Found</object>")
    #==========================================================================================



    #Plotting for four plot
    #==========================================================================================

    fichier_html_graphs.write("<h3>================================================Four Hop===============================================</h3> ")
    if len(fourHop)!=0:
        fourHopPlot=[]
        for hop in fourHop:

            dirpath = os.getcwd()
            withoutAccLocationPath=dirpath+'\\dataset\\NormalCase\\seed50_Correct_5min\\'+hop+'.csv'
            withAccLocationPath1=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1 close\\'+hop+'.csv'
            withAccLocationPath2=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2 close\\'+hop+'.csv'
            withAccLocationPath3=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2,3 close\\'+hop+'.csv'



            if os.path.isfile(withoutAccLocationPath) and os.path.isfile(withAccLocationPath1)\
                    and os.path.isfile(withAccLocationPath2) and os.path.isfile(withAccLocationPath3):


                df = pd.read_csv(withoutAccLocationPath,names=names1, header=None,skiprows=1)
                df1 = pd.read_csv(withAccLocationPath1, names=names2, header=None,skiprows=1)
                df2 = pd.read_csv(withAccLocationPath2, names=names2, header=None,skiprows=1)
                df3 = pd.read_csv(withAccLocationPath3, names=names2, header=None,skiprows=1)


                trace0 = go.Scatter(x=df['Time'], y=df['Flow'], mode = 'lines',name='Normal Case',
                                     line = dict(color =  ('rgb(0, 0, 255)'),width = 2)
                                    )
                trace1 = go.Scatter(x=df1['Time'], y=df1['Flow'], mode = 'lines',name='One-Lane Closure',
                                     line = dict(color =  ('rgba(16, 112, 2, 0.8)'),width = 2)
                                    )
                trace2 = go.Scatter(x=df2['Time'], y=df2['Flow'], mode = 'lines',name='Two-Lane Closure',
                                     line = dict(color =  ('rgb(255, 0, 0)'),width = 2)
                                    )
                trace3 = go.Scatter(x=df3['Time'], y=df3['Flow'], mode = 'lines',name='Three-Lane Closure',
                                     line = dict(color =  ('rgba(80, 26, 80, 0.8)'),width = 2)
                                    )
                data = [trace0,trace1,trace2,trace3]
                if (0 <= df2['Flow'].astype(float).max() <= 200):
                    max_range = 200
                elif (200 < df2['Flow'].astype(float).max() <= 400):
                    max_range = 400
                elif (400 < df2['Flow'].astype(float).max() <= 800):
                    max_range = 800
                elif (df2['Flow'].astype(float).max() >= 800):
                    max_range = 900
                # Edit the layout
                layout = go.Layout(title = '<b>Edge '+hop+'</b>',
                              titlefont=dict(
                                family='Courier New, monospace',
                                size=22,
                                color='#000000'
                                ),
                              legend=dict(traceorder='normal',
                                               font=dict(family='sans-serif', size=22, color='#000')),
                              xaxis = dict(title = 'Time (min)',tickangle=-45,color='#000000',
                                           tickfont=dict(family='sans-serif',size=19,color='#000'),tickmode = 'linear',dtick = 2),
                              yaxis = dict(title = 'Flow (veh/min)',color='#000000',range=[0,max_range],dtick=max_range/4,
                                           tickfont=dict(family='sans-serif',size=19,color='#000')),
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)',
                                   shapes= [
                                    # highlight first accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start1],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end1],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight second accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start2],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end2],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight third accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start3],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end3],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight fourth accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start4],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end4],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    }
                                ]
                              )
                fig = go.Figure(data=data, layout=layout)
                pio.write_image(fig, dirpath+'\\AccHappendLink\\flow\\images\\'+hop+'.png',width=1800, height=700)
                plotly.offline.plot(fig, filename=dirpath+'/AccHappendLink/flow/'+hop+'.html',auto_open=False)
                fichier_html_graphs.write("  <object data=\""+hop+'.html'+"\" width=\"1800\" height=\"400\" style=\"margin: 0px 0px\"></object>")
            else:
                print('Four Hop: '+hop+'File Not Found')
                fichier_html_graphs.write("  <object data='AccHappendLink/flow/FileNotFound.html' width=\"750\" height=\"400\">"+hop+"File Not Found</object>")
    #==========================================================================================
    fichier_html_graphs.write("</body></html>")
    print("CHECK YOUR DASHBOARD.html In the current directory")
#============================================================================================================================



def showFlowForDownstream(accLink,upstreamList,duration):
    dirpath = os.getcwd()
    fichier_html_graphs=open(dirpath+"/AccHappendLink/flow/"+accLink+" Downstream DashBoard.html",'w')
    fichier_html_graphs.write("<html><head></head><body style=\"margin:0\">"+"\n")

    fichier_html_graphs.write("<h3>============================================Downstream Links of "+accLink+"===========================================</h3> ")
    names1 =  ["Time","Edge ID","Edge Length","NumberOfLane","Lane Name","Jam Length","Density","Mean Speed","Mean Occupancy","Flow","Road State(basedOnJamLength)"]
    names2= ["Time","Edge ID","Edge Length","NumberOfLane","Lane Name","Jam Length","Density","Mean Speed","Mean Occupancy","Flow","Road State(basedOnJamLength)","Road State(basedOnFlow)"]

    grid=[]
    zeroHop=upstreamList[0]
    oneHop=upstreamList[1]
    twoHop=upstreamList[2]
    threeHop=upstreamList[3]
    fourHop=upstreamList[4]

    if (duration == 20):
        start1 = 2
        end1 = 6
        start2 = 11
        end2 = 15
        start3 = 20
        end3 = 24
        start4 = 29
        end4 = 33
    if (duration == 10):
        start1 = 2
        end1 = 4
        start2 = 11
        end2 = 13
        start3 = 20
        end3 = 22
        start4 = 29
        end4 = 31
    if (duration == 15):
        start1 = 2
        end1 = 5
        start2 = 11
        end2 = 14
        start3 = 20
        end3 = 23
        start4 = 29
        end4 = 32

    #Plotting for zero plot
    #==========================================================================================

    fichier_html_graphs.write("<h3>================================================Zero Hop===============================================</h3> ")
    if len(zeroHop)!=0:
        for hop in zeroHop:


            withoutAccLocationPath=dirpath+'\\dataset\\NormalCase\\seed50_Correct_5min\\'+hop+'.csv'
            withAccLocationPath1=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1 close\\'+hop+'.csv'
            withAccLocationPath2=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2 close\\'+hop+'.csv'
            withAccLocationPath3=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2,3 close\\'+hop+'.csv'



            if os.path.isfile(withoutAccLocationPath) and os.path.isfile(withAccLocationPath1)\
                    and os.path.isfile(withAccLocationPath2) and os.path.isfile(withAccLocationPath3):


                df = pd.read_csv(withoutAccLocationPath,names=names1, header=None,skiprows=1)
                df1 = pd.read_csv(withAccLocationPath1, names=names2, header=None,skiprows=1)
                df2 = pd.read_csv(withAccLocationPath2, names=names2, header=None,skiprows=1)
                df3 = pd.read_csv(withAccLocationPath3, names=names2, header=None,skiprows=1)


                trace0 = go.Scatter(x=df['Time'], y=df['Flow'], mode = 'lines',name='Normal Case',
                                     line = dict(color =  ('rgb(0, 0, 255)'),width = 2)
                                    )
                trace1 = go.Scatter(x=df1['Time'], y=df1['Flow'], mode = 'lines',name='One-Lane Closure',
                                     line = dict(color =  ('rgba(16, 112, 2, 0.8)'),width = 2)
                                    )
                trace2 = go.Scatter(x=df2['Time'], y=df2['Flow'], mode = 'lines',name='Two-Lane Closure',
                                     line = dict(color =  ('rgb(255, 0, 0)'),width = 2)
                                    )
                trace3 = go.Scatter(x=df3['Time'], y=df3['Flow'], mode = 'lines',name='Three-Lane Closure',
                                     line = dict(color =  ('rgba(80, 26, 80, 0.8)'),width = 2)
                                    )
                data = [trace0,trace1,trace2,trace3]
                if (0 <= df2['Flow'].astype(float).max() <= 200):
                    max_range = 200
                elif (200 < df2['Flow'].astype(float).max() <= 400):
                    max_range = 400
                elif (400 < df2['Flow'].astype(float).max() <= 800):
                    max_range = 800
                elif (df2['Flow'].astype(float).max() >= 800):
                    max_range = 900
                # Edit the layout
                layout = go.Layout(title = '<b>Edge '+hop+'</b>',
                              titlefont=dict(
                                family='Courier New, monospace',
                                  size=22,
                                color='#000000'
                                ),
                              legend=dict(traceorder='normal',
                                               font=dict(family='sans-serif', size=22, color='#000')),
                              xaxis = dict(title = 'Time (min)',tickangle=-45,color='#000000',
                                           tickfont=dict(family='sans-serif',size=19,color='#000'),tickmode = 'linear',dtick = 2),
                              yaxis = dict(title = 'Flow (veh/min)',color='#000000',range=[0,max_range],dtick=max_range/4,
                                           tickfont=dict(family='sans-serif',size=19,color='#000')),
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)',
                                shapes= [
                                    # highlight first accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start1],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end1],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight second accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start2],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end2],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight third accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start3],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end3],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight fourth accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start4],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end4],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    }
                                ]
                              )
                fig = go.Figure(data=data, layout=layout)
                pio.write_image(fig, dirpath+'\\AccHappendLink\\flow\\images\\'+hop+'.png',width=1800, height=700)
                plotly.offline.plot(fig, filename=dirpath+'/AccHappendLink/flow/'+hop+'.html',auto_open=False)
                fichier_html_graphs.write("  <object data=\""+hop+'.html'+"\" width=\"1800\" height=\"400\" style=\"margin: 0px 0px\"></object>")

            else:
                print('Zero Hop: '+hop+'File Not Found')
                fichier_html_graphs.write("  <object data='AccHappendLink/flow/FileNotFound.html' width=\"750\" height=\"400\">"+hop+"File Not Found</object>")
    #==========================================================================================



    #Plotting for one plot
    #==========================================================================================

    fichier_html_graphs.write("<h3>================================================One Hop===============================================</h3> ")
    if len(oneHop)!=0:
        for hop in oneHop:

            dirpath = os.getcwd()
            withoutAccLocationPath=dirpath+'\\dataset\\NormalCase\\seed50_Correct_5min\\'+hop+'.csv'
            withAccLocationPath1=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1 close\\'+hop+'.csv'
            withAccLocationPath2=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2 close\\'+hop+'.csv'
            withAccLocationPath3=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2,3 close\\'+hop+'.csv'



            if os.path.isfile(withoutAccLocationPath) and os.path.isfile(withAccLocationPath1)\
                    and os.path.isfile(withAccLocationPath2) and os.path.isfile(withAccLocationPath3):


                df = pd.read_csv(withoutAccLocationPath,names=names1, header=None,skiprows=1)
                df1 = pd.read_csv(withAccLocationPath1, names=names2, header=None,skiprows=1)
                df2 = pd.read_csv(withAccLocationPath2, names=names2, header=None,skiprows=1)
                df3 = pd.read_csv(withAccLocationPath3, names=names2, header=None,skiprows=1)


                trace0 = go.Scatter(x=df['Time'], y=df['Flow'], mode = 'lines',name='Normal Case',
                                     line = dict(color =  ('rgb(0, 0, 255)'),width = 2)
                                    )
                trace1 = go.Scatter(x=df1['Time'], y=df1['Flow'], mode = 'lines',name='One-Lane Closure',
                                     line = dict(color =  ('rgba(16, 112, 2, 0.8)'),width = 2)
                                    )
                trace2 = go.Scatter(x=df2['Time'], y=df2['Flow'], mode = 'lines',name='Two-Lane Closure',
                                     line = dict(color =  ('rgb(255, 0, 0)'),width = 2)
                                    )
                trace3 = go.Scatter(x=df3['Time'], y=df3['Flow'], mode = 'lines',name='Three-Lane Closure',
                                     line = dict(color =  ('rgba(80, 26, 80, 0.8)'),width = 2)
                                    )
                data = [trace0,trace1,trace2,trace3]
                if (0 <= df2['Flow'].astype(float).max() <= 200):
                    max_range = 200
                elif (200 < df2['Flow'].astype(float).max() <= 400):
                    max_range = 400
                elif (400 < df2['Flow'].astype(float).max() <= 800):
                    max_range = 800
                elif (df2['Flow'].astype(float).max() >= 800):
                    max_range = 900
                # Edit the layout
                layout = go.Layout(title = '<b>Edge '+hop+'</b>',
                              titlefont=dict(
                                family='Courier New, monospace',
                                size=22,
                                color='#000000'
                                ),
                                   legend=dict(traceorder='normal',
                                               font=dict(family='sans-serif', size=22, color='#000')),
                              xaxis = dict(title = 'Time (min)',tickangle=-45,color='#000000',
                                           tickfont=dict(family='sans-serif',size=19,color='#000'),tickmode = 'linear',dtick = 2),
                              yaxis = dict(title = 'Flow (veh/min)',color='#000000',range=[0,max_range],dtick=max_range/4,
                                           tickfont=dict(family='sans-serif',size=19,color='#000')),
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)',
                                   shapes= [
                                    # highlight first accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start1],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end1],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight second accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start2],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end2],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight third accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start3],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end3],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight fourth accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start4],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end4],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    }
                                ]
                              )
                fig = go.Figure(data=data, layout=layout)
                pio.write_image(fig, dirpath+'\\AccHappendLink\\flow\\images\\'+hop+'.png',width=1800, height=700)
                plotly.offline.plot(fig, filename=dirpath+'/AccHappendLink/flow/'+hop+'.html',auto_open=False)
                fichier_html_graphs.write("  <object data=\""+hop+'.html'+"\" width=\"1800\" height=\"400\" style=\"margin: 0px 0px\"></object>")

            else:
                print('One Hop: '+hop+'File Not Found')
                fichier_html_graphs.write("  <object data='AccHappendLink/flow/FileNotFound.html' width=\"750\" height=\"400\">"+hop+"File Not Found</object>")
    #==========================================================================================




    #Plotting for two plot
    #==========================================================================================

    fichier_html_graphs.write("<h3>================================================Two Hop===============================================</h3> ")
    if len(twoHop)!=0:
        twoHopPlot=[]
        for hop in twoHop:

            dirpath = os.getcwd()
            withoutAccLocationPath=dirpath+'\\dataset\\NormalCase\\seed50_Correct_5min\\'+hop+'.csv'
            withAccLocationPath1=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1 close\\'+hop+'.csv'
            withAccLocationPath2=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2 close\\'+hop+'.csv'
            withAccLocationPath3=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2,3 close\\'+hop+'.csv'



            if os.path.isfile(withoutAccLocationPath) and os.path.isfile(withAccLocationPath1)\
                    and os.path.isfile(withAccLocationPath2) and os.path.isfile(withAccLocationPath3):


                df = pd.read_csv(withoutAccLocationPath,names=names1, header=None,skiprows=1)
                df1 = pd.read_csv(withAccLocationPath1, names=names2, header=None,skiprows=1)
                df2 = pd.read_csv(withAccLocationPath2, names=names2, header=None,skiprows=1)
                df3 = pd.read_csv(withAccLocationPath3, names=names2, header=None,skiprows=1)


                trace0 = go.Scatter(x=df['Time'], y=df['Flow'], mode = 'lines',name='Normal Case',
                                     line = dict(color =  ('rgb(0, 0, 255)'),width = 2)
                                    )
                trace1 = go.Scatter(x=df1['Time'], y=df1['Flow'], mode = 'lines',name='One-Lane Closure',
                                     line = dict(color =  ('rgba(16, 112, 2, 0.8)'),width = 2)
                                    )
                trace2 = go.Scatter(x=df2['Time'], y=df2['Flow'], mode = 'lines',name='Two-Lane Closure',
                                     line = dict(color =  ('rgb(255, 0, 0)'),width = 2)
                                    )
                trace3 = go.Scatter(x=df3['Time'], y=df3['Flow'], mode = 'lines',name='Three-Lane Closure',
                                     line = dict(color =  ('rgba(80, 26, 80, 0.8)'),width = 2)
                                    )
                data = [trace0,trace1,trace2,trace3]
                if (0 <= df2['Flow'].astype(float).max() <= 200):
                    max_range = 200
                elif (200 < df2['Flow'].astype(float).max() <= 400):
                    max_range = 400
                elif (400 < df2['Flow'].astype(float).max() <= 800):
                    max_range = 800
                elif (df2['Flow'].astype(float).max() >= 800):
                    max_range = 900
                # Edit the layout
                layout = go.Layout(title = '<b>Edge '+hop+'</b>',
                              titlefont=dict(
                                family='Courier New, monospace',
                                size=22,
                                color='#000000'
                                ),
                                   legend=dict(traceorder='normal',
                                               font=dict(family='sans-serif', size=22, color='#000')),
                              xaxis = dict(title = 'Time (min)',tickangle=-45,color='#000000',
                                           tickfont=dict(family='sans-serif',size=19,color='#000'),tickmode = 'linear',dtick = 2),
                              yaxis = dict(title = 'Flow (veh/min)',color='#000000',range=[0,max_range],dtick=max_range/4,
                                           tickfont=dict(family='sans-serif',size=19,color='#000')),
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)',
                                   shapes= [
                                    # highlight first accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start1],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end1],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight second accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start2],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end2],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight third accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start3],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end3],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight fourth accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start4],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end4],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    }
                                ]
                              )
                fig = go.Figure(data=data, layout=layout)
                pio.write_image(fig, dirpath+'\\AccHappendLink\\flow\\images\\'+hop+'.png',width=1800, height=700)
                plotly.offline.plot(fig, filename=dirpath+'/AccHappendLink/flow/'+hop+'.html',auto_open=False)
                fichier_html_graphs.write("  <object data=\""+hop+'.html'+"\" width=\"1800\" height=\"400\" style=\"margin: 0px 0px\"></object>")

            else:
                print('Two Hop: '+hop+'File Not Found')
                fichier_html_graphs.write("  <object data='AccHappendLink/flow/FileNotFound.html' width=\"750\" height=\"400\">"+hop+"File Not Found</object>")
    #==========================================================================================


    #Plotting for three plot
    #==========================================================================================

    fichier_html_graphs.write("<h3>================================================Three Hop===============================================</h3> ")
    if len(threeHop)!=0:
        threeHopPlot=[]
        for hop in threeHop:

            dirpath = os.getcwd()
            withoutAccLocationPath=dirpath+'\\dataset\\NormalCase\\seed50_Correct_5min\\'+hop+'.csv'
            withAccLocationPath1=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1 close\\'+hop+'.csv'
            withAccLocationPath2=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2 close\\'+hop+'.csv'
            withAccLocationPath3=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2,3 close\\'+hop+'.csv'



            if os.path.isfile(withoutAccLocationPath) and os.path.isfile(withAccLocationPath1)\
                    and os.path.isfile(withAccLocationPath2) and os.path.isfile(withAccLocationPath3):


                df = pd.read_csv(withoutAccLocationPath,names=names1, header=None,skiprows=1)
                df1 = pd.read_csv(withAccLocationPath1, names=names2, header=None,skiprows=1)
                df2 = pd.read_csv(withAccLocationPath2, names=names2, header=None,skiprows=1)
                df3 = pd.read_csv(withAccLocationPath3, names=names2, header=None,skiprows=1)


                trace0 = go.Scatter(x=df['Time'], y=df['Flow'], mode = 'lines',name='Normal Case',
                                     line = dict(color =  ('rgb(0, 0, 255)'),width = 2)
                                    )
                trace1 = go.Scatter(x=df1['Time'], y=df1['Flow'], mode = 'lines',name='One-Lane Closure',
                                     line = dict(color =  ('rgba(16, 112, 2, 0.8)'),width = 2)
                                    )
                trace2 = go.Scatter(x=df2['Time'], y=df2['Flow'], mode = 'lines',name='Two-Lane Closure',
                                     line = dict(color =  ('rgb(255, 0, 0)'),width = 2)
                                    )
                trace3 = go.Scatter(x=df3['Time'], y=df3['Flow'], mode = 'lines',name='Three-Lane Closure',
                                     line = dict(color =  ('rgba(80, 26, 80, 0.8)'),width = 2)
                                    )
                data = [trace0,trace1,trace2,trace3]
                if (0 <= df2['Flow'].astype(float).max() <= 200):
                    max_range = 200
                elif (200 < df2['Flow'].astype(float).max() <= 400):
                    max_range = 400
                elif (400 < df2['Flow'].astype(float).max() <= 800):
                    max_range = 800
                elif (df2['Flow'].astype(float).max() >= 800):
                    max_range = 900
                # Edit the layout
                layout = go.Layout(title = '<b>Edge '+hop+'</b>',
                              titlefont=dict(
                                family='Courier New, monospace',
                                size=22,
                                color='#000000'
                                ),
                                   legend=dict(traceorder='normal',
                                               font=dict(family='sans-serif', size=22, color='#000')),
                              xaxis = dict(title = 'Time (min)',tickangle=-45,color='#000000',
                                           tickfont=dict(family='sans-serif',size=19,color='#000'),tickmode = 'linear',dtick = 2),
                              yaxis = dict(title = 'Flow (veh/min)',color='#000000',range=[0,max_range],dtick=max_range/4,
                                           tickfont=dict(family='sans-serif',size=19,color='#000')),
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)',
                                   shapes= [
                                    # highlight first accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start1],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end1],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight second accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start2],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end2],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight third accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start3],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end3],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight fourth accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start4],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end4],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    }
                                ]
                              )
                fig = go.Figure(data=data, layout=layout)
                pio.write_image(fig, dirpath+'\\AccHappendLink\\flow\\images\\'+hop+'.png',width=1800, height=700)
                plotly.offline.plot(fig, filename=dirpath+'/AccHappendLink/flow/'+hop+'.html',auto_open=False)
                fichier_html_graphs.write("  <object data=\""+hop+'.html'+"\" width=\"1800\" height=\"400\" style=\"margin: 0px 0px\"></object>")
            else:
                print('Three Hop: '+hop+'File Not Found')
                fichier_html_graphs.write("  <object data='AccHappendLink/flow/FileNotFound.html' width=\"750\" height=\"400\">"+hop+"File Not Found</object>")
    #==========================================================================================



    #Plotting for four plot
    #==========================================================================================

    fichier_html_graphs.write("<h3>================================================Four Hop===============================================</h3> ")
    if len(fourHop)!=0:
        fourHopPlot=[]
        for hop in fourHop:

            dirpath = os.getcwd()
            withoutAccLocationPath=dirpath+'\\dataset\\NormalCase\\seed50_Correct_5min\\'+hop+'.csv'
            withAccLocationPath1=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1 close\\'+hop+'.csv'
            withAccLocationPath2=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2 close\\'+hop+'.csv'
            withAccLocationPath3=dirpath+'\\dataset\\AccidentCase\\LaneClosure\\L10130\\seed50_20min\\1,2,3 close\\'+hop+'.csv'



            if os.path.isfile(withoutAccLocationPath) and os.path.isfile(withAccLocationPath1)\
                    and os.path.isfile(withAccLocationPath2) and os.path.isfile(withAccLocationPath3):


                df = pd.read_csv(withoutAccLocationPath,names=names1, header=None,skiprows=1)
                df1 = pd.read_csv(withAccLocationPath1, names=names2, header=None,skiprows=1)
                df2 = pd.read_csv(withAccLocationPath2, names=names2, header=None,skiprows=1)
                df3 = pd.read_csv(withAccLocationPath3, names=names2, header=None,skiprows=1)


                trace0 = go.Scatter(x=df['Time'], y=df['Flow'], mode = 'lines',name='Normal Case',
                                     line = dict(color =  ('rgb(0, 0, 255)'),width = 2)
                                    )
                trace1 = go.Scatter(x=df1['Time'], y=df1['Flow'], mode = 'lines',name='One-Lane Closure',
                                     line = dict(color =  ('rgba(16, 112, 2, 0.8)'),width = 2)
                                    )
                trace2 = go.Scatter(x=df2['Time'], y=df2['Flow'], mode = 'lines',name='Two-Lane Closure',
                                     line = dict(color =  ('rgb(255, 0, 0)'),width = 2)
                                    )
                trace3 = go.Scatter(x=df3['Time'], y=df3['Flow'], mode = 'lines',name='Three-Lane Closure',
                                     line = dict(color =  ('rgba(80, 26, 80, 0.8)'),width = 2)
                                    )
                data = [trace0,trace1,trace2,trace3]
                if (0 <= df2['Flow'].astype(float).max() <= 200):
                    max_range = 200
                elif (200 < df2['Flow'].astype(float).max() <= 400):
                    max_range = 400
                elif (400 < df2['Flow'].astype(float).max() <= 800):
                    max_range = 800
                elif (df2['Flow'].astype(float).max() >= 800):
                    max_range = 900
                # Edit the layout
                layout = go.Layout(title = '<b>Edge '+hop+'</b>',
                              titlefont=dict(
                                family='Courier New, monospace',
                                size=22,
                                color='#000000'
                                ),
                                   legend=dict(traceorder='normal',
                                               font=dict(family='sans-serif', size=22, color='#000')),
                              xaxis = dict(title = 'Time (min)',tickangle=-45,color='#000000',
                                           tickfont=dict(family='sans-serif',size=19,color='#000'),tickmode = 'linear',dtick = 2),
                              yaxis = dict(title = 'Flow (veh/min)',color='#000000',range=[0,max_range],dtick=max_range/4,
                                           tickfont=dict(family='sans-serif',size=19,color='#000')),
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)',
                                   shapes= [
                                    # highlight first accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start1],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end1],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight second accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start2],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end2],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight third accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start3],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end3],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    },
                                  # highlight fourth accident interval
                                    {
                                        'type': 'rect',
                                        # x-reference is assigned to the x-values
                                        'xref': 'x',
                                        # y-reference is assigned to the plot paper [0,1]
                                        'yref': 'y',
                                        'x0': df1['Time'].loc[start4],
                                        'y0': 0,
                                        'x1': df1['Time'].loc[end4],
                                        'y1':max_range,
                                        'fillcolor': '#FF69B4',
                                        'opacity': 0.2,
                                        'line': {'width': 2,'dash':'dot'}
                                    }
                                ]
                              )
                fig = go.Figure(data=data, layout=layout)
                pio.write_image(fig, dirpath+'\\AccHappendLink\\flow\\images\\'+hop+'.png',width=1800, height=700)
                plotly.offline.plot(fig, filename=dirpath+'/AccHappendLink/flow/'+hop+'.html',auto_open=False)
                fichier_html_graphs.write("  <object data=\""+hop+'.html'+"\" width=\"1800\" height=\"400\" style=\"margin: 0px 0px\"></object>")
            else:
                print('Four Hop: '+hop+'File Not Found')
                fichier_html_graphs.write("  <object data='AccHappendLink/flow/FileNotFound.html' width=\"750\" height=\"400\">"+hop+"File Not Found</object>")
    #==========================================================================================


    fichier_html_graphs.write("</body></html>")
    print("CHECK YOUR DASHBOARD.html In the current directory")
    #========================================================================

#************************************************Controller********************************************************

if __name__=="__main__":
    accLink='L10130'
    duration=20
    #duration=15
    #duration=10
    upstreamList=findUpStream(accLink)
    showMeanSpeedForUpstream(accLink,upstreamList,duration)
    showFlowForUpstream(accLink,upstreamList,duration)



    downstreamList=findDownStream(accLink)
    showMeanSpeedForDownstream(accLink,downstreamList,duration)
    showFlowForDownstream(accLink,downstreamList,duration)


#*************************************************************************************************************