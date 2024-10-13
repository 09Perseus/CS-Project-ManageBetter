# CS-Project-AI-Chatbot
AI Chatbot by Balaji, Dinith, Rui

##Specification
###Process 
Use Figma to design the UI for the websites.
Create the HTML and CSS files separately and add them into the project later when necessary.
Develop the app using the Django framework.
Deploy to web
 
###Inspirations / References
Microsoft Teams
Google Classrooms
 
###Structure 
Three apps -> 1. One for teachers 2. One for students 3. One that grants all permissions
Both teachers and students have a home grid view where they can see all their classes, like Microsoft teams.
Within each class, there is a message section as well as ability for teachers to add assignments and add grades

###Models 
Models will be created in the admin app 
Students ( studentid, full name, grade, DOB)
Teachers ( teacherid, full name)
Classes (classid, name, grade, fkey - teachers, mtom - students)
Assignments (fkey - classes)
