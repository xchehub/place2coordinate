#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import requests
import json
import os
from dotenv import load_dotenv

# load env variables
load_dotenv()

def get_coordinates(location_name):
    """
    Use Nominatim OpenStreetMap API to get place's coordinates
    a fress geo service, but some limitation
    """
    try:
        base_url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": location_name,
            "format": "json",
            "limit": 1,
        }
        
        headers = {
            "User-Agent": "LocationToCoordinates/1.0"  # for OpenStreetMap API, provide User-Agent info
        }
        
        response = requests.get(base_url, params=params, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            if data and len(data) > 0:
                lat = data[0]["lat"]
                lon = data[0]["lon"]
                display_name = data[0]["display_name"]
                return (float(lat), float(lon), display_name)
            else:
                return None
        else:
            print(f"API request error, status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"ERROR: {e}")
        return None

def main():
    """main function"""
    print("Convert place to coordinates")
    print("-" * 30)
    
    # check parameters in command line
    if len(sys.argv) > 1:
        location = " ".join(sys.argv[1:])
    else:
        # if no parameter, prompts to user
        location = input("please input place: ")
    
    if not location:
        print("ERROR：noe place name")
        return
    
    print(f"\nRequest '{location}' coordinates...")
    result = get_coordinates(location)
    
    if result:
        lat, lon, display_name = result
        print("\nResult:")
        print(f"Complete Address: {display_name}")
        print(f"latitude: {lat}")
        print(f"longitude: {lon}")
        print(f"Ccorordinate (latitude,longitude): {lat}, {lon}")
    else:
        print(f"\ncannot find '{location}' corordinate. please check place name.")

if __name__ == "__main__":
    main()
