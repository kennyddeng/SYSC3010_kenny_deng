from picamera import PiCamera
from time import sleep

# returns camera instance
def get_camera():
    return PiCamera()

# Input camera instance and preview_time
# displays camera preview for a preview_time
def camera_preview(camera, preview_time):
    camera.start_preview()
    sleep(preview_time)
    camera.stop_preview()
    
# input camera instance and degree
# rotates camera # of degrees
def rotate_camera(camera, degrees):
    camera.rotation(degrees)

# input camera instance, output image location, countdown time, and preview image Boolean
# if preview is true, preview is started
# code waits indicated countdown time before image is taken and stored in indicated location
# preview is stopped if it was started
def capture_image(camera, image_out_location, countdown_time, preview):
    if preview == True:
        camera.start_preview()
        for i in range(countdown_time, 0, -1):
            print(i-1)
            sleep(1)
        camera.capture(image_out_location)
        camera.stop_preview()
    elif preview == False:
        for i in range(countdown_time, 0, -1):
            print(i-1)
            sleep(1)
        camera.capture(image_out_location)
    else:
        sleep(countdown_time)
        camera.capture(image_out_location)

# input camera instance, output video location, video length, countdown time, and preview Boolean
# if preview is true, preview is started
# code waits indicated countdown time before image is taken and stored in indicated location
# preview is stopped if it was started
def capture_video(camera, video_out_location, video_length, countdown_time, preview):
    if preview == True:
        camera.start_preview()
        for i in range(countdown_time, 0, -1):
            print(i-1)
            sleep(1)
        camera.start_recording(image_out_location)
        sleep(video_length)
        camera.stop_recording()
        camera.stop_preview()
    elif preview == False:
        for i in range(countdown_time, 0, -1):
            print(i-1)
            sleep(1)
        camera.start_recording(image_out_location)
        sleep(video_length)
        camera.stop_recording()
