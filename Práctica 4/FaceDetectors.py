import cv2
from imutils import face_utils
import numpy as np
import dlib

class FaceDetector:
    def __init__(self):
        # DDN for face detection
        faceProto = "opencv_face_detector.pbtxt"
        faceModel = "opencv_face_detector_uint8.pb"
        self.faceNet = cv2.dnn.readNet(faceModel, faceProto)
        self.conf_threshold = 0.7

        # DLIB for facial landmarks
        p = "shape_predictor_68_face_landmarks.dat"
        self.predictor68 = dlib.shape_predictor(p)

    def getLargest(self, objects):
        if len(objects) < 1:
            return -1
        elif len(objects) == 1:
            return 0
        else:
            areas = [w * h for x, y, w, h in objects]
            return np.argmax(areas)

    def DetectLargestFaceEyesDNN(self, img):
        # Face detection DNN
        faces = self.FaceDetectionDNN(img)

        # Makes us of the largest face
        iface = self.getLargest(faces)
        if iface >= 0:
            (x, y, w, h) = faces[iface]
            # Composes rectangle
            face = dlib.rectangle(left=x, top=y, right=x + w, bottom=y + h)

            values = self.GetFacialLandmarks(img, face)

            if values is not None:
                points, shape = values

                le = np.mean(shape[36:42], 0)
                re = np.mean(shape[42:48], 0)

                return [x, y, w, h], [le[0], le[1], re[0], re[1]], shape
            else:
                return [-1, -1, -1, -1], [], []

        else:
            return [-1, -1, -1, -1], [], []


    def FaceDetectionDNN(self, img):

        # Detecta objetos
        frameHeight = img.shape[0]
        frameWidth = img.shape[1]
        blob = cv2.dnn.blobFromImage(img, 1.0, (300, 300), [104, 117, 123], True, False)

        self.faceNet.setInput(blob)
        detections = self.faceNet.forward()
        faces = []
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > self.conf_threshold:
                x1 = int(detections[0, 0, i, 3] * frameWidth)
                y1 = int(detections[0, 0, i, 4] * frameHeight)
                x2 = int(detections[0, 0, i, 5] * frameWidth)
                y2 = int(detections[0, 0, i, 6] * frameHeight)
                faces.append([x1, y1, x2 - x1, y2 - y1])

        return faces


    def GetFacialLandmarks(self, img,roi):

        points = self.predictor68(img, roi)

        if points is not None:
            # Dibujamos recuadro mayor
            shape = face_utils.shape_to_np(points)

            left_eye_x = int(points.part(3).x - abs(points.part(3).x - points.part(2).x) / 2.)
            left_eye_y = int(points.part(3).y - abs(points.part(3).y - points.part(2).y) / 2.)
            right_eye_x = int(points.part(1).x + abs(points.part(1).x - points.part(0).x) / 2.)
            right_eye_y = int(points.part(1).y - abs(points.part(1).y - points.part(0).y) / 2.)

            nose_x = int(points.part(4).x)
            nose_y = int(points.part(4).y)

            if right_eye_x - left_eye_x == 0:
                return None
            m1 = (right_eye_y - left_eye_y) / (right_eye_x - left_eye_x)
            if m1 != 0:
                m2 = -1 / m1
                b2 = nose_y - m2 * nose_x
                x_c = ((nose_y + 1.5 * abs(points.part(3).x - points.part(2).x) / 2.) - b2) / m2
                y_c = m2 * x_c + b2

                b3 = y_c - m1 * x_c
                left_mouth_x = ((y_c + m1 * 2 * abs(points.part(3).x - points.part(2).x) / 2.) - b3) / m1
                left_mouth_y = m1 * left_mouth_x + b3
                right_mouth_x = ((y_c - m1 * 2 * abs(points.part(3).x - points.part(2).x) / 2.) - b3) / m1
                right_mouth_y = m1 * right_mouth_x + b3
            else:
                left_mouth_x = points.part(4).x + 1.5 * abs(points.part(3).x - points.part(2).x) / 2.
                left_mouth_y = nose_y + abs(points.part(3).x - points.part(2).x) / 2.
                right_mouth_x = (points.part(4).x) - 1.5 * abs(points.part(3).x - points.part(2).x) / 2.
                right_mouth_y = nose_y + abs(points.part(3).x - points.part(2).x) / 2.

            points = [left_eye_x, right_eye_x, nose_x, left_mouth_x, right_mouth_x, left_eye_y, right_eye_y, nose_y,
                      left_mouth_y, right_mouth_y]


            return [points], shape
        else:
            return None
