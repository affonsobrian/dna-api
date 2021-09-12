# DNA
Supports registering and viewing DNAs.

## Register a new DNA

**Request**:

`POST` `/dna/`

Parameters:

Name       | Type         | Required | Description
-----------|--------------|----------|------------
dna        | List[string] | Yes      | The username for the new user.


*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
201 Created

{
  "id": 1,
  "dna": [
      "ATGCGA",
      "CAGTGC",
      "TTATGT",
      "AGAAGG",
      "CCCCTA",
      "TCACTG",
  ],
  "is_mutant": true
}
```


## Get a specific DNA information

**Request**:

`GET` `/dna/:id`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": 1,
  "dna": [
      "ATGCGA",
      "CAGTGC",
      "TTATGT",
      "AGAAGG",
      "CCCCTA",
      "TCACTG",
  ],
  "is_mutant": true
}
```


## List DNAs

**Request**:

`GET` `/dna/`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "dna": [
                "AACCTT",
                "AACCTT",
                "AACCTT",
                "AACCTT"
            ],
            "is_mutant": true
        }
    ]
}
```
