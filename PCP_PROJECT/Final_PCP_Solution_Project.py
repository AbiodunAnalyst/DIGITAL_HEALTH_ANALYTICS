#!/usr/bin/env python
# coding: utf-8

# In[75]:


import csv
from statistics import mean, median, mode
from tabulate import tabulate # to display the data in a readable format
import statistics


# In[90]:


# This part of the program is to load the data
#id varable was created in the table

file_path = 'C:/Users/NEW USER/Downloads/PCPFILE/heart_failure_clinical_records_dataset-pcp.csv'
def load_clinical(file_path):
    clinical_data = {}

    try:     #handling exceptions or errors
        with open(file_path, 'r') as cl_file:
            clinical_data_rd = csv.DictReader(cl_file) #csv.DictReader is used to read a csv file 
            for data in clinical_data_rd:
                id = data['id']  
                clinical_data[id] = {
                    'age': int(data['age']),
                    'anaemia': int(data['anaemia']),
                    'creatinine_phosphokinase': float(data['creatinine_phosphokinase']),
                    'diabetes': int(data['diabetes']),
                    'ejection_fraction': int(data['ejection_fraction']),
                    'high_blood_pressure': int(data['high_blood_pressure']),
                    'platelets': float(data['platelets']),
                    'serum_creatinine': float(data['serum_creatinine']),
                    'serum_sodium': float(data['serum_sodium']),
                    'gender': int(data['gender']),
                    'smoking': int(data['smoking']),
                    'time': float(data['time']),
                    'DEATH_EVENT': int(data['DEATH_EVENT'])
                }
                
    except Exception as e:
        print(f"Error loading data: {e}")

    return clinical_data


# In[91]:


clinical_data = load_clinical(file_path)


# In[92]:


#clinical_data


# In[93]:


#this part of the program defines the query class and the fuction of all calculation required for the program to run
import statistics

class QueryModule:
    def __init__(self, clinical_data):
        self.clinical_data = clinical_data
        
    #the filter is created to filter clinical data based on the value of DAETH EVENT
    def filter_by_death(self, death_df):
        return [data_df for data_df in self.clinical_data.values() if data_df['DEATH_EVENT'] == death_df]
        
    
    
    #this function is created to filter condition to be used in the program from the clinical data set
    def filter_by_condition(self, condition):
        return [data_df for data_df in self.clinical_data.values() if condition(data_df)]
    
    #Computing the average age result in death
    def compute_average_age(self, data_dfs):
        ages = [data_df['age'] for data_df in data_dfs]
        return sum(ages) / len(ages) if ages else None

    #Computing the modal age result in death
    def compute_modal_age(self, data_dfs):
        ages = [data_df['age'] for data_df in data_dfs]
        return statistics.mode(ages) if ages else None

    #Computing the median age result in death
    def compute_median_age(self, data_dfs):
        ages = [data_df['age'] for data_df in data_dfs]
        return statistics.median(ages) if ages else None

    #computing the average time taken for those whose heart failure did not result in death
    def compute_average_time(self, data_dfs):
        times = [data_df['time'] for data_df in data_dfs]
        return sum(times) / len(times) if times else None

    #computing median age, average age, and modal age of those with high blood pressure.
    def compute_statistics_for_high_blood_pressure(self):
        high_bp_data_dfs = self.filter_by_condition(lambda data_df: data_df['high_blood_pressure'] == 1)
        return {
            'average_age': self.compute_average_age(high_bp_data_dfs),
            'modal_age': self.compute_modal_age(high_bp_data_dfs),
            'median_age': self.compute_median_age(high_bp_data_dfs)
        }

    #computing the median age, average age, and modal age of those with diabetes.
    def compute_statistics_for_diabetes(self):
        diabetes_data_dfs = self.filter_by_condition(lambda data_df: data_df['diabetes'] == 1)
        return {
            'average_age': self.compute_average_age(diabetes_data_dfs),
            'modal_age': self.compute_modal_age(diabetes_data_dfs),
            'median_age': self.compute_median_age(diabetes_data_dfs)
        }

    #determine whether diabetes is linked to smoking and high blood pressure.
    def diabetes_linked_to_smoking_and_HBP(self):
        diabetic_smokers_and_hbp = self.filter_by_condition(
            lambda data_df: data_df['diabetes'] == 1 and data_df['smoking'] == 1 and data_df['high_blood_pressure'] == 1)
        return len(diabetic_smokers_and_hbp) > 0
        
    #compute the average serum sodium of those with diabetes.
    def average_serum_sodium_for_diabetes(self):
        diabetes_data_dfs = self.filter_by_condition(lambda data_df: data_df['diabetes'] == 1)
        serum_sodium_values = [data_df['serum_sodium'] for data_df in diabetes_data_dfs]
        return sum(serum_sodium_values) / len(serum_sodium_values) if serum_sodium_values else None
        
    #computing anaemia is linked to smoking or not.
    def anaemia_linked_to_smoking(self):
        anaemia_smokers = self.filter_by_condition(lambda data_df: data_df['anaemia'] == 1 and data_df['smoking'] == 1)
        return len(anaemia_smokers) > 0
        
    #computing high blood pressure that died of heart failure.
    def No_HBP_death_records(self):
        No_HBP_death_data_dfs = self.filter_by_condition(
            lambda data_df: data_df['DEATH_EVENT'] == 1 and data_df['high_blood_pressure'] == 0)
        return len(No_HBP_death_data_dfs)> 0



    #this part is to save the data in a csv file
    def save_to_csv(self, data, filename):
        with open(filename, 'w', newline='') as file_records:
            field_record = data[0].keys() if data else []
            writer = csv.DictWriter(file_records, fieldnames=field_record)
            writer.writeheader()
            writer.writerows(data)
    


