# Retrospective: the SuccessFactors LMS Integration Thermo Fisher Scientific 

When I tell people I work at Thermo Fisher Scientific, they pause, look up, and say, "Thermo Fisher...I think I know what they do. They make...lab equipment?" I immediately say "Yes, you're absolutely correct." People across the world have likely heard of Thermo Fisher but even those within the life sciences industry have trouble characterizing the company as an entity3. In essence, Thermo Fisher is a major supplier to the Biotech, Pharmaceutical, Clinical Research, and Medical Device industries made possible by constant acquisitions. They have a broad range of offerings from analytical testing instruments, DNA sequencing, buffers and media, and even specialized single use bags for products to be packaged in. Because they had existed for years prior, each business has its own legacy training program. Two years ago, Thermo Fisher made the decision to harmonize training across the business units by implementing SuccessFactors Learning Management System (SFLMS). Before the implementation, my site was at 80% training compliance. After the implementation, we are only 25% compliant. Despite those numbers, only 25% of individual trainings are late. SFLMS is an industry standard for training, and I have been exposed to other companies with a more effective setup. I have interviewed a Quality Analyst, the training coordinator, managers, and users at my site. I have also interacted with SFLMS as a user, SFLMS Admin, and the legacy training system. Based on their input, this retrospective is my assessment of the implementation of SFLMS to production processes and what I would have done differently. 

## Personas
- users - site level. Actions: - Users online need to open trainings, watch videos, read documents, sign up for training, access old training content, take quizzes, request extensions. Access rights: user
= managers - site level. Actions: same as users, assign trainings, extend, unlock tests, remove trainings, see user completion status, perform 3-year training review. Access rights: manager
- site Training Coordinators - same as managers, create curriculums, add content, add links, pull training metrics, show completion during audits. Access rights: SFLMS Admin
- division quality Assurance - Project manage the integration, work with the Human Resources and Technology Group to design the interface, get input from the training coordinators at each site, provide training coordinator support, launch information about new features. Access rights: SFLMS Admin
- Human resources technology team -  corporate, work with the software package to implement platform, integrate APIs from associated systems (Workday, OCPLM, etc.)


## Problems 
- Not enough foresight on user needs, inconsistent alliance across all personas to establish a platform to meet site needs. 
- Functions limited by license type, and actions lack adequate controls. 
- User interface makes it hard to perform routine functions and find information, which makes it hard to maintain. 
- rush, a lot of mistakes 
- once it's set up, it's hard to undo 
- manual 


Functional Challenges 
- Hierarchy of different training components are unclear, and the nesting structure cannot be traced upward. Different terminology and so many different item types disrupt communication across personas in the learning process and make it hard to manage. 
- Unintuitive interface makes finding information and performing tasks difficult. 
- Implementing changes and logging trainings requires users to locate information from to different pages that will clear once the user returns to the task page instead of the information being accessible from a single window so the process can be completed in a linear set of steps. 
- Refresh buttons, fast timeouts, and the use of similar titles in different places make it difficult to retrace your steps when you find the right process.
- The search feature is not broad, precise filters and different methods are necessary to find the right information and require a long series of clicks. 


Data Migration
- It was a rushed project, thousands of prior training records and current documents had to be implemented manually. 
- Future training logs must be performed manually. 
- Taking away automated process introduces risk for mistakes about the most important process (OJTs, the biggest pain point)
- With all of these features such as due date, other aspects of the training limitations. 
- It uses a curriculum structure where you can choose to group trainings, but the downside is that if you are late in one, you are overall late in the group level, and you might be assigned training to a process that happens infrequently or are outside of your job responsibiltiies, different sites with different products and different shifts, different roles. 
- And it's hard to undo all of the work, and then everyone who is assigned would be considered late. 
- Some choices were made about how the trainings were structured and grouped that were not what supervisors wante just to meet the launch deadline. 
- There would be a selection where you could choose to make it only unlockable by an admin, so managers couldn't modify or unassign. 
- To modify a parent curriculum to remove one, you would have to "break" the entire thing and it would make everyone who was assigned those trainings late. 


Overhaul strategy 
- Make sure I meet with the people so there's more of an alliance across all groups. 
- Figure out what the new system can and can't do, what admins can't do and what they are allowed to do 
- Assess what the previous system had that people liked and try to replicate it in the new one as best as possible.
- fix the curriculum structure so it's grouped the way people want, and allow leaders to edit their own.
- Set it up in a way where there are consistent markers of what workcenter it is or site. Current APIs add irrelevant IDs that make it hard to identify or pull accurate information because it's determined by HR or other departments that might not be always up to date. You can't rely on the accuracy of the current IDs or labels in place in terms of personnel 
- design the interface so functions can be performed in a linear way, and different information can be accessed from one page alongside the function and without having to move to different pages or start over 
- leaders have more flexibility - unlocking tests, let the leaders self govern 
- make information more available - data and trending and automation (reports are bad and manual, no API access), supplementary search functions or tools 
- Better instructions - make tutorials and documentation guides - screenshot instructions, videos for users and managers. I'd write something, and take a manager and a user and have them go through the instructions and give me feedback. 
- Create a user feedback loop showing ease of access or capability to perform functions 
- Actually effective monitoring that aren't just training compliance KPIs? Meet with leaders on a routine basis? 


