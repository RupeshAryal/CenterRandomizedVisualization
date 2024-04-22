import folium
import query
from streamlit_folium import st_folium
import streamlit as st
import maps

st.set_page_config(layout="centered")

# title of the dashboard
st.title("Center Randomized Visualization")
visual_type = st.radio("View Data BY:", options=("school", "center"))

# If school is selected from the radio
if visual_type == "school":
    list_of_school = query.list_of_schools()
    selected_school = st.selectbox("School Name", options=list_of_school)

    df = query.centers_assigned_to_school(selected_school)

    # st.subheader(f':red[{selected_school}]')

    total_students = df['allocation'].sum()
    average_distance = df['distance_km'].mean()

    map_column, data_column = st.columns(2)

    # plot map in first column
    with map_column:
        my_map = maps.plot_schools_maps(df)
        st_folium(my_map, use_container_width=True, height=300)

    # fill metrics and data in second column
    with data_column:

        metric1, metric2, metric3 = st.columns(3)

        # Displays the descriptive statistics

        with metric1:
            st.metric("total_students", total_students)

        with metric2:
            st.metric("No of centers", len(df))

        with metric3:
            st.metric("Average Distance", average_distance.round(2))

        # Display center information for colleges in a table

        df1 = df[['cscode', 'allocation', 'distance_km']].reset_index(drop=True)
        df1.rename(columns={'cscode': 'code',
                            'allocation': 'number of students',
                            'distance_km': 'distance'},
                   inplace=True)
        st.dataframe(df1)

# if center is selected from radio
else:
    list_of_school = query.list_of_centers()
    selected_school = st.selectbox("Center Namer", options=list_of_school)

    df = query.center_colleges(selected_school)

    # Display center information for colleges in a table

    stat_data = df[['scode', 'allocation', 'distance_km']].reset_index(drop=True)
    stat_data.rename(columns={'scode': 'code',
                              'allocation': 'number of students',
                              'distance_km': 'distance'},
                     inplace=True)

    total_students = stat_data['number of students'].sum()
    average_distance = stat_data['distance'].mean()

    mapcolumn, datacolumn = st.columns(2)
    with mapcolumn:
        my_map = maps.plot_centers_maps(df)
        st_data = st_folium(my_map, use_container_width=True, height=300)

    with datacolumn:
        metric1, metric2, metric3 = st.columns(3)

        with metric1:
            st.metric("total_students", total_students)

        with metric2:
            st.metric("No of centers", len(df))

        with metric3:
            st.metric("Average Distance", average_distance.round(2))

        st.dataframe(stat_data)
