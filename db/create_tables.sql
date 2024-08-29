CREATE DATABASE effipay;

USE effipay;

CREATE TABLE employee (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    position VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date DATE
);

CREATE TABLE payroll (
    id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT,
    amount DECIMAL(10, 2),
    date DATE,
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

CREATE TABLE timekeeping (
    id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT,
    hours_worked DECIMAL(5, 2),
    date DATE,
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);
