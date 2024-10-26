# Sub-Pixel-Precision-Optical-Flow-Tracker-for-Autonomous-Navigation-and-Flying-Object-Tracking

---

### **Project Overview**

This project implements a sub-pixel precision optical flow tracker designed for autonomous navigation and real-time tracking of flying objects in dynamic environments. The tracker uses optical flow algorithms for motion estimation and integrates object detection for real-time flying object tracking. This system is optimized for resource-constrained hardware like drones or embedded systems, making it ideal for applications in autonomous vehicles and UAVs.

---

### **Features**
- **Real-Time Optical Flow Tracking**: High-accuracy, real-time motion tracking for dynamic environments.
- **Sub-Pixel Precision**: Achieves fine-grained accuracy, crucial for reliable navigation and tracking.
- **Flying Object Detection**: YOLO-based model for detecting and tracking flying objects.
- **Robust Performance**: Adaptable to rapid movement, changing lighting, and complex textures.
- **Optimized for Embedded Hardware**: Efficient design for devices like NVIDIA Jetson and Raspberry Pi.

---

### **Getting Started**

#### **1. Prerequisites**
- **Python 3.7+**
- **CUDA Toolkit** (for GPU acceleration on NVIDIA Jetson or similar devices)
- **Hardware Support**: Raspberry Pi, NVIDIA Jetson Nano, or other embedded platforms
- **Python Libraries**:
  - OpenCV
  - PyTorch or TensorFlow (for YOLO)
  - NumPy

#### **2. Installation**
Clone the repository and install dependencies:
```bash
git clone https://github.com/yourusername/sub-pixel-optical-flow-tracker.git
cd sub-pixel-optical-flow-tracker
pip install -r requirements.txt
```

---

### **Project Structure**

- **`src/`**: Contains core scripts for optical flow, object detection, and tracking.
- **`models/`**: Pre-trained YOLO models for object detection.
- **`tests/`**: Evaluation scripts for testing under different conditions.
- **`docs/`**: Project documentation.
- **`demo/`**: Sample video footage and output files.

---

### **Usage**

#### **Running the Tracker**
To run the optical flow tracker with flying object detection, use:
```bash
python src/main.py --input <path_to_video> --output <output_path> --hardware <jetson/rpi/cpu>
```

#### **Key Parameters**
- **`--input`**: Path to input video or camera stream.
- **`--output`**: Path to save output video (optional).
- **`--hardware`**: Specify hardware configuration (`jetson`, `rpi`, or `cpu`).

---

### **Performance Evaluation**

To evaluate the tracker’s performance:
```bash
python tests/evaluate.py --dataset <KITTI/Middlebury/custom> --hardware <jetson/rpi/cpu>
```
This script outputs metrics such as sub-pixel accuracy, FPS, resource usage, and robustness in various environments.

---

### **Results Summary**

| Metric                    | NVIDIA Jetson Nano | Raspberry Pi 4 | Laptop GPU (GTX 1650) |
|---------------------------|--------------------|----------------|------------------------|
| **Frames Per Second (FPS)** | 28-32             | 18-22         | 45-50                 |
| **Sub-Pixel Accuracy (AEE)** | 0.15 pixels       | 0.20 pixels   | 0.15 pixels           |
| **Object Detection F1 Score** | 87%              | 80%           | 90%                   |
| **Resource Utilization**   | 70% GPU, 50% CPU  | 90% CPU       | 65% GPU, 40% CPU      |

---

### **Optimization Techniques**

- **CUDA Acceleration**: Enabled for GPU-based devices.
- **Model Quantization**: Reduces memory footprint and enhances processing speed.
- **Multi-Threading**: Parallelized processing pipeline for higher FPS.

---

### **Limitations**
- **Low-Light Performance**: Slight reduction in tracking accuracy in low-light conditions.
- **CPU Dependence on Raspberry Pi**: FPS is lower on Raspberry Pi due to lack of GPU.

---

### **Future Enhancements**
- **Improved Low-Light Performance**: Implementing image enhancement for better tracking in dim lighting.
- **Edge TPU Integration**: Integrate TPU with Raspberry Pi to boost processing power.
- **Advanced Model Compression**: Further model pruning and compression for higher efficiency.

---

### **Contributing**
Contributions are welcome! Fork the repository, create a feature branch, and submit a pull request. Refer to `CONTRIBUTING.md` for detailed guidelines.

---

### **License**
This project is licensed under the MIT License. See `LICENSE` for details.

---

### **Contact**
For questions or feedback, reach out to **[Priyanshu Bharadwaj]** at **[priyanshubharadwaj38@gmail.com]** or create an issue on GitHub.

---

This README provides all essential information on setting up, using, and understanding the **Sub-Pixel Precision Optical Flow Tracker**.
