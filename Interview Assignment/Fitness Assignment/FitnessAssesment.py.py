import json
import csv

# Read the json file
def read_data(input_file):
    with open(input_file,'r') as file:
        data = json.load(file)

    #calculate department-wise,month-wise steps
    department_month_totals = {}
    for record in data:
        department = record['department']
        month =record['date']
        steps = record['steps']

        if department not in department_month_totals:
            department_month_totals[department] = {}

        if month not in department_month_totals[department]:
            department_month_totals[department][month] = 0

        department_month_totals[department][month] += steps


    #generate TSV file
    with open('output.tsv','w',newline='') as file:
        writer = csv.write(file,delimeter='\t')
        writer.writerow(['Department','Month','Total Steps'])

        for department in department_month_totals.items():
            for month,total_steps in month.items():
                writer.writerow([department,month,total_steps])            


def read_leaderboard(input_file):
    with open(input_file,'r') as file:
        data = json.load(file)

    #leaderboard_months
    leaderboard_months = ['October', 'November', 'December']

    for month in leaderboard_months:
        leaderboard =[]
        for record in data:
            if record['month'] == month:
                employee_name = record['empolyee_name']
                steps = record['steps']
                leaderboard.append(({"Employee_Name":employee_name,"Steps":steps,"Month":month})) 

    #sort leaderboard in descending order based on steps
    leaderboard.sort(key = lambda x: x['Steps'],reverse=True)

    #generate TSV file
    with open(f'{month}.leaderboard.tsv','w',newline=''):
        writer = csv.writer(file,fieldnames = ['Employee_Name','Steps','Month'],delimiter='\t')
        writer.header()
        writer.writerows(leaderboard)
       

def main():
    input_file = "assignment\company_data.json"
    read_data(input_file)
    read_leaderboard(input_file)

if __name__ == "__main__":
    main()



                    
                
