from excel import OpenExcel

if __name__ == "__main__":
    f = OpenExcel('ejemplo.xlsx')
    print(f.read('A4'))
    #f.cls()