#!/usr/bin/env python3
"""Builds the synthetic student used for every help-site screenshot.

Everything here is invented: the student, the lecturers, the subjects and the
marks. Restore the output in the app (Settings > Data > Restore a backup) on a
fresh guest install, then capture. Dates are written around TODAY so the
dashboard, the planner and the deadlines all have something current to show;
change it and re-run to refresh the set for a later capture session.

    python3 tools/screenshot-data/make_dataset.py > /tmp/sample.json
"""
import json
import sys
from datetime import date, timedelta

TODAY = date(2026, 11, 24)  # a Tuesday, in teaching week 8


def iso(d):
    return d.isoformat()


def dmy(d):  # homework dates are dd/mm/yyyy, as the web app stored them
    return d.strftime('%d/%m/%Y')


def day(offset):
    return TODAY + timedelta(days=offset)


SEM = 'sample-semester-1'
uid = 'guest'
tables = {}


def add(table, row):
    tables.setdefault(table, []).append({'uid': uid, **row})


# ---- Academics ---------------------------------------------------------
add('grading_scale', {
    'id': 'sample-scale', 'name': 'University 4.0', 'mode': 'university',
    'mappings': json.dumps([
        {'grade': 'A', 'points': 4.0, 'minPercent': 80},
        {'grade': 'A-', 'points': 3.67, 'minPercent': 75},
        {'grade': 'B+', 'points': 3.33, 'minPercent': 70},
        {'grade': 'B', 'points': 3.0, 'minPercent': 65},
        {'grade': 'B-', 'points': 2.67, 'minPercent': 60},
        {'grade': 'C+', 'points': 2.33, 'minPercent': 55},
        {'grade': 'C', 'points': 2.0, 'minPercent': 50},
        {'grade': 'D', 'points': 1.0, 'minPercent': 40},
        {'grade': 'F', 'points': 0.0, 'minPercent': 0},
    ]),
})
add('programme', {
    'id': 'sample-programme', 'name': 'BSc Computer Science', 'timezone': '',
    'credits_required': 120, 'grading_mode': 'graded',
    'grading_scale_id': 'sample-scale', 'university': '',
})
add('year', {
    'id': 'sample-year-2', 'programme_id': 'sample-programme', 'name': 'Year 2',
    'start_date': '2026-09-28', 'end_date': '2027-07-30',
})
add('semester', {
    'id': SEM, 'year_id': 'sample-year-2', 'name': 'Semester 1',
    'start_date': '2026-10-05', 'end_date': '2027-02-12',
    'grading_mode': 'graded', 'grading_scale_id': 'sample-scale',
    'biweekly_anchor_date': '2026-10-05', 'archived': 0,
    'calendar_key': '', 'calendar_revision': 0,
})
for n, (kind, start, end, label, runs, counts) in enumerate([
    ('lectures', '2026-10-05', '2026-11-27', '', 1, 1),
    ('break', '2026-11-30', '2026-12-06', '', 0, 0),
    ('lectures', '2026-12-07', '2027-01-15', '', 1, 1),
    ('revision', '2027-01-18', '2027-01-22', '', 0, 0),
    ('exam', '2027-01-25', '2027-02-12', '', 0, 0),
]):
    add('semester_period', {
        'id': f'sample-period-{n + 1}', 'semester_id': SEM, 'type': kind,
        'start_date': start, 'end_date': end, 'label': label,
        'classes_run': runs, 'counts_as_week': counts, 'ordinal': n + 1,
    })

# ---- Subjects ----------------------------------------------------------
# code, name, lecturer, credits, colour, categories
SUBJECTS = [
    ('CSC 2103', 'Data Structures and Algorithms', 'Dr. Aisha Rahman', 4,
     'bg-blue-600', [('Assignments', 30, [(18, 20), (26, 30)]),
                     ('Quizzes', 20, [(8, 10), (9, 10)]),
                     ('Final Exam', 50, [])]),
    ('CSC 2205', 'Database Systems', 'Mr. Daniel Lee', 3,
     'bg-emerald-600', [('Lab Work', 25, [(23, 25)]),
                        ('Project', 25, [(40, 50)]),
                        ('Final Exam', 50, [])]),
    ('CSC 2301', 'Computer Networks', 'Dr. Priya Nair', 3,
     'bg-violet-600', [('Labs', 20, [(17, 20)]),
                       ('Midterm', 30, [(21, 30)]),
                       ('Final Exam', 50, [])]),
    ('MTH 2002', 'Discrete Mathematics', 'Prof. Tan Wei Ming', 3,
     'bg-amber-600', [('Problem Sets', 40, [(31, 40), (35, 40)]),
                      ('Final Exam', 60, [])]),
    ('ENG 2100', 'Technical Writing', 'Ms. Sarah Collins', 2,
     'bg-rose-600', [('Essays', 60, [(44, 50)]),
                     ('Presentation', 40, [])]),
]
for i, (code, name, teacher, credits, colour, cats) in enumerate(SUBJECTS):
    add('subject', {
        'id': f'sample-subject-{i + 1}', 'semester_id': SEM, 'code': code,
        'name': name, 'section': '1', 'teacher': teacher, 'credits': credits,
        'grade': '', 'grading_mode': 'graded', 'icon': '', 'color': colour,
        'categories': json.dumps([
            {'name': c, 'weight': w,
             'entries': [{'kind': 'custom', 'points': p, 'max': m}
                         for p, m in marks]}
            for c, w, marks in cats
        ]),
        'archived': 0,
    })

