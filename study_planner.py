from datetime import datetime

class StudyTask:
    def __init__(self, subject, deadline, importance, hours_required):
        self.subject = subject
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self.importance = importance
        self.hours_required = hours_required

    def priority_score(self):
        days_left = (self.deadline - datetime.now()).days
        urgency_score = max(1, 10 - days_left)
        return urgency_score + self.importance


class AIStudyPlanner:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def generate_study_plan(self):
        return sorted(self.tasks, key=lambda t: t.priority_score(), reverse=True)


# Example usage
if __name__ == "__main__":
    planner = AIStudyPlanner()

    planner.add_task(StudyTask("Programming", "2025-01-03", 5, 3))
    planner.add_task(StudyTask("Mathematics", "2025-01-05", 4, 2))
    planner.add_task(StudyTask("Physics", "2025-01-07", 3, 2))

    print("AI-Optimized Study Plan:\n")
    for task in planner.generate_study_plan():
        print(f"{task.subject} | Priority Score: {task.priority_score()}")
