FROM --platform=linux/amd64 python:3.9-buster

COPY . /update_data

WORKDIR /update_data

RUN apt-get update && apt-get install -y cron && \
    pip install -r requirements.txt && \
    echo "0 0 */5 * * cd /update_data && python update_data.py && python push.py" > /etc/cron.d/update_data_cron && \
    chmod 0644 /etc/cron.d/update_data_cron && \
    crontab /etc/cron.d/update_data_cron

CMD cron -f
