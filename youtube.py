from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    """
    Downloads the highest-resolution MP4 video from YouTube.

    Args:
        url (str): The YouTube video URL.
        save_path (str): The folder where the video should be saved.
    """
    try:
        yt = YouTube(url)  # Create a YouTube object
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        
        # Get the highest resolution video available
        highest_res_stream = streams.order_by("resolution").desc().first()

        if highest_res_stream:
            print(f"Downloading: {yt.title} ({highest_res_stream.resolution})")
            highest_res_stream.download(output_path=save_path)
            print("✅ Video downloaded successfully!")
        else:
            print("⚠ No suitable video stream found.")
    except Exception as e:
        print(f"❌ Error: {e}")

def open_file_dialog():
    """
    Opens a folder selection dialog and returns the selected folder path.

    Returns:
        str: The selected directory path or an empty string if no folder was selected.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the root Tkinter window
    root.attributes('-topmost', 1)  # Bring the file dialog to the front

    folder = filedialog.askdirectory()  # Open folder selection dialog
    if folder:
        print(f"📁 Selected folder: {folder}")
    else:
        print("⚠ No folder selected.")

    return folder

if __name__ == "__main__":
    # Get the YouTube video URL from the user
    video_url = input("🎥 Please enter a YouTube URL: ").strip()

    # Open file dialog to choose save directory
    save_dir = open_file_dialog()

    # Start download if a valid directory was chosen
    if save_dir:
        print("⬇ Downloading video...")
        download_video(video_url, save_dir)
    else:
        print("❌ Invalid save location. Download canceled.")
