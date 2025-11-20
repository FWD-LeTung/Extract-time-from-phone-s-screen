import cv2
import os
import sys
import argparse

def extract_from_video(input_path, output_path):
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    
    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        print("Input Video path is not existed")
        return 
    
    frame_count = 0
    while True:
        ret, frame = cap.read()

        if not ret:
            break
        frame_name = os.path.join(output_path, f'framr_{frame_count}.jpg')
        cv2.imwrite(frame_name,frame)
        frame_count += 1
    
    cap.release()
    print(f'Extract frame from {input_path} successfull, total frame coun: {frame_count}')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path')
    parser.add_argument('output_path')

    arg = parser.parse_args()

    extract_from_video(arg.input_path, arg.output_path)

if __name__ == '__main__':
    main()