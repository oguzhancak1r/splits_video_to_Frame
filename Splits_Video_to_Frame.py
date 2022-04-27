# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 22:47:34 2022

@author: oğuzhan çakır
@ E-mail : oguz.54.197@hotmail.com 
"""
import cv2

vid = cv2.VideoCapture("video1.mp4") # video name have to be "video1.mp4" 
 

i = 0
while True:

    ret, frame = vid.read()

    if ret is False:
        break

    img = frame
    img = cv2.resize(img, (1260, 980)) # kullanılabilir kod açıklaması aşağıda .
    """
    ↑↑↑↑ yukarıdaki kodu isterseniz kullanabilirsiniz.Yukarıdaki kod her frame'in
    yeniden boyutlanmasına yarar her birinin size'ı 1260x980
    """
    print(i)
    i += 1
    # if i <= 3000:
        # continue
    if i % 10 != 0:     #frame sayısını azalt, her 10 frame'de 1 frame'i .jpg uzantılı kaydet.
    # isterseniz kaç FPS'te bir frame alacaksanız seçebilirsiniz.
        continue
    cv2.imwrite(str(i) + ".jpg", img) #her 10 frame'de bir cihaza kaydetmeye başlar.
    


    if (cv2.waitKey(1) & 0xFF == ord("q")):
        break

    if i == 600:
        break
# 
    cv2.imshow("frame", frame)

vid.release()
cv2.destroyAllWindows()
