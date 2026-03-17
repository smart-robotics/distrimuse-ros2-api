cmake_minimum_required(VERSION 3.8)
project(distrimuse_ros2_api)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(vision_msgs REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/AitekDetectedPerson.msg"
  "msg/AitekDetectionResult.msg"
  "msg/AitekPersonBehavior.msg"
  "msg/EmojDetectedPerson.msg"
  "msg/EmojDetectionResult.msg"
  "msg/EmojPersonJointPosition.msg"
  "msg/PumacyActivity.msg"
  "msg/RulexAreaScore.msg"
  "msg/RulexDetectionResult.msg"
  "msg/UnigraResult.msg"
  DEPENDENCIES geometry_msgs sensor_msgs std_msgs vision_msgs
)

ament_package()
