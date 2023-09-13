from flask import Flask, request, make_response, send_from_directory, jsonify
from flask import render_template
from datetime import datetime, timezone, timedelta
from werkzeug.utils import secure_filename
from flask import send_from_directory
import requests
from requests import Response
import os
import json

app = Flask(__name__)

@app.after_request
def add_header(response):
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, public, max-age=0'
    return response


@app.route('/img/<path:filename>')
def send_img(filename):
    response = make_response(send_from_directory(app.static_folder, filename))
    response.headers['Cache-Control'] = 'public, max-age=86400'
    return response

@app.route("/")
def index()-> str:    
    return render_template('home.html')

@app.route("/view2")
def newview()-> str:    
    return render_template('home2.html')
    
@app.route("/api")
def api()-> str:
    # 楼下公交站 编号 43431
    lta_api_response_downstairs_985_176 = get_next_bus_info('43431')
    downstairs_985 = filter_bus_route_from_api_response(lta_api_response_downstairs_985_176, '985')
    downstairs_176 = filter_bus_route_from_api_response(lta_api_response_downstairs_985_176, '176')
    # 楼下街对面公交站 编号 43439
    lta_api_response_downstairs_opp_985_176 = get_next_bus_info('43439')
    downstairs_opp_985 = filter_bus_route_from_api_response(lta_api_response_downstairs_opp_985_176, '985')
    downstairs_opp_176 = filter_bus_route_from_api_response(lta_api_response_downstairs_opp_985_176, '176')
    # 小区大门公交站 编号 43549
    lta_api_response_downstairs_945 = get_next_bus_info('43549')
    downstairs_945 = filter_bus_route_from_api_response(lta_api_response_downstairs_945, '945')
    # 九六三 编号 43161
    lta_api_response_963 = get_next_bus_info('43161')
    bus_963 = filter_bus_route_from_api_response(lta_api_response_963, '963')
    
    return jsonify(
        downstairs_985=downstairs_985,
        downstairs_176=downstairs_176,
        downstairs_opp_985=downstairs_opp_985,
        downstairs_opp_176=downstairs_opp_176,
        downstairs_945=downstairs_945,
        bus_963=bus_963
    )

@app.route("/api2")
def api2()-> str:
    # 楼下公交站 编号 43431
    lta_api_response_downstairs_985_176 = get_next_bus_info('43431')
    downstairs_985 = filter_bus_route_from_api_response2(lta_api_response_downstairs_985_176, '985')
    downstairs_176 = filter_bus_route_from_api_response2(lta_api_response_downstairs_985_176, '176')
    # 楼下街对面公交站 编号 43439
    lta_api_response_downstairs_opp_985_176 = get_next_bus_info('43439')
    downstairs_opp_985 = filter_bus_route_from_api_response2(lta_api_response_downstairs_opp_985_176, '985')
    downstairs_opp_176 = filter_bus_route_from_api_response2(lta_api_response_downstairs_opp_985_176, '176')
    # 小区大门公交站 编号 43549
    lta_api_response_downstairs_945 = get_next_bus_info('43549')
    downstairs_945 = filter_bus_route_from_api_response2(lta_api_response_downstairs_945, '945')
    # 九六三 编号 43161
    lta_api_response_963 = get_next_bus_info('43161')
    bus_963 = filter_bus_route_from_api_response2(lta_api_response_963, '963')
    
    #获取天气预报
    weather = getweather('Bukit Batok')
    
    return jsonify(
        downstairs_985=downstairs_985,
        downstairs_176=downstairs_176,
        downstairs_opp_985=downstairs_opp_985,
        downstairs_opp_176=downstairs_opp_176,
        downstairs_945=downstairs_945,
        bus_963=bus_963,
        weather=weather
    )
    
def filter_bus_route_from_api_response(api_response, ServiceNo):
    services = [[service['NextBus'].get('EstimatedArrival') if service.get('NextBus') else None,
            service['NextBus2'].get('EstimatedArrival') if service.get('NextBus2') else None,
            service['NextBus3'].get('EstimatedArrival') if service.get('NextBus3') else None] for service in api_response['Services'] if service['ServiceNo'] == ServiceNo]
    if services:
        services = services[0]
        new_services = []
        for item in services:
            try:
                new_item = datetime.strptime(item, '%Y-%m-%dT%H:%M:%S%z') - datetime.now(timezone.utc)
                minutes, seconds = divmod(new_item.total_seconds(), 60)
                new_item = f"{int(minutes)}"
                new_services.append(new_item)
            except:
                new_item = ''
        services = new_services
    else:
        services = []
    return services
    
def filter_bus_route_from_api_response2(api_response, ServiceNo):
    services = [[service['NextBus'].get('EstimatedArrival') if service.get('NextBus') else None,
            service['NextBus2'].get('EstimatedArrival') if service.get('NextBus2') else None,
            service['NextBus3'].get('EstimatedArrival') if service.get('NextBus3') else None] for service in api_response['Services'] if service['ServiceNo'] == ServiceNo]
    if services:
        services = services[0]
        new_services = []
        for item in services:
            try:
                new_item = datetime.strptime(item, '%Y-%m-%dT%H:%M:%S%z')
                new_services.append(item)
            except:
                new_item = ''
        services = new_services
    else:
        services = []
    return services
    
def get_next_bus_info(bus_stop_code):
    api_key = os.getenv('api_key')

    if not api_key:
        raise ValueError("Apikey not set in the environment variables.")

    # 构建URL
    url = f"http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode={bus_stop_code}"
    headers = {'AccountKey': api_key, 'Cache-Control': 'no-cache', "Pragma": "no-cache"}
    # 发送GET请求
    lta_api_response = requests.get(url, headers=headers)

    # 如果请求成功，解析JSON并返回，否则抛出异常
    if lta_api_response.status_code == 200:
        print("API Request successful")
        return lta_api_response.json()
    else:
        lta_api_response.raise_for_status()
        
def getweather(region_name):
    url = "https://api.data.gov.sg/v1/environment/2-hour-weather-forecast"
    try:
        weather_forcast_response = requests.get(url)
        response_json = weather_forcast_response.json()
        forecasts = response_json["items"][0]["forecasts"]
        weather_forcast = next((item["forecast"] for item in forecasts if item["area"] == region_name), "Get data, but region not found")
        return weather_forcast
    except:
        return "no weather data"
    