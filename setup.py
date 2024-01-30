from setuptools import find_packages, setup
import subprocess, os, platform, glob

package_name = 'face_detect'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob.glob('launch/*.py')),
    
       
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='diamond',
    maintainer_email='adamjacobs272@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'face_detect_node = face_detect.face_detect_node:main',
            
        ],
    },
)