# ---- Classes -----------------------------------------------------------
CLASSES = [
    # id, code, name, day, start, end, place, parity
    ('dsa-lec', 'CSC 2103', 'Data Structures and Algorithms', 'mon', '09:00', '11:00', 'Lecture Hall 2', 'all'),
    ('dsa-lab', 'CSC 2103', 'Data Structures and Algorithms', 'wed', '14:00', '16:00', 'Computer Lab 3', 'all'),
    ('db-lec', 'CSC 2205', 'Database Systems', 'tue', '10:00', '12:00', 'Lecture Hall 1', 'all'),
    ('db-lab', 'CSC 2205', 'Database Systems', 'thu', '14:00', '16:00', 'Computer Lab 1', 'a'),
    ('net-lec', 'CSC 2301', 'Computer Networks', 'tue', '14:00', '16:00', 'Room B204', 'all'),
    ('net-tut', 'CSC 2301', 'Computer Networks', 'fri', '09:00', '10:00', 'Room B110', 'all'),
    ('mth-lec', 'MTH 2002', 'Discrete Mathematics', 'mon', '14:00', '16:00', 'Lecture Hall 3', 'all'),
    ('mth-tut', 'MTH 2002', 'Discrete Mathematics', 'thu', '09:00', '10:00', 'Room A102', 'all'),
    ('eng-sem', 'ENG 2100', 'Technical Writing', 'wed', '09:00', '11:00', 'Seminar Room 4', 'all'),
]
for cid, code, name, d, start, end, place, parity in CLASSES:
    add('schedule', {
        'id': f'sample-class-{cid}', 'semester_id': SEM, 'subject_id': code,
        'subject': name, 'day': d, 'start_time': start, 'end_time': end,
        'location': place, 'icon': 'event',
        'color': next(s[4] for s in SUBJECTS if s[0] == code),
        'week_parity': parity, 'recurrence': 'weekly', 'start_week': 1,
        'end_week': None, 'timezone': '',
        'exceptions': json.dumps(
            [{'date': iso(day(8)), 'type': 'cancelled'}] if cid == 'net-tut'
            else []),
    })

# ---- Homework ----------------------------------------------------------
HOMEWORK = [
    # title, code, module, due offset, progress, done, time (start, end) or None
    ('Binary search tree assignment', 'CSC 2103', 'Assignment 3', 3, 60, False, None),
    ('Normalisation worksheet', 'CSC 2205', 'Lab 7', 0, 80, False, ('23:59', '23:59')),
    ('Subnetting practice set', 'CSC 2301', 'Lab 6', 1, 20, False, None),
    ('Graph theory problem set', 'MTH 2002', 'Problem Set 4', 6, 0, False, None),
    ('Literature review draft', 'ENG 2100', 'Essay 2', 9, 35, False, None),
    ('ER diagram for the project', 'CSC 2205', 'Project', -1, 50, False, None),
    ('Sorting algorithms report', 'CSC 2103', 'Assignment 2', -12, 100, True, None),
    ('Proof by induction exercises', 'MTH 2002', 'Problem Set 3', -8, 100, True, None),
    ('Presentation outline', 'ENG 2100', 'Presentation', 14, 0, False, None),
]
for i, (title, code, module, due, progress, done, times) in enumerate(HOMEWORK):
    add('homework', {
        'id': f'sample-task-{i + 1}', 'semester_id': SEM, 'subject_id': code,
        'class_id': '', 'title': title, 'module': module,
        'due_date': dmy(day(due)),
        'start_time': times[0] if times else '',
        'end_time': times[1] if times else '',
        'time_mode': 'custom' if times else 'endofday',
        'status': 'Completed' if done else 'Not Completed',
        'progress': progress, 'score': None, 'max_score': None,
        'complete_date': dmy(day(due - 1)) if done else '',
    })

# ---- Study topics ------------------------------------------------------
STUDY = [
    ('Trees and traversals', 'CSC 2103', 1, 70),
    ('Graph algorithms', 'CSC 2103', 2, 30),
    ('SQL joins and subqueries', 'CSC 2205', 1, 90),
    ('Transactions and locking', 'CSC 2205', 2, 10),
    ('IP addressing and subnetting', 'CSC 2301', 1, 55),
    ('Routing protocols', 'CSC 2301', 2, 0),
    ('Logic and proofs', 'MTH 2002', 1, 100),
    ('Combinatorics', 'MTH 2002', 2, 40),
]
for i, (title, code, number, progress) in enumerate(STUDY):
    add('study', {
        'id': f'sample-topic-{i + 1}', 'semester_id': SEM, 'subject_id': code,
        'title': title, 'number': number, 'progress': progress,
        'due_date': '', 'notes': '',
    })

