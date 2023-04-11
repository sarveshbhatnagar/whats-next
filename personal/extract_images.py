import cv2
import os
import math
import glob

def extract_frames(video_path, dest_path):
    # Create destination directory if it doesn't exist
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    # Open video file
    cap = cv2.VideoCapture(video_path)

    # Get total number of frames and FPS
    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Extract first frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(os.path.join(dest_path, 'frame1.jpg'), frame)

    # Extract middle frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, math.floor(num_frames/2))
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(os.path.join(dest_path, 'frame2.jpg'), frame)

    # Release video file
    cap.release()

# Example usage
# extract_frames('../data/videos/__bdFiweOJY.mp4', '../data/frames/__bdFiweOJY')
# print("DONE")

if __name__ == '__main__':
    video_paths = glob.glob('../data/videos/*')
    for video_path in video_paths:
        video_id = video_path.split('/')[-1]
        dest_path = os.path.join('../data/frames', video_id)
        extract_frames(video_path, dest_path)
