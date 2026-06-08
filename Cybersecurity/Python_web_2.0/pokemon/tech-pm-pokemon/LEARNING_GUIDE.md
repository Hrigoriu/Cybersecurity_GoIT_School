# Learning Guide: Understanding Frontend, Backend & Database

This document explains the three-tier architecture using the Pokemon app as a reference.

---

## 🎯 Three Tiers Explained

### Tier 1: Frontend (User Interface)

**Location:** `frontend/index.html`

The **Frontend** is what users see and interact with.

**Key Characteristics:**

- Runs in the **browser** (client-side)
- Built with HTML, CSS, JavaScript
- Handles user interactions (clicks, typing, scrolling)
- Sends requests to the backend
- Displays data to the user

**In our app:**

```
┌─────────────────────────────────┐
│      Pokemon Search Box          │
│  ┌────────────────────────────┐  │
│  │  Search: [pikachu____]  🔍 │  │
│  └────────────────────────────┘  │
│                                  │
│  Pokemon Details:               │
│  ┌──────────────────────────┐    │
│  │ [Image]  Name: Pikachu   │    │
│  │          Type: Electric  │    │
│  │          Height: 0.4m    │    │
│  │          [Add to Collection] │
│  └──────────────────────────┘    │
│                                  │
│  Your Collection:               │
│  ┌──────┐ ┌──────┐ ┌──────┐     │
│  │Pika │ │Char │ │Squir │     │
│  │[Del]│ │[Del]│ │[Del] │     │
│  └──────┘ └──────┘ └──────┘     │
└─────────────────────────────────┘
```

**Frontend Responsibilities:**

1. Show a search input for the user
2. Display Pokemon when user searches
3. Let user add Pokemon to collection
4. Show all saved Pokemon
5. Let user delete Pokemon

**Frontend Does NOT:**

- Talk directly to the database
- Store data permanently
- Access other websites
- Handle sensitive logic

---

### Tier 2: Backend (Business Logic & API)

**Location:** `backend/server.js`

The **Backend** is the "middleman" that handles requests and manages data.

**Key Characteristics:**

- Runs on a **server** (server-side)
- Built with Node.js + Express
- Listens for HTTP requests from the frontend
- Processes data
- Communicates with the database
- Calls external APIs
- Returns data as JSON

**In our app:**

```
┌──────────────────────────────────────────┐
│          Express.js Server               │
│      Running on Port 3001                │
│                                          │
│  Routes:                                 │
│  ┌──────────────────────────────────┐   │
│  │ GET /api/pokemon                 │   │
│  │ → Query database for all Pokemon  │   │
│  │ → Return JSON to frontend        │   │
│  └──────────────────────────────────┘   │
│                                          │
│  ┌──────────────────────────────────┐   │
│  │ GET /api/search/:name            │   │
│  │ → Call Pokemon API               │   │
│  │ → Extract relevant data          │   │
│  │ → Return JSON to frontend        │   │
│  └──────────────────────────────────┘   │
│                                          │
│  ┌──────────────────────────────────┐   │
│  │ POST /api/pokemon                │   │
│  │ → Validate received data         │   │
│  │ → Insert into database           │   │
│  │ → Return confirmation to frontend│   │
│  └──────────────────────────────────┘   │
│                                          │
│  ┌──────────────────────────────────┐   │
│  │ DELETE /api/pokemon/:id          │   │
│  │ → Check if Pokemon exists        │   │
│  │ → Remove from database           │   │
│  │ → Return confirmation to frontend│   │
│  └──────────────────────────────────┘   │
└──────────────────────────────────────────┘
```

**Backend Responsibilities:**

1. Listen for requests from the frontend
2. Validate the incoming data
3. Fetch data from Pokemon API (external source)
4. Perform database operations
5. Process and format responses
6. Send JSON back to frontend

**Backend Does NOT:**

- Handle UI rendering (that's frontend's job)
- Display things to users (that's frontend's job)
- Store temporary sessions (that's frontend's job)

