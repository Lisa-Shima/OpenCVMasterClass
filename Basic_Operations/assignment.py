import cv2

image = cv2.imread("assignment-001-given.jpg")
label_background = image.copy()

cv2.rectangle(label_background, (805,80), (1260, 192), (0,0,0), -1) #set thickness to -1 to mean: fill the whole rectangle not border thickness this time

blended = cv2.addWeighted(label_background, 0.5, image, 0.5, 0)

cv2.rectangle(blended, (265, 192), (985, 923), (0, 255, 0), 5)

cv2.putText(blended, 'RAH972U', (820,165), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 7)

cv2.imshow("Assignment-Image", blended)

cv2.waitKey(0)

cv2.imwrite("assignment_result_practice.jpg", blended)

cv2.destroyAllWindows()