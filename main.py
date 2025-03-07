from DetectionOfCopyMoveForgery import *

def getFmeasure(ground_true, test_img, width, height):

    DP=0
    YP=0
    YN=0
    for i in range(height):
        for j in range(width):
            if ground_true[i][j]==255 and test_img[i][j]==255:
                DP +=1
            if ground_true[i][j]==0 and test_img[i][j]==255:
                YP +=1
            if ground_true[i][j]==255 and test_img[i][j]==0:
                YN +=1

    precision =DP/(DP+YP)
    recall =DP/(DP+YN)

    return 2*((precision*recall)/(precision+recall))




# for i in range(160,0,-2):
#     path ="forged_images/"+str(i)+".png"
#     img = cv2.imread(path ,0)
#     height, width= img.shape
#     # (img, height, width, blocksize, oklid_threshold, correlation_threshold, vec_len_threshold, num_ofvector_threshold)
#     asd = DetectionofCopyMoveForgery(img, height, width, 8,3.5,8,100,5)
#     asd.detection_forgery()
#     cv2.waitKey(0)
#     path = "forged_images/" + str(i-1) + ".png"
#     original_img = cv2.imread(path,0)
#     print(getFmeasure(original_img,img,width,height))



inp = cv2.imread("cad_0.png" ,0)
height, width= inp.shape
# (img, height, width, blocksize, oklid_threshold, correlation_threshold, vec_len_threshold, num_ofvector_threshold)
asd = DetectionofCopyMoveForgery(inp, height, width, 8,3.5,8,100,5)
asd.detection_forgery()
cv2.waitKey(0)

ground = cv2.imread("cad_9.png",0)
print(getFmeasure(ground , inp , width ,height))
cv2.destroyAllWindows()









