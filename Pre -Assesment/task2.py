import csv
from tabulate import tabulate

# Read data from CSV files
def read_department_data(filename):
    department = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # To Skip the header row from csv file
        
        for row in reader:
            #print(row)
            department[row[1]] = row[0]      
    return department

def read_employee_data(filename):
    employee = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # To Skip the header row from csv file
        
        for row in reader:
           employee.append(row)

    return employee

def read_salary_data(filename):
    salaries = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # To Skip the header row from csv file
        
        for row in reader:
           salaries.append(row)

    return salaries

#Provide appropiate paths to  read functions
department = read_department_data('./data/ASDE Assignment - Departments.csv')
employee = read_employee_data('./data/ASDE Assignment - Employees.csv')
salaries = read_salary_data('./data/ASDE Assignment - Salaries.csv')

# Get list of employees in each department
def get_emplist(department):
    emp_list = {}
    for x in department.values():
        temp = []
        for emp in employee:
            if x == emp[2]:
                temp.append(emp[0])
                emp_list[x] = temp                       
    return emp_list

employees_list = get_emplist(department)

# Get average salary of each department
def get_avg_dept_salaries(employees_list, salaries):
  dept_id = 0
  dept_salaries = {}
  for dept_employees in employees_list.values():
    avg_sal = 0
    count = 0
    for individual_employee in dept_employees:
      for salary in salaries:
        if(individual_employee == salary[0]):
          count += 1
          avg_sal += int(salary[2])
    dept_id += 1
    avg_sal = avg_sal/count
    dept_salaries[str(dept_id)] = avg_sal
  
  return dept_salaries
          
# Get top 3 departments with their average monthly salary
def get_top_departments(avg_dept_sal_with_names):
    sorted_top_3_dept_by_avg_salary = sorted(avg_dept_sal_with_names.items(), key=lambda x:x[1], reverse=True)[:3]
    return sorted_top_3_dept_by_avg_salary

# Print top 3 departments with their average monthly salary
dept_salaries = get_avg_dept_salaries(employees_list, salaries)

#Inverting department & department salaries dictionaries to get desired dictionary
avg_dept_sal_with_names = {key: dept_salaries[value] for key, value in department.items() if value in dept_salaries}
top_departments = get_top_departments(avg_dept_sal_with_names)



# Main function that will give us the final output report
def generate_report(top_departments):
    headers = ["DEPT_NAME", "AVG_MONTHLY_SALARY(USD)"]
    rows = []
    for department, salaries in top_departments:
        rows.append([department, f"{salaries:.2f}"])
    print(tabulate(rows, headers, tablefmt="grid"))
    print('\n')

generate_report(top_departments)