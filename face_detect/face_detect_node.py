import cv2
import rclpy
from sensor_msgs.msg import Image
from threading import Lock
from cv_bridge import CvBridge, CvBridgeError
import os
workspace='/home/diamond/AuRo/ros2_ws'
#Get the path of the colcon workspace
class ImagePipeline:
    def __init__(self):
        self.mutex = Lock()
        rclpy.init()
        self.node = rclpy.create_node('my_node')
        self.bridge = CvBridge()
        topic = '/image_raw'
        imRos = self.node.create_subscription(Image, topic, self.imageCallBack, 3)

        self.ImOut = self.node.create_publisher(Image, '/out/image', 3)
        print('1')
        try:
            print("Node is running")
            rclpy.spin(self.node)
        except KeyboardInterrupt:
            print("Rospy Spin Shut down")

    def imageCallBack(self, inp_im):
        print("recieved image")
        try:
            imCV = self.bridge.imgmsg_to_cv2(inp_im, "bgr8")
        except CvBridgeError as e:
            print(e)
        if imCV is None:
            print ('frame dropped, skipping tracking')
        else:
            #Load the cascade 
            xmlpath = '/src/face_detect/face_detect/'
            face_cascade = cv2.CascadeClassifier(workspace + xmlpath + 'haarcascade_frontalface_default.xml')
            gray = cv2.cvtColor(imCV, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))
            for (x, y, w, h) in faces:
                cv2.rectangle(imCV, (x, y), (x+w, y+h), (0, 255, 0), 2)
            imageOut = self.bridge.cv2_to_imgmsg(imCV, "bgr8")
            self.ImOut.publish(imageOut)
            print("image published")

def main():
    n = ImagePipeline()
if __name__ == "__main__":
     main()
    