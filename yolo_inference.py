from ultralytics import YOLO 

model = YOLO('path_model')

results = model.predict('input_videos/test_7.mp4',save=True)
print(results[0])
print('=====================================')
for box in results[0].boxes:
    print(box)