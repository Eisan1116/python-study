class StudyLog:
    def __init__(self, subject):
        self.subject = subject
        self.minutes = 0

    def add(self,minutes):
        self.minutes += minutes

    def show(self):
        print(f"{self.subject}:合計{self.minutes}分")

log = StudyLog("Python")
log.add(30)
log.add(60)
log.show()   # Python：合計90分