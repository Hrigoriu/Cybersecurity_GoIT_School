# API Documentation

## Base URL

```
http://localhost:3001/api
```

All responses are JSON.

---

## Endpoints

### 1. Get All Saved Pokemon

**Endpoint:** `GET /pokemon`

**Description:** Retrieves all Pokemon from your collection stored in the database.

**Request:**

```
GET /api/pokemon
```

**Response (200 OK):**

```json
[
  {
    "id": 1,
    "pokemon_id": 25,
    "name": "pikachu",
    "height": 4,
    "weight": 60,
    "base_experience": 112,
    "image_url": "https://raw.githubusercontent.com/...",
    "types": ["electric"],
    "stats": [
      { "name": "hp", "value": 35 },
      { "name": "attack", "value": 55 },
      { "name": "defense", "value": 40 },
      { "name": "sp. atk", "value": 50 },
      { "name": "sp. def", "value": 50 },
      { "name": "speed", "value": 90 }
    ],
    "created_at": "2024-04-09 10:30:00"
  },
  {
    "id": 2,
    "pokemon_id": 4,
    "name": "charmander",
    "height": 6,
    "weight": 85,
    "base_experience": 62,
    "image_url": "https://raw.githubusercontent.com/...",
    "types": ["fire"],
    "stats": [
      { "name": "hp", "value": 39 },
      { "name": "attack", "value": 52 },
      { "name": "defense", "value": 43 },
      { "name": "sp. atk", "value": 60 },
      { "name": "sp. def", "value": 50 },
      { "name": "speed", "value": 65 }
    ],
    "created_at": "2024-04-09 10:35:00"
  }
]
```

**Error Response (500):**

```json
{
  "error": "Database error message"
}
```

---

### 2. Search Pokemon from API

**Endpoint:** `GET /search/:name`

**Description:** Searches for a Pokemon by name from the official Pokemon API and returns full details.

**Request:**

```
GET /api/search/pikachu
```

**URL Parameters:**

- `name` (string, required) - Pokemon name (case-insensitive)

**Response (200 OK):**

```json
{
  "pokemon_id": 25,
  "name": "pikachu",
  "height": 4,
  "weight": 60,
  "base_experience": 112,
  "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
  "types": ["electric"],
  "stats": [
    { "name": "hp", "value": 35 },
    { "name": "attack", "value": 55 },
    { "name": "defense", "value": 40 },
    { "name": "sp. atk", "value": 50 },
    { "name": "sp. def", "value": 50 },
    { "name": "speed", "value": 90 }
  ]
}
```

**Error Response (404):**

```json
{
  "error": "Pokemon not found"
}
```

**Error Response (500):**

```json
{
  "error": "Failed to fetch Pokemon"
}
```

**Example Usage:**

```javascript
// From Frontend
fetch("http://localhost:3001/api/search/charizard")
  .then((res) => res.json())
  .then((pokemon) => console.log(pokemon));
```

---

### 3. Add Pokemon to Collection

**Endpoint:** `POST /pokemon`

**Description:** Adds a Pokemon to your saved collection in the database.

**Request:**

```
POST /api/pokemon
Content-Type: application/json

{
  "pokemon_id": 25,
  "name": "pikachu",
  "height": 4,
  "weight": 60,
  "base_experience": 112,
  "image_url": "https://raw.githubusercontent.com/...",
  "types": ["electric"],
  "stats": [
    { "name": "hp", "value": 35 },
    { "name": "attack", "value": 55 },
    { "name": "defense", "value": 40 },
    { "name": "sp. atk", "value": 50 },
    { "name": "sp. def", "value": 50 },
    { "name": "speed", "value": 90 }
  ]
}
```

**Response (200 OK):**

