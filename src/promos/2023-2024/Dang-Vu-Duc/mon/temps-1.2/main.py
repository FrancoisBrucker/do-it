import openpyxl
from openpyxl.styles import Font, PatternFill
from create_timetable import Create_timetable

test = Create_timetable()
# test.create_all_timetable()
# test.create_timetable_automatic("Dang vu", "duc")
# test.add_course("edt de Duc Dang Vu.xlsx")
test.remove_course("edt de Duc Dang Vu.xlsx")
