'''
A simple Program for grabing video from basler camera and converting it to opencv img.
Tested on Basler acA1300-200uc (USB3, linux 64bit , python 3.5)

For Right Cells, 02, 04, 06, 08, 10.
On Cell 02. ACS are X -162, Y 30, Z -120

'''
from pypylon import pylon
from datetime import datetime
import cv2

# Pseudo constant for camera calibration
# When the QR code is centered in this circle with sensor U300 at 250 mm of the plate.
# We suppose the gripper is centererd on Nest Number 6
# DEFAULT_QR_CODE_CIRCLE_X_CENTER = 3617
# DEFAULT_QR_CODE_CIRCLE_Y_CENTER = 618   
# DEFAULT_QR_CODE_CIRCLE_RADIUS = 598
DEFAULT_QR_CODE_CIRCLE_X_CENTER = 1657
DEFAULT_QR_CODE_CIRCLE_Y_CENTER = 618   
DEFAULT_QR_CODE_CIRCLE_RADIUS = 598

camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

# Grabing Continusely (video) with minimal delay
camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
camera.ExposureAuto.SetValue("Continuous") # TODO : tester si le paramétre est bien changé !
converter = pylon.ImageFormatConverter()

# converting to opencv bgr format
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

def getOnePicture():
    img=None
    grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

    if grabResult.GrabSucceeded():
        # Access the image data
        image = converter.Convert(grabResult)
        img = image.GetArray()

    grabResult.Release()

    return img


if __name__ == "__main__":

    # One Shot
    grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

    while camera.IsGrabbing():
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

        if grabResult.GrabSucceeded():
            # Access the image data
            image = converter.Convert(grabResult)
            img = image.GetArray()
            cv2.namedWindow('FromRobot Continuous Update', cv2.WINDOW_NORMAL)
            cv2.circle(img, center=(DEFAULT_QR_CODE_CIRCLE_X_CENTER, DEFAULT_QR_CODE_CIRCLE_Y_CENTER), radius=DEFAULT_QR_CODE_CIRCLE_RADIUS, color=(0, 255, 0), thickness=20)             
            cv2.resizeWindow("FromRobot Continuous Update", 1236, 900) 
            cv2.imshow('FromRobot Continuous Update', img)

            # Wait for 1 millisecond for a key event
            key = cv2.waitKey(1) & 0xFF
    
            # Check if the window is still open
            if cv2.getWindowProperty('FromRobot Continuous Update', cv2.WND_PROP_VISIBLE) < 1:
                break

            

        grabResult.Release()
        
    # Releasing the resource
    camera.StopGrabbing()

    cv2.destroyAllWindows()
