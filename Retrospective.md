# Retrospective: the SuccessFactors LMS Integration Thermo Fisher Scientific 

Thermo Fisher is a major supplier to the Biotech and Pharmaceutical industries that offers a broad range of products made possible by acquisitions. I am a Quality Engineer in the Purification business unit located in Bedford and Chelmsford, Massachusetts. My previous focus was investigations, and I have recently changed roles to manage the Training System. 

Two years ago, there was a company-wide training harmonization that transitioned legacy training systems to the SuccessFactors Learning Management System (SFLMS). Currently, my business is 25% training compliant. Prior to implementation, we were 80% training compliant. This is my retrospective on the implementation of SFLMS and the actions I am taking to improve the system moving forward.


## Personas 
- User - Site-level direct contributor, User Access rights. Functions: review and complete trainings content: videos, documents, quizzes, sign up for training, access previous training content, request training extensions. 
= Managers - Site-level leader with direct reports, Manager Acccess rights. Functions: same as users. In addition, assign, extend, and remove trainings for direct reports, unlock quizzes, view user completion status.
- Training Coordinators - Site level, SFLMS Admin rights. Functions: same as users and managers. In addition, create curriculums and learning items that link documents, videos, and quizzes, generate training metrics, present training content during audits. 
- Quality Assurance Analyst - Division level, SFLMS Admin rights. Functions: same as Users, Managers, and Training Coordinators. In addition, project manage the integration, provide user input to the Human Resources and Technology Group, seek input from the training coordinators at each site, provide Training Coordinator support, and develop and communicate new features. 
- Human Resources Technology Analyst - Corporate level. Functions: works with the software package to implement the platform, integrate APIs from associated systems (Workday, OCPLM, etc.). 

I have interviewed a Quality Analyst, my site's previous Training Coordinator, Managers, and Users at my site. I have also used SFLMS as a User and SFLMS Admin. 

## Problems 

License type - limited functionality and lack of adequate controls. 
- For example, Admins have the ability to add documents to a user's learning history, such as signed training completion forms that are pulled during audits. 

Functional Challenges - User Interface 

- Unclear hierarchy of different training components; can view child items nested below but cannot trace upwards. 
- Precise set of filters or steps are needed to perform basic functions or searches and require detailed local instructions. 
- Functions require multiple pivots and clicks away from the main page for information instead of being a self-contained and linear process that can be completed from a single window. 
- Fast session timeouts, inconsistent back-button availability, and session clearing 
- Confusing terminology leads to communication issues across personas and complicates collaboration. 
- Use of similar titles for completely different outcomes make it difficult to retrace steps or interpret system. 
- From a user standpoint, its hard to interpret the user interface and know what to do to find what you want. Too many terms, 

I'm unsure about how much the interface is defined by our license type or whether we had the ability to design the user interface ourselves. 


Data Migration - Site level 
- Not enough foresight on user needs, inconsistent alliance and communication across all personas to establish a platform that meets site needs
- It was a rushed project, thousands of prior training records and current documents had to be set up manually. 
- Future training logs must be performed manually. 
- She didn't have the support, training, or bandwidth to do the job. 
- Eliminating automated process introduces risk for mistakes about the most important process (OJTs, the biggest pain point)
    - Required features such as due date,  other aspects of the training limitations. 
- It uses a curriculum structure where you can choose to group trainings, but the downside is that if you are late in one, you are considered late at the group level, and you might be assigned training to a process that happens infrequently or are outside of your job responsibiltiies. Different sites with different products and different shifts, different roles. One training might be used across different departments and different curriculums 
- Some choices were made about how the trainings were structured and grouped  were not what managers wanted and were set up in haste just to meet the launch deadline. 
- There would be a selection where you could choose to make it only modifiable by an admin, so managers couldn't modify or unassign. 
- To modify a parent curriculum to remove one training, you would have to "break" the entire thing and it would make everyone who was assigned those trainings late. 
- Difficult to undo mistakes. 

Solution strategy - What I am doing to fix the training compliance problem
- Meet with all personas at the site so there's more of an alliance across the site. 
- Figure out what the new software can and can't do, what admins can't do and what they are allowed to do 
- Assess what the previous system had that people liked and try to replicate it in the new one.
- fix the curriculum structure so it's grouped the way people want, and make selection that allows leaders to edit their own and self govern their team.
- Establish consistent markers of groups. Current APIs add irrelevant IDs are currently added that make it hard to identify or pull accurate information because it's determined by HR or other departments that might not be always up to date or be grouping different things. 
- design the interface so functions can be performed in a linear way, and different information can be accessed from one page alongside the function without having to move to different pages or start over 
- make information more available - data and trending and automation (reports are bad and manual, no API access), supplementary search functions or tools 
- Better and more circulated instructions - make tutorials and documentation guides - screenshot instructions, videos for users and managers. I'd create content, and have a manager and a user use the instructions and give me feedback. 
- Create a user feedback loop to monitor whether they understand the process and con perform their tasks
- Establish monitoring that aren't just training compliance KPIs? Meet with leaders on a routine basis? 