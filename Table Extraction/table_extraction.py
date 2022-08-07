import pandas as pd  # html and csv
import camelot

# Read a html table from url
simpsons = pd.read_html(
    "https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)"
)
print(simpsons[1])

# Read a csv table from url
premier21 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/E0.csv")
print(premier21)
# Rename columns
premier21.rename(columns={"FTHG": "home_goals", "FTAG": "away_goals"}, inplace=True)
print(premier21)

# Read a table from a pdf
tables = camelot.read_pdf("foo.pdf", pages="1")
print(tables)  # n=1
# Export table(s) to a csv
tables.export("foo.csv", f="csv", compress=True)
tables[0].to_csv("foo.csv")  # there is only one table
