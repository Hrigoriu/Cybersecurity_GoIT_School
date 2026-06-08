# Pokemon App Architecture Overview

## System Diagram

```
                           🌐 INTERNET
                                ▲
                                │
                                │ (Pokemon Data)
                                │
                    https://pokeapi.co/api/v2


                    ┌─────────────────────────┐
                    │    BACKEND SERVER       │
                    │   (Node.js + Express)   │
                    │   http://3001           │
                    │                         │
                    │  ┌─────────────────┐   │
                    │  │  API Routes:    │   │
                    │  │                 │   │
                    │  │ GET /pokemon    │   │
                    │  │ POST /pokemon   │   │
                    │  │ DELETE /pokemon │   │
                    │  │ GET /search/:name   │
                    │  │                 │   │
                    │  │ Fetches from:   │   │
                    │  │ - Pokemon API   │   │
                    │  │ - SQLite DB     │   │
                    │  └─────────────────┘   │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │  LOCAL DATABASE         │
                    │  (SQLite)               │
                    │  pokemon.db             │
                    │                         │
                    │  Table: saved_pokemon   │
                    │  ├─ id                  │
                    │  ├─ pokemon_id          │
                    │  ├─ name                │
                    │  ├─ height              │
                    │  ├─ weight              │
                    │  ├─ image_url           │
                    │  ├─ types (JSON)        │
                    │  ├─ stats (JSON)        │
                    │  └─ created_at          │
                    └─────────────────────────┘

(HTTP Requests from Browser)
           ▲              │
           │              ▼
    ┌──────┴──────────────┐
    │   FRONTEND UI       │
    │  (HTML/CSS/JS)      │
    │  http://3000        │
    │                     │
    │ ┌─────────────────┐ │
    │ │  Components:    │ │
    │ │                 │ │
    │ │ • Search Box    │ │
    │ │ • Pokemon List  │ │
    │ │ • Details View  │ │
    │ │ • Action Buttons│ │
    │ │                 │ │
    │ │ Functions:      │ │
    │ │ • Search        │ │
    │ │ • Add           │ │
    │ │ • Delete        │ │
    │ │ • Display       │ │
    │ └─────────────────┘ │
    └─────────────────────┘
```

## Data Flow: Adding a Pokemon

```
User Types "pikachu" in search box
                │
                ▼
        [Frontend] Sends: GET /api/search/pikachu
                │
                ▼
        [Backend] Fetches from https://pokeapi.co/api/v2/pokemon/pikachu
                │
                ▼
        [Backend] Extracts: stats, types, height, weight, image
                │
                ▼
        [Frontend] Receives JSON with Pokemon data
                │
                ▼
        [Frontend] Displays Pokemon preview with "Add to Collection" button
                │
                ▼
        User Clicks "Add to Collection"
                │
                ▼
        [Frontend] Sends: POST /api/pokemon + Pokemon data
                │
                ▼
        [Backend] Validates data
                │
                ▼
        [Backend] Executes: INSERT INTO saved_pokemon VALUES (...)
                │
                ▼
        [SQLite] Stores data in database file
                │
                ▼
        [Backend] Returns: {success: true, id: 1}
                │
                ▼
        [Frontend] Shows "Added!" message
                │
                ▼
        [Frontend] Sends: GET /api/pokemon
                │
                ▼
        [Backend] Executes: SELECT * FROM saved_pokemon
                │
                ▼
        [SQLite] Returns all saved Pokemon rows
                │
                ▼
        [Frontend] Renders all Pokemon cards including new one
```

## Key Technologies

### Frontend

- **HTML5**: Structure
- **CSS3**: Styling with gradient backgrounds
- **Vanilla JavaScript**: DOM manipulation, fetch API calls

### Backend

- **Node.js**: JavaScript runtime
- **Express.js**: Web framework
- **node-fetch**: HTTP client for Pokemon API
- **CORS**: Enable cross-origin requests

### Database

- **SQLite3**: Lightweight file-based database
- **No server needed**: Just a file on disk

### External API

- **PokéAPI**: Free Pokemon data (https://pokeapi.co)

## Running the App

Terminal 1 - Backend:

```bash
npm start
```

Terminal 2 - Frontend:

```bash
cd frontend
python3 -m http.server 3000
```

Then visit: http://localhost:3000

## Concepts Illustrated

1. **Separation of Concerns**
   - Frontend: User interface only
   - Backend: Business logic & data access
   - Database: Persistent storage

2. **Client-Server Architecture**
   - Frontend (Client) makes requests
   - Backend (Server) processes and responds
   - HTTP for communication

3. **REST API Design**
   - GET: Retrieve data
   - POST: Create data
   - DELETE: Remove data

4. **Database Transactions**
   - INSERT: Add data
   - SELECT: Query data
   - DELETE: Remove data

5. **External Integration**
   - Backend consumes third-party APIs
   - Frontend never talks directly to external APIs

6. **Data Persistence**
   - Database survives app restarts
   - Data persists across sessions
