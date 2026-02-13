cmake_minimum_required(VERSION 3.8)
project(distrimuse_ros2_api)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/RobotBehavior.msg"
  "msg/PersonBehavior.msg"
  "msg/PersonJointPosition.msg"
  "msg/DetectedPerson.msg"
  "msg/DetectionResult.msg"
  "msg/PumacyActivity.msg"
  DEPENDENCIES std_msgs
)

ament_package()
