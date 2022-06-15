################### **start react application on the system** ############################

1. clone the repository and open it in VS Code
2. open terminal in VS Code and change directory to Frontend folder-> 
  **cd Frontend**
 
3. install the dependencies->
  **npm install --legacy-peer-deps**

4. start the server-> 
  **npm start**

5. react application will start locally on **localhost:3000**
6. build react application->
  **npm run build**
  
  It will build the application and create build folder inside the directory and this build folder will be shared for deployment

########################################################################################


########## **deploy the application on the server** ########################################


1. Download and copy nginx to C:/.

2. Install Python 3.7 in C:/Python37 and install all dependencies from requirement.txt.

3. Edit ALLOWED_HOSTS in settings.py. And run the runserver with 0.0.0.0:8000

4. Collect static files by running python manage.py collectstatic

5. Edit nginx/webproject_nginx.conf

    Edit the server_name like *.example.com
    
    Edit the path to /static (and /media if needed)
    
    Edit proxy_pass to match the server running from runserver (i.e. runserver.py). This will usually be localhost or your IP address

6. Create two directories inside of C:/nginx/

    Create sites-enabled and sites-available
    
    Copy webproject_nginx.conf to the two directories

7. Edit C:/nginx/conf/nginx.conf

    Add include <path to your sites-enabled/webproject_nginx.conf>;
    
    Change port 80 to a non-essential port like 10. We will need to utilize 80 for our Django project

8. Open a terminal at C:/nginx/ and run nginx.exe -t to check files, and if everything is successful run nginx.exe to start the server

9. Open a web browser and navigate to http://localhost

#################################################################################
