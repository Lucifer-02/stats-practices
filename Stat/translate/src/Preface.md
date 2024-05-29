# Preface

_What song the Sirens sang, or what name Achilles assumed when he hid among women, though puzzling questions, are not beyond all conjecture._

SIR THOMAS BROWNE (ENGLAND, 1605–1682)

## TO THE READER

Chúng tôi sẽ kể cho bạn nghe về một số vấn đề thú vị đã được nghiên cứu với sự trợ giúp của các phương pháp thống kê và chỉ cho bạn cách tự mình sử dụng các phương pháp này. Chúng tôi sẽ cố gắng giải thích tại sao các phương pháp này lại hiệu quả và những điều cần chú ý khi người khác sử dụng chúng. Ký hiệu toán học dường như chỉ gây nhầm lẫn cho nhiều người, vì vậy cuốn sách này dựa vào các từ, biểu đồ và bảng biểu; hầu như không có bất kỳ x hoặc y nào. Trên thực tế, ngay cả khi các nhà toán học chuyên nghiệp đọc sách kỹ thuật, mắt họ vẫn có xu hướng bỏ qua các phương trình. Điều họ thực sự muốn là một người bạn thông cảm, người sẽ giải thích các ý tưởng và vẽ ra những bức tranh đằng sau các phương trình. Chúng tôi sẽ cố gắng trở thành người bạn đó của những ai đọc cuốn sách của chúng tôi.

## WHAT IS STATISTICS?

Thống kê là nghệ thuật đưa ra những phỏng đoán bằng số về những câu hỏi khó hiểu.

- Tác dụng của phương pháp điều trị y tế mới là gì?
- Điều gì tạo nên sự giống nhau giữa cha mẹ và con cái, và nó mạnh đến mức nào?
- Tại sao sòng bạc kiếm được lợi nhuận khi chơi roulette?
- Ai sẽ thắng trong cuộc bầu cử tiếp theo? bao nhiêu khả năng?
- Có bao nhiêu người được tuyển dụng? thất nghiệp?

Đây là những vấn đề khó khăn và các phương pháp thống kê sẽ giúp ích rất nhiều nếu bạn muốn nghĩ về chúng. Các phương pháp này đã được phát triển trong hàng trăm năm bởi những người đang tìm kiếm câu trả lời cho câu hỏi của họ. Một số trong số họ sẽ được giới thiệu sau.

## AN OUTLINE

Phần I nói về thiết kế thí nghiệm. Với một thiết kế tốt, những kết luận đáng tin cậy có thể được rút ra từ dữ liệu. Một số nghiên cứu được thiết kế tồi cũng được thảo luận - vì vậy bạn có thể thấy những cạm bẫy và tìm hiểu những câu hỏi nên đặt ra khi đọc về một nghiên cứu. Thiết kế nghiên cứu có lẽ là chủ đề quan trọng nhất của chúng tôi; đó là lý do tại sao chúng tôi bắt đầu ở đó. Ý tưởng tưởng chừng đơn giản nhưng bề ngoài có thể gây nhầm lẫn: phần I rất sâu sắc.

Các nghiên cứu thường đưa ra rất nhiều con số nên cần phải có bản tóm tắt. Thống kê mô tả - nghệ thuật tóm tắt dữ liệu - được giới thiệu ở phần II. Các biểu đồ, giá trị trung bình, độ lệch chuẩn và đường cong chuẩn của ông đều được xem xét. Cuộc thảo luận tiếp tục ở phần III, trong đó trọng tâm là phân tích các mối quan hệ, ví dụ, sự phụ thuộc của thu nhập vào giáo dục. Ở đây, mối tương quan và hồi quy là chủ đề chính.

