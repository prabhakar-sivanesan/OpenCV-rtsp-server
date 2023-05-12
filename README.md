# RTSP streaming using GStreamer
==================================

Modify by: Heru-sp

Date: 2023/05/12

Title project: Python implementation to stream camera feed from OpenCV videoCapture via RTSP server using GStreamer 1.0.

## Installation

This implementation has been developed and tested on Ubuntu 20.04. So the installation steps are specific to debian based linux distros.

### Step-1 Install GStreamer-1.0 and related plugins

```commandline
   $ sudo apt-get install gstreamer1.0-tools gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav
```

### Step-2 Install RTSP server
```commandline
    $ sudo apt-get update

    $ sudo apt-get install gstreamer1.0-tools gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly libgstrtspserver-1.0-dev
```

### Requirement
Python 3.10

```commandline
    $ pip install opencv-python 

    $ sudo apt install libcairo2-dev libxt-dev libgirepository1.0-dev

    $ pip install pycairo PyGObject
```

### Usage
> Run stream.py with required arguments to start the rtsp server


##### Sample
```commandline

    $ python stream.py --device_id 0 --fps 30 --image_width 640 --image_height 480 --port 8554 --stream_uri /video_stream
    
```
### Visualization

- You can view the video feed on `rtsp://server-ip-address:8554/stream_uri`

    e.g: `rtsp://192.168.103.75:8554/video_stream`

- You can either use any video player which supports rtsp streaming like VLC player or you can use the `open-rtsp.py` script to view the video feed.

