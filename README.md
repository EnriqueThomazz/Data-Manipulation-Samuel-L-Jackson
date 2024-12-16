# Data-Manipulation-Samuel-L-Jackson
This project covers the creation of a small data lake with data from movies and series in wich Samuel L Jackson has participated.


# The data

The data in this repository covers all the series and movies that Samuel L. Jackson has participated. The data was acquired through the [TMDB API](https://developer.themoviedb.org/reference/intro/getting-started).

# Processing the data

I used jupyter notebooks to write [code](./Scripts/) in Python, using Spark and SQL.


# Architecture

The data is divided into three layers: Bronze, Silver and Gold. Bronze corresponds to the raw data, obtained directly from the TMDB API. The Silver Layer refines the data, removing duplicates and errors. Finally the Gold layer is where all the useful information is and where I created the [Star Schema model](./Gold/Star%20Schema%20Samuel.png).


# Data Visualization

Power BI was the tool chosen to visualize the processed data and create a single [dashboard](./DataViz%20PowerBI/samuel_dashboard_complete.pdf).
