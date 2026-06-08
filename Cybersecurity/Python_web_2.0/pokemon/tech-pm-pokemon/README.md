# Pokemon Collection App

A simple full-stack application demonstrating how **Frontend**, **Backend**, and **Database** work together. test

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     FRONTEND (UI Layer)                 │
│              (HTML/CSS/JavaScript in Browser)           │
│                   http://localhost:3000                 │
└─────────────────┬───────────────────────────────────────┘
                  │ HTTP Requests/Responses
                  │
┌─────────────────▼───────────────────────────────────────┐
│                   BACKEND (API Layer)                   │
│            (Node.js/Express Server)                     │
│                   http://localhost:3001                 │
│                                                         │
│  ├─ GET  /api/pokemon     - Get all saved Pokemon       │
│  ├─ GET  /api/search/:name - Search Pokemon API         │
│  ├─ POST /api/pokemon      - Add Pokemon to DB          │
│  └─ DELETE /api/pokemon/:id - Remove Pokemon from DB    │
└─────────────────┬───────────────────────────────────────┘
                  │ SQL Queries
                  │
┌─────────────────▼───────────────────────────────────────┐
│              DATABASE (Data Layer)                      │
│           (SQLite - Local File Database)                │
│          database/pokemon.db                            │
│                                                         │
│  Table: saved_pokemon                                   │
│  ├─ id (auto-generated)                                 │
│  ├─ pokemon_id (from API)                               │
│  ├─ name, height, weight                                │
│  ├─ stats, types                                        │
│  └─ created_at (timestamp)                              │
└─────────────────────────────────────────────────────────┘
```

## 🚀 Setup & Run

### 1. Install Dependencies

```bash
npm install
```

### 2. Start the Backend Server

```bash
npm start
```

The server will run on `http://localhost:3001`

### 3. Open the Frontend

In a **new terminal**, serve the frontend:

**Option A: Using Python (macOS/Linux)**

```bash
cd frontend
python3 -m http.server 3000
```

**Option B: Using Node.js**

```bash
cd frontend
npx http-server -p 3000
```

**Option C: Open directly in browser**

- Simply open `frontend/index.html` in your browser (works but APIs might have CORS issues)

Then visit: `http://localhost:3000`

## 📱 How It Works

### Frontend (UI Layer)

- **File**: `frontend/index.html`
- User-facing interface built with HTML/CSS/JavaScript
- Displays saved Pokemon collection
- Search box to find new Pokemon
- **Responsibilities**:
  - Collect user input (search, add, delete)
  - Display data to the user
  - Send requests to the backend
  - Update UI based on responses

### Backend (API Layer)

- **File**: `backend/server.js`
- Express.js REST API
- Handles business logic
- Validates requests
- Communicates with database
- Integrates with Pokemon API
- **Responsibilities**:
  - Route HTTP requests
  - Fetch data from Pokemon API
  - Execute database operations
  - Return structured JSON responses

### Database (Data Layer)

- **File**: `database/pokemon.db`
- SQLite local file database
- Stores your Pokemon collection
- **Responsibilities**:
  - Persist data (survives app restarts)
  - Organize data efficiently
  - Return data on query

## 🔄 Data Flow Examples

### Adding a Pokemon

```
1. Frontend: User types "pikachu" and clicks Search
   └─> Calls: GET /api/search/pikachu

2. Backend:
   └─> Fetches from Pokemon API
   └─> Formats response with stats, types, image
   └─> Sends back to Frontend

3. Frontend: Displays Pokemon details
   └─> User clicks "Add to Collection"
   └─> Calls: POST /api/pokemon with data

4. Backend:
   └─> Validates data
   └─> Executes SQL INSERT into saved_pokemon table
   └─> Returns success response

5. Frontend:
   └─> Shows success message
   └─> Refreshes collection by calling: GET /api/pokemon

6. Backend:
   └─> Queries all rows from saved_pokemon table
   └─> Returns JSON array

7. Frontend:
   └─> Renders all Pokemon cards with new addition
```

### Deleting a Pokemon

```
1. Frontend: User clicks "Delete from Collection"
   └─> Calls: DELETE /api/pokemon/[id]

2. Backend:
   └─> Executes SQL DELETE on saved_pokemon table
   └─> Returns success

3. Frontend:
   └─> Refreshes collection list
```

## 🎮 Features

✅ Search Pokemon from official API (https://pokeapi.co)
✅ View detailed stats, types, height, weight
✅ Add favorite Pokemon to your local collection
✅ See all saved Pokemon with beautiful cards
✅ Delete Pokemon from your collection
✅ Data persists (stored in local database)

## 📚 Key Concepts Demonstrated

| Concept              | Where              | Purpose                                    |
| -------------------- | ------------------ | ------------------------------------------ |
| **HTTP Requests**    | Frontend → Backend | Frontend asks backend for data             |
| **REST API**         | Backend            | Structured way to handle requests          |
| **External API**     | Backend → PokéAPI  | Fetch real data from internet              |
| **SQL Database**     | Backend ↔ SQLite   | Store and retrieve user data               |
| **CORS**             | Backend config     | Allow frontend to communicate with backend |
| **JSON**             | Communication      | Format for data exchange                   |
| **DOM Manipulation** | Frontend           | Update page content dynamically            |

## 🐛 Troubleshooting

**"Failed to load collection" error?**

- Make sure backend is running (`npm start`)
- Check it's on port 3001

**"Pokemon not found"?**

- Try lowercase Pokemon names: `pikachu`, `charizard`, `dragonite`

**Frontend can't connect to backend?**

- Check CORS is enabled in backend (it is by default)
- Ensure different ports: Frontend on 3000, Backend on 3001

**Database errors?**

- Database file is created automatically in `database/pokemon.db`
- Delete the file if it gets corrupted: `rm database/pokemon.db`

## 🎯 Learning Path

1. **Start Frontend First**: Open `frontend/index.html` to understand the UI
2. **Then Backend**: Look at `backend/server.js` to see API endpoints
3. **Finally Database**: Check `database/` for where data is stored
4. **Trace a Request**: Pick one feature (add/delete) and trace it through all 3 layers

## 📝 Next Steps to Enhance

- Add user authentication
- Add filters (by type, stats range)
- Add favorite/rating system
- Deploy to cloud (Heroku, Vercel, Railway)
- Switch to PostgreSQL for production
- Add TypeScript for type safety