# In[94]:


#this is the part that interact with the query module and the data
class UserInterface:
    def __init__(self, query_module):
        self.query_module = query_module
        #self.solution = None
    
    #the function gives user the interface to select what statistics is needed to be displayed
    def display_menu(self):
        print("1. Age statistics for Patients whose heart failure resulted to death")
        print("2. Average Time taken for patients whose heart failure did not result to death")
        print("3. Age Statistics for Patients with High Blood Pressure")
        print("4. Age Statistics for for Patients with diatetes")
        print("5. Statistics for diabetes linked to smoking and High Blood Pressure")
        print("6. Statistics for average serum sodium of Patients with diabetes")
        print("7. Statistics for anaemia linked to smoking")
        print("8. Statistics for no High Blood Pressure death record")
        
    # this part of the program allow user to interact with the program, it form the entry point
    def main(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (or 'q' to quit): ")

            if choice.lower() == 'q':
                print("Exiting the system. Goodbye!")
                break

            try:
                choice = int(choice)
                self.process_choice(choice)
            except ValueError:
                print("Invalid input. Please enter a number or 'q' to quit.")

    
    # this part of the program interact with the display function which the dispaly function intract with the quary module
    #it handle user choice
    def process_choice(self, choice):
        
        try:
            if 1 <= choice <= 8:
                if choice == 1:
                    self.display_age_statistics_for_heart_failure_result_to_death()
                elif choice == 2:
                    self.display_average_time_for_heart_failure_not_result_to_death()
                elif choice == 3:
                    self.display_age_statistics_for_high_blood_pressure()
                elif choice == 4:
                    self.display_age_statistics_for_diabetes()
                elif choice == 5:
                    self.display_statistics_for_diabetes_link_to_smoking_HBP()
                elif choice == 6:
                    self.display_average_Serum_Sodium_for_diabetes_Patients()
                elif choice == 7:
                    self.display_anaemia_link_smoking()
                elif choice == 8:
                    self.display_No_HBP_death_records()
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")
                
        except Exception as e:
            print(f"An error occurred: {e}")

   


    
        
        
        
        # Display output statistics for health failure that result to death
    def display_age_statistics_for_heart_failure_result_to_death(self):
        deceased_records = self.query_module.filter_by_death(1)
        average_age = self.query_module.compute_average_age(deceased_records)
        modal_age = self.query_module.compute_modal_age(deceased_records)
        median_age = self.query_module.compute_median_age(deceased_records)
        
        
        solution = {
            'Average Age': average_age,
            'Modal Age': modal_age,
            'Median Age': median_age
        }
        
        # Print the tabulated result
        print(tabulate(solution.items(), headers=['Metric', 'Value']))
        
        try:

            # Save the result to a CSV file
            self.query_module.save_to_csv([solution], 'query_solution_death_output.csv')
            print("Results saved to 'query_solution_death_output.csv'")

        except Exception as e:
            print(f"Error saving results to CSV: {e}")
    
     
        
        
        # Display output statistics for average time that health failure did not result to death
    def display_average_time_for_heart_failure_not_result_to_death(self):
        survived_records = self.query_module.filter_by_death(0)
        average_time = self.query_module.compute_average_time(survived_records)
        
        solution = {
            'Average time heart failure not result to death' : average_time
        }
       
        try:
            # Print the tabulated result
            print(tabulate(solution.items(), headers=['Metric', 'Value']))

            # Save the result to a CSV file
            self.query_module.save_to_csv([solution], 'query_solution_time_not_death_output.csv')
            print("Results saved to 'query_solution_time_not_death_output.csv'")
            
        except Exception as e:
            print(f"Error saving results to CSV: {e}")
        
    
    
    
    # Display output statistics for high blood pressure
    def display_age_statistics_for_high_blood_pressure(self):
        statistics_high_BH = self.query_module.compute_statistics_for_high_blood_pressure()
        
        solution = {
            "Average Age": statistics_high_BH['average_age'],
            "Modal Age": statistics_high_BH['modal_age'],
            "Median Age": statistics_high_BH['median_age']

        }
        
        # Print the tabulated result
        print(tabulate(solution.items(), headers=['Metric', 'Value']))
        
        try:
           
            # Save the result to a CSV file
            self.query_module.save_to_csv([solution], 'query_solution_High_blood_pressure_output.csv')
            print("Results saved to 'query_solution_High_blood_pressure_output.csv'")
            
        except Exception as e:
            print(f"Error saving results to CSV: {e}")
    
            
    # Display output statistics diabetes patients
    def display_age_statistics_for_diabetes(self):
        statistics_diabetes = self.query_module.compute_statistics_for_diabetes()
        
        solution = {
            "Average Age": statistics_diabetes['average_age'],
            "Modal Age": statistics_diabetes['modal_age'],
            "Median Age": statistics_diabetes['median_age']
        }
        
         # Print the tabulated result
        print(tabulate(solution.items(), headers=['Metric', 'Value']))
        
        try:

            # Save the result to a CSV file
            self.query_module.save_to_csv([solution], 'query_solution_diabetes_output.csv')
            print("Results saved to 'query_solution_diabetes_output.csv'")
            
        except Exception as e:
            print(f"Error saving results to CSV: {e}")
        
    
     # Display output statistics for diabetes link to smoking and HBP 
        
    def display_statistics_for_diabetes_link_to_smoking_HBP(self):
        statistics_diabetes_LSHBP = self.query_module.diabetes_linked_to_smoking_and_HBP()
        
        solution = {
            'Number of diabetes link to smoking and HBP':statistics_diabetes_LSHBP
        }
        
        # Print the tabulated result
        print(tabulate(solution.items(), headers=['Metric', 'Value']))
        
        try:

            # Save the result to a CSV file
            self.query_module.save_to_csv([solution], 'query_solution_diabetes_Link_Smoking_HBP_output.csv')
            print("Results saved to 'query_solution_diabetes_Link_Smoking_HBP_output.csv'")
            
        except Exception as e:
            print(f"Error saving results to CSV: {e}")
  
      
    #display_average_Serum_Sodium_for_diabetes_Patients
    def display_average_Serum_Sodium_for_diabetes_Patients(self):
        Statistics_Serum_Sodium = self.query_module.average_serum_sodium_for_diabetes()
        
        solution = {
            "Average Serum Sodium for Patients with Diabetes": Statistics_Serum_Sodium
        }
        
        # Print the tabulated result
        print(tabulate(solution.items(), headers=['Metric', 'Value']))
        
        try:

            # Save the result to a CSV file
            self.query_module.save_to_csv([solution], 'query_solution_average_serum_sodium_diabetes_output.csv')
            print("Results saved to 'query_solution_average_serum_sodium_diabetes_output.csv'")
            
        except Exception as e:
            print(f"Error saving results to CSV: {e}")
         
   
    # display_statistics_for_anaemia_link_smoking       
    def display_anaemia_link_smoking(self):
        anaemia_LS = self.query_module.anaemia_linked_to_smoking()
        
        solution = {'Anaemia link to smoking':anaemia_LS}
        
        # Print the tabulated result
        print(tabulate(solution.items(), headers=['Metric', 'Value']))
        
        try:

            # Save the result to a CSV file
            self.query_module.save_to_csv([solution], 'query_solution_anaemia_link_to_smoking_output.csv')
            print("Results saved to 'query_solution_anaemia_link_to_smoking_output.csv'")
        except Exception as e:
            print(f"Error saving results to CSV: {e}")
        
    
    # display statistics of patients with no high blood pressure and result to death
    def display_No_HBP_death_records(self):
        No_HBP_D_R = self.query_module.No_HBP_death_records()
        
        solution = {'No High Blood Pressure death record': No_HBP_D_R}
                
        # Print the tabulated result
        print(tabulate(solution.items(), headers=['Metric', 'Value']))
        
        try:
           
            # Save the result to a CSV file
            self.query_module.save_to_csv([solution], 'query_solution_for_No_HBP_death_records_output.csv')
            print("Results saved to 'query_solution_for_No_HBP_death_records_output.csv'")
            
        except Exception as e:
            print(f"Error saving results to CSV: {e}")
    
    
        


# In[95]:


query_module = QueryModule(clinical_data)


# In[96]:


user_interface = UserInterface(query_module)


# In[ ]:


user_interface.main()


# 
