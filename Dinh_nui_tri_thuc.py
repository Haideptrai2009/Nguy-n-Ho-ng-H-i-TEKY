import time
import random
tong_diem = 0
lan_sai = 0
thong_bao_sai_1 = 'Bạn đã sai lần 1, tổng điểm hiện tại của bạn là: '
thong_bao_sai_2 = 'Bạn đã sai hai lần rồi, sai lần nữa là end game! Tổng điểm hiện tại của bạn là: '
nhap_dap_an = 'Nhập đáp án của bạn tại đây: '
dap_an_dung = 0
ten_nguoi_choi_nhap = str(input('Nhập tên của bạn vào đây nào: '))
ten_nguoi_choi_sua = ten_nguoi_choi_nhap.strip()
ten_nguoi_choi = ten_nguoi_choi_sua.title()
print("Chào mừng đến với trò chơi 'đỉnh cao trí thức',",ten_nguoi_choi,'!')
time.sleep(3)
print('Sẽ có 7 câu hỏi về toán học, tương đương với từng độ khó khác nhau!')
time.sleep(2)
print('Trả lời đúng mỗi câu bạn sẽ được 10 điểm!')
time.sleep(2)
print('Trả lời sai lần một sẽ bị trừ 5 điểm, lần hai sẽ bị trừ 20 điểm, lần ba thì sẽ thua!')
time.sleep(3)
print('Nhắc nhở quan trọng: nhớ cầm sẳn máy tính bỏ túi để tính đấy nhé!')
time.sleep(2)
sang_san = str(input('Bạn đã sẳn sàng chưa? (Có/Không): '))
print('Dù bạn có sẳn sàng hay không thì...')
time.sleep(1)
print('trò chơi bắt đầu!')
time.sleep(3)
#print('Quyền trợ giúp hiện tại: \n* Nhân đôi số điểm hiện tại nếu trả lời đúng câu này (a)\n* Bỏ qua câu hỏi này (b)\n* Hiển thị hai đáp án (1 cái đúng và 1 cái sai) (c)')
PT1_cau1 = random.randint(0,10)
PT2_cau1 = random.randint(0,10)
dap_an_dung = PT1_cau1 + PT2_cau1
print('\nCâu hỏi 1 trên 7 (cấp độ khó: non nớt):\n',PT1_cau1,'+',PT2_cau1,'= ?')
time.sleep(1)
dap_an_1 = int(input(nhap_dap_an))
if dap_an_1 == PT1_cau1 + PT2_cau1:
    tong_diem = tong_diem + 10
    print('Xin chúc mừng! Bạn có thêm 10 điểm, tổng điểm hiện tại của bạn là',tong_diem,'!')
    time.sleep(3)
else:
    lan_sai = lan_sai + 1
    if lan_sai == 1: 
        tong_diem = tong_diem - 5
        print(thong_bao_sai_1,tong_diem)
        print('Đáp án của câu trên là: ',dap_an_dung)
        time.sleep(2)
    elif lan_sai == 2:
        tong_diem = tong_diem - 20
        print(thong_bao_sai_2,tong_diem)
        print('Đáp án của câu trên là: ',dap_an_dung)
        time.sleep(2)
    else: 
        print('Bạn đã thua rồi :(, tổng điểm mà bạn đã đạt được là: ',tong_diem)
        exit()
PT1_cau2 = random.randint(99,999)
PT2_cau2 = random.randint(99,999)
dap_an_dung = PT1_cau2 + PT2_cau2
print('\nCâu hỏi thứ 2 trên 7 (cấp độ khó: khởi đầu):\n',PT1_cau2,'+',PT2_cau2,'= ?')
time.sleep(1)
dap_an_2 = int(input(nhap_dap_an))
if dap_an_2 == PT1_cau2 + PT2_cau2:
    tong_diem = tong_diem + 20
    print('Xin chúc mừng! Bạn có thêm 20 điểm, tổng điểm hiện tại của bạn là',tong_diem,'!')
    time.sleep(3)
