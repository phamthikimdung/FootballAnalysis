
# Công Cụ Phân Tích Video Và Theo Dõi Đối Tượng (Cầu Thủ, Bóng) 

## Giới Thiệu

Đây là công cụ tự động phân tích video, theo dõi đối tượng (cầu thủ, bóng) và ước tính các thông số như tốc độ, khoảng cách di chuyển, kiểm soát bóng, và di chuyển của camera. Công cụ này được thiết kế để xử lý các video thể thao, giúp hiển thị các thông tin theo dõi và phân tích dưới dạng video được chú thích.

## TỔNG QUAN
## BEFORE
https://github.com/user-attachments/assets/f45b7b71-d032-48ed-b7b6-437ed162f274

## AFTER
https://github.com/user-attachments/assets/63bd6b5b-dc79-40b4-9a03-02c61be2413c

## Nội Dung

### 1. Giới Thiệu về Công Cụ Phân Tích Video

**Tổng quan:**  
Công cụ phân tích video này sử dụng các mô hình học sâu để theo dõi vị trí của đối tượng (cầu thủ, bóng) trong mỗi khung hình video, ước tính các chuyển động của camera và cung cấp các phân tích như đội bóng của cầu thủ và kiểm soát bóng. Kết quả sẽ được xuất dưới dạng video chú thích hoàn chỉnh.

**Tính năng:**
- **Đọc và lưu video**: Đọc video từ tệp đầu vào và lưu video đã phân tích.
- **Theo dõi đối tượng**: Sử dụng mô hình được huấn luyện để theo dõi đối tượng qua các khung hình.
- **Ước tính chuyển động của camera**: Điều chỉnh vị trí đối tượng dựa trên sự di chuyển của camera.
- **Phân loại đội bóng**: Tự động gán đội bóng cho cầu thủ dựa trên màu sắc trang phục.
- **Ước tính tốc độ và khoảng cách**: Tính toán tốc độ và khoảng cách di chuyển của đối tượng.
- **Chú thích video**: Vẽ chú thích trên video như vị trí, tốc độ, đội bóng, và kiểm soát bóng.

### 2. Công Cụ và Gói Cần Thiết

- **Python 3.9 hoặc cao hơn:** Ngôn ngữ lập trình chính.
- **OpenCV:** Thư viện xử lý ảnh và video.
- **NumPy:** Thư viện tính toán khoa học.
- **Các mô hình theo dõi đối tượng và các module hỗ trợ khác** như `utils`, `trackers`, `team_assigner`, `player_ball_assigner`, `camera_movement_estimator`, `view_transformer`, và `speed_and_distance_estimator`.

### 3. Hướng Dẫn Chi Tiết

#### Bước 1: Thiết Lập Cơ Bản
1. Tạo cấu trúc dự án và môi trường ảo.
2. Cài đặt các gói cần thiết:

```bash
pip install opencv-python numpy
```

3. Đảm bảo các tệp mô hình đã được huấn luyện trước như `models/best.pt` có sẵn trong thư mục dự án.

#### Bước 2: Chạy Công Cụ Phân Tích Video

1. **Đọc video đầu vào**: Video được đọc từ đường dẫn `'input_videos/test_7.mp4'`.
2. **Theo dõi đối tượng**: Sử dụng mô hình huấn luyện để theo dõi các cầu thủ và bóng trong video.
3. **Ước tính chuyển động của camera**: Điều chỉnh vị trí cầu thủ và bóng dựa trên sự di chuyển của camera giữa các khung hình.
4. **Gán đội bóng cho cầu thủ**: Tự động nhận diện đội bóng của cầu thủ dựa trên màu áo.
5. **Gán quyền kiểm soát bóng**: Xác định cầu thủ nào đang kiểm soát bóng trong từng khung hình.
6. **Ước tính tốc độ và khoảng cách**: Tính toán và thêm thông tin về tốc độ và khoảng cách di chuyển của các đối tượng vào video.
7. **Xuất video**: Lưu video đã chú thích với các phân tích chi tiết vào thư mục `output_videos/` dưới dạng tệp `.mp4`.

#### Bước 3: Chạy Lệnh

Để chạy công cụ, sử dụng lệnh sau:

```bash
python main.py
```

Video đầu ra với các chú thích sẽ được lưu tại `output_videos/output_video.mp4`.

### 4. Kết Luận

Công cụ phân tích video này giúp tự động hóa việc theo dõi và phân tích các trận đấu thể thao. Với khả năng gán đội bóng, theo dõi quyền kiểm soát bóng, và ước tính tốc độ, khoảng cách, công cụ này có thể hỗ trợ việc phân tích video một cách hiệu quả và chi tiết.

## Liên Hệ

Nếu có bất kỳ câu hỏi hoặc thắc mắc nào, vui lòng liên hệ qua email: [phamthikimdung.it@gmail.com].
