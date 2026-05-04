# Retrospective: the SuccessFactors LMS Integration Thermo Fisher Scientific 

Thermo Fisher is a major supplier to the Biotech and Pharmaceutical industries that offers a broad range of products made possible by acquisitions. I am a Quality Engineer in the Purification business unit located in Bedford and Chelmsford, Massachusetts. My previous focus was investigations, and I have recently changed roles to manage the Training System. 

Two years ago, there was a company-wide training harmonization that transitioned legacy training systems to the SuccessFactors Learning Management System (SFLMS). Currently, my business is 25% training compliant. Prior to implementation, we were 80% training compliant. This is my retrospective on the implementation of SFLMS and the actions I am taking to improve the system moving forward.


## Personas 
- User - Site-level direct contributor, User Access rights. Functions: review and complete trainings content, complete quizzes, sign up for training, access previous training content, request training extensions. 
= Managers - Site-level leader, Manager Acccess rights. Functions: same as users, assign, extend, and remove trainings, unlock quizzes, view user completion status.
- Training Coordinators - Site level, SFLMS Admin rights. Functions: same as users and managers, and create curriculums and learning items that link content, generate training metrics, present training content during audits. 
- Quality Assurance Analyst - Division level, SFLMS Admin rights. Functions: same as Users, Managers, and Training coordinators project manage the integration, provide user input to the Human Resources and Technology Group, seek input from the training coordinators at each site, provide Training Coordinator support, and develop and communicate new features. 
- Human Resources Technology Analyst - Corporate level. Functions: works with the software package to implement the platform, integrate APIs from associated systems (Workday, OCPLM, etc.). 

## Problems 

License type - limited functionality and lack of adequate controls. 
- For example, Admins have the ability to add documents to a user's learning history, such as signed training completion forms that are pulled during audits. 


## Functional Challenges - User Interface 

- Unclear hierarchy of different training components; can view child items nested below but cannot trace upwards. 
- Precise set of filters or steps are needed to perform basic functions or searches and require detailed local instructions. 
- Functions require multiple pivots and clicks away from the main page for information instead of being a self-contained and linear process that can be completed from a single window. 
- Fast session timeouts, inconsistent back-button availability, and session clearing 
- Use of similar titles for completely different outcomes makes it difficult to retrace steps, interpret or navigate the system, and communicate across personas. 

I'm unsure about how much the interface is defined by our license type or whether we had the ability to design the user interface ourselves. 


Data Migration
- Inconsistent alliance and communication across Quality Analysts and Training Coordinators to identify site needs.
- Quality Analysts did not have a technical background to have direct input on features. 
- Short project timeline: +10 years of legacy training records and current documents were manually transferred by 2 people.
- All automated processes were eliminated, making the system harder to maintain and introducing risk of manual error. 
- Restrictive grouping: to remove a training from a curriculum, an SFLMS Admin must "break" the entire curriculum and mark all users who were assigned as late, even if they had completed the training.
- Many curriculums were incorrectly scoped and did not account for the differences in the business, making users late on processes that could not be completed based on shift, site, and roles, or are performed infrequently due to unpredictable product demand.
- Many curriculums were created so they were only modifiable by an admin, so managers couldn't modify or unassign. 
- Difficult to undo mistakes after initially setting it up. 


## Solution - What I am doing to fix the training compliance problem
- Conducting meetings with managers to understand their barriers, needs, what they liked about the legacy system, and how to support them after the curriculum corrections have been made. 
- Developing a website that allows managers to review and reorganize the curriculum structure, create new groups, and track changes. s
- Figure out what the new software can and can't do, what admins can't do and what they are allowed to do.
- Establish consistent markers of groups. Current APIs add irrelevant IDs are currently added that make it hard to identify or pull accurate information because it's determined by HR or other departments that might not be always up to date or be grouping different things.
- make information more available - data and trending and automation (reports are bad and manual, no API access), supplementary search functions or tools 
- Better and more circulated instructions - make tutorials and documentation guides - screenshot instructions, videos for users and managers. I'd create content, and have a manager and a user use the instructions and give me feedback. 
- Create a user feedback loop to monitor whether they understand the process and con perform their tasks
- Establish monitoring that aren't just training compliance KPIs? Meet with leaders on a routine basis