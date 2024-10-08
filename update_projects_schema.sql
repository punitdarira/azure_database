-- 1. Create 'departments' table
CREATE TABLE IF NOT EXISTS departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL
);

-- 2. Insert sample data into 'departments' table
INSERT INTO departments (department_name, location) VALUES 
('Human Resources', 'New York'),
('Engineering', 'San Francisco'),
('Marketing', 'Chicago'),
('Sales', 'Los Angeles');

-- 3. Create 'employees' table
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    department_id INT,
    hire_date DATE NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- 4. Update the 'departments' table (e.g., change the 'location' column size)
ALTER TABLE departments
MODIFY COLUMN location VARCHAR(150);

-- 5. Delete a specific row from 'departments' table (e.g., delete department with department_id 2)
DELETE FROM departments WHERE department_id = 2;
