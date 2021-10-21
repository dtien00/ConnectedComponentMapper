# ConnectedComponentMapper
Python code to determine connected components given a textfile
Given a text file: 
 - First line being how many vertices
 - Second being how many edges
 - The rest being paired numbers representing edges between them.  
This Python program prints out all connected components existing from it.

Example:  
9  
10  
1 2  
1 8  
2 4  
2 5  
2 6  
4 8  
5 8  
5 10  
9 10  

When the program is fed this, the output is  

Connected Component # 1 :   
 [1, 2, 8, 4, 5, 6, 10, 9]  
Connected Component # 2 :   
 [3]  
Connected Component # 3 :   
 [7]  
 
 
