# automatedWebScrapper


# Project Planning
1. Data collection
    a. Select 5 types of products
    b. Get 10 links of each
    c. Scrape the data and to create json file

2. Set-up of the project
    a. PHP for the back-end
    b. MongoDB for the Database
    c. React for front-end and visualize the graphs

3. Creating links
    a. Add the products data from the json file
    b. products : get request to get all products
    c. products/:type : get request to products belong to specific type
    d. /:product_id : get details of products
    e. /trigger : post present cost and update to all products

4. Automation 
    a. Create task to windows task manager to trigger every day at a particular time
    b. Scrape the data with selenium to get present cost
    c. Post the scraped data to the back-end to url '/trigger' and add todays cost

5. Front-end React
    a. Set up the react
    b. Create a dashboard to display the products
    c. React router dom to routes
    d. visualisation page to get visualisation each product

