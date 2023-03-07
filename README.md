# Parcel-Delivery-System


## Task
Write and test an application <RESTful APIs> for a parcel delivery system covering at least 5 use cases, 3 entities and two user types.

Example of a user type: Recipient

Example of an Entity: Parcel

Example of a use case: Create a Parcel delivery. The use case should be in form of an endpoint making a particular action.


## SOLUTION
The parcel delivery system allows customers to create and manage parcels that are to be delivered to recipients. The system has two user types - Recipient and delivery agents. Recipient/Customer can create and manage parcels, while delivery agents can view and update the status of parcels that are assigned to them.

Resources
--------
* [Database Schema](https://drive.google.com/file/d/1pNdiAggyn44Qpky3HQWtsTqsyfKdUixg/view?usp=share_link)

Requirement
-----------
* Python
* Django
* Django Rest Framework



Use Cases
--------
Here are five use cases that the parcel delivery system should support:
* Create a parcel: Customers should be able to create a new parcel by providing the parcel details (name, description, recipient name and phone number, pickup and delivery addresses).
* Update a parcel: Customers should be able to update the details of a parcel (e.g. change the recipient's phone number,update the pickup or delivery address, etc.) as long as the parcel hasn't been assigned to a delivery agent yet.
* Assign a parcel to a delivery agent: A delivery agent should be able to view a list of parcels that are available for delivery and assign themselves to a parcel. Once a delivery agent is assigned to a parcel, the status of the parcel should be updated to "in transit".
* Update the status of a parcel: A delivery agent should be able to update the status of a parcel (e.g. mark it as "delivered") once they have completed the delivery.

* View a list of parcels: Customers and delivery agents should be able to view a list of parcels, with the ability to filter by status (e.g. view only parcels that are "in transit" or "delivered").

## Endpoints

* AUthentication | To gain access to the endpoint run this code in terminal
``` curl -X POST -d "username=<admin>&password=<admin123>" http://localhost:8000/api-token-auth/```


* Create a parcel: Send a POST request to the /parcels/ endpoint with the following JSON data:

```
{
    "name": "Test Parcel",
    "description": "This is a test parcel",
    "recipient_name": "Ayomide Samuel",
    "recipient_phone": "234-8025-3755",
    "pickup_address": "12 Ketu, Lagos",
    "delivery_address": "Ikeja"
}

```

* Update a parcel: Send a PATCH request to the /parcels/{id}/ endpoint with the parcel ID in the URL and the updated JSON data in the request body.

```
 /parcels/{id}/
 
 ```

* Assign a parcel to a delivery agent: Send a GET request to the ```/parcels/?status=available``` endpoint to retrieve a list of parcels that are available for delivery. Then send a PATCH request to the ```/parcels/{id}/``` endpoint with the parcel ID in the URL and the delivery agent ID in the request body

* Update the status of a parcel: Send a PATCH request to the ```/parcels/{id}/``` endpoint with the parcel ID in the URL and the updated JSON data in the request body.
This should update the status of the parcel to "delivered".



* View a list of parcels: Send a GET request to the `/parcels/` endpoint to retrieve a list of all parcels, or send a GET request to the `/parcels/?status=in_transit` endpoint to retrieve a list of parcels that are currently in transit.

* Create a new customer: Send a POST request to the /customers/ endpoint with the following JSON data

``` 
{
    "name": "John Doe",
    "phone": "555-555-5555",
    "email": "johndoe@example.com",
    "address": "123 Main St, Anytown, USA",
    "password": "secretpassword"
}
```
This should create a new customer in the database.

* View a list of customers: Send a GET request to the `/customers/` endpoint to retrieve a list of all customers.

* Update a customer: Send a PATCH request to the `/customers/{id}/` endpoint with the customer ID in the URL and the updated JSON data in the request body.

* Delete a customer: Send a DELETE request to the `/customers/{id}/` endpoint with the customer ID in the URL.

* Create a new delivery agent: Send a POST request to the `/deliveryagents/` endpoint with the following JSON data
```
{
    "name": "Jane Doe",
    "phone": "555-555-5555",
    "email": "janedoe@example.com",
    "vehicle_type": "car",
    "vehicle_plate_number": "ABC123",
    "password": "secretpassword"
}
```DefaultRouter.


* View a list of delivery agents: Send a GET request to the `/deliveryagents/` endpoint to retrieve a list of all delivery agents.

* Update a delivery agent: Send a PATCH request to the `/deliveryagents/{id}/` endpoint with the delivery agent ID in the URL and the updated JSON data in the request body.

* Delete a delivery agent: Send a DELETE request to the `/deliveryagents/{id}/` endpoint with the delivery agent ID in the URL.
