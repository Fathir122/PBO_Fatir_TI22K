import cv2

def play_video(file_path):
    try:
        # Open the video file
        cap = cv2.VideoCapture(file_path)

        # Check if the video file is opened successfully
        if not cap.isOpened():
            print(f"Error opening video file: {file_path}")
            return

        # Get the video's width and height
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Create a window to display the video
        cv2.namedWindow("Video Player", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Video Player", width, height)

        while True:
            ret, frame = cap.read()

            if not ret:
                break

            cv2.imshow("Video Player", frame)

            # Check for the 'q' key to quit the video
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break

        # Release the video capture object and close the window
        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"Error playing video: {e}")

if _name_ == "_main_":
    video_path = r'C:\Users\nazar\PBO\Pertemuan_3\Media\Wireless Drinking.mp4'
    play_video(video_path)