# ---- Quizzes and exams -------------------------------------------------
QUIZZES = [
    # title, code, class, date, start, end, exam type, seat, topics, score
    ('Quiz 3: Trees', 'CSC 2103', 'dsa-lec', day(6), '09:00', '09:30', '', '', [1], None),
    ('SQL practical test', 'CSC 2205', 'db-lab', day(2), '14:00', '15:00', '', '', [3], None),
    ('Midterm test', 'CSC 2301', 'net-lec', day(-14), '14:00', '15:30', '', '', [5], (21, 30)),
    ('Quiz 2: Recursion', 'CSC 2103', 'dsa-lec', day(-21), '09:00', '09:30', '', '', [], (9, 10)),
    ('Final Exam', 'CSC 2103', '', date(2027, 1, 26), '09:00', '12:00', 'final', 'B12', [1, 2], None),
    ('Final Exam', 'CSC 2205', '', date(2027, 1, 28), '14:30', '17:30', 'final', 'C04', [3, 4], None),
    ('Final Exam', 'CSC 2301', '', date(2027, 2, 2), '09:00', '12:00', 'final', 'A21', [5, 6], None),
    ('Final Exam', 'MTH 2002', '', date(2027, 2, 4), '09:00', '11:00', 'final', 'D07', [7, 8], None),
]
for i, (title, code, cls, d, start, end, kind, seat, topics, score) in enumerate(QUIZZES):
    add('quiz', {
        'id': f'sample-quiz-{i + 1}', 'semester_id': SEM, 'subject_id': code,
        'class_id': f'sample-class-{cls}' if cls else '', 'title': title,
        'date': iso(d), 'start_time': start, 'end_time': end,
        'time_mode': 'custom',
        'status': 'completed' if score else 'scheduled',
        'score': score[0] if score else None,
        'max_score': score[1] if score else None,
        'exam_type': kind, 'seat_number': seat,
        'topic_ids': json.dumps([f'sample-topic-{t}' for t in topics]),
        'notes': 'Bring your student card.' if kind == 'final' else '',
    })

# ---- Calendar ----------------------------------------------------------
for i, (title, start, end, kind, notes) in enumerate([
    ('Career Fair', day(2), '', 'event', 'Main hall, 10:00-16:00'),
    ('Christmas Day', date(2026, 12, 25), '', 'holiday', ''),
    ('New Year', date(2027, 1, 1), '', 'holiday', ''),
    ('Hackathon weekend', day(11), day(12), 'event', 'Team of four'),
]):
    add('event', {
        'id': f'sample-event-{i + 1}', 'title': title, 'date': iso(start),
        'end_date': iso(end) if end else '', 'kind': kind, 'notes': notes,
    })

# ---- Attendance (a few recorded marks; the rest assume present) --------
for cid, offset, status, note in [
    ('dsa-lec', -15, 'absent', 'Doctor appointment'),
    ('db-lec', -7, 'late', ''),
    ('net-lec', -21, 'absent', ''),
    ('net-lec', -14, 'absent', 'Train delayed'),
    ('net-tut', -18, 'absent', ''),
    ('mth-tut', -12, 'excused', 'University sports event'),
    ('dsa-lec', -1, 'present', ''),
]:
    d = iso(day(offset))
    add('attendance', {
        'id': f'sample-class-{cid}_{d}', 'class_id': f'sample-class-{cid}',
        'date': d, 'status': status, 'note': note,
    })

# ---- Focus sessions ----------------------------------------------------
for i, (offset, minutes, code) in enumerate([
    (-9, 25, 'CSC 2103'), (-8, 50, 'MTH 2002'), (-6, 25, 'CSC 2205'),
    (-5, 75, 'CSC 2103'), (-4, 25, 'CSC 2301'), (-3, 50, 'ENG 2100'),
    (-2, 50, 'CSC 2103'), (-1, 25, 'CSC 2205'), (-1, 25, 'MTH 2002'),
    (0, 25, 'CSC 2103'),
]):
    add('pomodoro', {
        'id': f'sample-focus-{i + 1}', 'semester_id': SEM,
        'date': iso(day(offset)), 'focus_seconds': minutes * 60,
        'per_subject': json.dumps({code: minutes * 60}),
        'homework_ids': '[]',
    })

# ---- Settings ----------------------------------------------------------
add('settings', {
    'id': 'sample-settings', 'default_class_duration': 120,
    'default_exam_length': 180, 'exam_sessions': '[]',
    'calendar_sync_enabled': 0, 'calendar_reminders': 0,
    'attendance_enabled': 1, 'attendance_unit': 'hours',
    'attendance_warning_pct': 10, 'attendance_bar_pct': 20,  # % of the term missed
    'attendance_marking': 'assume_present', 'attendance_alerts': 'nudge',
})

json.dump({'format': 'planner-backup', 'version': 1,
           'exportedAt': f'{iso(TODAY)}T08:00:00Z', 'tables': tables},
          sys.stdout, indent=2)
print()
