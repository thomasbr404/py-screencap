import cv2
import numpy as np
import pyautogui

SCREEN_SIZE = pyautogui.size() # Get screen size of primary monitor
fourcc = cv2.VideoWriter_fourcc(*"XVID") # Codec

output = cv2.VideoWriter("recording.avi", fourcc, 20.0, (SCREEN_SIZE)) # Define output content

for i in range (400):
    img = pyautogui.screenshot() #Take screenshots
    frame = np.array(img) # COnvert to OpenCV compatable array
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # BGR --> RGB
    output.write(frame) # Write the frame
    #cv2.imshow("screenshot", frame) # Show the frame
    if cv2.waitKey(1) == ord("q"): # Exit on q
        break

cv2.destroyAllWindows()
output.release()
