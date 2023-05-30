import pandas as pd
import plotly.express as px

data = pd.read_csv('r3z1.csv')

# построение гистограмы для столбца X
histogram = px.histogram(data, x='X')
histogram.show()


# построение круговой диаграммы
area = px.pie(data, values='X')
area.show()
