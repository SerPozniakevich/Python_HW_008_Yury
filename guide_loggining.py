
file_guide_xls = "guide_log.csv"
file_guide_txt = "guide_log.txt"
file_guide_xls_1 = "guide_log_1.csv"
file_guide_txt_1 = "guide_log_1.txt"


def write_log_guide(fam, nam, phone, descrip):
    with open(file_guide_xls, "a") as f:
        f.write(f"\n{fam},{nam},{phone},{descrip}")


def write_log_guide_1(fam, nam, phone, descrip):
    with open(file_guide_xls_1, "a") as f:
        f.write(f"\n{fam}\n\n{nam}\n\n{phone}\n\n{descrip}\n")


def write_log_guide_txt(fam, nam, phone, descrip):
    with open(file_guide_txt, 'a') as txt:
        txt.write(f"\n{fam},{nam},{phone},{descrip}")


def write_log_guide_txt_1(fam, nam, phone, descrip):
    with open(file_guide_txt_1, 'a') as txt:
        txt.write(f"\n{fam}\n\n{nam}\n\n{phone}\n\n{descrip}\n")


def read_log_guide():
    with open(file_guide_xls, "r") as f:
        print(f.read())
