# (1) Phân tích lỗi
# Dictionary employee gồm những key nào?
# → "employee_id", "full_name", "department", "status"
# Vì sao dòng employee_id = employee[0] gây lỗi?
# → Dictionary không truy cập bằng index (như list). employee[0] đang tìm key tên 0, không tồn tại → KeyError: 0
# Dictionary có truy cập phần tử bằng index giống list không?
# → Không. Dictionary truy cập bằng key (string/number).
# Lấy mã nhân viên đúng:
# Pythonemployee_id = employee["employee_id"]
# Vì sao dòng full_name = employee["name"] gây lỗi?
# → Không tồn tại key "name".
# Key đúng để lấy họ tên: "full_name"
# Vì sao dòng employee["employee_status"] = "official" chưa đúng?
# → Sai key. Nó tạo key mới "employee_status" thay vì cập nhật key "status" đã có.
# Key đúng để cập nhật trạng thái: "status"
# Vì sao dòng employee.append("base_salary", 15000000) gây lỗi?
# → Dictionary không có phương thức append() (append là của list).
# Cách thêm lương cơ bản đúng:
# Pythonemployee["base_salary"] = 15000000
# Vì sao dòng del employee["team"] gây lỗi?
# → Không tồn tại key "team".
# Key cần xóa (phòng ban): "department"

# Thông tin nhân viên ban đầu
employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

# Lấy mã nhân viên
employee_id = employee["employee_id"]

# Lấy họ tên nhân viên
full_name = employee["full_name"]

# Cập nhật trạng thái nhân viên
employee["status"] = "official"

# Thêm lương cơ bản
employee["base_salary"] = 15000000

# Xóa thông tin phòng ban
del employee["department"]

# Kết quả
print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)