Bedford Campus

What went well
The SFLMS implementation was completed in 2 years. Almost 100% of sites have integrated SFLMS and can be governed by Training Coordinators. A centralized platform is in place where the software is managed by a technical team that offloads the workload of the individual site. There is  consistency and has created links spanning the Training Coordinators across the company who had not previously interacted before. 

What did not go well


It's unclear what license we have specifically, its functions are limited or there are poor controls. For example, Admins have the ability to add documents to a user's learning history, such as signed training completion forms that are pulled during audits. Although we have the capability, doing this would increase the cost of the license. Either there is a disconnect between the Human Resources Technical System team and the actual users where actions should be limited, no one collected the needs of the users before implementation, or the company did not evaluate the license enough. This would not be the first time-- The implementation of Oracle Cloud Platform Lifecycle Management had a similar issue where all users were granted authoring roles where they could initiate change orders to make their own document changes, but the company evaluated the license again, found that it was too expensive to provide everyone access, and removed almost everyone's author access level, which caused a host of production problems. 


There are UI problems, and it's not intuitive to perform simple tasks. There are too many inputs and filters required that need to be selected instead of it having a strong search engine. There are all these nested folders and things you need to click to get where you need to be, if you find the answer, clicking the back button will sometimes reset everything, and the inactivity log-out window is quite short. 

Finding information, language, and user interface. 

The groups with the power over how SFLMS was implemented. Each group I spoke to 


The project management did not take user input and needs into account, it was rushed, and the communication between the groups building the project wasn't effective enough. 

It's unclear whether it was a license issue or a build issue. But at any rate, user needs were not taken into account when building and deploying the platform. If I was at either level, I'd spend more time talking with site-level Training Coordinators to determine the user requirements or industry standards, and then either choose the correct license that allows those things. 



The implementation was rushed, and the Training Coordinators did not have enough support or ability to provide input during the process. Training Coordinators transferred their site's previous training content to SFLMS in the curriculum structure, where they could define the initial due dates and whether they could be modified by managers. Multiple trainings can be grouped under a single curriculum to make it easier for managers to assign groups of trainings depending on their roles and responsibilities. This backfired when 


There are multiple features that our site never utilized. The information and ability is technically out there, but it's not useful if it's this hidden or hard to find. 

Issues with the current state: 
Users are late on training. Leaders cannot 

The migration timeline was too aggressive. 

The implementation was rushed, and the Training Coordinators did not have enough support or opportunity to provide input throughout the process. The new platform layout is very complicated. From an admin perspective, performing simple tasks such as searching for a certain training or logging training to a user's learning history is complex. A long and specific set of clicks, filters, and toggling is required, and one wrong move messes it up, and it's unclear where you went wrong. IDs or descriptions will be needed at different stages of the process where you need to move back and forth instead of performing the steps in a linear way from within one window, and the inactivity time window is short. Search functions are hyper specialized and not broad enough for it to be helpful, requiring the user to switch between pages. It's hard to retrace your steps. You need to jump through too many windows to find a limited amount of information that you might need for something else. The terminology of the different learning items is completely new and difficult to understand from just using the software itself, and users are unfamiliar with terms, so it becomes difficult to communicate their needs or understand their problem also. As an SFLMS Admin, you can search for an item at the top level and see what is grouped down, but if you have the lowest level item, you cannot trace its path up to see what curriculums and items it is grouped in. 


At my site, there were 2 people assigned to this who had to learn this entire processs within a short span of time and migrate thousands of training records. They had to manually link documents from a different system, and determine requirements. The Training Coordinators transferred defined time requirements and the nature of how they could be assigned or removed. Some were grouped in a way where you had to complete all the trainings in one curriculum, or else you would be considered past due, and they were "locked". Some users were assigned training they may never have the opportunity to get the hands-on training they would need to get signed off due to a product being made infrequently, different responsibilities in shifts, or they were never expected to perform the task in the first place. But if it was assigned at the curriculum level, then it would forever sit on their training as late. To remove one training grouped under one curriculum, you would have to "break" the entire curriculum, and reassemble the entire thing where everyone who had completed it would lose their training status for all of the other ones. 

The implementation process was so intensive and performed by too few people, that there was not enough time or resources to dismantle and reconstruct the training system and set them the right way. In the end, the site is noncompliant, and are constantly receiving audit observations about training discrepancies from customers. 

TLDR
- The user interface doesn't fit the business needs 
- Finding information and performing tasks is non intuitive and requires clicking and transitioning through many pages in a non-linear way. 
- Finding information is difficult, search fields are very limited. 
- There is no consistency when it comes to identifying groups of people based on work centers, sites, or anything that could be meaningful to the business itself, because there are multiple IDs and sources from other APIs that have combined with the filtering that may or may not be updated themselves. There is no single source of truth. 


Doing it differently, I would've created more of an alliance between those building the software and the people using it at the site level. I'd understand the hierarchical structure of the business: divisions, sites, work centers, and departments, and integrate a search feature with terms everyone already uses to make it easier to narrow down information to a single page. I'd understand what groupings need to be higher level kept at a higher level to maintain consistency. After a certain point, the sites need to establish and govern how their own business wants to group their departments and roles. 
