from helper_functions import camera, computer_vision, sensehat
from time import sleep

def main():
    camera_i = camera.get_camera() #DO NOT MODIFY, function call must work as is 
    sense = sensehat.get_sensehat() #DO NOT MODIFY, function call must work as is
    sense.clear() # set intial state, clear led matrix 
    
    take_background_image = input("Take new background photo? \"Y/N\" \n")
    # convert input string to boolean
    if take_background_image == "N" or take_background_image == "n":
        take_background_image = False
    elif take_background_image == "Y" or take_background_image == "y":
        take_background_image = True
    
    # take new background photo
    if take_background_image == True:
        preview = input("Preview background photo? \"Y/N\" \n")
        # convert input string to boolean
        if preview == "N" or preview == "n":
            preview = False
        elif preview == "Y" or preview == "y":
            preview = True
    
        countdown = int(input("Enter countdown time in seconds before the camera takes a photo: \n"))
        camera.capture_image(camera_i,"data/images/background.jpg", countdown_time=countdown, preview=preview) #DO NOT MODIFY, function call must work as is 
    
    arm_system = input("Arm system? \"Y/N\" \n")
    # convert input string to boolean
    if arm_system == "N" or arm_system == "n":
        arm_system = False
    elif arm_system == "Y" or arm_system == "y":
        arm_system = True
    
    if arm_system == True:
        interval = int(input("Enter time interval between camera photos taken in seconds: \n"))
        t1 = int(input("Enter threshold t1: \n"))
       
        time_monitor_start = int(input("Enter countdown time in seconds before system arms/monitoring begins: \n"))
        print("Monitoring will begin in " + str(time_monitor_start) + " seconds.")
        for i in range(time_monitor_start, 0, -1):
            print(i-1)
            sleep(1)

        count = 0
        while True: #DO NOT MODIFY, function call must work as is 
            camera.capture_image(camera_i,"data/images/image%s.jpg" % count, countdown_time=interval, preview = None) #DO NOT MODIFY, function call must work as is
                                                                                                                        # modified to pass preview = None (no preview for Arm System photos)
            person_detected = computer_vision.person_detected("data/images/background.jpg","data/images/image%s.jpg" % count, t1)  #DO NOT MODIFY, function call must work as is                                                                                                                                          
            if person_detected: #DO NOT MODIFY, function call must work as is 
                print("Person Detected") #DO NOT MODIFY, function call must work as is 
                sensehat.alarm(sense,interval)  #DO NOT MODIFY, function call must work as is 
            else:
                print("No Person Detected") #DO NOT MODIFY, function call must work as is 
            count += 1


if __name__ == "__main__":
    main()
