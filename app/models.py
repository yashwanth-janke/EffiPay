from app import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.Numeric(10, 2), nullable=False)
    hire_date = db.Column(db.Date, default=db.func.current_date())
    is_active = db.Column(db.Boolean, default=True)


class Payroll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    date = db.Column(db.Date, default=db.func.current_date())

class Timekeeping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    hours_worked = db.Column(db.Numeric(5, 2), nullable=False)
    date = db.Column(db.Date, default=db.func.current_date())
