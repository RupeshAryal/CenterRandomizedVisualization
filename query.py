import pandas as pd
import numpy as np

school_center = pd.read_table('dataset/school-center.tsv')
school_center_distance = pd.read_table('dataset/school-center-distance.tsv')
school_lat_long = pd.read_table('dataset/schools_lat_long_2081.tsv')


def extract_lat_lon(scode):
    """
    Takes school code(scode) and returns latitude and longitude values for the school
    """
    filt_ = school_lat_long[school_lat_long['scode'] == scode]
    lat, lon = filt_[['lat', 'long']].to_numpy()[0]
    return lat, lon


def extract_school_details(scode, school_type="school"):
    """
    Takes school code (scode) and returns school name
    """
    if school_type == 'center':
        filter_ = school_center[school_center['cscode'] == scode]['center'].reset_index(drop=True)[0]
        return filter_

    filter_ = school_center[school_center['scode'] == scode]['school'].reset_index(drop=True)[0]
    return filter_


def get_centers_by_location(center_address):
    """
    :param center_address: address of center
    :return: list of schools by address
    """
    centers_detail = school_center[school_center['center_address'] == center_address]['center']
    return list(centers_detail.unique())


def list_of_centers():
    """
    :return: list of all centers
    """
    a = list(school_center['center'].unique())
    return a


def list_of_schools():
    """
    :return: list of all the schools
    """
    a = list(school_center['school'].unique())
    return a


def center_colleges(center_name):
    data = school_center[school_center['center'] == center_name]
    return data


def schools_assigned_to_center(center_name):
    filt = school_center[['center', 'scode', 'school', 'center_address', 'allocation', 'distance_km']]
    return filt[filt['center'] == center_name]


def centers_assigned_to_school(school_name):
    school = school_center[school_center['school'] == school_name]
    return school[['school', 'center', 'cscode', 'allocation', 'distance_km']]


def get_schoolcode_by_name(school_name):
    school = school_center[school_center['school'] == school_name]
    return school['scode'].iloc[0]
