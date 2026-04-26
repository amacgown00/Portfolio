# Retrospective: the SuccessFactors LMS Integration Thermo Fisher Scientific 

When I tell people I work at Thermo Fisher Scientific, they pause, look up, and say, "Thermo Fisher...I think I know what they do. They make...lab equipment?" I immediately say "Yes, you're absolutely correct." People across the world have likely heard of Thermo Fisher but even those within the life sciences industry have trouble characterizing the company as an entity. In essence, Thermo Fisher is a major supplier to the Biotech, Pharmaceutical, Clinical Research, and Medical Device industries made possible by constant acquisitions. They have a broad range of offerings from analytical testing instruments, DNA sequencing, buffers and media, and even specialized single use bags for products to be packaged in. Because these companies were commercial prior to the acquisition, each business has its own legacy training program. Two years ago, Thermo Fisher made the decision to harmonize training across the business units by implementing SuccessFactors Learning Management System (SFLMS). Before the implementation, my site was at 80% training compliance. After the implementation, we are only 25% personnel compliant. Despite these numbers, only 25% of individual trainings are late. This is my retrospective of the implementation of SFLMS and what I would have done differently. Based on their input, this retrospective is my assessment of the implementation of SFLMS to production processes and what I would have done differently. 

Thermo fisher is in the life sciences vertical. My role has changed recently, I was a Quality Engineer for investigations and my role has transitioned where I am in the Training System. I work for this branch that does x 

## Personas and functions on SFLMS
- users - site level, User Access rights. Functions/Actions: - open trainings, watch videos, read documents, sign up for training, access old training content, complete quizzes, request training extensions. Access rights: user
= Managers - site level, Manager Acccess rights. Actions: same as users, and assign trainings, extend, unlock tests, remove trainings, see user completion status, perform 3-year training review. 
- Training Coordinators - site level, SFLMS Admin rights. Functions: same as users and managers, create curriculums, set up content links, videos, quizzes, pull training metrics, present training during audits. 
- Quality Assurance Analyst- Division level, SFLMS Admin rights. Fuctions: Project manage the integration, provide user input to the Human Resources and Technology Group, seek input from the training coordinators at each site, provide training coordinator support, communicate new features. 
- Human Resources Technology Analyst - corporate. work with the software package to implement the platform, integrate APIs from associated systems (Workday, OCPLM, etc.). 

I have interviewed a Quality Analyst, my site training coordinator, managers, and users at my site. I have also interacted with SFLMS as a user, SFLMS Admin, and the legacy training system. 

## Problems 
- Not enough foresight on user needs, inconsistent alliance across all personas to establish a platform to meet site needs. 
- Functions limited by license type, and actions lack adequate controls. 
- User interface makes it hard to perform routine functions and find information, which makes it hard to maintain. 
- Rush timeline, a lot of mistakes 
- once it's set up, it's hard to undo 
- manual process 

License type - limited functionality and lack of adequate controls. 
- For example, Admins have the ability to add documents to a user's learning history, such as signed training completion forms that are pulled during audits. 

Functional Challenges interface and 
- Hierarchy of different training components is unclear, and the nesting structure cannot be traced upward. Different terminology and so many different item types disrupt communication across personas in the learning process and make it hard to make changes. As an SFLMS Admin, you can search for an item at the top level and see what is grouped down, but if you have the lowest level item, you cannot trace its path up to see what curriculums and items it is grouped in. 
- Unintuitive interface makes finding information and performing tasks difficult. 
- Functions require multiple pivots to find information that require its own set of clicks, then return to the main page to complete the tasks, instead of the task being self contined from a single window in a linear set of clicks. 
- After pivoting to find the required information and returning to the original task page, the information will clear, and fast timeouts, inconsistent back-button availability, and the use of similar titles in different places make retracing steps difficult once you find the right process.
- Search functions is not broad, precise filters and different steps are necessary to find the right information and require a long series of clicks in an unintuitive way from the user interface. Some of the steps to finding very simple information are like, once you learn them, I'm like, I never would've guessed that I needed to do that. There are other choices and toggles that sound the same but mean something different and have complete different outcomes. 
- every single time you get it wrong, it tells you that there are no results. So there are too many filters. The first page setup wil lhave filters that have a default option that is exact match only, so it narrows down the search function from the start, and it's unclear what to change to find the desired result. 
- From a user standpoint, its hard to interpret the user interface and know what to do to find what you want. Too many terms, 

