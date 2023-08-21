# Patterns

There are many patterns that can be used to achieve a good design. Here there are the patterns presented in the book `Architecture Patterns with Python` by Harry Percival and Bob Gregory.

- **Repository** - Abstraction on persistent storage
- **Service layer** - use case boundary
- **Unit of work** - atomic operations
- **Aggregate pattern** - enforce data integrity

## Repository

Modeling the domain entities is not enough. We need to persist the data in a database or in a file. The repository pattern is a way to abstract the persistent storage. It is a way to decouple the domain entities from the persistent storage.

Common frameworks like Django or Flask have their own way to persist data. For example Django uses its `ORM` based on an `Active record pattern`. Django is powerful but it's not domain driven. The main concept is that the orm hides data persistence detailt and provide an interface to get and save data.
