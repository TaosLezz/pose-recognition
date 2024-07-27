# # import cv2
# # import mediapipe as mp
# # import numpy as np
# # import sys
# # mp_drawing = mp.solutions.drawing_utils
# # mp_pose = mp.solutions.pose

# # pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# # cap = cv2.VideoCapture(sys.argv[1])

# # if cap.isOpened() == False:
# #     print("Error opening video stream or file")
# #     raise TypeError

# # frame_width = int(cap.get(3))
# # frame_height = int(cap.get(4))

# # outdir, inputflnm = sys.argv[1][:sys.argv[1].rfind(
# #     '/')+1], sys.argv[1][sys.argv[1].rfind('/')+1:]
# # inflnm, inflext = inputflnm.split('.')
# # out_filename = f'{outdir}{inflnm}_annotated.{inflext}'
# # out = cv2.VideoWriter(out_filename, cv2.VideoWriter_fourcc(
# #     'M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

# # while cap.isOpened():
# #     ret, image = cap.read()
# #     if not ret:
# #         break

# #     image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
# #     image.flags.writeable = False
# #     results = pose.process(image)

# #     image.flags.writeable = True
# #     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
# #     mp_drawing.draw_landmarks(
# #         image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
# #     out.write(image)
# # pose.close()
# # cap.release()
# # out.release()
# import cv2
# import mediapipe as mp

# mp_drawing = mp.solutions.drawing_utils
# mp_pose = mp.solutions.pose

# pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# # Thay đổi tên file video cần chạy
# video_file = "tes.mp4"

# cap = cv2.VideoCapture(video_file)

# if not cap.isOpened():
#     print("Error opening video stream or file")
#     raise TypeError

# frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# out_filename = f"{video_file[:-4]}_annotated.mp4"  # Đổi tên file output nếu cần

# out = cv2.VideoWriter(out_filename, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

# while cap.isOpened():
#     ret, image = cap.read()
#     if not ret:
#         break

#     image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
#     image.flags.writeable = False
#     results = pose.process(image)

#     image.flags.writeable = True
#     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#     mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
#     out.write(image)

# pose.close()
# cap.release()
# out.release()

import cv2
import mediapipe as mp
import time


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Thay đổi tên file video cần chạy
video_file = "tes.mp4"

cap = cv2.VideoCapture(video_file)

if not cap.isOpened():
    print("Error opening video stream or file")
    raise TypeError

frame_count = 0
start_time = time.time()
while cap.isOpened():
    ret, image = cap.read()
    if not ret:
        break

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = pose.process(image)

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    frame_count+=1
    elapsed_time = time.time() - start_time
    fps = frame_count/elapsed_time
    cv2.putText(image, f"FPS: {fps:.2f}", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1,(0,255,0), 2)

    cv2.imshow('Pose Estimation', image)  # Hiển thị khung hình đã xử lý


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

pose.close()
cap.release()
cv2.destroyAllWindows()
