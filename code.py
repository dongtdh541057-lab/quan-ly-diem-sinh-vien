import pandas as pd

data = {
    "Họ và Tên": [
        "Đỗ Thị Ngọc Cầm",
        "Nguyễn Thị Mỹ Duyên",
        "Nguyễn Xuân Dự",
        "Trương Đình Hải Đông",
        "Nguyễn Tuấn Hào",
        "Nguyễn Dũ Hào",
        "Đặng Anh Hạo",
        "Võ Văn Quy",
        "Nguyễn Thanh Việt",
        "Nguyễn Thị Trúc Mai"
    ],
    "Điểm Chuyên Cần": [9, 8, 7, 6, 9, 8, 5, 7, 6, 10],
    "Điểm Giữa Kỳ": [8, 7, 6, 7, 9, 8, 8, 7, 6, 9],
    "Điểm Cuối Kỳ": [9, 8, 7, 8, 9, 7, 5, 8, 6, 10]
}

# Yêu cầu 1: Tạo DataFrame
df = pd.DataFrame(data)

print("Bảng Dữ Liệu 10 Sinh Viên")
print(df)

# Yêu cầu 2: Tính Điểm Tổng Kết
df["Tong_ket"] = (
    0.2 * df["Điểm Chuyên Cần"]
    + 0.3 * df["Điểm Giữa Kỳ"]
    + 0.5 * df["Điểm Cuối Kỳ"]
).round(2)

print("\nBẢNG ĐIỂM TỔNG KẾT")
print(df)




# Yêu cầu 3: Xếp Loại Sinh Viên
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

# Thêm cột Xep_loai 
df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# Hiển thị bảng điểm và xếp loại
print("\nBẢNG ĐIỂM VÀ XẾP LOẠI SINH VIÊN")
print(df)


# Yêu cầu 4: Thống kê

# Tính Điểm trung bình của lớp
diem_trung_binh = df["Tong_ket"].mean()
print("\nĐiểm tổng kết trung bình của lớp:", round(diem_trung_binh, 2))

# Tìm sinh viên có điểm tổng kết cao nhất
sv_cao_nhat = df.loc[df["Tong_ket"].idxmax()]
print("\nSinh viên có điểm tổng kết cao nhất:")
print("Họ và tên:", sv_cao_nhat["Họ và Tên"])
print("Điểm tổng kết:", sv_cao_nhat["Tong_ket"])

# Tìm sinh viên có điểm tổng kết thấp nhất
sv_thap_nhat = df.loc[df["Tong_ket"].idxmin()]
print("\nSinh viên có điểm tổng kết thấp nhất:")
print("Họ và tên:", sv_thap_nhat["Họ và Tên"])
print("Điểm tổng kết:", sv_thap_nhat["Tong_ket"])

# Dếm số sinh viên đạt
so_sinh_vien_dat = (df["Tong_ket"] >= 5).sum()
print("\nSố sinh viên đạt:", so_sinh_vien_dat)


