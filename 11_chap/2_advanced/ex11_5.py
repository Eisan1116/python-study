class StudyLog:
    def __init__(self, subject):
        self.subject = subject
        self.minutes = 0

    def add(self, minutes):
        self.minutes += minutes

    def show(self):
        return f"{self.subject}:{self.minutes}分"

class ExamStudyLog(StudyLog):
    def __init__(self, subject, exam_date):
        super().__init__(subject)
        self.exam_date = exam_date

    def show(self):
        text = super().show()
        print(f"{text}（試験日:{self.exam_date}）")

log = ExamStudyLog("確率統計", "2026-11-20")
log.add(60)
log.add(60)
log.show()   # 確率統計：合計120分（試験日：2026-11-20）