# RTSP streaming using GStreamer

Python implementation to stream camera feed from OpenCV videoCapture via RTSP server using GStreamer 1.0.

## Installation

This implementation has been developed and tested on Ubuntu 16.04 and 18.04. So the installation steps are specific to debian based linux distros.

### Step-1 Install GStreamer-1.0 and related plugins
    sudo apt-get install libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
### Step-2 Install RTSP server
    sudo apt-get install libglib2.0-dev libgstrtspserver-1.0-dev gstreamer1.0-rtsp
### Requirement
- Python 3.x
- Opencv 3.x or above ( pip install opencv-python )

### Usage
> Run stream.py with required arguments to start the rtsp server
##### Sample 
    python stream.py --device_id 0 --fps 30 --image_width 640 --image_height 480 --port 8554 --stream_uri /video_stream
    
### Visualization

You can view the video feed on `rtsp://server-ip-address:8554/stream_uri`

e.g: `rtsp://192.168.1.12:8554/video_stream`

You can either use any video player which supports rtsp streaming like VLC player or you can use the `open-rtsp.py` script to view the video feed.

