# Status
Supports viewing Status.


## Get a specific Status information

**Request**:

`GET` `/stats/:id`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": 1,
  "count_mutant_dna": 1,
  "count_human_dna": 1,
  "ratio": 1.0
}
```


## List DNAs

**Request**:

`GET` `/stats/`

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
            "count_mutant_dna": 1,
            "count_human_dna": 1,
            "ratio": 1.0
        }
    ]
}
```