else:
    lan_sai = lan_sai + 1
    if lan_sai == 1: 
        tong_diem = tong_diem - 5
        print(thong_bao_sai_1,tong_diem)
        print('Đáp án của câu trên là: ',dap_an_dung)
        time.sleep(2)
    elif lan_sai == 2:
        tong_diem = tong_diem - 20
        print(thong_bao_sai_2,tong_diem)
        print('Đáp án của câu trên là: ',dap_an_dung)
        time.sleep(2)
    else: 
        print('Bạn đã thua rồi :(, tổng điểm mà bạn đã đạt được là: ',tong_diem)
        exit()
PT1_cau3 = random.randint(200,5555)
PT2_cau3 = random.randint(200,5555)
PT3_cau3 = random.randint(200,5555)
dap_an_dung = PT1_cau3 + PT2_cau3 + PT3_cau3
print('\nCâu hỏi thứ 3 trên 7 (cấp độ khó: làm quen):\n',PT1_cau3,'+',PT2_cau3,'+',PT3_cau3,'= ?')
time.sleep(1)
dap_an_3 = int(input(nhap_dap_an))
if dap_an_3 == PT1_cau3 + PT2_cau3 + PT3_cau3:
    tong_diem = tong_diem + 30
    print('Xin chúc mừng! Bạn có thêm 30 điểm, tổng điểm hiện tại của bạn là',tong_diem,'!')
    time.sleep(3)
else:
    lan_sai = lan_sai + 1
    if lan_sai == 1: 
        tong_diem = tong_diem - 5
        print(thong_bao_sai_1,tong_diem)
        print('Đáp án của câu trên là: ',dap_an_dung)
        time.sleep(2)
    elif lan_sai == 2:
        tong_diem = tong_diem - 20
        print(thong_bao_sai_2,tong_diem)
        print('Đáp án của câu trên là: ',dap_an_dung)
        time.sleep(2)
    else: 
        print('Bạn đã thua rồi :(, tổng điểm mà bạn đã đạt được là: ',tong_diem)
        exit()
PT1_cau4 = random.randint(1001,10001)
PT2_cau4 = random.randint(1001,10001)
PT3_cau4 = random.randint(1001,10001)
dap_an_dung = PT1_cau4 + PT2_cau4 * PT3_cau4
print('\nCâu hỏi thứ 4 trên 7 (cấp độ khó: không còn dễ nữa):\n',PT1_cau4,'+',PT2_cau4,'x',PT3_cau4,'= ?')
time.sleep(1)
dap_an_4 = int(input(nhap_dap_an))
if dap_an_4 == PT1_cau4 + PT2_cau4 * PT3_cau4:
    tong_diem = tong_diem + 40
    print('Xin chúc mừng! Bạn có thêm 40 điểm, tổng điểm hiện tại của bạn là',tong_diem,'!')
    time.sleep(3)
else:
    lan_sai = lan_sai + 1
    if lan_sai == 1: 
        tong_diem = tong_diem - 5
        print(thong_bao_sai_1,tong_diem)
        print('Đáp án của câu trên là: ',dap_an_dung)
        time.sleep(2)
    elif lan_sai == 2:
        tong_diem = tong_diem - 20
        print(thong_bao_sai_2,tong_diem)
        print('Đáp án của câu trên là: ',dap_an_dung)
        time.sleep(2)
    else: 
        print('Bạn đã thua rồi :(, tổng điểm mà bạn đã đạt được là: ',tong_diem)
        exit()
PT2_cau5 = random.randint(-2000,-100)
PT3_cau5 = random.randint(-2000,-100)
PT1_cau5 = random.randint(-2000,-100)
dap_an_dung = PT1_cau5 - PT2_cau5 + PT3_cau5
print('\nCâu hỏi thứ 5 trên 7 (cấp độ khó: khó):\nTìm ?:\n? +',PT2_cau5,'-',PT3_cau5,'=',PT1_cau5)
time.sleep(1)
dap_an_5 = int(input(nhap_dap_an))
if dap_an_5 == PT1_cau5 - PT2_cau5 + PT3_cau5:
    tong_diem = tong_diem + 50
    print('Xin chúc mừng! Bạn có thêm 50 điểm, tổng điểm hiện tại của bạn là',tong_diem,'!')
    time.sleep(3)
