FROM python:3.7

# RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 04EE7237B7D453EC 648ACFD622F3D138
# RUN echo 'deb http://httpredir.debian.org/debian buster-backports main contrib non-free' | tee -a /etc/apt/sources.list.d/debian-backports.list
# RUN apt update && sudo apt upgrade -y
# RUN apt install libseccomp2 -t buster-backports


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
        libtbb2 \
        libtbb-dev \
        libjpeg-dev \
        libpng-dev \
        libtiff-dev \
        libavformat-dev \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install numpy flask

RUN apt-get --fix-missing update && apt-get --fix-broken install

# Install OpenCV
COPY cv_install.sh cv_install.sh
RUN sed -i -e 's/\r$//' cv_install.sh
RUN chmod +x cv_install.sh
RUN ./cv_install.sh
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
