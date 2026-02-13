# DistriMuSe ROS2 API

A ROS2 message definitions package for the DistriMuSe project. This package provides standardized message types for inter-robot communication and person detection/behavior analysis in robotic applications.

## Overview

This package defines core message interfaces used by robotic systems to:
- Detect and track people in environments
- Monitor robot behavioral states
- Analyze human activities and poses
- Exchange detection and activity recognition results between distributed nodes

## Installation

### Using Pixi

This project uses Pixi for dependency management:

```bash
# Install dependencies
pixi install

# Build the package
pixi run colcon build

# Run tests
pixi run test
```

## Usage

Once built, import the messages in your ROS2 nodes:

### Python Example
```python
from distrimuse_ros2_api.msg import DetectionResult, RobotBehavior, PumacyActivity

# Subscribe to detection results
def detection_callback(msg: DetectionResult):
    print(f"Detected {len(msg.detected_persons)} persons in {msg.scene}")
    print(f"Robot behavior: {msg.robot_behavior.type}")
```

### C++ Example
```cpp
#include "distrimuse_ros2_api/msg/detection_result.hpp"

void detectionCallback(const distrimuse_ros2_api::msg::DetectionResult & msg) {
    RCLCPP_INFO(rclcpp::get_logger("rclcpp"),
                "Detected %zu persons in %s",
                msg.detected_persons.size(),
                msg.scene.c_str());
}
```