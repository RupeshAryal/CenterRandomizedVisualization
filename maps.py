import folium
import pandas as pd
import numpy as np
import query


def plot_centers_maps(dataframe: pd.DataFrame):
    dataframe = dataframe.reset_index(drop=True)

    center_code = dataframe['cscode'][0]
    center_name = dataframe['center'][0]

    lat, lon = query.extract_lat_lon(center_code)

    # max_lat, max_lon = 30.904099607254718, 80.4816491612127
    # min_lat, min_lon = 26.1162751692073, 88.50605663476142

    max_lat, max_lon = 31, 81
    min_lat, min_lon = 27, 89

    maps = folium.Map(location=(lat, lon), zoom_start=15,
                      max_lat=max_lat,
                      min_lat=min_lat,
                      max_lon=max_lon,
                      min_lon=min_lon
                      )

    folium.Circle(location=(lat, lon), radius=50, fill_color='red', color='red', tooltip=center_name).add_to(maps)

    for index, value in dataframe.iterrows():
        scode = value['scode']
        school_name = query.extract_school_details(scode)
        school_lat, school_lon = query.extract_lat_lon(scode)
        folium.Circle(location=(school_lat, school_lon),
                      radius=50,
                      color='blue',
                      fill_color='blue',
                      tooltip=school_name
                      ).add_to(maps)

    return maps


def plot_schools_maps(dataframe: pd.DataFrame):
    dataframe = dataframe.reset_index(drop=True)

    school_name = dataframe['school'].iloc[0]
    school_code = query.get_schoolcode_by_name(school_name)

    lat, lon = query.extract_lat_lon(school_code)

    # max_lat, max_lon = 30.904099607254718, 80.4816491612127
    # min_lat, min_lon = 26.1162751692073, 88.50605663476142

    max_lat, max_lon = 31, 81
    min_lat, min_lon = 27, 89

    maps = folium.Map(location=(lat, lon), zoom_start=15,
                      max_lat=max_lat,
                      min_lat=min_lat,
                      max_lon=max_lon,
                      min_lon=min_lon
                      )

    folium.Circle(location=(lat, lon), radius=50, fill_color='red', color='red', tooltip=school_name).add_to(maps)

    for index, value in dataframe.iterrows():
        scode = value['cscode']
        center_name = query.extract_school_details(scode, "center")
        school_lat, school_lon = query.extract_lat_lon(scode)
        folium.Circle(location=(school_lat, school_lon),
                      radius=50,
                      color='blue',
                      fill_color='blue',
                      tooltip=center_name
                      ).add_to(maps)

    return maps
