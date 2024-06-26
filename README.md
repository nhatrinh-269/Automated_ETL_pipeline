# Automated ETL Pipeline

## Overview

**Automated ETL Pipeline** is an automated system designed to minimize the time and effort required for collecting, processing, storing, and updating **multispectral satellite images**. This project focuses on automating the **ETL** (Extract, Transform, Load) process and **automatic updates** to ensure the **quality** and **accuracy** of the data in the system, this Pipeline has brought significant benefits to projects related to satellite images. Key features of the system include the ability to **automatically collect images** from the **Sentinel Hub**. In our project, the amount of data collected in a day can be up to more than **11000** satellite images a day, equivalent to about **18gb**, so the images need to be processed effectively to standardize, compress and save. Another important feature of the pipeline is the ability to **automatically update** new satellite images after a certain period of time. This ensures that the system always maintains the latest and most accurate data, without the need for manual intervention. To enhance the automation of the system, we deploy the project on **Docker**. Using Docker simplifies **deployment** and **management**, and better facilitates building a flexible and stable automated pipeline. Overall, Automated ETL Pipeline is an efficient and flexible solution for multispectral satellite imagery management. By automating the process from collection to processing and updating, this pipeline brings convenience and reliability to projects involving satellite imagery data.

### **Key Features:**

- **Automated Data Collection:** The system automatically collects **multispectral satellite images** along a **time series** from the **Sentinel Hub API**.
  
- **Efficient Processing:** Multispectral images are processed using **Discrete Wavelet Transform** to compress them into **labels** and **codebooks**, reducing storage requirements.

- **Centralized Storage:** We have built a **MySQL** database to **store** multispectral satellite image data.

- **Automatic Updates:** Data is **updated automatically** at specified intervals using **Cron jobs** in **Docker containers**, data updates happen automatically and regularly, keeping the system in sync with **the latest satellite images**.


### **Deployment on Docker:** 
- This project is deployed on **Docker** to enhance the automation of the Pipeline and reduce dependency on the environment.

With the Automated Satellite Image ETL Pipeline, we aim to provide an efficient and flexible solution for managing multispectral satellite images in projects related to geographic and environmental data.

## System Requirements
- **Docker 25.0.5** [here](https://docs.docker.com/get-docker/).
- **Docker-compose 2.27.0** [here]( https://docs.docker.com/compose/).
## Required Skills
- **Python**
- **Docker**
- **MySQL**
- **Discrete Wavelet Transform**
- **ETL**
- **Pipeline**

## Installation Instructions
1. **Install Docker and Docker Compose:**
   - Download and install Docker from [here]( https://docs.docker.com/compose/install/).
   - Download and install Docker Compose from [here](https://docs.docker.com/compose/install/).

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/nhatrinh-269/Automated_ETL_pipeline
   cd Automated_ETL_pipeline
   ```

### Usage Instructions
- **Build and Run Docker Compose:**
   ```bash
   docker-compose up --build
   ```
- **Manage Containers:**
  ```bash
  docker-compose exec -it id_container bash
  ```
  
- **MySQL:**
  ```bash
  docker-compose exec -it id_container mysql -uroot - p
  ```
- **Accessing Jupyter Notebook:**
   - Visiting `http://<hostname>:port/?token=<token>` in a browser loads JupyterLab.

## Project Structure
```
.
├── SATELLITE_IMAGE
│   ├── multispectral_satellite_images.tiff
│   └── log.txt
├── collection
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
### **Explanation**

The project is organized into multiple folders and files, each serving a specific purpose in the ETL process and its automation:

- **SATELLITE_IMAGE/**: Contains collected multispectral satellite images and log files to track activities.
    - `multispectral_stellite_images.tiff`: satellite images.
    - `log.txt`: Log file records details of data collection and updates.

- **collection/**: Focuses on the initial data collection phase.
    - `Dockerfile`: Instructions for building a Docker image for the collection service.
    - `requirements.txt`: Required dependencies for the collection service.
    - `collection_image.py`: Script to collect images from the Sentinel Hub API.
    - `create_table.py`: Script to create necessary tables in MySQL database.
    - `push.py`: Script to push collected data into the database.

- **update_data/**: Handles automatic data updates at specified intervals.
    - `Dockerfile`: Instructions for building Docker images for the automatic update service.
    - `requirements.txt`: Required dependencies for the update service.
    - `update_data.py`: Script to update new satellite images after a period of time.
    - `push.py`: Script that pushes updated data to the database.

- **jupyter_notebook/**: Provides an environment for analysis and testing.
    - `Dockerfile`: Instructions for building Docker images for the Jupyter Notebook service.
    - `requirements.txt`: Dependencies are required to run Jupyter Notebook.

- **work/**: Directory containing work files.
    - `Example.ipynb`: A Jupyter Notebook example that illustrates how to use the data.

- **docker-compose.yml**: Configuration file to orchestrate multiple Docker containers needed for the project.

- **README.md**: Provides general information and instructions for setting up and using the project.

  
### **Sentinel Hub OAuth Credentials**

To access the Sentinel Hub API, you need to set up your OAuth credentials. Follow these steps to configure your client ID and client secret:

1. **Obtain OAuth Credentials:**
   - Register on the [Sentinel Hub](https://www.sentinel-hub.com/) platform.
   - Create a new OAuth client in your Sentinel Hub dashboard.
   - Note down your client ID and client secret.

2. **Reference the Environment Variables in Your Code:**
   - Ensure your scripts reference these environment variables when making API calls. For example, in `collection_image.py`:
     ```python
     from sentinelhub import SHConfig

     config = SHConfig()
     config.sh_client_id = client_id  # Set OAuth client ID
     config.sh_client_secret = client_secret  # Set OAuth client secret

     # Use the config object in your API requests
     ```

By following these steps, you'll ensure that your application can authenticate and access the Sentinel Hub API using your OAuth credentials.
## Summary
By building an automated process, we hope to reduce the time and effort in managing the collection, processing, and updating of multispectral satellite images. Helps researchers easily exploit and use them to build machine learning models.
### **Potential**
1. **Cloud Deployment:** This project would be better deployed in the cloud to ensure Docker is always running.
2. **New Application Development:** The project provides a flexible platform to develop new applications based on multispectral satellite data.
3. **Research and Learning:** The project can be used as a resource and platform for research and learning activities in the fields of data science, artificial intelligence, and data processing. image management.

### **Limitations**
1. **Internet Connection:** Persistent Internet connection is required to fetch satellite images from Sentinel Hub API. Interruptions in internet access may disrupt data collection.
2. **Resource consumption:** Because satellite images collected over time series and in many different locations will create huge data. Therefore, applying a distributed data structure can further improve the storage and access process.
3. **Search tool:** In this project, the part to search an image by coordinates has not been built yet. To fix this, users can use a hash function to define each key of the image. Thereby improving the speed of searching images in the database.

## Contribution
If you want to contribute to this project, please contact me via email `nhatrinh.26902@gmail.com`

## License

This project is licensed under the MIT License - see file [LICENSE](LICENSE) for details.

---

Feel free to further customize according to your project's specific requirements.