I'm unsure about how much the interface is defined by our license type or whether we had the ability to design the user interface ourselves. 


Data Migration - Site level 
- It was a rushed project, thousands of prior training records and current documents had to be set up manually. 
- Future training logs must be performed manually. 
- She didn't have the support, training, or bandwidth to do the job. 
- Eliminating automated process introduces risk for mistakes about the most important process (OJTs, the biggest pain point)
    - Required features such as due date,  other aspects of the training limitations. 
- It uses a curriculum structure where you can choose to group trainings, but the downside is that if you are late in one, you are considered late at the group level, and you might be assigned training to a process that happens infrequently or are outside of your job responsibiltiies. Different sites with different products and different shifts, different roles. One training might be used across different departments and different curriculums 
- Some choices were made about how the trainings were structured and grouped  were not what managers wanted and were set up in haste just to meet the launch deadline. 
- There would be a selection where you could choose to make it only modifiable by an admin, so managers couldn't modify or unassign. 
- To modify a parent curriculum to remove one training, you would have to "break" the entire thing and it would make everyone who was assigned those trainings late. 

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



Bedford Campus

What went well
The SFLMS implementation was completed in 2 years. Almost 100% of sites have integrated SFLMS and can be governed by Training Coordinators. A centralized platform is in place where the software is managed by a technical team that offloads the workload of the individual site. There is  consistency and has created links spanning the Training Coordinators across the company who had not previously interacted before. 

What did not go well


Although we have the capability, doing this would increase the cost of the license. Either there is a disconnect between the Human Resources Technical System team and the actual users where actions should be limited, no one collected the needs of the users before implementation, or the company did not evaluate the license enough. This would not be the first time-- The implementation of Oracle Cloud Platform Lifecycle Management had a similar issue where all users were granted authoring roles where they could initiate change orders to make their own document changes, but the company evaluated the license again, found that it was too expensive to provide everyone access, and removed almost everyone's author access level, which caused a host of production problems. 


There are UI problems, and it's not intuitive to perform simple tasks. There are too many inputs and filters required that need to be selected instead of it having a strong search engine. There are all these nested folders and things you need to click to get where you need to be, if you find the answer, clicking the back button will sometimes reset everything, and the inactivity log-out window is quite short. 

Finding information, language, and user interface. 

The groups with the power over how SFLMS was implemented. Each group I spoke to 


The project management did not take user input and needs into account, it was rushed, and the communication between the groups building the project wasn't effective enough. 


The implementation was rushed, and the Training Coordinators did not have enough support or ability to provide input during the process. Training Coordinators transferred their site's previous training content to SFLMS in the curriculum structure, where they could define the initial due dates and whether they could be modified by managers. Multiple trainings can be grouped under a single curriculum to make it easier for managers to assign groups of trainings depending on their roles and responsibilities. This backfired when 


There are multiple features that our site never utilized. The information and ability is technically out there, but it's not useful if it's this hidden or hard to find. 

Issues with the current state: 
Users are late on training. Leaders cannot 

The migration timeline was too aggressive. 

The implementation was rushed, and the Training Coordinators did not have enough support or opportunity to provide input throughout the process. The new platform layout is very complicated. From an admin perspective, performing simple tasks such as searching for a certain training or logging training to a user's learning history is complex. A long and specific set of clicks, filters, and toggling is required, and one wrong move messes it up, and it's unclear where you went wrong. IDs or descriptions will be needed at different stages of the process where you need to move back and forth instead of performing the steps in a linear way from within one window, and the inactivity time window is short. Search functions are hyper specialized and not broad enough for it to be helpful, requiring the user to switch between pages. 