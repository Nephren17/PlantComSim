import numpy as np

def simulate_tropical_savanna_climate_daily():
    # 设置参数
    num_days = 360
    temp_range_rainy = 8
    temp_range_dry = 15
    temp_mean_rainy = 27
    temp_mean_dry = 22
    temp_amplitude = 5
    rain_amplitude = 30
    dry_start_day = 91  # 4月1日是第91天
    dry_end_day = 273  # 9月30日是第273天
    
    # 计算每天的平均气温和昼夜温差
    temp = np.zeros(num_days)
    diurnal_temp_range = np.zeros(num_days)
    for i in range(num_days):
        if i >= dry_start_day and i <= dry_end_day:  # 旱季
            temp[i] = np.random.normal(temp_mean_dry, temp_range_dry / 2)
            diurnal_temp_range[i] = np.random.normal(temp_amplitude, temp_amplitude / 4)
        else:  # 雨季
            temp[i] = np.random.normal(temp_mean_rainy, temp_range_rainy / 2)
            diurnal_temp_range[i] = np.random.normal(temp_amplitude / 2, temp_amplitude / 8)
            
    # 计算每天的降水量
    rain = np.zeros(num_days)
    for i in range(num_days):
        if i >= dry_start_day and i <= dry_end_day:  # 旱季
            rain[i] = np.random.normal(0, rain_amplitude / 2)
        else:  # 雨季
            rain[i] = np.random.normal(rain_amplitude, rain_amplitude / 4)
            if rain[i] < 0:
                rain[i] = 0
                
    return temp, rain, diurnal_temp_range

def simulate_temperate_grassland_climate_daily():
    # 定义一年中每月的天数
    days_per_month = [30] * 12
    
    # 定义一年中每月的平均气温，单位：摄氏度
    monthly_avg_temps = [5, 6, 10, 15, 20, 25, 28, 27, 23, 16, 10, 6]
    
    # 定义一年中每月的降水量，单位：毫米
    monthly_precipitations = [20, 20, 30, 50, 75, 90, 110, 90, 60, 50, 30, 20]
    
    # 定义一年中每月的白天平均温度和夜晚平均温度之差，单位：摄氏度
    monthly_day_night_temperature_diffs = [15, 13, 11, 9, 7, 5, 5, 6, 7, 9, 12, 14]
    
    # 定义每天的平均气温，降水量和昼夜温差
    daily_avg_temps = []
    daily_precipitations = []
    daily_day_night_temperature_diffs = []
    
    # 循环遍历每个月
    for i in range(12):
        # 计算当前月份的每天平均气温，单位：摄氏度
        daily_temps = np.random.normal(loc=monthly_avg_temps[i], scale=2.0, size=days_per_month[i])
        daily_avg_temps.extend(daily_temps)
        
        # 计算当前月份的每天降水量，单位：毫米
        daily_precips = np.random.normal(loc=monthly_precipitations[i], scale=5.0, size=days_per_month[i])
        daily_precipitations.extend(daily_precips)
        
        # 计算当前月份的每天昼夜温差，单位：摄氏度
        daily_day_night_temps = np.random.normal(loc=monthly_day_night_temperature_diffs[i], scale=1.0, size=days_per_month[i])
        daily_day_night_temperature_diffs.extend(daily_day_night_temps)
        
    return daily_avg_temps, daily_precipitations, daily_day_night_temperature_diffs

