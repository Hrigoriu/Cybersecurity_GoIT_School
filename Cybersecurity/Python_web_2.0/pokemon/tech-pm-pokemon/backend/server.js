const express = require('express');
const cors = require('cors');
const sqlite3 = require('sqlite3').verbose();
const fetch = require('node-fetch');
const path = require('path');

const app = express();
const PORT = 3001;

// Middleware
app.use(cors());
app.use(express.json());

// Database setup
const dbPath = path.join(__dirname, '../database/pokemon.db');
const db = new sqlite3.Database(dbPath, (err) => {
  if (err) {
    console.error('Database connection error:', err);
  } else {
    console.log('Connected to SQLite database');
    initializeDatabase();
  }
});

// Initialize database schema
function initializeDatabase() {
  db.run(`
    CREATE TABLE IF NOT EXISTS saved_pokemon (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      pokemon_id INTEGER UNIQUE,
      name TEXT NOT NULL,
      height INTEGER,
      weight INTEGER,
      base_experience INTEGER,
      image_url TEXT,
      types TEXT,
      stats TEXT,
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
  `);
}

// Routes

// Get all saved Pokemon from database
app.get('/api/pokemon', (req, res) => {
  db.all('SELECT * FROM saved_pokemon ORDER BY created_at DESC', [], (err, rows) => {
    if (err) {
      res.status(500).json({ error: err.message });
      return;
    }
    const pokemon = rows.map(row => ({
      ...row,
      types: JSON.parse(row.types || '[]'),
      stats: JSON.parse(row.stats || '[]')
    }));
    res.json(pokemon);
  });
});

// Search and fetch Pokemon from API
app.get('/api/search/:name', async (req, res) => {
  try {
    const name = req.params.name.toLowerCase();
    const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${name}`);
    
    if (!response.ok) {
      return res.status(404).json({ error: 'Pokemon not found' });
    }

    const data = await response.json();
    
    // Extract relevant stats
    const stats = data.stats.map(stat => ({
      name: stat.stat.name,
      value: stat.base_stat
    }));

    const types = data.types.map(t => t.type.name);

    const pokemon = {
      pokemon_id: data.id,
      name: data.name,
      height: data.height,
      weight: data.weight,
      base_experience: data.base_experience,
      image_url: data.sprites.other['official-artwork'].front_default || data.sprites.front_default,
      types,
      stats
    };

    res.json(pokemon);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch Pokemon' });
  }
});

// Add Pokemon to database
app.post('/api/pokemon', (req, res) => {
  const { pokemon_id, name, height, weight, base_experience, image_url, types, stats } = req.body;

  db.run(
    `INSERT INTO saved_pokemon (pokemon_id, name, height, weight, base_experience, image_url, types, stats)
     VALUES (?, ?, ?, ?, ?, ?, ?, ?)`,
    [pokemon_id, name, height, weight, base_experience, image_url, JSON.stringify(types), JSON.stringify(stats)],
    function(err) {
      if (err) {
        if (err.message.includes('UNIQUE constraint failed')) {
          return res.status(400).json({ error: 'Pokemon already saved' });
        }
        return res.status(500).json({ error: err.message });
      }
      res.json({ 
        id: this.lastID,
        pokemon_id,
        name,
        height,
        weight,
        base_experience,
        image_url,
        types,
        stats
      });
    }
  );
});

// Delete Pokemon from database
app.delete('/api/pokemon/:id', (req, res) => {
  const id = req.params.id;

  db.run('DELETE FROM saved_pokemon WHERE id = ?', [id], function(err) {
    if (err) {
      return res.status(500).json({ error: err.message });
    }
    if (this.changes === 0) {
      return res.status(404).json({ error: 'Pokemon not found' });
    }
    res.json({ success: true, message: 'Pokemon deleted' });
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`Backend server running on http://localhost:${PORT}`);
  console.log(`Frontend: http://localhost:3000`);
});

// Graceful shutdown
process.on('SIGINT', () => {
  db.close((err) => {
    if (err) console.error(err.message);
    console.log('Database connection closed');
    process.exit(0);
  });
});