---

### Tier 3: Database (Data Storage)

**Location:** `database/pokemon.db`

The **Database** is where data lives permanently.

**Key Characteristics:**

- Runs on the **file system** or a database server
- Uses SQL for queries
- Stores data in structured tables
- Survives app restarts
- Can be queried and updated by the backend

**In our app:**

```
┌─────────────────────────────────────────────────┐
│        SQLite Database File                     │
│       (pokemon.db on disk)                      │
│                                                 │
│  Table: saved_pokemon                          │
│  ┌──────────────────────────────────────────┐  │
│  │ id │ pokemon_id │ name │ height │ weight │  │
│  ├──────────────────────────────────────────┤  │
│  │ 1  │    25      │ pika │   4    │   60   │  │
│  │ 2  │    4       │ char │   6    │   85   │  │
│  │ 3  │    7       │ squi │   5    │   90   │  │
│  │ 4  │    6       │ char │   17   │  156   │  │
│  └──────────────────────────────────────────┘  │
│                                                 │
│  (Also stores: base_experience, image_url,     │
│   types, stats, created_at)                    │
└─────────────────────────────────────────────────┘
```

**Database Responsibilities:**

1. Store Pokemon data permanently
2. Allow querying (SELECT)
3. Allow inserting new data (INSERT)
4. Allow updating data (UPDATE)
5. Allow deleting data (DELETE)
6. Return results to the backend

**Database Does NOT:**

- Talk to the frontend directly
- Make external API calls
- Display data
- Handle user interactions

---

## 🔄 How They Work Together

### Example 1: Adding a Pokemon

