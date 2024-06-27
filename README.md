# datadog-sensors
DataDog plugin to report sensors metrics

## Instructions
* Install lm-sensors
```sh
sudo apt install lm-sensors 
```

* Detect sensors
```sh
sudo sensors-detect
```
(Save the file at the end)

* Install PySensors
```sh
/opt/datadog-agent/embedded/bin/pip install PySensors
```
* Copy over the custom check and check config file to the DataDog agent install directory   
```sh
cp custom_sensors.yaml /etc/datadog-agent/conf.d/
cp custom_sensors.py /etc/datadog-agent/checks.d/
```

* Restart the Datadog agent
```sh
sudo systemctl restart datadog-agent
```
