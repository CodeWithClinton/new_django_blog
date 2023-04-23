# new_django_blog
This is a new and improved django blog.
## Steps To Deploy on Amazon EC2
Update the System   
                      
``sudo dnf update -y``            

Install Git   
          
``sudo dnf install git -y``  
    
To get this repository, run the following command inside your git enabled terminal     
                     
`` git clone https://github.com/ClintonCode20/new_django_blog.git ``  
   
Install pip    
      
``sudo dnf install pip -y``   
     
Install Django     
              
``pip install django``   
           
Make Migrations      
        
``python3 manage.py makemigrations``  
    
Migrate          
             
``python3 manage.py migrate``    
     
Createsuperuser   
     
``python3 manage.py createsuperuser``   
    
Runserver   
   
``python3 manage.py runserver 0.0.0.0:8000`` 

