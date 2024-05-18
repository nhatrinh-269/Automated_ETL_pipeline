import mysql.connector
from mysql.connector import Error
from datetime import datetime
import os

# Log messages with timestamps
def log(message, path):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now() 
    timestamp = now.strftime(timestamp_format)
    with open(path, "a") as f:
        f.write(timestamp + ',' + message + '\n')

logfile = '/collection/image/log.txt'

connection = mysql.connector.connect(
        user='USER', password='PASSWORD', host='mysql', port='3306', database='SATELLITE_DB'
    )

if connection.is_connected():
    cursor = connection.cursor()
    print("conneted")

try: 
    location_table = """
        CREATE TABLE location (
            id_loc VARCHAR PRIMARY KEY,
            lat_1 DECIMAL(9, 10),
            lng_1 DECIMAL(9, 10),
            lat_2 DECIMAL(9, 10),
            lng_2 DECIMAL(9, 10),
        );
        """
    cursor.execute(location_table)
    log("created table Location successfully",logfile)

    infor_images_table = """
        CREATE TABLE infor_images (
            id_img VARCHAR PRIMARY KEY,
            id_loc VARCHAR,
            source VARCHAR(255),
            coeff_img JSON,
            date DATE,
            FOREIGN KEY (id_loc) REFERENCES location(id_loc)
        );
        """
    cursor.execute(infor_images_table)
    log("created table Infor_image successfully",logfile)

    codebooks_table = """
        CREATE TABLE codebooks (
            id_codebook INT AUTO_INCREMENT PRIMARY KEY,
            id_img INT,
            band VARCHAR(50),
            codebook JSON,
            FOREIGN KEY (id_img) REFERENCES infor_images(id_img)
        );
        """
    cursor.execute(codebooks_table)
    log("created table Codebooks successfully",logfile)

    labels_table = """
        CREATE TABLE labels (
            id_label INT AUTO_INCREMENT PRIMARY KEY,
            id_img INT,
            band VARCHAR(50),
            label JSON,
            FOREIGN KEY (id_img) REFERENCES infor_images(id_img)
        );
        """
    cursor.execute(labels_table)
    log("created table Labels successfully",logfile)

    cursor.close()

except Error as e:
    log(f"{e}",logfile)
    print(f"{e}")