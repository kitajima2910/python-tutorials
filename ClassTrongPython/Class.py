class SinhVien:

    def __init__(sinhVien, tenSinhVien, tuoiSinhVien):
        sinhVien.tenSinhVien = tenSinhVien
        sinhVien.tuoiSinhVien = tuoiSinhVien

    def thongTinSinhVien(sinhVien):
        print('Tên sinh viên: ', sinhVien.tenSinhVien)
        print('Tuổi sinh viên: ', sinhVien.tuoiSinhVien)

sv = SinhVien('Phạm Xuân Hoài', 25)

sv.thongTinSinhVien()