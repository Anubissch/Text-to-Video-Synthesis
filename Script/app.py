import cv2
import torch
import tkinter as tk
from tkinter import Button, Label, scrolledtext
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video
from PIL import Image, ImageTk
import imageio
import numpy as np

def export_to_video(frames, output_video_path="output_video.mp4", fps=5):
    # Create video writer
    video_writer = imageio.get_writer(output_video_path, fps=fps)

    try:
        for frame in frames:
            # Reshape the frame to (height, width, channels)
            frame = frame[0]

            # Convert the frame to uint8
            frame = (frame * 255).astype(np.uint8)

            video_writer.append_data(frame)
    finally:
        video_writer.close()

    return output_video_path

class TextToVideoApp:
    def __init__(self, master):
        self.master = master
        master.title("Text-to-Video Synthesis by HeroTheGreat")
        master.configure(bg='#f0f0f0')  # Set background color to grey

        self.label = Label(master, text="Enter Text:", bg='#f0f0f0')
        self.label.pack()

        self.text_entry = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=4)
        self.text_entry.pack()

        self.generate_button = Button(master, text="Generate Video", command=self.generate_video)
        self.generate_button.pack()

        self.loading_label = Label(master, text="", bg='#f0f0f0')  # Add label for loading text
        self.loading_label.pack()

        self.video_display = tk.Label(master)
        self.video_display.pack()

    def generate_video(self):
        # Get text from the entry
        prompt = self.text_entry.get("1.0", tk.END).strip()

        # Display loading text
        self.loading_label.config(text="Generating video...")

        # Load the DiffusionPipeline
        pipe = DiffusionPipeline.from_pretrained("damo-vilab/text-to-video-ms-1.7b", torch_dtype=torch.float16, variant="fp16")
        pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
        pipe.enable_model_cpu_offload()

        # Generate video frames
        video_frames = pipe(prompt, num_inference_steps=25).frames

        # Export video and get the file path
        video_path = export_to_video(video_frames, output_video_path="output_video.mp4")

        # Display the video in the UI
        self.display_video(video_path)

        # Hide loading text
        self.loading_label.config(text="")

    def display_video(self, video_path):
        cap = cv2.VideoCapture(video_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=img)
            self.video_display.config(image=img)
            self.video_display.image = img
            self.master.update()
        cap.release()

def main():
    root = tk.Tk()
    app = TextToVideoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
