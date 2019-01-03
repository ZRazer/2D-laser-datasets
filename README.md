# 2D-laser-datasets

# remove specific transform/topic

python scripts: tf_filter.py(Retain the specified transform)

         usage: python tf_filter.py input.bag output.bag
         
build-in functions(remove transform map):

         usage: rosrun bag_tools remove_tf.py -i input.bag -o output.bag -f map
         
build-in functions(Retain the specified topic):
         
         rosbag filter input.bag output.bag 'topic == "/scan" or topic == "/tf" or topic == "/imu" or topic == "/odom"'

# self-recorded datasets:

floor1.bag  floor3.bag || lidar:Rplidar A3(There are many measurement noises)

gyy_floor3.bag || lidar：Ydlidar G4（Maybe... I have forgotten） Odometery is bad.

         author = {Richard Zander},

# malaga dataset:

malaga.bag  || lidar:SICK

         author = {Blanco, José-Luis and Fernández-Madrigal, Juan-Antonio and Gonzalez-Jimenez, Javier},
          title = {A New Approach for Large-Scale Localization and Mapping: Hybrid Metric-Topological SLAM},
      booktitle = {IEEE International Conference on Robotics and Automation (ICRA'07)},
           year = {2007},
       location = {Roma (Italy)}