```
1. USER INTERACTION (Frontend)
   ├─ User types "charizard" in search box
   └─ User clicks search button
                    │
                    ▼

2. FRONTEND SENDS REQUEST (Frontend)
   └─ fetch('http://localhost:3001/api/search/charizard')

      HTTP Request:
      ┌──────────────────────────────┐
      │ GET /api/search/charizard    │
      │ Host: localhost:3001         │
      │ Accept: application/json     │
      └──────────────────────────────┘
                    │
                    ▼

3. BACKEND RECEIVES REQUEST (Backend)
   └─ Express route handler activated
      app.get('/api/search/:name', async (req, res) => {
        const name = req.params.name  // "charizard"

4. BACKEND FETCHES EXTERNAL DATA (Backend)
   └─ fetch('https://pokeapi.co/api/v2/pokemon/charizard')

      External Pokemon API returns:
      {
        id: 6,
        name: "charizard",
        height: 17,
        weight: 156,
        sprites: { ... },
        stats: [ ... ],
        types: [ ... ]
      }
                    │
                    ▼

5. BACKEND PROCESSES DATA (Backend)
   └─ Extract and format relevant fields
      stats = data.stats.map(...)
      types = data.types.map(...)

6. BACKEND SENDS RESPONSE (Backend)
   ├─ res.json({ pokemon_id, name, height, ... })

   HTTP Response:
   ┌──────────────────────────────┐
   │ 200 OK                       │
   │ Content-Type: application/json
   │                              │
   │ {                            │
   │   "pokemon_id": 6,           │
   │   "name": "charizard",       │
   │   "height": 17,              │
   │   "weight": 156,             │
   │   "stats": [ ... ],          │
   │   "types": ["fire", "flying"]│
   │ }                            │
   └──────────────────────────────┘
                    │
                    ▼

7. FRONTEND RECEIVES RESPONSE (Frontend)
   └─ .then(res => res.json())
   └─ Response data now available in JavaScript variable

8. FRONTEND DISPLAYS DATA (Frontend)
   ├─ Update DOM with Pokemon name
   ├─ Show image
   ├─ Display types, height, weight
   └─ Show "Add to Collection" button
                    │
                    ▼

9. USER CLICKS "Add to Collection" (Frontend)
   └─ JavaScript function triggered
                    │
                    ▼

10. FRONTEND SENDS ADD REQUEST (Frontend)
    └─ fetch('http://localhost:3001/api/pokemon', {
         method: 'POST',
         body: JSON.stringify({ pokemon_id, name, ... })
       })

       HTTP Request:
       ┌──────────────────────────────┐
       │ POST /api/pokemon            │
       │ Content-Type: application/json
       │                              │
       │ {                            │
       │   "pokemon_id": 6,           │
       │   "name": "charizard",       │
       │   "height": 17,              │
       │   "weight": 156,             │
       │   "image_url": "https://...", │
       │   "types": ["fire", "flying"],
       │   "stats": [ ... ]           │
       │ }                            │
       └──────────────────────────────┘
                    │
                    ▼

11. BACKEND PROCESSES ADD REQUEST (Backend)
    ├─ Validate data structure
    ├─ Check for duplicates
    └─ If valid, prepare SQL INSERT statement
                    │
                    ▼

12. BACKEND INSERTS INTO DATABASE (Backend)
    └─ db.run(`
         INSERT INTO saved_pokemon
         (pokemon_id, name, height, weight, ...)
         VALUES (6, "charizard", 17, 156, ...)
       `)
                    │
                    ▼

13. DATABASE STORES DATA (Database)
    ├─ SQLite creates a new row in saved_pokemon table
    ├─ Auto-generates id = 1 (or next available)
    ├─ Stores all fields
    └─ Data is now PERSISTENT (survives app restart!)
                    │
                    ▼

14. DATABASE RETURNS CONFIRMATION (Database)
    └─ Callback indicates success/failure
                    │
                    ▼

15. BACKEND SENDS RESPONSE (Backend)
    └─ res.json({ id: 1, pokemon_id: 6, name: "charizard", ... })

       HTTP Response:
       ┌──────────────────────────────┐
       │ 200 OK                       │
       │ Content-Type: application/json
       │                              │
       │ {                            │
       │   "id": 1,                   │
       │   "pokemon_id": 6,           │
       │   "name": "charizard",       │
       │   "success": true            │
       │ }                            │
       └──────────────────────────────┘
                    │
                    ▼

16. FRONTEND RECEIVES CONFIRMATION (Frontend)
    ├─ Shows "Added to collection!" message
    └─ Calls loadPokemonCollection() to refresh list
                    │
                    ▼

17. FRONTEND REQUESTS FULL LIST (Frontend)
    └─ fetch('http://localhost:3001/api/pokemon')
                    │
                    ▼

18. BACKEND QUERIES DATABASE (Backend)
    └─ db.all('SELECT * FROM saved_pokemon', ...)
                    │
                    ▼

19. DATABASE RETURNS ALL SAVED POKEMON (Database)
    └─ Returns array of all rows:
       [
         { id: 1, name: "charizard", ... },
         { id: 2, name: "dragonite", ... },
         { id: 3, name: "blastoise", ... }
       ]
                    │
                    ▼

20. BACKEND FORMATS AND SENDS (Backend)
    └─ res.json(allPokemon)
                    │
                    ▼

21. FRONTEND DISPLAYS UPDATED COLLECTION (Frontend)
    └─ Renders cards for all 3 Pokemon
    └─ User sees Charizard added to their collection!
```

---

## 💡 Key Concepts

### HTTP Requests

- **GET**: Ask for data

  ```
  GET /api/pokemon → "Give me all Pokemon"
  GET /api/search/pikachu → "Get pikachu data"
  ```

- **POST**: Send and store data

  ```
  POST /api/pokemon + {data} → "Save this Pokemon"
  ```

- **DELETE**: Remove data
  ```
  DELETE /api/pokemon/1 → "Delete Pokemon with id 1"
  ```

### JSON (JavaScript Object Notation)

- Format for sending data between frontend and backend

```json
{
  "name": "pikachu",
  "height": 4,
  "types": ["electric"]
}
```

### REST API

