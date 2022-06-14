################### **start react application on the system** ############################

1. clone the project from the git repository
2. open the cloned project in VS Code
3. open the terminal in the VS Code and change the directory to Frontend folder using command: **cd Frontend**
4. when inside the Frontend folder, install the dependencies using command as: **npm install --legacy-peer-deps**
5. after installing all the dependency successfully, start the server using command as : **npm start**
6. the react application will start locally on localhost:3000

**Note:** use below command to build the react application, it will genarate the build folder in the directory. 
      Use this build folder while deploying the application.
      
  **npm run build**

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
