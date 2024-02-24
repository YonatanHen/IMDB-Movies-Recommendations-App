# Tondo-task

## Set Up Instructions:

- Python version: 3.11.6
- Pip version: 23.2.1

#### Create a Virtual Environment:

1. You may set up a virtual environment for this project using the command template below:

```
python3 -m venv <virtual env name>
```
2. Source the virtual environment:

```
source tondo-task/bin/activate
```

#### Required Packages Installation:

All of the requirements are saved under the requirements.txt file. You can install them as follows:

```
pip3 install -r requirements.txt
```

For your convenience, the requirements.txt content is as follows:
```
beautifulsoup4==4.12.3
bs4==0.0.2
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
iniconfig==2.0.0
numpy==1.26.4
packaging==23.2
pandas==2.2.0
pillow==10.2.0
pluggy==1.4.0
pytest==8.0.1
python-dateutil==2.8.2
pytz==2024.1
requests==2.31.0
six==1.16.0
soupsieve==2.5
tzdata==2024.1
urllib3==2.2.1
```

## Operating Instructions

Please run the project from the project's root folder using the command below:
```
python3 main.py
```

## Screenshots:

#### Scenario 1:
![image](https://github.com/YonatanHen/Tondo-task/assets/57364867/53346c46-5ba3-47af-97ee-1914458a9ed8)

![image](https://github.com/YonatanHen/Tondo-task/assets/57364867/9741cb02-9568-4829-842d-0de4db99c0f4)

![image](https://github.com/YonatanHen/Tondo-task/assets/57364867/7b32b8b5-4473-4d1f-a4dd-0061a9b1e221)

#### Scenario 2:
![image](https://github.com/YonatanHen/Tondo-task/assets/57364867/f2208474-d472-45aa-835e-d8ebc6c2aead)

![image](https://github.com/YonatanHen/Tondo-task/assets/57364867/47b4f216-dcc8-44ba-80d2-75880f2d4e03)

#### Scenario 3:
![image](https://github.com/YonatanHen/Tondo-task/assets/57364867/d247e3a0-05f0-4f9e-90c5-b01ad012d7d0)

![image](https://github.com/YonatanHen/Tondo-task/assets/57364867/658c1dac-d187-4ccc-a675-3eb07b91e883)

#### Scenario 4:
![image](https://github.com/YonatanHen/Tondo-task/assets/57364867/872552ff-fdc7-4fa4-a21a-90bd34420119)


## Side Notes:
- The Tkinter GUI works a little bit slow on my PC.
- This Project was built on MacOS (M1 processor)
- Please reach out to me if any clarifications are required or updates should be done in the project.
- The search is based on the following URL: https://www.imdb.com/search/title/?title_type=feature,tv_movie (returns only the movies as this is a movie recommendations app)
