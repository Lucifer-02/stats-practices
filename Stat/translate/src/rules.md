# Thuật ngữ

- Tất cả các thuật ngữ được để nguyên ở tiếng Anh và
- Chỉ các thuật ngữ được highlight theo format: `<term>`
- Viết thường
- Tên tổ chức để nguyên tiếng Anh

# Dịch

- Nếu dịch chưa rõ nghĩa mà vẫn chưa tìm được nghĩa phù hợp thì vẫn để bản dịch đó, sau này sẽ quay lại khi có ý tưởng

# Chú thích

- Nội dung được đặt làm footnote markdown
- Đánh số theo đúng số trong sách(dù markdown sẽ tự động đánh số lại)

# Danh ngôn

- In nghiêng nội dung
- Tên tác giả bỏ dấu -- đầu dòng và xuống dòng

# Hội thoại

- Người nói: in đậm, không dịch khi không cần thiết
- Theo sau người nói là dấu `: `

# Ký hiệu, công thức

- Trừ phép toán phức tạp hơn và biểu thức không cần dùng Latex. Lý do là để đơn giản hóa source và có thể copy liền mạch nội dung output

- Không dịch công thức

- Nếu có văn bản trong công thức thì dùng `\text{}` thay vì `\\ ` để tạo khoảng trắng trong văn bản, không dịch

- Khoảng trăng trong công thức: `−1.5 \quad −0.5 \quad 0 \quad 0.5 \quad 1.5`

- Căn chỉnh công thức:
  \\[
  \begin{align*}
  a &= b & c &= d \\\\
  e &= f & g &= h & r &= k
  \end{align*}
  \\]

# Số liệu

- Nếu trong sách gốc ở dạng bảng kẻ ô thì để dạng bảng, còn không thì để dạng code block
- Trong câu văn thì in đậm

# Ảnh

- Tên ảnh đặt theo tên ảnh trong sách.
  <!-- Vd: `![](fig3.png)` -->
  <center><img src="fig2.png" width="90%" height="auto"></center>

- Ảnh không có tên thì đặt theo tên đề cập trong văn bản hoặc theo nội dung ảnh. Vd: `![](vote.jpg)`
- Caption format:

**<center>abc</center>**

- Short:
**<center>
</center>**
<center><img src="fig2.png" width="90%" height="auto"></center>

- Ảnh được đặt ngay sau đoạn văn nhắc đến nó(trong sách gốc, để bố trí trang hợp lý, ảnh có thể bị di chuyển ra sau, điều này là không cần thiết trong format bản dịch)

# Bảng

| Syntax    | Description |
| --------- | ----------- |
| Header    | Title       |
| Paragraph | Text        |

# Nhấn mạnh

- In hoa

# Tham chiếu

[Mục 5.1][sec5.1]
[sec5.1]: ../ch05/ch05-01.md
hoặc
[Mục 18.3](../ch18/ch18-03.md)

# Quy trình

> Mục tiêu hướng đến là sau khi viết nội dung theo sách gốc, ta có thể chuyển sang side by side source và sách dịch.

1. Từ sách gốc, dịch và thay thế thuật ngữ. Công thức, ký hiệu theo bản gốc.
2. Thêm phần chú thích, hình ảnh, bảng.
3. Chuyển sang edit format sách dịch.
