## DIGITAL HEALTH ANALYTICS

![image](https://github.com/AbiodunAnalyst/DIGITAL_HEALTH_ANALYTICS/assets/110310940/16911222-4a5f-4462-8a56-a0c755d68d1e)


## INTRODUCTION
#### Digital health is transforming not only how people’s health is managed but also helping to prevent avoidable deaths. From translating health data and care into actions, it is gradually becoming an integral part of how health care providers and patients themselves manage health related problems. In addition, the availability of network enabled devices such as smartphone and wearable devices is enabling mobile medical apps and software that can provide support for clinicians to make clinical decisions using available data and artificial intelligence (AI) or machine learning (ML). 
#### The project looks at developing an interactive interface that will allow user to select from range of selection what vital health information they want to see. The project is divided into three part, the first part is where the data is loaded, the second part of the project looks at creating a query modules that contains all function and method the program want to solve  and the last which is the third part contain the user interface where all the interaction  of the query module, the data set, the menu selection, and the display code reside.
---

## PROBLEM ANALYSIS
The project is to design and analyze this dataset, and then design and implement an application that can help clinicians monitor patients’ vital signs such as blood pressure, etc. to prevent an impending fatality.
The implementation of the project will be looking at been able to:
  - Compute the average age, modal age, median age of those whose heart failure resulted in death.
  - Compute the average time taken for those whose heart failure did not result in death.
  - Compute the median age, average age, and modal age of those with high blood pressure.
  -	Compute the median age, average age, and modal age of those with diabetes.
  -	Determine whether diabetes is linked to smoking and high blood pressure.
  -	Compute the average serum sodium of those with diabetes.
  -	Determine if anaemia is linked to smoking or not.
  -	Returns anyone without high blood pressure that died of heart failure.
  -	Computes and returns the IQRs (Interquartile Range) of ejection fraction and serum creatinine.
  -	Compute and return the sample variance of creatinine phosphokinase and serum sodium.
  The outputs of any of these functions should be persisted into an external file in csv format.
  This will be achieved through proper plan of all parameter, function, method and modules that will be used.
  ---

## SOLUTION REQUIREMENT
The project solution plan is divided into three part
1.	Loading the data and this involves
  a.	Implementing a function to read the data
  b.	Implement a function to hand exception and error while load
  c.	Implement a function that read the csv file in a format required
  d.	Introduced a variable called id 
  e.	Convert the data to required data type for better out put

2.	Implement a Query Module
  a.	Implement a filter function
  b.	Implement function for every problem to be solved
3.	Implement User Interface Module
  a.	Implement a function that display what the user wants to select and see (display menu)
  b.	Implement a function that allow user to input there choice (main function)
  c.	Implement a try function
  d.	Implement a function that handle user choice
  e.	Implement a filter function that handle the death data set
  f.	Implement all the display function
---

## IMPLEMENTATION OF SOLUTION
#### The implementation started by first creating a function that will be use to read the data set for the project. The program also uses exceptional handling to handle exception and error and it is used in the project at different part for different error capturing for example when used during loading of the data set it is expected to block any exception if the file is not found. The program introduce csv.DictReader which allow the data to be read but maps the information read into a dictionary. The variable called id was introduced which makes every entry a unique entry and for proper outputting the data was also formatted to required data format for easy calculation and output.
#### The second part of the project involved the query module implementation which is the part involved with implementation of all function that defined the question the project will be solving. And also a filter function was created to filter condition to be used in the program from the data set.
#### The third part of the project which is the User Interface Module, this module contains many functions that make it easy for user to interact with the program. One of the functions is the display menu faction that display choice of different statistics that the user will like to see. Another function is the is the main function that display an interface that allow user to input that choice based on the information they want to see. The process choice function is one vital function in the project that host the choice of the user and it interact with the display function to output the required information needed by the user and the display function interact with the query module to fetch required statistics. 

#### All code are attached to the Project File
---

## PROGRAM STRUCTURE CHART

![image](https://github.com/AbiodunAnalyst/DIGITAL_HEALTH_ANALYTICS/assets/110310940/7ea98b7b-9a32-4a9e-abcc-799e58bd4a53)
---

## PROGRAM EXECUTION

You can interact with the project video [here](https://drive.google.com/file/d/1BW3Iv3hMrpxQD75kBUCzs2YCWWUqrJOq/view?usp=drive_link)