- **RE**presentational **S**tate **T**ransfer
- Structured way to design web APIs
- Uses HTTP methods (GET, POST, DELETE)
- Resources identified by URLs

### SQL Database Queries

**SELECT** - Get data

```sql
SELECT * FROM saved_pokemon;
SELECT name FROM saved_pokemon WHERE id = 1;
```

**INSERT** - Add data

```sql
INSERT INTO saved_pokemon (name, height, weight)
VALUES ('pikachu', 4, 60);
```

**DELETE** - Remove data

```sql
DELETE FROM saved_pokemon WHERE id = 1;
```

### CORS (Cross-Origin Resource Sharing)

- Allows frontend to talk to backend
- Backend enables with: `app.use(cors())`
- Otherwise browser blocks requests for security

---

## 🎓 Learning Checklist

Use this to verify your understanding:

### Frontend Understanding

- [ ] I can identify the search form in `frontend/index.html`
- [ ] I understand how DOM manipulation updates the page
- [ ] I know how `fetch()` sends HTTP requests
- [ ] I can trace where clicked buttons trigger functions
- [ ] I understand how JSON is parsed and displayed

### Backend Understanding

- [ ] I can identify routes in `backend/server.js`
- [ ] I understand how `app.get()` handles GET requests
- [ ] I understand how `app.post()` handles POST requests
- [ ] I know how backend validates incoming data
- [ ] I understand how to call external APIs (Pokemon API)
- [ ] I know how backend returns JSON responses

### Database Understanding

- [ ] I know SQLite uses SQL queries
- [ ] I understand INSERT adds rows
- [ ] I understand SELECT retrieves rows
- [ ] I understand DELETE removes rows
- [ ] I know data persists in `pokemon.db` file
- [ ] I can name the columns in saved_pokemon table

### Integration Understanding

- [ ] I can trace a complete feature (add/delete) through all 3 tiers
- [ ] I understand frontend never talks directly to database
- [ ] I understand backend is the intermediary
- [ ] I know why this separation is important
- [ ] I can explain why data persists after app restart

---

## 🚀 Next Learning Steps

1. **Modify the Frontend**
   - Add a filter by type button
   - Add sorting (by height, weight, etc.)

2. **Enhance the Backend**
   - Add input validation
   - Add error handling
   - Add logging

3. **Expand the Database**
   - Add a users table
   - Add favorite status for Pokemon
   - Add a history table

4. **Deploy the App**
   - Deploy backend to Heroku/Railway
   - Deploy frontend to Vercel/Netlify
   - Use a cloud database (PostgreSQL)

5. **Add Security**
   - Add authentication (login/signup)
   - Add user-specific collections
   - Validate and sanitize inputs

---

## 📞 Quick Reference

| Layer    | What                  | Where              | Port |
| -------- | --------------------- | ------------------ | ---- |
| Frontend | UI, User Interactions | Browser            | 3000 |
| Backend  | API, Business Logic   | Node.js Server     | 3001 |
| Database | Data Storage          | File (pokemon.db)  | N/A  |
| External | Pokemon Data          | https://pokeapi.co | N/A  |

---

## ❓ Common Questions

**Q: Why can't the frontend talk directly to the database?**
A: Security. Database credentials should never be exposed to the browser.

**Q: Why can't the frontend call Pokemon API directly?**
A: CORS restrictions and API rate limits. Backend can handle these better.

**Q: Why does data persist after restarting the app?**
A: Database stores data in a file on disk, independent of the running app.

**Q: What if I restart the backend but not delete the database?**
A: All your Pokemon are still there! They're in the .db file.

**Q: Can I use a different database?**
A: Yes! PostgreSQL, MySQL, MongoDB, etc. Just change the code in backend/server.js.

**Q: Can I add authentication/login?**
A: Yes! Add a users table and require login before accessing collections.

**Q: What about the Pokemon API rate limits?**
A: Pokemon API is free and generous. No authentication needed for basic usage.
