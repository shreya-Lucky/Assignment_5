# Week 7 - Data Aggregation

#   Set imports
import pandas as pd
from sqlalchemy import create_engine
import pymysql

#   Create engine and connect
engine = create_engine('mysql+pymysql://anfro:hello@localhost/vgsales_db')
conn = engine.connect()

#   Read SQL into a DataFrame
frame = pd.read_sql("SELECT * FROM vgsales_2016;", conn)

pd.set_option('display.max_columns', 500)


# Set up 2 data sets
new_frame = frame[frame["Publisher"]=="Tecmo Koei"]
df2 = frame[frame["Publisher"] == "Nintendo"]

# Example of an append
combined_df = df2.append(new_frame)

#=====================

# Example of a concat
combined_df = pd.concat([df2,new_frame], axis=0)

# ===================

#  WHERE in python
action_df = frame[frame["Genre"]== "Action"]

# =======================

#   GROUP BY in PYTHON
df_platform_genre = frame.groupby(["Platform", "Genre"])["NA_Sales"].sum().reset_index()

# =======================
#   TEMPLATE FORMULA: df.loc[(condition), new_column_name] = value

#   Apply a CASE to your DF
df_genre_action.loc[(df_genre_action["NA_Sales"] > 100), "Status"] = "Popular"
df_genre_action.loc[(df_genre_action["NA_Sales"] < 100), "Status"] = "Okay"
df_genre_action.loc[(df_genre_action["NA_Sales"] < 20), "Status"] = "Not Popular"
