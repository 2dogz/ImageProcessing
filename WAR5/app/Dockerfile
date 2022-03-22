FROM python:3.7

RUN apt-get update \
    && apt-get install -y \
        build-essential \
        cmake \
        git \
        wget \
        unzip \
        yasm \
        pkg-config \
        libswscale-dev \
        libffi-dev \
        libssl-dev \
        libtbb2 \
        libtbb-dev \
        libjpeg-dev \
        libpng-dev \
        libtiff-dev \
        libavformat-dev \
        libpq-dev \
        vim -y\
    && rm -rf /var/lib/apt/lists/*


RUN pip install numpy flask

RUN apt-get --fix-missing update && apt-get --fix-broken install

# Install OpenCV
COPY cv_install.sh cv_install.sh
RUN sed -i -e 's/\r$//' cv_install.sh
RUN chmod +x cv_install.sh
RUN ./cv_install.sh
ARG CACHEBUST=1
RUN git clone https://github.com/2dogz/ImageProcessing.git
ENTRYPOINT ["bash"]
#ENTRYPOINT ["python"]
WORKDIR "/ImageProcessing/WAR5/app"
#CMD ["app.py"]