```json
{
  "id": 1,
  "pokemon_id": 25,
  "name": "pikachu",
  "height": 4,
  "weight": 60,
  "base_experience": 112,
  "image_url": "https://raw.githubusercontent.com/...",
  "types": ["electric"],
  "stats": [
    { "name": "hp", "value": 35 },
    { "name": "attack", "value": 55 },
    { "name": "defense", "value": 40 },
    { "name": "sp. atk", "value": 50 },
    { "name": "sp. def", "value": 50 },
    { "name": "speed", "value": 90 }
  ]
}
```

**Error Response (400):**

```json
{
  "error": "Pokemon already saved"
}
```

**Error Response (500):**

```json
{
  "error": "Database error message"
}
```

**Example Usage:**

```javascript
const pokemon = {
  pokemon_id: 25,
  name: "pikachu",
  height: 4,
  weight: 60,
  base_experience: 112,
  image_url: "https://...",
  types: ["electric"],
  stats: [{ name: "hp", value: 35 }, ...]
};

fetch('http://localhost:3001/api/pokemon', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(pokemon)
})
  .then(res => res.json())
  .then(result => console.log('Added:', result))
```

---

### 4. Delete Pokemon from Collection

**Endpoint:** `DELETE /pokemon/:id`

**Description:** Removes a Pokemon from your saved collection.

**Request:**

```
DELETE /api/pokemon/1
```

**URL Parameters:**

- `id` (integer, required) - Database ID of the Pokemon record

**Response (200 OK):**

```json
{
  "success": true,
  "message": "Pokemon deleted"
}
```

**Error Response (404):**

```json
{
  "error": "Pokemon not found"
}
```

**Error Response (500):**

```json
{
  "error": "Database error message"
}
```

**Example Usage:**

```javascript
fetch("http://localhost:3001/api/pokemon/1", {
  method: "DELETE",
})
  .then((res) => res.json())
  .then((result) => console.log("Deleted:", result));
```

---

## Data Structures

### Pokemon Object (from Database)

```json
{
  "id": 1,
  "pokemon_id": 25,
  "name": "pikachu",
  "height": 4,
  "weight": 60,
  "base_experience": 112,
  "image_url": "https://raw.githubusercontent.com/...",
  "types": ["electric"],
  "stats": [
    { "name": "hp", "value": 35 },
    { "name": "attack", "value": 55 },
    { "name": "defense", "value": 40 },
    { "name": "sp. atk", "value": 50 },
    { "name": "sp. def", "value": 50 },
    { "name": "speed", "value": 90 }
  ],
  "created_at": "2024-04-09 10:30:00"
}
```

### Stats Format

```json
[
  { "name": "hp", "value": 35 },
  { "name": "attack", "value": 55 },
  { "name": "defense", "value": 40 },
  { "name": "sp. atk", "value": 50 },
  { "name": "sp. def", "value": 50 },
  { "name": "speed", "value": 90 }
]
```

### Types Format

```json
["electric", "water"]
```

---

## Testing with cURL

### Get all Pokemon

```bash
curl http://localhost:3001/api/pokemon
```

### Search for a Pokemon

```bash
curl http://localhost:3001/api/search/pikachu
```

### Add a Pokemon

```bash
curl -X POST http://localhost:3001/api/pokemon \
  -H "Content-Type: application/json" \
  -d '{
    "pokemon_id": 25,
    "name": "pikachu",
    "height": 4,
    "weight": 60,
    "base_experience": 112,
    "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
    "types": ["electric"],
    "stats": [{"name": "hp", "value": 35}]
  }'
```

### Delete a Pokemon

```bash
curl -X DELETE http://localhost:3001/api/pokemon/1
```

---

## CORS Policy

The backend has CORS enabled, allowing requests from:

- Any origin (configured with `cors()` middleware)

In production, you would restrict this to specific domains.

---

## Rate Limiting

Not implemented in this basic version. Pokemon API has its own rate limits.

---

## Authentication

Not implemented in this basic version. All endpoints are public.

---

## Error Handling

All errors return appropriate HTTP status codes:

- `200` - Success
- `400` - Bad request (e.g., Pokemon already saved)
- `404` - Not found
- `500` - Server error

Always include `Content-Type: application/json` header in your requests.
