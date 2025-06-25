from setuptools import setup

package_name = 'ultralytics_cones'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=[
        'rclpy',
        'sensor_msgs',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A ROS package for processing sensor_msgs::msg::Image topics.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'image_node = ultralytics_cones.image_node:main'
        ],
    },
)