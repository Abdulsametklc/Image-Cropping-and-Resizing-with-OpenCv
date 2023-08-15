import cv2

img = cv2.imread("Lenna_(test_image).png")
print("Resim Boyutu:", img.shape)
cv2.imshow("Original", img)


#rezise
imgResized = cv2.resize(img, (800,800))
print("Resized Img Shape:", imgResized.shape)
cv2.imshow("Img Resized",imgResized)

#kırp
imgCropped = img[:200,0:300]
cv2.imshow("Kırpık Resim:",imgCropped)