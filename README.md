# Parcel-Delivery-System


## Task

## SOLUTION
The parcel delivery system allows customers to create and manage parcels that are to be delivered to recipients. The system has two user types - Recipient and delivery agents. Customers can create and manage parcels, while delivery agents can view and update the status of parcels that are assigned to them.

Resources
--------
* [Database Schema](https://drive.google.com/file/d/1pNdiAggyn44Qpky3HQWtsTqsyfKdUixg/view?usp=share_link)

Use Cases
--------
Here are five use cases that the parcel delivery system should support:
* Create a parcel: Customers should be able to create a new parcel by providing the parcel details (name, description, recipient name and phone number, pickup and delivery addresses).
* Update a parcel: Customers should be able to update the details of a parcel (e.g. change the recipient's phone number,update the pickup or delivery address, etc.) as long as the parcel hasn't been assigned to a delivery agent yet.
* Assign a parcel to a delivery agent: A delivery agent should be able to view a list of parcels that are available for delivery and assign themselves to a parcel. Once a delivery agent is assigned to a parcel, the status of the parcel should be updated to "in transit".
* Update the status of a parcel: A delivery agent should be able to update the status of a parcel (e.g. mark it as "delivered") once they have completed the delivery.

* View a list of parcels: Customers and delivery agents should be able to view a list of parcels, with the ability to filter by status (e.g. view only parcels that are "in transit" or "delivered").

## Endpoints

* 