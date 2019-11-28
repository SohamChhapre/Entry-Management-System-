# Entry-Management-System-

This is the simple Entry management system in which host and visitors are the end user of the system.
Home page contains simple buttons which include host and visitor.
After clicking on button host can add his information in the form and then submit it.Submission of form generates a post request to api server which then add's host in the database with all its credentials.

Same steps can be followed by the visitor but at the time of cheking in the post api is requested which then sends an email-Through smtp(simple mail transfer protocol) to host and Sms -Through fast2sms Api to the host containing the visitor details.

At the time of chekout the visitor gets an email containing all the details about the visit.

Technology stack:Used React for frontend and Flask for backend
Restful Api has been created to perform registration and fetching visitor and host details if needed.

Email Scheduler is used to schedule an email at checkout time for the visitor.
Sqllite database is used to  store data of host and visitors
Object Realation Mapper model is used to create and map the database.
Randomly generated strings are considered as primary in both the tables.And alternative keys are email and phone_no
A standard coding structured is followed in both API and UI
