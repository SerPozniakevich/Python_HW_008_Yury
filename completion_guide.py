from guide_loggining import write_log_guide as wlg
from guide_loggining import write_log_guide_txt as wlgt
from guide_loggining import write_log_guide_1 as wlg_1
from guide_loggining import write_log_guide_txt_1 as wlgt_1
from input_guide import input_name, input_fam, input_description, input_number


def complection():
    a = input_fam()
    b = input_name()
    c = input_number()
    d = input_description()
    print(f'фамилия: {a} имя: {b} телефон: {c} описание: {d}')
    wlg(a, b, c, d)
    wlgt(a, b, c, d)
    wlg_1(a, b, c, d)
    wlgt_1(a, b, c, d)
