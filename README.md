# Automated PCB NG Detection System Using YOLOv8 and Raspberry Pi 4

## Overview

The PCB NG Detection System is a real-time computer vision application designed to automatically detect and classify Printed Circuit Boards (PCBs) as either **OK (Good)** or **NG (No Good / Defective)** using a YOLOv8 object detection model.

The system runs on a Raspberry Pi with a USB camera and performs live inspection of multiple PCBs within a single image frame. Detected PCBs are highlighted with bounding boxes and classified into predefined categories.

This project aims to support automated quality inspection in manufacturing environments by reducing manual inspection effort and improving detection consistency.


**User Interface**

![streamlit](https://github.com/amjadzkwn/PCB-NG-Detection-System/blob/2ab1a47a76b9692fd809bf5ea37dff38700a07ee/pcbDetection_streamlit.jpg)


---

## Features

* Real-time PCB inspection using a USB camera
* YOLOv8-based object detection
* Detection of multiple PCBs in a single frame
* Classification of PCB status:

  * PCB_A_OK
  * PCB_A_NG
  * PCB_B_OK
  * PCB_B_NG
* Color-coded bounding boxes:

  * Green = OK
  * Red = NG (Defective)
* PyTorch-based YOLOv8 model deployment for real-time inference

---

## System Architecture

USB Camera → Raspberry Pi → YOLOv8 pt Model → PCB Classification → Detection Display

---

## Dataset

The model was trained using a custom PCB dataset consisting of:

* PCB_A_OK
* PCB_A_NG
* PCB_B_OK
* PCB_B_NG

Images were manually annotated using bounding boxes and exported in YOLO format.

---

## Hardware Requirements

* Raspberry Pi 4
* USB Camera
* MicroSD Card
* Power Supply
* Monitor (optional)

---

## Software Requirements

* Python 3.9+
* OpenCV
* Ultralytics YOLOv8

Install required packages:

```bash
pip install ultralytics opencv-python
```

---

## Model

The system uses a custom-trained YOLOv8 object detection model stored in PyTorch format:

```text
best.pt
```

The model was trained on a custom PCB dataset and deployed directly on a Raspberry Pi for real-time inference.

Benefits of using the .pt model:

* High detection accuracy
* Easy deployment with Ultralytics YOLO
* Supports real-time object detection
* Suitable for prototyping and research applications

---

## Running the System

Execute the detection script:

```bash
python app.py
```

The system will:

1. Open the USB camera.
2. Capture live video frames.
3. Run YOLOv8 inference using best.pt.
4. Detect multiple PCBs in a single frame.
5. Display bounding boxes and confidence scores.
6. Highlight defective PCBs in red and good PCBs in green.

Press:

```text
Q
```

to exit the application.

---

## Detection Classes

| Class ID | Label    |
| -------- | -------- |
| 0        | PCB_A_OK |
| 1        | PCB_A_NG |
| 2        | PCB_B_OK |
| 3        | PCB_B_NG |

---

## Example Output

For each detected PCB:

```text
PCB_A_OK 0.95
PCB_B_NG 0.91
```

**OK Detection**

![ok_detection](https://github.com/amjadzkwn/PCB-NG-Detection-System/blob/0ae5693ef0902464f3f16b9f8a857ba4d0970c79/OK_Detect.jpg)

**NG Detection**

![ng_detection](https://github.com/amjadzkwn/PCB-NG-Detection-System/blob/1bc9a6ea09ea925daa08980f4bc8733edfd19e66/NG_Detect.jpg)

Bounding boxes are displayed around detected objects along with confidence scores.

---

## Applications

This system can be used for:

* PCB quality inspection
* Manufacturing automation
* Defect detection
* Smart factory solutions
* Industrial AI deployment
* Edge AI applications

---

## Future Improvements

* Raspberry Pi AI Accelerator integration
* Change to Raspberry Pi 5
* Conveyor belt inspection system
* Automatic NG counting
* Defect reporting dashboard
* Cloud monitoring system
* Streamlit web interface
* Real-time production analytics

---

## Author

Muhammad Amjad Zakwan Bin Abu Hanipah

Bachelor of Computer Science with Honours (Data Science)

Universiti Malaysia Sabah (UMS)

---

## License

This project was developed for academic purposes and as part of an industry collaboration with Betamek Electronics (M) Sdn. Bhd.
