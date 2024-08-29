from flask import render_template, request, redirect, url_for, flash
from app import app, db
from .models import Employee, Payroll, Timekeeping

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        salary = request.form['salary']
        employee = Employee(name=name, position=position, salary=salary)
        db.session.add(employee)
        db.session.commit()
        flash('Employee added successfully!')
        return redirect(url_for('view_employees'))
    return render_template('add_employee.html')

@app.route('/view_employees')
def view_employees():
    employees = Employee.query.all()
    return render_template('view_employees.html', employees=employees)

@app.route('/generate_payroll', methods=['GET'])
def generate_payroll():
    employees = Employee.query.filter_by(is_active=True).all()
    for employee in employees:
        timekeeping_entries = Timekeeping.query.filter_by(employee_id=employee.id).all()
        total_hours = sum(entry.hours_worked for entry in timekeeping_entries)
        gross_pay = total_hours * (employee.salary / 160)  # Assuming 160 hours per month
        payroll_entry = Payroll(employee_id=employee.id, amount=gross_pay, date=db.func.current_date())
        db.session.add(payroll_entry)
    db.session.commit()
    flash('Payroll generated successfully!')
    return redirect(url_for('view_payroll'))


@app.route('/admin_dashboard')
def admin_dashboard():
    employees = Employee.query.all()
    payrolls = Payroll.query.all()
    return render_template('admin_dashboard.html', employees=employees, payrolls=payrolls)


@app.route('/view_payroll')
def view_payroll():
    payrolls = Payroll.query.all()
    return render_template('payroll_report.html', payrolls=payrolls)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Implement your authentication logic here
        flash('Login successful!')
        return redirect(url_for('index'))
    return render_template('login.html')



@app.route('/update_employee/<int:id>', methods=['GET', 'POST'])
def update_employee(id):
    employee = Employee.query.get_or_404(id)
    if request.method == 'POST':
        employee.name = request.form['name']
        employee.position = request.form['position']
        employee.salary = request.form['salary']
        employee.is_active = 'is_active' in request.form
        db.session.commit()
        flash('Employee details updated successfully!')
        return redirect(url_for('view_employees'))
    return render_template('update_employee.html', employee=employee)



@app.route('/add_timekeeping/<int:employee_id>', methods=['GET', 'POST'])
def add_timekeeping(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    if request.method == 'POST':
        hours_worked = request.form['hours_worked']
        date = request.form['date']
        timekeeping_entry = Timekeeping(employee_id=employee_id, hours_worked=hours_worked, date=date)
        db.session.add(timekeeping_entry)
        db.session.commit()
        flash('Timekeeping entry added successfully!')
        return redirect(url_for('view_employee_timekeeping', employee_id=employee_id))
    return render_template('add_timekeeping.html', employee=employee)
