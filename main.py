import cv2
import os

directoryFiles = os.listdir(".")
print(directoryFiles)

videos = list(filter(lambda k: '.mp4' in k, directoryFiles))
print(videos)

sortedVideos = sorted(videos);
print(sortedVideos)

totalvideos = len(sortedVideos)

counter = 0;

currentVideo = 0

cap = cv2.VideoCapture(sortedVideos[currentVideo])
if not cap.isOpened():
  print("Cannot initialize cap.")
  exit()

# Get length of the video.
video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# Initialize count.
count = 0


fps = cap.get(cv2.CAP_PROP_FPS)      # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = frame_count/fps
duration_seconds = duration % 60

ret, frame = cap.read()


count = 0


playedTimes = 0;
quit = False

timeToChange = int(input("Enter the video change time in seconds: "))

while not quit:

    # Frames loop.
    if count == timeToChange:
        print('count:', count)
        count = 0
        currentVideo += 1
        if currentVideo > (totalvideos-1):
            currentVideo = 0
        cap = cv2.VideoCapture(sortedVideos[currentVideo])
        if not cap.isOpened():
            print("Cannot initialize cap.")
            exit()

        # Get length of the video.
        video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        # Initialize count.
        count = 0

        fps = cap.get(cv2.CAP_PROP_FPS)  # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps
        duration_seconds = duration % 60

        ret, frame = cap.read()

        count = 0

        playedTimes = 0;


    # Check length of the video.
    if count == video_length:
        # Reset to the first frame. Returns bool.
        _ = cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        count = 0
        playedTimes += 1
        print('Current video repeated times: ', playedTimes)

    # Get the frame.
    success, image = cap.read()
    if not success:
        print("Cannot read frame.")
        break

    # do something with the image.
    cv2.imshow("Frame", image)

    # Quit by pressing 'q'.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        quit = True
    count += 1

    # Post loop.
cap.release()
cv2.destroyAllWindows()







# input time in seconds
