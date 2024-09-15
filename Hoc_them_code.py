import time
tiep_tuc = 0
ten_nguoi_choi = input('Vui lòng nhập tên của bạn, điệp viên 001: ')
ten_nguoi_choi_1 = ten_nguoi_choi.strip()
ten_nguoi_choi_he_thong = ten_nguoi_choi_1.title()
print('Chào mừng đến với văn phòng làm việc, điệp viên',ten_nguoi_choi_he_thong,'!')
time.sleep(2)
print('Hiệp tại hệ thống kiểm soát an ninh mạng của chúng ta đang bị hacker tấn công, nhiệm vụ của bạn là phải\nđoán được mật khẩu của chúng dựa trên những gợi ý cho trước.')
time.sleep(3)
print('Tổng cộng có 3 mật mã cần bạn phá giải.')
time.sleep(2)
print('Mật mã đầu tiên: ')
time.sleep(2)
print('hAii23KKAassaaw1\n Chuyển chữ hoa thành chữ thường\n Chuyễn chữ thường thành chữ hoa\n Xóa tất cả các chữ số')
time.sleep(2)
dap_an_1 = str(input('Hãy giải mã mật khẩu trên: '))
if dap_an_1 == 'HaIIkkaASSAAW':
    print('Xin chúc mừng! Cậu đã phá giải thành công mật khẩu... dễ nhất.\n Tôi có chút tự hào đấy.')
    tiep_tuc = 1
else: 
    print('ĐÁP ÁN LÀ: HaIIkkaASSAAW')
    time.sleep(2)
    print('Thật là một điệp viên non trẻ! Xin lỗi, nhưng cậu đã bị đuổi!')
    tiep_tuc = 0
if tiep_tuc == 1:
    time.sleep(2)
    print('Mật mã thứ 2: ')
    time.sleep(2)
    print('sdososlq1212jdSj81j01so0s1wj0s12JS12\n Viết hoa chữ cái đầu tiên\n cộng các số đứng liên tiếp lại với nhau\n Thêm 2 dấu * ở hai đầu\n thêm 3 dấu _ ở phía bên phải \n Nếu chữ s đứng cạnh chứ o, viết hoa tất cả chứ s và 0 đứng bên cạnh hai chữ ấy \n Ghi thường chữ cái cuối cùng')
    time.sleep(2)
    dap_an_2 = str(input('Hãy giải mã mật khẩu hơi dài trên: '))
    if dap_an_2 == '**SdOSOSlq6jdSj9j1so0s1wj0s3Js3**___':
        print('Xin chúc mừng! Cậu đã phá giải thành công mật khẩu... hơi dài.\n Cậu có lẽ khá giỏi đấy!')
        tiep_tuc = 2
    else: 
        print('ĐÁP ÁN LÀ: **SdOSOSlq6jdSj9j1so0s1wj0s3Js3**___')
        time.sleep(2)
        print('Không sao! Chúng tôi hiểu công việc này có lẽ quá sức với cậu. CẬU BỊ ĐUỔI!')
        tiep_tuc = 0
    if tiep_tuc == 2:
        time.sleep(2)
        print('Mật mã cuối cùng: ')
        time.sleep(2)
        print('23HhAi gUp23 jahsw 223 jshas2 whhhs2sx i2so 22 eija 23d kdshosdk 232h31\n thêm vào đầu mỗi từ bằng tổng số từ\n Thêm vào cuối mỗi từ bằng tổng số chữ cái (bao gồm số và chữ)\n Bỏ tất cả dấu cách và thay bằng số 23 \n Viết hoa tất cả chữ j\n thêm vào số lượng chứ H thường ở phía cuối và chuyển số đó thành chữ luôn (không dấu)')
        time.sleep(2)
        dap_an_3 = str(input('Hãy giải mã mật khẩu siêu khó tối thượng trên!!?!??!: '))
        if dap_an_3 == '1223HhAi842312gUp23842312Jahsw842312223842312Jshas2842312whhhs2sx842312i2so84231222842312eiJa84231223d842312kdshosdk842312232h3184tam':
            print('Xin chúc mừng! Chính thức được nhận vào\n Hãy cống hiến hết mình cho trụ sở hacker xấu xa của chúng ta nhé! :)')
            tiep_tuc = 3
        else:
            print('ĐÁP ÁN LÀ: 1223HhAi842312gUp23842312Jahsw842312223842312Jshas2842312whhhs2sx842312i2so84231222842312eiJa84231223d842312kdshosdk842312232h3184tam')
            time.sleep(2)
            print('Quá gà')
            tiep_tuc = 4
        if tiep_tuc == 3:
            print('Bạn đã chính thức trở thành kẻ xấu (Bad ending)')
        if tiep_tuc == 4:
            print('Ngay từ đầu bạn đã nhận ra đây là một tổ chức xấu xa nên cố tình trả lời sai.\n Bạn trở về nhà và tiếp tục tìm cách để xin vào một công việc chân chính khác (Best ending (hay còn được gọi là good ending))')