# Automation of the PO process from Magento to email.

This program was used from 2020 to early 2021, then we refactored and moved the script to a Jupyter notebook file as it was easier to use by the whole team. 
See repo "Order script Jupyter"


Problem:
The purchasing system is all manual, time consuming and all about copy and pasting.

Solution :
Automating most of the process

Current procedure:
1. Import orders placed from the back end (Magento). The import is a pdf file with all the orders placed.
2. Office to go through each order and one by one, copy and paste the sku number and quantities needed
to the google sheet inventory file.
The inventory file is used by
    - Office to get the POs ready and inform customers of stock levels when asked
    - Warehouse to find products location, the warehouse updates the stock levels daily
3. The Google sheet calculates the quantity of items needed to be ordered.
4. Office needs to manually check if the minimum order quantities (MOQ) are meet in the PO
ex : glassware is ordered in min case of 24 from supplier, but end customers can purchase by multiple of 6 quantities
5. Prepare the POs, for some suppliers that involves slightly changing the Sku numbers between ours and our suppliers'
6. Send POs via email.

** Notes :

Step 2 and 5 are the one that takes the longest time since it involves a lot of back and forth between files and boring copy and pasting.

Step 4 is not critical since suppliers fix the MOQ but it annoys them to have to change it and doesn't look professional
on our end. It also sometimes involves waste of time and back and forth communication to confirm quantities ordered, which could be avoided for a smoother process.

Step 3 will be the last to be improved since it involves a full change of the current process and remote access to the database, which I am not able to work on for now.

** Resolutions:

Step 1 resolution:
Since I couldn't manage to extract the information from the pdf, I choose to use Zapier to create Zaps; orders coming through via email would be recorded on a google sheet, exported as csv
14/09 Step likely to change once we change software.

Step 2 resolution :
The necessary information extracted via the function "daily_orders"
14/09 This step could be improved as there are a few details to be fixed and automated, but the upgrade is on hold for now as we are changing platforms and I'll wait to see what happens on that end before making major changes

Step 4 resolution
By using a dataframe with all price lists from all suppliers standardized and concatenated.
A couple of price lists are still missing, waiting on an excell file from the supplier. They are not major ones and the MOQ is usually 1 for now.

Step 5 resolution:
Removed suffixes from supplier's product codes
create order drafts by seperating the orders according to the product codes
14/09 this will be improved now that the price list including all suppliers is ready
