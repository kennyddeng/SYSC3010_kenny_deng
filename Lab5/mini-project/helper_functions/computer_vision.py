from PIL import Image
import numpy as np

# Input image1 and image2 locations, and t1
# returns Boolean value indicating if a "person" is in the image based on t1
def person_detected(image1_file, image2_file, t1):
    image1 = Image.open(image1_file)
    image1 = np.array(image1)
    image1 = np.sum(image1, dtype = int)
    
    image2 = Image.open(image2_file)
    image2 = np.array(image2)
    image2 = np.sum(image2, dtype = int)
    
    # outputs absolute difference of both images, for testing purposes to find good t1 value
    #print(np.absolute(image2 - image1)) # uncomment to test output
    #print(np.absolute(image2 - image1))
    if np.absolute(image2 - image1) < t1:
        return False
    if np.absolute(image2 - image1) > t1:
        return True