import cv2

def face_recog(pil_image):
	casc_path = 'models/haarcascade_frontalface_default.xml'
	faceCascade = cv2.CascadeClassifier(casc_path)

	# Convert RGB to BGR	
	cv_image = pil_image[:, :, ::-1].copy()
	# convert to gray scale
	gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(gray,
                                    scaleFactor= 1.1,
                                    minNeighbors= 5,
                                    minSize= (30,30),
                                    flags= cv2.CASCADE_SCALE_IMAGE)

	for (x,y,w,h) in faces:
		cv2.rectangle(cv_image, (x, y), (x+w, y+h), (0,255,0), 2)

	cv_image= cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)
	return cv_image

# cv2.imshow('Faces found', face_recog('people.jpg'))
# cv2.waitKey(0)