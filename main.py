import cv2
import os
import shutil

# 영상 파일 경로 설정
video_path = "videos/yuna_jump.mp4"
# 프레임 저장 폴더 경로 설정
output_folder = "frames"
# 저장 폴더 없으면 생성
if os.path.exists(output_folder):
    # 기존 폴더가 있다면 삭제
    shutil.rmtree(output_folder)
os.makedirs(output_folder, exist_ok=True)
# 영상 파일 열기
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("영상 파일을 열 수 없습니다.")
    exit()

# 프레임 간격 설정(5프레임마다 지정)
save_every = 5
frame_count = 0
saved_count = 0

while True:
    # 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        break
    
    if frame_count % save_every == 0:
        filename = f"{output_folder}/frame_{frame_count:04d}.jpg"
        cv2.imwrite(filename, frame)
        saved_count += 1
    
    frame_count += 1

cap.release()

print(f"총 {frame_count}개의 프레임 저장 완료")