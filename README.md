# InoPortal 
##A Portal for Automation and Simplification of College Paperwork

###Track:
Automation in paperwork and procedures in institutes

###Motivation and Idea:
In today's fast and digital world, time is of the utmost importance. However, a large chunk of our time in college as students and faculty is used up by paperwork and traditional procedures. The need of the hour is a digital portal which can act as a platform in the nexus between the administration, faculty and the students. Hence, InoPortal. It is a Web-application that completely gets rid of tedious paperwork and acts as a digital interface between faculty and students. 

Also, in college, it is difficult and impractical to carry around multiple ID's such as Institute ID, Mess ID, Library Card,etc. Hence, InoPortal also utilizes the latest RFID tags to store all information about a student in a single database. Data can be requested from this database securely and immediately with the help of RFID readers. Thus, a cost-effective and easy to use solution to the problem of multiple ID's is implemented in this portal.

###Technology used:
The front-end of this portal is made in HTML, CSS and JavaScript along with Bootstrap3. The HTTP requests are made through the Ajax framework.
 
The server-end of the application is prepared using the Django-framework. It uses several views, models and serializers to render JSON data to the client making the RESTful API call. 

The RFID scanning is done using the RFID RC522 reader module and RFID tags. Python scripts and libraries are used to read data from and write unique Roll number data to the RFID tags.

###Future Scope:
With proper development, InoPortal can be made a one-stop shop for all college paperwork and procedure. Some features that can be added to this portal are:

1. Professor Flag. Students can check the portal to find out if a particular faculty is present in the department or not.

2. Document Bank. At the time of admission, all scanned copies can be uploaded to the portal so that repeated scanning and submission is not required for different applications by the students. Pupils can directly share the relevant documents from the portal for any application or permission.

3. Permission Processing. As students apply for permissions, the administration can view them and the accompanying documents to decide whether the permission should be granted or not.

4. Pre-placement Process Automation. Google forms released by employers can be shared using the portal so that data is directly fetched from the student database instead of asking the same details from the students repeatedly.