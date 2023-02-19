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