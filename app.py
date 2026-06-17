import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
import tempfile
import time

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="PCB Detection System",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Real-Time PCB Detection System")
st.markdown("YOLOv8 PCB Defect Detection using Webcam / USB Camera")

# =========================================================
# LOAD MODEL
# =========================================================
MODEL_PATH = r"E:\pcbDetection\pcb_training-2\weights\best.pt"

@st.cache_resource
def load_model():
    model = YOLO(MODEL_PATH)
    return model

model = load_model()

# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.header("Settings")

camera_index = st.sidebar.selectbox(
    "Select Camera",
    [0, 1, 2],
    index=0
)

confidence = st.sidebar.slider(
    "Confidence Threshold",
    min_value=0.1,
    max_value=1.0,
    value=0.5,
    step=0.05
)

run = st.sidebar.button("Start Camera")
stop = st.sidebar.button("Stop Camera")

# =========================================================
# CLASS NAMES
# =========================================================
CLASS_NAMES = {
    0: "PCB_A_OK",
    1: "PCB_A_NG",
    2: "PCB_B_OK",
    3: "PCB_B_NG"
}

# =========================================================
# DISPLAY AREA
# =========================================================
frame_placeholder = st.empty()
status_placeholder = st.empty()

# =========================================================
# CAMERA
# =========================================================
if run:

    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        st.error("❌ Cannot open camera")
        st.stop()

    status_placeholder.success("✅ Camera Started")

    while True:

        ret, frame = cap.read()

        if not ret:
            st.error("❌ Failed to read frame")
            break

        # =================================================
        # YOLO INFERENCE
        # =================================================
        results = model.predict(
            source=frame,
            conf=confidence,
            verbose=False
        )

        annotated_frame = frame.copy()

        # =================================================
        # DRAW RESULTS
        # =================================================
        for result in results:

            boxes = result.boxes

            for box in boxes:

                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                cls = int(box.cls[0])
                conf_score = float(box.conf[0])

                label = f"{CLASS_NAMES[cls]} {conf_score:.2f}"

                # Color
                if "NG" in CLASS_NAMES[cls]:
                    color = (0, 0, 255)  # Red
                else:
                    color = (0, 255, 0)  # Green

                # Bounding Box
                cv2.rectangle(
                    annotated_frame,
                    (x1, y1),
                    (x2, y2),
                    color,
                    2
                )

                # Label
                cv2.putText(
                    annotated_frame,
                    label,
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    color,
                    2
                )

        # =================================================
        # DISPLAY FRAME
        # =================================================
        annotated_frame = cv2.cvtColor(
            annotated_frame,
            cv2.COLOR_BGR2RGB
        )

        frame_placeholder.image(
            annotated_frame,
            channels="RGB",
            use_container_width=True
        )

        # Small delay
        time.sleep(0.01)

        # Stop button
        if stop:
            break

    cap.release()
    cv2.destroyAllWindows()

    status_placeholder.warning("🛑 Camera Stopped")
