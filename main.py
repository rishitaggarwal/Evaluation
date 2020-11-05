import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import pandas
import csv

df = pandas.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()
std1 = statistics.stdev(data)
mean1 = statistics.mean(data)
print("The standard deviation for Student Marks is :",std1)
print("The mean for Student Marks is :",mean1)

def RandomSetOfMean(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value  = data[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean
mean_list = []
for i in range(0,1000):
    setOfmeans = RandomSetOfMean(100)
    mean_list.append(setOfmeans)

standardDeviation = statistics.stdev(mean_list)

firstStStart,firstStEnd = mean1-standardDeviation,mean1+standardDeviation
secondStStart,secondStEnd = mean1-(standardDeviation*2),mean1+(standardDeviation*2)
thirdStStart,thirdStEnd = mean1-(standardDeviation*3),mean1+(standardDeviation*3)

fig = ff.create_distplot([mean_list],["studentMarks"],show_hist= False)
fig.add_trace(go.Scatter(x = [mean1,mean1],y = [0,0.17],mode = "lines",name ="mean"))
fig.add_trace(go.Scatter(x = [firstStStart,firstStStart],y = [0,0.17],mode = "lines",name ="std1start"))
fig.add_trace(go.Scatter(x = [secondStStart,secondStStart],y = [0,0.17],mode = "lines",name ="std2start"))
fig.add_trace(go.Scatter(x = [thirdStStart,thirdStStart],y = [0,0.17],mode = "lines",name ="std3start"))
fig.add_trace(go.Scatter(x = [firstStEnd,firstStEnd],y = [0,0.17],mode = "lines",name ="firstStEnd"))
fig.add_trace(go.Scatter(x = [secondStEnd,secondStEnd],y = [0,0.17],mode = "lines",name ="secondStEnd"))
fig.add_trace(go.Scatter(x = [thirdStEnd,thirdStEnd],y = [0,0.17],mode = "lines",name ="thirdStEnd"))

fig.show()


