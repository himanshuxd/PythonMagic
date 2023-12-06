import os
from moviepy.editor import VideoFileClip

def is_low_resolution(file_path, threshold_width=426, threshold_height=240):
    try:
        clip = VideoFileClip(file_path)
        width, height = clip.size
        return width < threshold_width or height < threshold_height
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return False

def find_low_resolution_videos(folder_path):
    low_resolution_videos = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            # Check if the file is a video
            if file_path.lower().endswith((".mp4", ".avi", ".mkv", ".mov", ".wmv", ".webm")):
                print("Found : ", file_path)
                if is_low_resolution(file_path):
                    print("is low res")
                    low_resolution_videos.append(file_path)

    return low_resolution_videos

if __name__ == "__main__":
    folder_path = "\\path\\to\\folder"
    low_resolution_videos = find_low_resolution_videos(folder_path)

    print("Low Resolution Videos:")
    for video_path in low_resolution_videos:
        print(video_path)
