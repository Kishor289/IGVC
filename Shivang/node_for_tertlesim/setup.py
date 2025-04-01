from setuptools import find_packages, setup

package_name = 'node_for_tertlesim'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shivang',
    maintainer_email='shivang@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "mtl=node_for_tertlesim.move_to_location:main",
            "mic=node_for_tertlesim.move_in_circle:main"
        ],
    },
)
