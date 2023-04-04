from setuptools import setup

package_name = 'PingPong'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='marchettins',
    maintainer_email='marchettins@vcu.edu',
    description='Ping Pong project HIVE Lab',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'talker = PingPong.Ping:main',
        'listener = PingPong.Pong:main',
        ],
    },
)
