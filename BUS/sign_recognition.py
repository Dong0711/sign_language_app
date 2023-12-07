from PyQt6.QtGui import QImage
from PyQt6.QtCore import QThread,pyqtSignal
from PyQt6.QtCore import Qt
import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import mediapipe as mp
from keras.models import load_model
class recogintion(QThread):
    # TF_ENABLE_ONEDNN_OPTS=0
    mp_holistic = mp.solutions.holistic # Mô hình holistic
    mp_drawing = mp.solutions.drawing_utils
    DATA_PATH = os.path.join('Data') 
    actions = np.array(['Xin chào','Xin lỗi','Cảm ơn','Tạm biệt','Hãy liên hệ với tôi một cách an toàn', 'Rất vui được gặp bạn','Mẹ','Cha','Lại lần nữa','Ăn','Thêm nữa','Ngủ','Tắm'])
    no_sequences = 30
    sequence_length = 60    
    def mediapipe_detection(self,image, model):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # COLOR CONVERSION BGR 2 RGB
        image.flags.writeable = False                  # Image is no longer writeable
        results = model.process(image)                 # Make prediction
        image.flags.writeable = True                   # Image is now writeable 
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # COLOR COVERSION RGB 2 BGR
        return image, results
    def extract_keypoints(self,results):
        lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
        rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
        return np.concatenate([lh, rh])
    # 1. New detection variables
    
    image_update = pyqtSignal(QImage)
    text_change=pyqtSignal(str)
    def run(self):
        
        self.ThreadActive = True
        sequence = []
        sentence = []
        threshold = 0.8
        model=load_model('13.h5')

        Capture = cv2.VideoCapture(0)
        
        while self.ThreadActive :
            with self.mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
                ret, frame = Capture.read()
                image, results = self.mediapipe_detection(frame, holistic) # gọi biến image và result = giá trị RGB của ảnh
                keypoints = self.extract_keypoints(results) # xuất ra array các keypoints cơ thể (mấy cái đốt í)
                sequence.append(keypoints)
                sequence = sequence[-60:]
                if ret:
                    
                    if len(sequence) == 60:
                        res =model.predict(np.expand_dims(sequence, axis=0))[0]
                        if res[np.argmax(res)] > threshold: 
                            if len(sentence) > 0: 
                                if self.actions[np.argmax(res)] != sentence[-1]:
                                    sentence.append(self.actions[np.argmax(res)])
                            else:
                                sentence.append(self.actions[np.argmax(res)])
                        if len(sentence) > 0: 
                            sentence = sentence[-1:]
                            print(sentence)  
                            self.text_change.emit(sentence[0])
                            
                    # cv2.rectangle(image, (0,0), (640, 40), (245, 117, 16), -1)
                    # cv2.putText(image, ' '.join(sentence), (3,30), 
                    # cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                    out_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    ConvertToQtFormat = QImage(out_image.data, out_image.shape[1], out_image.shape[0],QImage.Format.Format_BGR888)
                    out_image = ConvertToQtFormat.rgbSwapped()
                    pic=out_image.scaled(640, 480, Qt.AspectRatioMode(1))
                    self.image_update.emit(pic)
    def stop(self):
        self.ThreadActive = False