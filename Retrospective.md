# Retrospective: the SuccessFactors LMS Integration Thermo Fisher Scientific 

When I tell people I work at Thermo Fisher Scientific, they pause, look off into the distance for a split second, look back at me, and say "Thermo Fisher...do they make lab equipment?" I immediately say "Yes! You're correct." Even folks within the industry aren't entirely sure what Thermo Fisher makes or does. In concept, Thermo Fisher is a company that supplies the Biotech, Pharmaceutical, Clinical Research, and Medical Device industries. They have a wide portfolio of offerings from analytical testing instruments, DNA sequencing, buffers and media, and even specialized bags for products to be packaged in. This is because Thermo Fisher acquires companies that are already commercial, and let them continue to self -govern. Because they had existed for years prior, they have their own internal training programs. Training is a key part of this industry due to the impact of the health care products and is a mandatory part of audits.  

## Personas
- users - site level. Actions: - Users online need to open trainings, watch videos, read documents, sign up for training, access old training content, take quizzes, request extensions. 
= managers - site level. Actions: same as users, assign trainings, extend, unlock tests, remove trainings, see user completion status, perform 3-year training review. 
- site Training Coordinators - same as managers, create curriculums, add content, add links, pull training metrics, show completion during audits.
- division quality Assurance - Project manage the integration, work with the Human Resources and Technology Group to design the interface, get input from the training coordinators at each site, and 
- huamn resources technology team - work with the software package to implement platform, integrate APIs from associated systems (Workday, OCPLM, etc.)


## Problems 
- Not enough foresight on user needs, weak alliance across all personas to customize interface to individual site needs. 
- License limiting functions. 
- user interface is terrible, hard to perform tasks or search for information. 
    - Hard to maintain across all users
- rush, a lot of mistakes 
- once it's set up, it's hard to undo 
- manual 

Problem - implementation with license and technical created user interface problems where simple tasks were more complicated. finding information became difficult as well, adn they have difficulty accessing past trainings. Platform features such as refreshing, back buttons, timeouts, different windows, made it hard to retrace steps or keep track of information while on the same page. Not enough pre-work was done to determine user needs and functions. It's 
Thermo fisher is so big and just a collection of smaller companies, each one had originally had their own training system. They did a project to harmonize it to one platform, SFLMS. From a project management perspective, not enough was done to gather user needs at the site level, and either the license bought wasn't right, or the interface was built where normally straightforward processes were longer, a million clicks and different pages that made a non-linear process from different windows. You need precise filters and steps to find simple information you want, and it'll clear out or time you out if you try to retrace your step and the solition is non intuitive. There's also no clear relatinoship between different items in the hierarchy, and the terms are unclear and hard to follow, which made ecommunication difficult. And then it was built by people who did not work at the site level to understand what was needed. You can know the top level and find content below, but can't retrace hierarchy upwards. One learning item or curriculum might be added to several parent curriculums across departments. 

- It was a rushed project, so thousands of prior training records and current documents had to be rush implemented manually. 
- Taking away automated process introduces risk for mistakes about the most important process (OJTs, the biggest pain point)
- With all of these features such as due date, other aspects of the training limitations. Not enough support, all manual, wtih a million different elements. 
- It uses a curriculum structure where you can choose to group trainings, but the downside is that if you are late in one, you are overall late in the group level, and you might be assigned training to a process that happens infrequently or are outside of your job responsibiltiies, different sites with different products and different shifts, different roles. 
- And it's hard to undo all of the work, and then everyone who is assigned would be considered late. 
- Some choices were made about how the trainings were strcutred and grouped that were not what supervisors or people wanted, and the setup was really important. - There would be a selection where you could choose to make it only unlockable by an admin, so managers couldn't unassign. 
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


Thermo Fisher Scientific is a company that manufactures and delivers a diverse porfolio of products spanning analytical instruments, DNA sequencing, laboratory materials, and sometimes is the only manufacturer of specialized equipment. It considered a leading supplier across Biotech, Pharma, Med Device, and Clinical Research industries. When I tell people that I work there, they will pause, look up, knit their eyebrows, and slowly say "I think I know what that company does...Do they make lab equipment?" I immediately say "Yes, you're absolutely correct." What is not always evident to those outside the industry is that it's not Biotech, it's not Pharma, and it's not the same as pointing out Moderna where you can say with confidence that it makes vaccines. Thermo Fisher makes so many products that are often completely unrelated to the point where the company cannot be easily characterized. This is because Thermo Fisher a collection of companies that were already commercial that were brought into the Thermo alliance without any technical influence and were left unchanged, process and culture-wise. As it stands, Thermo is actively M&A heavy and is constantly reevaluating its business units and incorporating new companies. In the life sciences industry, training is a critical point given that products will eventually impact people and is a standard audit topic. Given that companies were already independantly operating for years prior to the acquisition, most had already developed their own training system that fit the individual needs of their business. In 2023, the decision was made to implement a company-wide transition to  SFLMS (SuccessFactors Learning Management System) for training. My Quality Assurance role had previously been focused on the CAPA System and deviation management (investigations), and I transitioned to support the Training System in December 2025. This is my assessment of Thermo Fisher's implementation of SFLMS: how it was done, what went well, what did not, what the current state is, what I am doing to fix it, and what I recommend moving forward. I am only speaking from my experience in the Purification business, an individual business unit,
\ with 2 connected sites producing the same product. 

Vertical (Thermo Fisher Scientific)

Personas

Human Resources and Technology Analyst 
- Level - Corporate
- Department - Human Resources and Technology
- Technical direct contributor  
- Using APIs to build SFLMS and link other systems (Workday, SAP, Oracle Cloud Product Lifecycle Management).
- Has no input on 
- Works with Quality Analyst

Quality Analyst
- Level - Division (BioProduction Group)
- Department - Quality Assurrance 
- Non-technical direct contributor 
- Provides system requirement input based on industry training standards
- Interprets industry training standards 
- Tests builds, conducts user acceptance testing, deploys the software, and develops and manages new features throughout the lifecycle of the software.
- Works with Human Resources and Technology Analysts and Training Coordinators
- Has no background of an individual site's training needs (processes, products, or original training structure)
- Helps Training Coordinators migrate current training to SFLMS
- Allows Training Coordinators decide how
- SFLMS account rights: SFLMS Admin

Training Coordinator
- Direct contributor at the site-level. 
- Determines and manages curriculum structure and training requirements across all department functions. 
- Participates in all Audits to present training material. 
- SFLMS account rights: SFLMS Admin Role
- Manages the site-specific training: can assign, extend, reset, remove, and override training
- Works with Quality Analysts and all site personnel.

Leaders - Supervisors and Managers
- Site-level roles with direct reports.
- SFLMS account rights - Manager Role
- Assigns training to direct reports. 
- Cannot modify or remove trainings assigned by an SFLMS Admin. 
- Cannot modify curriculum structure or requirements. 

Current state:
2 years following the implementation, Only 25% of the people at the site have a noncompliant training status. Prior to the SFLMS implementation, the site training compliance was at 90%. 

Bedford Campus

What went well
The SFLMS implementation was completed in 2 years. Almost 100% of sites have integrated SFLMS and can be governed by Training Coordinators. A centralized platform is in place where the software is managed by a technical team that offloads the workload of the individual site. There is  consistency and has created links spanning the Training Coordinators across the company who had not previously interacted before. 

What did not go well

It was a rushed implementation. The Quality Analysts were working with the Training Coordinators and scrambling to migrate years worth of learning data into a new system. 

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
