1. To make sure the environment is perfectly setup, please use the following commands in the terminal after installing python (in case it isn't already installed)
	a. pip install fastapi
	b. pip install uvicorn
	c. pip install dnspython

We are making use of FastAPI to run the API I have written. Uvicorn is used for web server implementation of Python in this project.

Run the command in the following line from the concerned folder to make the uvicorn up and running.
uvicorn assignment:app --reload

Once you have run the above command, it shall show you a link on which Uvicorn is running.
Let's assume that link is <localhost>.

It is suggested that you use POSTMAN as the API platform for this project (as this project has been built using the same.)

Use this URL to run the API once the above installations are complete.
<localhost>/compute_tax_and_final_bill_amount

Choose GET Method for the above API.
Inside the Body, choose raw --> JSON format.
Paste the input list inside it. An example of the input Body is shown below.

[{
       "item": "Classical Songs Collection",
       "itemCategory": "Music",
       "quantity": 1,
       "price": 500
   },
   {
       "item": "Pants",
       "itemCategory": "Clothes",
       "quantity": 2,
       "price": 1200
   }
]

Please ensure that "quantity" and "price" are of data_type int.
 
Run the command and the output shall be something similar to the following:
{
    "Time of Purchase": "11-05-2022 18:27:36",
    "List of Commodities": [
        {
            "Item Name": "Classical Songs Collection",
            "Tax on Item": 15.0,
            "Final Price of Item": 515.0
        },
        {
            "Item Name": "Pants",
            "Tax on Item": 288.0,
            "Final Price of Item": 2568.0
        }
    ],
    "Total Amount Payable": 3083.0,
    "Total Tax": 303.0
}

This is a screenshot of the entire POSTMAN setup for the API.
![](compute_tax_and_final_bill_amount.png)

THANK YOU!
