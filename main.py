import cv2
import mediapipe as mp
import pygame
import time
from eye_utils import eye_aspect_ratio

# --------------------
# Alarm Initialization
# --------------------
pygame.mixer.init()
pygame.mixer.music.load("mixkit-emergency-alert-alarm-1007 (1).wav")

# --------------------
# MediaPipe
# --------------------
mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    refine_landmarks=True,
    max_num_faces=1
)

# Left eye landmarks
LEFT_EYE = [33,160,158,133,153,144]

# Right eye landmarks
RIGHT_EYE = [362,385,387,263,373,380]

EAR_THRESHOLD = 0.22
CLOSED_FRAMES = 20

counter = 0
alarm_on = False

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame,1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:

        for face_landmarks in results.multi_face_landmarks:

            h,w,_ = frame.shape

            left_eye=[]
            right_eye=[]

            for idx in LEFT_EYE:
                x=int(face_landmarks.landmark[idx].x*w)
                y=int(face_landmarks.landmark[idx].y*h)
                left_eye.append((x,y))
                cv2.circle(frame,(x,y),2,(0,255,0),-1)

            for idx in RIGHT_EYE:
                x=int(face_landmarks.landmark[idx].x*w)
                y=int(face_landmarks.landmark[idx].y*h)
                right_eye.append((x,y))
                cv2.circle(frame,(x,y),2,(0,255,0),-1)

            leftEAR = eye_aspect_ratio(left_eye)
            rightEAR = eye_aspect_ratio(right_eye)

            ear = (leftEAR + rightEAR)/2

            cv2.putText(frame,
                        f"EAR:{ear:.2f}",
                        (20,40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (255,255,0),
                        2)

            if ear < EAR_THRESHOLD:

                counter += 1

                if counter >= CLOSED_FRAMES:

                    cv2.putText(frame,
                                "SLEEPING!",
                                (150,100),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1.5,
                                (0,0,255),
                                3)

                    if not alarm_on:
                        pygame.mixer.music.play(-1)
                        alarm_on=True

            else:

                counter=0

                if alarm_on:
                    pygame.mixer.music.stop()
                    alarm_on=False

                cv2.putText(frame,
                            "AWAKE",
                            (180,100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1.5,
                            (0,255,0),
                            3)

    cv2.imshow("Sleep Detection",frame)

    key=cv2.waitKey(1)

    if key==27:
        break

cap.release()
cv2.destroyAllWindows()
pygame.mixer.music.stop()