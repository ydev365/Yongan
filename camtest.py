import cv2

cap = cv2.VideoCapture(0)
if(cap.isOpened()==False):
  print("error1")
  
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    cv.imshow('Frame',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
  else:
    break
cap.release()
cv2.destroyAllWindows()