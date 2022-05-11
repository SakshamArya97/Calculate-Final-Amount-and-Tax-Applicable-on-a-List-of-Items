from fastapi import FastAPI
from fastapi.param_functions import Body
import sys, traceback
from datetime import datetime


app = FastAPI()



@app.get("/compute_tax_and_final_bill_amount")
def compute_tax_and_final_bill(
    item_list: list = Body(...)
):
    try:
        total_amount_payable = 0
        total_tax = 0
        list_of_commodities = []
        #Running a loop over all the items
        for item in item_list:
            # print(item)
            if type(item["quantity"])!=int or type(item["price"])!=int:
                return {"Please make sure quantity and price are entered as int types"}
            
            if item["quantity"]==0 or item["price"]==0:
                return {"Please make sure quantity and price are not entered as 0"}

            total_amount_for_item = item["quantity"] * item["price"]
    
            #compute_tax is a function which simply returns the tax and the final amount of the item
            amount_with_tax,tax = compute_tax(item["itemCategory"],total_amount_for_item)
            total_amount_payable += amount_with_tax
            total_tax += tax

            commodity_dict = {
                "Item Name":item["item"],
                "Tax on Item":tax,
                "Final Price of Item":amount_with_tax,
            }
            list_of_commodities.append(commodity_dict)

        # this final_list_of_commodities is basically list_of_commodities, but sorted according to corresponding 'Item Name'
        final_list_of_commodities = sorted(list_of_commodities, key = lambda l:l["Item Name"])

        return_dict = {
            "Time of Purchase":datetime.strftime(datetime.utcnow(), "%d-%m-%Y %H:%M:%S"),
            "List of Commodities":final_list_of_commodities,
            "Total Amount Payable":total_amount_payable,
            "Total Tax":total_tax,
        }
        return return_dict
    except Exception as err:
        traceback.print_exc()
        return {repr(err)}





def compute_tax(item_category,total_amount_for_item):
    try:
        #Calculating taxes based on the item_categories
        if item_category=="Medicine" or item_category=="Food":
            tax = total_amount_for_item*0.05
        elif item_category=="Imported":
            tax = total_amount_for_item*0.18
        elif item_category=="Book":
            tax = 0
        elif item_category=="Music":
            tax = total_amount_for_item*0.03
        elif item_category=="Clothes":
            if total_amount_for_item<1000:
                tax = total_amount_for_item*0.05
            else:
                tax = total_amount_for_item*0.12

        #Adding tax to the original amount
        amount_with_tax = total_amount_for_item + tax
        
        #In case the total amount surpasses 2000, we apply a 5% discount
        if total_amount_for_item>2000:
            amount_with_tax -= total_amount_for_item*0.05

        return amount_with_tax,tax
    except Exception as err:
        traceback.print_exc()
        return {repr(err)}