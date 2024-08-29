# automatedWebScrapper

# Local Project
1. Select 5 types of products and scrape links from amazon to each product
2. First time scrape the amazon for title, img link and cost
3. Every day when triggered go for only cost and update in visualize.json
4. create exe or window to open visualised data
5. use .bat file to create trigger


# Cloud Project Planning
1. Data collection
    - Select 5 types of products
    - Get 10 links of each
    - Scrape the data and to create json file

2. Set-up of the project
    - PHP for the back-end
    - MongoDB for the Database
    - React for front-end and visualize the graphs

3. Creating links
    - Add the products data from the json file
    - products : get request to get all products
    - products/:type : get request to products belong to specific type
    - /:product_id : get details of products
    - /trigger : post present cost and update to all products

4. Automation 
    - Create task to windows task manager to trigger every day at a particular time
    - Scrape the data with selenium to get present cost
    - Post the scraped data to the back-end to url '/trigger' and add todays cost

5. Front-end React
    - Set up the react
    - Create a dashboard to display the products
    - React router dom to routes
    - visualisation page to get visualisation each product