else:
    lan_sai = lan_sai + 1
    if lan_sai == 1: 
        tong_diem = tong_diem - 5
        print(thong_bao_sai_1,tong_diem)
        print('Đáp án của câu trên là: ',dap_an_dung)
        time.sleep(2)
    elif lan_sai == 2:
        tong_diem = tong_diem - 20
        print(thong_bao_sai_2,tong_diem)
        print('Đáp án của câu trên là: ',dap_an_dung)
        time.sleep(2)
    else: 
        print('Bạn đã thua rồi :(, tổng điểm mà bạn đã đạt được là: ',tong_diem)
        exit()
PT2_cau6 = random.randint(-555,-200)
PT3_cau6 = random.randint(-555,-200)
PT1_cau6 = random.randint(-555,-200)
dap_an_dung = PT3_cau6 * (0-PT2_cau6) * PT1_cau6
print('\nCâu hỏi thứ 6 trên 7 (cấp độ khó: khó hơn):\nTìm ?:\n? :',PT1_cau6,': (-(',PT2_cau6,')) =',PT3_cau6)
time.sleep(1)
dap_an_6 = int(input(nhap_dap_an))
if dap_an_6 == PT3_cau6 * (0-PT2_cau6) * PT1_cau6:
    tong_diem = tong_diem + 60
    print('Xin chúc mừng! Bạn có thêm 60 điểm, tổng điểm hiện tại của bạn là',tong_diem,'!')
    time.sleep(3)
else:
    lan_sai = lan_sai + 1
    if lan_sai == 1: 
        tong_diem = tong_diem - 5
        print(thong_bao_sai_1,tong_diem)
        print('Đáp án của câu trên là: ',dap_an_dung)
        time.sleep(2)
    elif lan_sai == 2:
        tong_diem = tong_diem - 20
        print(thong_bao_sai_2,tong_diem)
        print('Đáp án của câu trên là: ',dap_an_dung)
        time.sleep(2)
    else: 
        print('Bạn đã thua rồi :(, tổng điểm mà bạn đã đạt được là: ',tong_diem)
        exit()
PT1_cau7 = random.randint(-100,-70)
PT2_cau7 = random.randint(-100,-70)
PT3_cau7 = random.randint(-100,-70)
PT4_cau7 = random.randint(-100,-70)
dap_an_dung = PT3_cau7 * (0-PT4_cau7) * PT1_cau7 * (0-PT2_cau7)
print('\nCâu hỏi thứ 7 trên 7 (câu hỏi cuối cùng) (cấp độ khó: khó hơn nữa):\nTìm ?:\n? :',PT1_cau7,': (-(',PT2_cau7,')) =',PT3_cau7,'* (-(',PT4_cau7,'))')
time.sleep(1)
dap_an_7 = int(input(nhap_dap_an))
if dap_an_7 == PT3_cau7 * (0-PT4_cau7) * PT1_cau7 * (0-PT2_cau7):
    tong_diem = tong_diem + 70
    print('Xin chúc mừng! Bạn có thêm 70 điểm, tổng điểm hiện tại của bạn là',tong_diem,'!')
    time.sleep(3)
else:
    lan_sai = lan_sai + 1
    if lan_sai == 1: 
        tong_diem = tong_diem - 5
        print(thong_bao_sai_1,tong_diem)
        print('Đáp án của câu trên là: ',dap_an_dung)
        time.sleep(2)
    elif lan_sai == 2:
        tong_diem = tong_diem - 20
        print(thong_bao_sai_2,tong_diem)
        print('Đáp án của câu trên là: ',dap_an_dung)
        time.sleep(2)
    else: 
        print('Bạn đã thua rồi :(, tổng điểm mà bạn đã đạt được là: ',tong_diem)
        exit()
print('Xin chúc mừng! Tổng số điểm cuối cùng của bạn là... ',tong_diem,'/ 280 !')
time.sleep(2)
danh_gia = str(input('Hãy trình bày trãi nhiệm của bạn về tựa game này: '))
print('Cảm ơn bạn đã chơi tựa game này! Chúc bạn một ngày mới tốt lành!')