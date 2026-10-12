
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# =====================================
# 1. TAO DATAFRAME 10 SINH VIEN
# =====================================

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

df = pd.DataFrame(data)

# =====================================
# 2. TINH DIEM TONG KET
# =====================================

df["Tong_ket"] = (
    0.2 * df["Điểm Chuyên Cần"]
    + 0.3 * df["Điểm Giữa Kỳ"]
    + 0.5 * df["Điểm Cuối Kỳ"]
).round(2)

# =====================================
# 3. XEP LOAI SINH VIEN
# =====================================

def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# =====================================
# 4. THONG KE
# =====================================

diem_trung_binh = df["Tong_ket"].mean()
sv_cao_nhat = df.loc[df["Tong_ket"].idxmax()]
sv_thap_nhat = df.loc[df["Tong_ket"].idxmin()]
so_sinh_vien_dat = (df["Tong_ket"] >= 5).sum()

# =====================================
# 5. CAU HINH STREAMLIT
# =====================================

st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    page_icon="📚",
    layout="wide"
)

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# =====================================
# 6. HIEN THI BANG DIEM
# =====================================

st.subheader("1. Bảng điểm 10 sinh viên")

bang_diem = df.rename(columns={
    "Họ và Tên": "Họ tên",
    "Điểm Chuyên Cần": "Chuyên cần",
    "Điểm Giữa Kỳ": "Giữa kỳ",
    "Điểm Cuối Kỳ": "Cuối kỳ",
    "Tong_ket": "Tổng kết",
    "Xep_loai": "Xếp loại"
})

st.dataframe(
    bang_diem,
    use_container_width=True,
    hide_index=True
)

# =====================================
# 7. HIEN THI THONG KE
# =====================================

st.subheader("2. Thống kê kết quả học tập")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Điểm trung bình lớp",
    f"{diem_trung_binh:.2f}"
)

col2.metric(
    "Điểm cao nhất",
    f"{sv_cao_nhat['Tong_ket']:.2f}"
)

col3.metric(
    "Điểm thấp nhất",
    f"{sv_thap_nhat['Tong_ket']:.2f}"
)

col4.metric(
    "Số sinh viên đạt",
    f"{so_sinh_vien_dat}/10"
)

st.write(
    f"Sinh viên có điểm cao nhất: "
    f"**{sv_cao_nhat['Họ và Tên']}** "
    f"({sv_cao_nhat['Tong_ket']:.2f} điểm)"
)

st.write(
    f"Sinh viên có điểm thấp nhất: "
    f"**{sv_thap_nhat['Họ và Tên']}** "
    f"({sv_thap_nhat['Tong_ket']:.2f} điểm)"
)

# =====================================
# 8. SELECTBOX TRA CUU SINH VIEN
# =====================================

st.subheader("3. Tra cứu điểm sinh viên")

ten_sv = st.selectbox(
    "Chọn sinh viên:",
    df["Họ và Tên"].tolist()
)

sv = df[df["Họ và Tên"] == ten_sv].iloc[0]

st.write(f"**Họ và tên:** {sv['Họ và Tên']}")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Điểm chuyên cần",
    f"{sv['Điểm Chuyên Cần']:.2f}"
)

col2.metric(
    "Điểm giữa kỳ",
    f"{sv['Điểm Giữa Kỳ']:.2f}"
)

col3.metric(
    "Điểm cuối kỳ",
    f"{sv['Điểm Cuối Kỳ']:.2f}"
)

col1, col2 = st.columns(2)

col1.metric(
    "Điểm tổng kết",
    f"{sv['Tong_ket']:.2f}"
)

col2.metric(
    "Xếp loại",
    sv["Xep_loai"]
)

# =====================================
# 9. VE BIEU DO COT
# =====================================

st.subheader("4. Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(12, 6))

bars = ax.bar(
    df["Họ và Tên"],
    df["Tong_ket"]
)

ax.set_title("ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN")
ax.set_xlabel("Họ và tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)

plt.xticks(rotation=45, ha="right")

# Hien thi gia tri tren dau cot
for bar in bars:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.1,
        f"{bar.get_height():.2f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# =====================================
# 10. THONG TIN NGUOI TAO
# =====================================

st.divider()

st.caption(
    "Người tạo: Trương Đình Hải Đông | MSSV: Nhập MSSV của bạn"
)
