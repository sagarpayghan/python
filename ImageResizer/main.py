import cv2

#configurable parameter
source="kv52.jpg"
destination="newimage.jpg"
src=cv2.imread(source, cv2.IMREAD_UNCHANGED)
scale_percent=50

#cv2.imshow("Title",src)
#cv2.waitKey(0)

#percentage by which image is resized


#calculate the 50 percent of original dimension
new_width=int(src.shape[1] * scale_percent/100)
new_height=int(src.shape[0] * scale_percent/100)

#resize image
output=cv2.resize(src, (new_width,new_height))

cv2.imwrite(destination, output)
cv2.waitKey(0)


