import cv2


camera = cv2.VideoCapture(0)
i = 0
while i < 10:
    raw_input('Press Enter to capture')
    return_value, image = camera.read()
    cv2.imwrite('opencv'+str(i)+'.png', image)
    i+=1
del(camera)

# while True:
# 	ret_val, img = cam.read()
# 	img = cv2.flip(img, 1)
# 	cv2.imshow('my webcam', img)
# 	if cv2.waitKey(1) == 27: 
# 		break  # esc to quit
# cv2.destroyAllWindows()