Phần lớn lý luận thống kê phụ thuộc vào lý thuyết xác suất, được thảo luận ở phần IV; sự kết nối được thực hiện thông qua các mô hình cơ hội được phát triển trong phần V. Đồng xu, xúc xắc và bánh xe roulette là những ví dụ chính trong phần IV và V. Giá trị kỳ vọng và sai số chuẩn được giới thiệu; biểu đồ xác suất được phát triển và sự hội tụ về đường cong chuẩn được thảo luận.

Suy luận thống kê - đưa ra những khái quát hóa có giá trị từ các mẫu - là chủ đề của phần VI - VIII. Phần VI là về ước tính. Ví dụ: Gallup Poll dự đoán số phiếu bầu như thế nào? Tại sao một số phương pháp lấy mẫu tốt hơn những phương pháp khác? Phần VII sử dụng các mô hình cơ hội để phân tích sai số đo lường và phát triển lý thuyết di truyền. Phần VIII giới thiệu các kiểm định có ý nghĩa, để đánh giá xem mẫu có phù hợp với các giả thuyết về tổng thể hay không. Như phần VI - VIII cho thấy, các suy luận thống kê phụ thuộc vào các mô hình ngẫu nhiên. Nếu mô hình sai, kết quả suy luận có thể khá lung lay.

Ngày nay, suy luận là nhánh của thống kê được các chuyên gia quan tâm nhất. Tuy nhiên, những người không chuyên về thống kê thường thấy thống kê mô tả là một nhánh hữu ích hơn và dễ hiểu hơn. Đó là lý do tại sao chúng tôi thực hiện thống kê mô tả trước khi suy luận. Phần cốt lõi của chủ đề của chúng tôi được trình bày trong các chương từ 1 đến 6, 13, 16 đến 21, 23 và 26. Sau đó, người đọc có thể duyệt bất cứ đâu. Các chương tiếp theo nên đọc có thể là 8, 10, 27 và 29.

## EXERCISES

Các phần trong mỗi chương thường có một bộ bài tập, có đáp án ở cuối sách. Nếu bạn thực hiện những bài tập này khi chúng xuất hiện và kiểm tra câu trả lời, bạn sẽ được thực hành những kỹ năng mới của mình - và tìm ra mức độ bạn đã thành thạo chúng. Mỗi chương (trừ chương 1 và 7) đều kết thúc bằng một loạt bài tập ôn tập. Cuốn sách không đưa ra đáp án cho những bài tập đó. Các chương 6, 15, 23 và 29 cũng có “bài tập ôn tập đặc biệt”, bao gồm tất cả các tài liệu trước đó. Những bài tập như vậy phải được trả lời mà không có manh mối do ngữ cảnh cung cấp.

Khi làm bài tập, bạn có thể muốn lật ngược các trang cho đến khi công thức liên quan được hiện thực hóa. Tuy nhiên, đọc cuốn sách phía sau sẽ tỏ ra rất bực bội. Bài tập ôn tập đòi hỏi nhiều hơn so với bài tập. Họ yêu cầu những phỏng đoán sơ bộ và đánh giá định tính. Nói cách khác, chúng đòi hỏi sự hiểu biết trực quan tốt về những gì đang diễn ra. Cách để phát triển sự hiểu biết đó là đọc tiếp cuốn sách.

Tại sao sách có nhiều bài tập đến mức không thể giải bằng cách cắm công thức vào? Lý do là rất ít bài toán thống kê trong đời thực có thể được giải theo cách đó. Việc mù quáng đưa vào các công thức thống kê đã gây ra rất nhiều nhầm lẫn. Vì vậy cuốn sách này dạy một cách tiếp cận khác: tư duy.

## GRAPHICS

Giống như các phiên bản trước, đồ họa máy tính được sử dụng rộng rãi để hiển thị dữ liệu. Tuy nhiên, các bản vẽ làm việc được thực hiện tự do; người đọc được khuyến khích thực hiện những bản phác thảo tương tự, thay vì bị đe dọa bởi độ chính xác quá cao. Cuốn sách vẫn có phim hoạt hình của Dana Fradon của The New Yorker.
