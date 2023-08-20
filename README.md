# Architecture Patterns with Python

This repository contains the code used to study the book `Architecture Patterns with Python` by Harry Percival and Bob Gregory.  
Most of my focus is on applying the concepts to my own Django projects but I try to understand the concepts in a more general way too.

## Introduction

Mind map of the book arguments first `Domain driven design`:

```mermaid
graph
    B[Domain driven design]
    B --> P[Patterns]
    P --> Q[Repositories]
    Q --> O[Orm depends on model]
    P --> R[Services]
    R --> S[Unit of work]


    B --> E[Domain modelling]
    E --> D[Value objects vs entities]
    E --> F[Domain testing]

    E --> G[Aggregates]
    G --> H[Invariants]
    G --> I[Consistency]
    G --> J[Constraitns]



```

then `Event driven microservices`:

```mermaid
graph
    C[Event driven microservices]
    C --> D[Message bus]
    C --> K[Micro service integration]
    D --> F[Implementation]
    F --> H[Commands]
    F --> I[Events]
    F --> J[Error handling]
    D --> G[Refactoring service]
    G --> E[Everything is an \n event handler]
```

Arguments with no places in the mind map (for now):

- Summary Diagram and Table
- A Template Project Structure
- Swapping Out the Infrastructure: Do Everything with CSVs
- Repository and Unit of Work Patterns with Django
