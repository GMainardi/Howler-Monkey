# Change to prebuild container
FROM ultralytics/ultralytics

RUN sudo apt-get update && sudo apt-get upgrade -y
RUN sudo apt-get install -y libgl1-mesa-glx

COPY ./requirements.txt .

RUN pip install -r requirements.txt