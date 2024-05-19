# Automated ETL Pipeline

## Overview

**Automated ETL Pipeline** is an automated system designed to minimize the time and effort required for collecting, processing, storing, and updating **multispectral satellite images**. This project focuses on automating the **ETL** (Extract, Transform, Load) process and **automatic updates** to ensure the **quality** and **accuracy** of the data in the system, this Pipeline has brought significant benefits to projects related to satellite images. Key features of the system include the ability to **automatically collect images** from the **Sentinel Hub**. The images are then efficiently processed to normalize, compress and save to the database. Another important feature of the pipeline is the ability to **automatically update** new satellite images after a certain period of time. This ensures that the system always maintains the latest and most accurate data, without the need for manual intervention. To enhance the automation of the system, we deploy the project on **Docker**. Using Docker simplifies **deployment** and **management**, and better facilitates building a flexible and stable automated pipeline. Overall, Automated ETL Pipeline is an efficient and flexible solution for multispectral satellite imagery management. By automating the process from collection to processing and updating, this pipeline brings convenience and reliability to projects involving satellite imagery data.

### **Key Features:**

- **Automated Data Collection:** The system automatically collects **multispectral satellite images** along a **time series** from the **Sentinel Hub API**.
  
- **Efficient Processing:** Multispectral images are processed using **Discrete Wavelet Transform** to compress them into **labels** and **codebooks**, reducing storage requirements.

- **Centralized Storage:** We have built a **MySQL** database to **store** multispectral satellite image data.

- **Automatic Updates:** Data is **automatically updated** at specified intervals to ensure that the system maintains the latest data.

### **Deployment on Docker:** 
- This project is deployed on **Docker** to enhance the automation of the Pipeline and reduce dependency on the environment.

With the Automated Satellite Image ETL Pipeline, we aim to provide an efficient and flexible solution for managing multispectral satellite images in projects related to geographic and environmental data.

## System Requirements
- **Docker 25.0.5**
- **Docker-compose 2.27.0**
## Required Skills
- **Python**
- **Docker**
- **MySQL**
- **Discrete Wavelet Transform**
- **ETL**
- **Pipeline**
  
## Project Structure
```
.
├── SATELLITE_IMAGE
│   ├── multispectral_satellite_images.tiff
│   └── log.txt
├── Collection
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── collection_image.py
│   ├── create_table.py
│   └── push.py
├── update_data
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── update_data.py
│   └── push.py
├── jupyter_notebook
│   ├── Dockerfile
│   └── requirements.txt
├── work
│   └── Example.ipynb
├── docker-compose.yml
└── README.md
```
giải thích dưới đây
