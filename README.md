# Face Detection ROS Package

## Author
Adam Jacobs
- Email: adam.jacobs@ufl.edu
- UFID: 6394-7174

## System Information
- OS: Ubuntu 22.04
- ROS Version: ROS 2 Humble

## Description
This ROS2 package implements OpenCV to detect faces in camera images. It consists of the following ROS nodes:

- **usb_camera_node:** Receives image data from a USB camera and publishes it for processing.
- **face_detect_node:** Subscribes to the image data, determines the location of faces, and publishes new image data with a bounding box around each detected face.
- **rqt_image_view:** Displays the image data with bounding boxes drawn over each detected face.

## Installation
### Prerequisites
- Ubuntu 22.04
- ROS 2 Humble
- Colcon
- Python
- OpenCV 

### Clone the Repository
```bash
git clone https://github.com/adamjacobs2/FaceDetectionROS.git
```
### Change Path 
In face_detect/face_detect_node.py, change the workspace to the absolute path of your colcon workspace
```python
workspace = '/home/username/rest_of_path_here/ros2_ws'
```

### Build the Package and Source the Workspace
```bash
cd ros_workspace_path
colcon build --symlink-install
source install 
```
### Launch the Package
```bash
ros2 launch face_detect launch.py
```
### Output 
![Face Detection](Output.png)

