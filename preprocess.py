import argparse
import cv2
import os
import glob
import json

def process_structured_data(json_file_path, output_dir):
    print("Data preprocessing STARTED!")
    # Read the JSON file
    with open(json_file_path) as json_file:
        data = json.load(json_file)
    if not os.path.exists(output_dir):
        print('making directory')
        os.makedirs(output_dir)

    # Iterate over the videoData and text arrays in both the train and test sections
    num_text_prompts = 0
    num_videos = 0
    full_vid_list = ""
    text_file_path = "data/vid_list.txt"
    for section in ['train', 'test']:
        # for text, video_data in zip(data[section]['text'], data[section]['videoData']):
        if (section in data):
            for i, data_point in enumerate(data[section]):
                text, video_data = data_point[0], data_point[1]
                # Check if the file has the .mp4 format
                if video_data.endswith('.mp4') or video_data.endswith('.mov'):
                    # Create the text file name
                    # Create the full path for the text file
                    # video_file_path_out = os.path.join(output_dir, video_data)
                    video_file_path_out = os.path.join(video_data)
                    # Create the text file
                    if i == 0:
                        next_line = ""
                    else:
                        next_line = "\n"
                    full_vid_list += f"{next_line}{video_file_path_out}|||{text}"
                    num_videos += 1
                    num_text_prompts += 1


    with open(text_file_path, 'w') as text_file:
        # Write the corresponding text from the text array as the content of the text file
        text_file.write(full_vid_list)
    print(f"Data preprocessing DONE: {num_text_prompts} text prompts -> {num_videos} videos")


# #input dir is folder of images and json is the json for anntoations corresponding to the images in appimate data folder
# input_dir = '/content/drive/MyDrive/Colab Notebooks/datasets/Appimate'
# json_file_path = '/content/drive/MyDrive/Colab Notebooks/datasets/Appimate/dataset.json'
# output_dir = '/content/drive/MyDrive/Colab Notebooks/datasets/Appimate/T2V/train_all_mp4'
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json_file_path", type=str, required=True, help="Path to Data Structure JSON file")
    parser.add_argument("--output_dir", type=str, default="/data/videos", required=True, help="Directory to output data")
    args = parser.parse_args()

    process_structured_data(args.json_file_path, args.output_dir)