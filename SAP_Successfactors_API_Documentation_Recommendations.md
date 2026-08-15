# Improvements I Would Make to SAP SuccessFactors API Documentation

I am learning Python and am using SAP SuccessFactors Learning Management System as a way to learn REST APIs. I validate my API actions and data in the user interface with my SuccessFactors Admin account access. These are changes I would make to the existing documentation. 

1. Document how to perform actions first, service information after. 
- The current document version: 1H 2026 = 2026-06-16 is 623 pages. 
- Pages 7-452 outlines service paths, endpoints, parameters, and properties before code instructions are introduced. 

7. Service Path Documentation Structure
- Explain that the complex type Alias name needs to be placed before the query property in GET calls.
- Complex type should be called out in an endpoint that it is the query property set, for non OData users. 
- For each endpoint, on one page place the query properties on the left column and the response properties on the right with an example GET call.
- State the required query properties to see the minimum information.  
- List the property descriptions and data types after the property mapping page, and shift the property type to the second column so the description can be a larger column to conserve page space. 
- It lists the endpoint response properties and descriptions in a long list, and there can be several endpoints for one service path, and then the query properties at the very bottom, requiring the user to scroll up and down several pages back and forth.

2. What are Primary Keys? 
- The value is ignored in wrapper entities but is required.
- The background knowledge section that explains OData standards states that Primary Keys are required for all PUT calls but does not explain what they are or how to find them. 

5. User Exams
- It does not explain a GET call that identifies when a user failed an exam and is locked out. 
- Does not document how to find exam question information. 
- The `onlineStatus` property has codes that do not reflect the user's locked-out state from comparing it with my admin rights on the user interface. 
- It does not document the call that unlocks the user and allows them to retake the exam. 

8. Document Key Actions
- How to extend a learning item. 
- A date can be set at the beginning but changing the item required date cannot be done through the API.

9. Updating Service Path Code Examples
- The documentation recommends to use new paths with the word "service" in the URL, but the code examples use the old paths. 


## Product Design Changes 
Here are things I would change about the product. 

1. Remove revision requirement from PUT/POST calls. 
- Once a revision is retired, the PUT/POST calls should by default only update the active revision. 
- Create a separate service to call and update past revisions. 

1. There is no way of identifying the SAP endpoints the organization has implemented.  

2. Add jobLocID as a query property in the user search service paths. 
- It is a critical property in large organizations. 
- Without it, accurate user reporting data cannot be fully automated. 

3. Create service path to identify a user's training status at a certain point in time. 
- It can be done now but only through post-retrieval processing. 

4. New Learning Item Users Trained endpoint
- I would add an endpoint that allows you to search for a learning item and display all users trained to it. 

5. New relationship service path 
- Add a service path that lets you search one item or curriculum and show the hierarchical relationships. 
- Current `Learning-Service/UserTodoItems` endpoint shows item-curriculum-root curriculum relationship, but can only be found when searching a user. 
- Search for a learning item: see its subcurriculum and root curriculum relationships
- Search for a curriculum: see if it is a subcurriculum underneath a parent, and see what items it contains. 

6. Learning Item Get calls 
- The documentation says "the way that you call for a single learning item in SAP SuccessFactors Learning is unusual because it needs three data elements to return a single learning item." and that "...in addition to their ID, learning items have a type and a revision. You must pass all three to return a single, unique learning item." 
- I would change it so you can search the learning item with just the item ID, a single piece of information. 
- End users know the learning item ID and wouldn't know the other two without looking for it. 