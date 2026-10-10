class StudyLog:
    total_minutes = 0

    def __init__(self, subject):
        self.subject = subject
        self.minutes = 0

    def add(self,minutes):
        self.minutes += minutes
        StudyLog.total_minutes += minutes

    def show(self):
        print(f"{self.subject}:合計{self.minutes}分")

py = StudyLog("Python")
st = StudyLog("確率統計")
py.add(60)
st.add(30)
py.add(20)

py.show()                       # Python：合計80分
st.show()                       # 確率統計：合計30分
print(StudyLog.total_minutes)   # 110