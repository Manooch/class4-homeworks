FROM python:3.7.2
MAINTAINER Kian

WORKDIR ./

COPY cct_parser_Boston.py .

COPY housing.data.txt .

RUN apt-get update && apt-get install -y python3-pip

#ENTRYPOINT ["cct_parser_Boston.py","housing.data.txt"]

CMD ["python", "cct_parser_Boston.py"]

#RUN apt-get install -y python3-pip

#
#  CHECK!  Install: python3 instead of python2 (if its not 3 already)
#  Install: pip (python package installer) for the corresponding Python 3,
#  Use pip to install: numpy, pandas 
#
