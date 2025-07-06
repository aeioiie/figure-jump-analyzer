import cv2
import os

# 영상 파일 경로 설정
video_path = "videos/yuna_jump.mp4"
# 프레임 저장 폴더 경로 설정
output_folder = "frames"
# 저장 폴더 없으면 생성
os.makedirs(output_folder, exist_ok=True)
# 영상 파일 열기
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("영상 파일을 열 수 없습니다.")
    exit()
# 프레임 반복 추출
frame_count = 0
while True:
    # 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        break
    filename = f"{output_folder}/frame_{frame_count:04d}.jpg"
    cv2.imwrite(filename, frame)
    frame_count += 1

cap.release()

print(f"총 {frame_count}개의 프레임 저장 완료")