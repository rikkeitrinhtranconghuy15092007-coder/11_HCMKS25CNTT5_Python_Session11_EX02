# Số lượng phần tử: product_info ban đầu có 4 phần tử.

# Vị trí của "SP001": Nằm ở index 0.

# Vì sao dòng product_code = product_info[1] sai? Vì index trong Python bắt đầu từ 0. Index 1 là vị trí của tên sản phẩm, không phải mã sản phẩm.

# Vị trí của "Áo polo nam": Nằm ở index 1.

# Vì sao dòng product_name = product_info[2] sai? Vì index 2 là vị trí của kích cỡ ("Size L").

# Lỗi .length(): Dòng product_info.length() bị lỗi vì kiểu dữ liệu tuple trong Python không có phương thức này.

# Hàm thay thế: Phải dùng hàm len(product_info).

# Lỗi thay đổi giá trị (product_info[3] = 279000): Dòng này không hợp lệ vì tuple là kiểu dữ liệu immutable (bất biến), không cho phép sửa trực tiếp phần tử sau khi tạo.

# Cách xử lý: Phải tạo một tuple mới chứa giá bán mới.

# Thông tin sản phẩm ban đầu
product_info = ("SP001", "Áo polo nam", "Size L", 299000)

# Lấy mã sản phẩm (Sửa index thành 0)
product_code = product_info[0]

# Lấy tên sản phẩm (Sửa index thành 1)
product_name = product_info[1]

# Đếm số lượng thông tin sản phẩm (Dùng hàm len())
product_length = len(product_info)

# Cập nhật giá bán bằng cách tạo một tuple mới hoàn toàn
product_info = (product_info[0], product_info[1], product_info[2], 279000)

# Hiển thị kết quả
print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", product_info)
