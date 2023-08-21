# Domain modelling

The domain model is the core of the application. It contains the `domain entities` and the `business rules`. It is responsible for the application behavior and belongs to the business logic layer of the application.

`Domain-driven design` let domain modelling to be popular. DDD concepts involve `repositories`, `value objects`, `entities` and `aggregates`.

Building a domain model consists of making the code reflect the business problem using the same language used to describe the work, the process and involved actors.

To complete the case, is necessary to develop a `glossary` and use the same language used by a company manager to describe the business problem.

## Forniture retailer, the MADE.com case study.

> MADE.com is a furniture retailer that `sells online`. It has a large catalog of `products` and a large number of `customers`. It has a `warehouse` where the products are stored and a `delivery service` that delivers the products to the customers.

> A `product` is identified by a `SKU` code (Stock Keeping Unit)  
> Customers place `orders` identified by an order reference and comprises multiple order lines  
> For example 1 unit of Pencil, 10 units of Pen.  
> The purchase department orders small `batches` of products from suppliers.  
> Each batch is identified by a `batch reference`, a `SKU` and `qty`.

> We need to `allocate` the `order lines` to `batches`.  
> When the order line is allocathed to a batch, we will send a stock from that specific batch to the customer.
> When X units of a product are allocated to a batch, `available_quantity` of the batch is decreased by X.
> We can't allocate a batch if the `available_quantity` is less than the `order line quantity`.

## The design process
This is the problem. The first step is to create some `unit tests` and empty classes to start the development of the domain model with `NO DEPENDENCIES AT ALL` from databases, web frameworks or other external libraries. This process should be done considering the following points.

### Entities or value objects?
Creating classes and unit tests, each class should be defined as `entity` or `value object`.

- `Entity` is an object that has an identity and is mutable.
- `Value object` is an object that has no identity and should be immutable.

The main difference to understand if an object is an entity or a value object is to ask if the object can be replaced by another object with the same properties. If the answer is yes, the object is a value object, otherwise it is an entity. A concrete example is `money`: if I need `5 EUR`, any bill of `5 EUR` can be used and the bill is identified as a `value object`. If I need the `bill number 1234`, only the bill with that number can be used and the bill is identified as an `entity` because it has an identity.

So each class should be defined as `entity` or `value object` and the unit tests should be written accordingly.

