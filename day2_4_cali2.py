#day2_4_cali.py
import numpy as np, cv2 as cv, glob
chessboardSize = (6, 9)
frameSize = (1280, 800)
criteria = (
cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((chessboardSize[0] * chessboardSize[1],
                 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboardSize[1], 
                       0:chessboardSize[0]].T.reshape(
    -1, 2)
print(objp.shape)
size_squares_mm = 20
objp = objp * size_squares_mm
objp = objp.reshape(-1,1,3)
print(objp.shape)
objpoints, imgpoints = [], []
images = glob.glob(
    "c:/VIsualSLAM/VisualSlam_Lecture/calibration3/*.jpg")
for image in images:
    img = cv.imread(image)
    #cv.imshow("img1", img)
    #cv.waitKey(300)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, corners = cv.findChessboardCorners(img, chessboardSize,
                                              flags=cv.CALIB_CB_ADAPTIVE_THRESH + cv.CALIB_CB_NORMALIZE_IMAGE)
    #cv.findChessboardCorners(gray,
    #                        chessboardSize, None)
    if ret:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray, corners,
                    (11,11), (-1,-1), criteria)
        imgpoints.append(corners)
        cv.drawChessboardCorners(img, chessboardSize,
                        corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(1000)
cv.destroyAllWindows()
(ret, cameraMatrix, distortion, rvecs,
  tvecs) = cv.calibrateCamera(objpoints, imgpoints,
             frameSize, None, None)
print(ret, "\ncameraMatrix:", cameraMatrix, 
      "\ndistortion", distortion, "\nrvecs", 
      [(i, v) for i,v in enumerate(rvecs)],
       "\ntvecs", [(i, v) for i,v in enumerate(tvecs)])
h,  w = frameSize
newCameraMatrix, roi = cv.getOptimalNewCameraMatrix(
    cameraMatrix, distortion, (w,h), 1, (w,h))

# Undistort
dst = cv.undistort(img, cameraMatrix, distortion,
                    None, newCameraMatrix)

# crop the image
x, y, w, h = roi
cv.imwrite('caliResult1.png', dst)

# Undistort with Remapping
mapx, mapy = cv.initUndistortRectifyMap(
    cameraMatrix, distortion, None, newCameraMatrix, (w,h), 5)
dst = cv.remap(img, mapx, mapy, cv.INTER_LINEAR)

# crop the image
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv.imwrite('caliResult2.png', dst)


# Reprojection Error
mean_error = 0

for i in range(len(objpoints)):
    imgpoints2, _ = cv.projectPoints(
        objpoints[i], rvecs[i], tvecs[i], cameraMatrix, distortion)
    error = cv.norm(imgpoints[i], imgpoints2, cv.NORM_L2)/len(imgpoints2)
    mean_error += error

print( "total error: {}".format(mean_error/len(objpoints)) )

