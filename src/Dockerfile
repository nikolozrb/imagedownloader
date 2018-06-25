FROM python:3.6.4
# update os-libs
RUN apt-get update && apt-get install -y gcc g++

# install python packages
RUN pip install flask
RUN apt-get -qq update && apt-get install python3-dev git  -y
RUN pip install pycurl

# Bundle app source
RUN mkdir /src/
ADD ./ /src/
# port
EXPOSE 5000

# set workdir
WORKDIR /src

# start python program
CMD ["python", "main.py"]

