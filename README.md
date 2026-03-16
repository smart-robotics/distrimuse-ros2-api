# DistriMuSe ROS2 API

A ROS2 message definitions package for the DistriMuSe project. This package provides message types for partner-specific detection and analysis results.

## Overview

This package defines message interfaces for each partner in the DistriMuSe project:

- **Aitek** — Person detection with bounding boxes and behavior classification
- **Emoj** — Person detection with skeleton joint positions and ergonomic risk assessment
- **Pumacy** — Activity recognition with anomaly detection
- **Rulex/UniTo** — Area-based anomaly detection
- **UniGra** — Digital twin collision risk assessment

## Messages

### Aitek
| Message | Description |
|---------|-------------|
| `AitekDetectionResult` | Detection results containing a list of detected persons |
| `AitekDetectedPerson` | Detected person with bounding box, 3D position, and behavior |
| `AitekPersonBehavior` | Behavior classification (standing, sitting, walking, falling, etc.) |

### Emoj
| Message | Description |
|---------|-------------|
| `EmojDetectionResult` | Detection results containing a list of detected persons |
| `EmojDetectedPerson` | Detected person with 2D position, skeleton joints, and ergonomic risk |
| `EmojPersonJointPosition` | Skeleton joint position (2D/3D) for joints like head, shoulders, knees, etc. |

### Pumacy
| Message | Description |
|---------|-------------|
| `PumacyActivity` | Activity type with confidence score and anomaly flag |

### Rulex/UniTo
| Message | Description |
|---------|-------------|
| `RulexDetectionResult` | Detection results per area with optional image on anomaly |
| `RulexAreaScore` | Per-area anomaly detection result |

### UniGra
| Message | Description |
|---------|-------------|
| `UnigraResult` | Collision risk level from digital twin (no risk, low, high) |

## Installation

This project uses Pixi for dependency management:

```bash
pixi install
pixi run colcon build
pixi run test
```

## Usage

Once built, import the messages in your ROS2 nodes:

### Python
```python
from distrimuse_ros2_api.msg import (
    AitekDetectedPerson, AitekDetectionResult, AitekPersonBehavior,
)
from vision_msgs.msg import BoundingBox2D
from geometry_msgs.msg import Point, Pose2D

# Constructing a message
behavior = AitekPersonBehavior(type=AitekPersonBehavior.WALKING, confidence=0.95)
person = AitekDetectedPerson(
    camera_id="cam_front",
    bounding_box=BoundingBox2D(center=Pose2D(x=320.0, y=240.0), size_x=80.0, size_y=200.0),
    position_3d=Point(x=1.5, y=0.3, z=0.0),
    confidence=0.92,
    behavior=behavior,
)
result = AitekDetectionResult(detected_persons=[person])

# Reading from a callback
def aitek_callback(msg: AitekDetectionResult):
    for person in msg.detected_persons:
        print(f"Camera: {person.camera_id}, behavior: {person.behavior.type}")
```

### C++
```cpp
#include "distrimuse_ros2_api/msg/aitek_detected_person.hpp"
#include "distrimuse_ros2_api/msg/aitek_detection_result.hpp"
#include "distrimuse_ros2_api/msg/aitek_person_behavior.hpp"

// Constructing a message
distrimuse_ros2_api::msg::AitekPersonBehavior behavior;
behavior.type = distrimuse_ros2_api::msg::AitekPersonBehavior::WALKING;
behavior.confidence = 0.95;

distrimuse_ros2_api::msg::AitekDetectedPerson person;
person.camera_id = "cam_front";
person.bounding_box.center.x = 320.0;
person.bounding_box.center.y = 240.0;
person.bounding_box.size_x = 80.0;
person.bounding_box.size_y = 200.0;
person.position_3d.x = 1.5;
person.position_3d.y = 0.3;
person.confidence = 0.92;
person.behavior = behavior;

distrimuse_ros2_api::msg::AitekDetectionResult result;
result.detected_persons.push_back(person);

// Reading from a callback
void aitekCallback(const distrimuse_ros2_api::msg::AitekDetectionResult & msg) {
    RCLCPP_INFO(rclcpp::get_logger("rclcpp"),
                "Detected %zu persons", msg.detected_persons.size());
}
```