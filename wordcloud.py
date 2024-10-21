from wordcloud import WordCloud, STOPWORDS
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


from matplotlib.pyplot import figure

from pandas import read_csv, DataFrame

# Load alternative dataset
import psycopg2
from psycopg2.extras import RealDictCursor

mov = psycopg2.connect(dbname='mov_db', user='app', host='192.168.3.44', port='5432', password='postgres')

mdr_memo = "select memo from company.mdr"
complaint_memo = "select memo from patients.complaint"
dia = "select d_name from patients.p2d"

def getData(connection, query):
    cur = connection.cursor(cursor_factory = RealDictCursor)
    cur.execute(query)
    data = cur.fetchall()
    connection.commit()
    cur.close()
    del cur
    return data

dataset = DataFrame(getData(mov, mdr_memo))

text = str(dataset)
# skip following words
nichtinteressant = "und waren memo v d wg columns d_name rows x Ayko links rechts"
liste_der_unerwuenschten_woerter = nichtinteressant.split()

STOPWORDS.update(liste_der_unerwuenschten_woerter)

wordcloud = WordCloud(background_color="white").generate(text)

import matplotlib.pyplot as plt
#plt.rcParams['figure.figsize'] = [16, 12]
plt.rcParams['figure.dpi'] = 300


plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")

#figure(figsize=(100, 75), dpi=300)

plt.show()
