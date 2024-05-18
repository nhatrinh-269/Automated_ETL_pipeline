import mysql.connector
from mysql.connector import Error
from datetime import datetime
import os
import pywt
import rasterio
import numpy as np
import json

def log(message, path):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now() 
    timestamp = now.strftime(timestamp_format)
    with open(path, "a") as f:
        f.write(timestamp + ',' + message + '\n')

def list_dir(path):
    try:
        if not os.path.exists(path):
            print("The path does not exist.")
            return
        if not os.path.isdir(path):
            print("The path is not a directory.")
            return
        files = os.listdir(path)
        return files
    
    except Exception as e:
        print("An error occurred:", e)

connection = mysql.connector.connect(
        user='USER', password='PASSWORD', host='mysql', port='3306', database='SATELLITE_DB'
    )

if connection.is_connected():
    cursor = connection.cursor()
    print("conneted")

path_save_tif = '/collection/image'
logfile = path_save_tif+ 'log.txt'

recent_day = sorted(list_dir(path_save_tif))[-1].split("-")

# Date range
year = recent_day[0]
start_month = recent_day[1]
end_month = datetime.now().month
start_date = recent_day[2]
end_date = datetime.now().day

log(f'Start insert satellite images to database', logfile)

# Loop through each day in the specified date range
for j in range(start_month, end_month + 1):
    if j < 10:
        month = f'0{j}'
    else:
        month = j
    for i in range(start_date, end_date + 1):
        if i < 10:
            day = f'0{i}'
        else:
            day = i
        start = f'{year}-{month}-{day}' 
        end = f'{year}-{month}-{day}'  
        path = f'{path}/{start}/'
        path_tiff = f"{path}/{list_dir(path)[-1]}/response.tiff"
        file_size = os.path.getsize(path_tiff)

        keep = 0.05
        w = 'db4'
        n = 3
        lat_1,long_1,lat_2,long_2 = "lat_1","long_1","lat_2","long_2"
        source = "sentinel_hub"
        bands = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B8A', 'B9', 'B10','B11', 'B12'] 

        location_data = (f"{lat_1}-{long_1}-{lat_2}-{long_2}",lat_1,long_1,lat_2,long_2) 
        location_query = "INSERT INTO location (id_loc,lat_1, lng_1, lat_2, lng_2) VALUES (%s,%s, %s, %s, %s)"
        cursor.execute(location_query, location_data)
        log("Inserted data into location table successfully", logfile)

        with rasterio.open(path_tiff) as src:
            all_bands = src.read()
            for band_index in range(all_bands.shape[0]):
                coeffs = pywt.wavedec2(all_bands[band_index], wavelet=w, level=n)
                coeff_arr, coeff_slices = pywt.coeffs_to_array(coeffs)
                break
        infor_images_data = (f"{lat_1}-{long_1}-{lat_2}-{long_2}-{start}",f"{lat_1}-{long_1}-{lat_2}-{long_2}",source, coeff_slices,start) 
        infor_images_query = "INSERT INTO infor_images (id_img,id_loc,source, date) VALUES (%s,%s,%s, %s)"
        cursor.execute(infor_images_query, infor_images_data)
        log("Inserted data into infor_images table successfully", logfile)

        if file_size > 400 * 1024:  
            #compression image before insert to database
            with rasterio.open(path_tiff) as src:
                all_bands = src.read()
                for band_index in range(all_bands.shape[0]):
                    coeffs = pywt.wavedec2(all_bands[band_index], wavelet=w, level=n)
                    coeff_arr, coeff_slices = pywt.coeffs_to_array(coeffs)
                    Csort = np.sort(np.abs(coeff_arr.reshape(-1)))
                    thresh = Csort[int(np.floor((1 - keep) * len(Csort)))]
                    ind = np.abs(coeff_arr) > thresh
                    Cfilt = coeff_arr * ind
                    
                    index = []
                    coeff_ = []
                    count = 0
                    
                    for i in range(Cfilt.shape[0]):
                        for j in range(Cfilt.shape[1]):
                            if Cfilt[i][j] != 0:
                                coeff_.append(Cfilt[i][j])
                                index.append(count)
                            count+=1
                            
                    matrix = np.zeros((Cfilt.shape[0],Cfilt.shape[1]), dtype=np.uint8)
                    matrix[np.unravel_index(index, (Cfilt.shape[0],Cfilt.shape[1]))] = 1

                    try:
                        codebook_json = json.dumps(coeff_)
                        codebook_data = (f"{lat_1}-{long_1}-{lat_2}-{long_2}-{start}",bands[band_index], codebook_json)  
                        codebook_query = "INSERT INTO codebooks (id_img, band, codebook) VALUES (%s, %s, %s)"
                        cursor.execute(codebook_query, codebook_data)
                        log("Inserted data into codebooks table successfully", logfile)

                        label_json = json.dumps(matrix)
                        label_data = (f"{lat_1}-{long_1}-{lat_2}-{long_2}-{start}",bands[band_index], label_json)
                        label_query = "INSERT INTO labels (id_img, band, label) VALUES (%s, %s, %s)"
                        cursor.execute(label_query, label_data)
                        log("Inserted data into labels table successfully", logfile)

                        connection.commit()

                    except Error as e:
                        log(f"Error: {e}", logfile)
                        print(f"Error: {e}")
        else:
            continue

log(f'finish insert satellite images to database', logfile)